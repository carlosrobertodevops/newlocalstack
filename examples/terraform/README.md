# Terraform examples — AWS · Azure · GCP via LocalStack

Three single-file Terraform configs that exercise the LocalStack
multi-cloud emulator. Each runs the matching `terraform init/plan/apply`
against the local edge.

## Prereqs

```bash
# 1. Start LocalStack + TLS sidecar
docker compose up -d localstack localstack-tls localstack-ui

# 2. Install terraform >= 1.5
brew install terraform   # or https://developer.hashicorp.com/terraform/install
```

## AWS

```bash
cd aws
terraform init
terraform apply -auto-approve
terraform destroy -auto-approve
```

Uses `http://localhost:4566` and the standard
`access_key = "test", secret_key = "test"` LocalStack credentials.

## Azure

```bash
cd azure
source env.sh           # exports ARM_* creds + SSL_CERT_FILE + GODEBUG fallback

terraform init
terraform plan
terraform apply -auto-approve
```

`env.sh` sets every variable the `azurerm` provider needs and exposes
the self-signed TLS sidecar cert via `SSL_CERT_FILE` and
`GODEBUG=x509usefallbackroots=1`.

### Cert trust on macOS

Go's `crypto/x509` on macOS uses `Security.framework` and may ignore
`SSL_CERT_FILE` even with the fallback flag set. If `terraform plan`
still fails with:

```
tls: failed to verify certificate: x509: certificate signed by unknown authority
```

run the helper to add the cert to the System keychain as a trusted
root (requires `sudo`):

```bash
./trust-cert-macos.sh         # add
./trust-cert-macos.sh remove  # undo
```

On Linux, `SSL_CERT_FILE` alone is enough — no keychain step needed.

## GCP

```bash
cd gcp
export GOOGLE_OAUTH_ACCESS_TOKEN=dummy-token
export GOOGLE_PROJECT=localstack-project

terraform init
terraform apply -auto-approve
```

No TLS needed for GCP — gcloud SDKs accept HTTP when endpoints are
overridden explicitly.

## Notes

- The `terraform destroy` plans rebuild the same resources on the next
  `apply`. State lives in `terraform.tfstate` in each example directory.
- LocalStack data is volatile by default; set `PERSISTENCE=1` in
  `docker-compose.yml` to persist between container restarts.
- Only services listed under `localstack/{aws,azure,gcp}/services/` are
  emulated — exotic resources (Azure AKS, GCP GKE, AWS Macie) will fail
  with 404 from the gateway.
