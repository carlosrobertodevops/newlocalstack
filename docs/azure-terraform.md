# Terraform + LocalStack Azure

End-to-end guide for running `terraform-provider-azurerm` (v3.110+) against the LocalStack Azure emulator without an Azure subscription, `az login`, or environment variables.

Working example: [`examples/terraform/azure/main.tf`](../examples/terraform/azure/main.tf).

## What works today

| Resource                       | Status |
|--------------------------------|--------|
| `azurerm_resource_group`       | OK     |
| `azurerm_storage_account`      | OK     |
| `azurerm_storage_container`    | OK     |
| `azurerm_storage_queue`        | partial (control plane only) |
| `azurerm_storage_share`        | partial (control plane only) |

`terraform init`, `terraform plan`, and `terraform apply -auto-approve` complete against the local stack with no real cloud credentials.

## One-time setup

```bash
# 1. mkcert root CA + TLS sidecar cert (sudo prompt first run)
make setup-azure-tls

# 2. Bring up the stack (LocalStack + nginx TLS sidecar)
docker-compose up -d

# 3. /etc/hosts entries for the storage account name used in main.tf
bin/azure-register-host tflocalstackstor
```

What each step does:

1. `bin/setup-azure-tls` installs mkcert's local CA into your OS trust store and issues a cert with SANs covering all storage subdomains plus `management.azure.com`, `login.microsoftonline.com`, `graph.microsoft.com`. Go's TLS stack (used by `terraform-provider-azurerm`) then trusts the LocalStack sidecar without `SSL_CERT_FILE`.
2. `docker-compose.yml` exposes the TLS sidecar (`localstack-tls`) on `127.0.0.1:4569` AND `127.0.0.1:443`. Port 443 is required because `hashicorp/go-azure-sdk` rejects storage URLs that include an explicit port.
3. `bin/azure-register-host <account>` writes `127.0.0.1 <account>.blob.core.windows.net` (and the queue/table/file/dfs/web subdomains) to `/etc/hosts`. The Azure SDK hardcodes the `core.windows.net` suffix, so the storage host has to resolve to the sidecar by name.

## Run

```bash
cd examples/terraform/azure
terraform init
terraform plan
terraform apply -auto-approve
```

The provider block in [`main.tf`](../examples/terraform/azure/main.tf) is fully self-contained:

```hcl
provider "azurerm" {
  features {}
  metadata_host  = "localhost:4569"

  client_id       = "00000000-0000-0000-0000-000000000001"
  client_secret   = "test-secret"
  tenant_id       = "00000000-0000-0000-0000-000000000002"
  subscription_id = "00000000-0000-0000-0000-000000000000"

  use_cli  = false
  use_msi  = false
  use_oidc = false

  skip_provider_registration = true
}
```

No `env.sh sourcing`, no `az login`, no `ARM_*` environment variables.

## How it works under the hood

### 1. Cloud discovery via `/metadata/endpoints`

The provider's first call is `GET https://localhost:4569/metadata/endpoints?api-version=2022-09-01`. LocalStack (`localstack-core/localstack/azure/gateway.py:49`) returns a body whose key fields are:

```json
{
  "name": "AzureCloud",
  "authentication": {
    "tenant": "common",
    "identityProvider": "AAD",
    "loginEndpoint": "https://localhost:4569",
    "audiences": ["https://localhost:4569"]
  },
  "resourceManager": "https://localhost:4569",
  "graph":           "https://localhost:4569",
  "suffixes": { "storage": "core.windows.net", ... }
}
```

`name=AzureCloud` + `identityProvider=AAD` are mandatory — anything else makes `go-azure-helpers` classify the response as Azure Stack and abort with *"The AzureRM Provider … does not support Azure Stack"*.

### 2. Token exchange

`POST https://localhost:4569/<tenant>/oauth2/v2.0/token` is served by `azure/services/entra/token_router.py`. It hands out a JWT-shaped opaque token that the rest of the emulator accepts at face value (no signature verification).

### 3. Service-principal lookup (Microsoft Graph)

The provider then resolves the object ID of the calling service principal:

```
GET https://localhost:4569/v1.0/servicePrincipals(appId='00000000-0000-0000-0000-000000000001')
```

Handled by `azure/services/entra/graph_router.py`. Two URL shapes are supported:

- `?$filter=appId eq '<uuid>'` (older SDKs)
- OData key-call `(appId='<uuid>')` (current `hashicorp/go-azure-sdk`)

Object IDs are deterministic — `sha256(client_id)` truncated to a UUID layout.

The multi-cloud router (`localstack-core/localstack/aws/handlers/multi_cloud.py`) needs to recognize the OData key-call form, otherwise `/v1.0/servicePrincipals(appId='...')` is parsed as the S3 bucket `v1.0` and returns `NoSuchBucket`. The fix lives in `_looks_like_azure_graph`, which now strips `(` from the path segment before matching.

### 4. ARM control plane

`azure/arm_router.py` serves:

- `/subscriptions`, `/tenants`, `/subscriptions/<id>/locations`, `/subscriptions/<id>/providers[/<ns>[/register|/unregister]]`
- `/subscriptions/<id>/resourceGroups/<rg>` CRUD
- Nested resources at `/subscriptions/<id>/resourceGroups/<rg>/providers/<ns>/<type>/<name>` with full CRUD
- Resource actions (`POST .../listKeys`) — returns two deterministic dummy keys
- Sub-resources (`/blobServices/default`, `/fileServices/default`, `/queueServices/default`, `/tableServices/default`)

`azure/arm_serializers.py` enriches storage account GETs with `properties.primaryEndpoints`/`secondaryEndpoints`, `sku`, `kind`, `identity`. Without those fields the azurerm provider fails with `model.Properties.PrimaryEndpoints was nil`.

### 5. Storage data plane

`<account>.blob.core.windows.net` resolves to `127.0.0.1:443` via `/etc/hosts`, hits the TLS sidecar, then LocalStack. The blob and queue routers (`azure/services/storage/{blob,queue}_router.py`) implement enough of the REST API for `terraform plan`/`apply` to converge: service properties (`?restype=service&comp=properties`), service stats, container/queue list, container/queue CRUD.

## Helper scripts

| Script                       | Purpose |
|------------------------------|---------|
| `bin/setup-azure-tls`        | Install mkcert CA + issue sidecar cert covering all Azure hostnames |
| `bin/azure-register-host`    | Add (or `--remove`) `/etc/hosts` entries for a storage account's six storage subdomains |
| `bin/docker-sync.sh`         | Copy in-tree Python changes (incl. `localstack-core/localstack/azure/`) into the running container without rebuilding the image |

## Troubleshooting

**`x509: certificate signed by unknown authority`** — run `make setup-azure-tls`. mkcert needs to install its root CA into the OS trust store at least once.

**`The AzureRM Provider … does not support Azure Stack`** — `/metadata/endpoints` is returning the wrong shape. Verify with:

```bash
curl -ks https://localhost:4569/metadata/endpoints?api-version=2022-09-01 | jq '.name, .authentication.identityProvider, .authentication.tenant'
```

Expected: `"AzureCloud"`, `"AAD"`, `"common"`. If you edited `azure/gateway.py`, re-run `bin/docker-sync.sh` then `docker restart localstack-main`.

**`NoSuchBucket … BucketName>v1.0`** — multi-cloud router did not recognize the path as Microsoft Graph. Confirm `localstack-core/localstack/aws/handlers/multi_cloud.py:_looks_like_azure_graph` strips `(` (so OData key-call paths are detected) and the in-container copy is current.

**`model.Properties.PrimaryEndpoints was nil`** — `azure/arm_serializers.py` did not synthesize the storage endpoints block; sync the container and restart.

**Storage data plane times out** — likely `/etc/hosts` not registered. Re-run `bin/azure-register-host <account>` and confirm with `dscacheutil -q host -a name <account>.blob.core.windows.net` (macOS) or `getent hosts <account>.blob.core.windows.net` (Linux).

## Known limits

- No real authentication. Any non-empty bearer token is accepted; `client_secret` is not verified.
- `listKeys` returns deterministic dummy keys (`AAAA…`); do not embed them in real Azure clients expecting parity with a real account.
- Queue / table / file data planes are partial — control plane works, full message/row CRUD is in progress (`docs/superpowers/plans/2026-05-22-azure-services-parity.md`).
- Persistence across container restarts depends on `PERSISTENCE=1` (set in `docker-compose.yml`).
