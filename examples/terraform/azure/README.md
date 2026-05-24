# Terraform · Azure on LocalStack

Provisiona Resource Group + Storage Account + Container via `azurerm` provider
apontando para o gateway TLS local (`https://localhost:4569`).

## Pré-requisitos

1. LocalStack + sidecar TLS rodando:
   ```bash
   docker-compose up -d localstack localstack-tls
   ```
2. Terraform >= 1.5.
3. (Opcional) `tflocal`: `pip install terraform-local`.

## Caminho 1 — DEFINITIVO: instalar cert no sistema (uma vez)

Resolve TLS para `tflocal`, `terraform`, `az`, `curl`, qualquer ferramenta —
sem env var, sem wrapper, em qualquer shell.

```bash
cd examples/terraform/azure
./trust-cert.sh                 # sudo: instala cert no keychain (macOS) ou /usr/local/share/ca-certificates (Linux)
```

Depois disso, basta:

```bash
export ARM_CLIENT_ID="00000000-0000-0000-0000-000000000001"
export ARM_CLIENT_SECRET="test-secret"
export ARM_TENANT_ID="localstack-tenant"
export ARM_SUBSCRIPTION_ID="00000000-0000-0000-0000-000000000000"
export ARM_METADATA_HOST="localhost:4569"
tflocal apply -auto-approve     # funciona em qualquer dir, qualquer shell
```

Remover depois: `./trust-cert.sh remove`

## Caminho 2 — Makefile (sem trust, sem direnv)

```bash
cd examples/terraform/azure
make setup     # roda trust + init
make plan
make apply
make destroy
```

`make` invoca `./tflocal-azure` que auto-exporta os envs no mesmo shell.

## Caminho 3 — wrapper local

```bash
cd examples/terraform/azure
./tflocal-azure init
./tflocal-azure apply -auto-approve
```

## Caminho 4 — direnv

```bash
direnv allow                    # uma vez
cd .                            # sai/entra; envs carregam via .envrc
tflocal apply -auto-approve     # `tflocal` resolve para shim via PATH_add .
```

## Caminho 5 — manual

```bash
source ./setup-env.sh
terraform init && terraform apply -auto-approve
```

## Troubleshoot

### `tls: failed to verify certificate: x509: certificate signed by unknown authority`

Cert não confiado pelo Go HTTP do `azurerm`. Soluções por ordem de robustez:

1. `./trust-cert.sh` (definitivo, qualquer shell)
2. `make apply` ou `./tflocal-azure apply` (wrapper local)
3. `source ./setup-env.sh && terraform apply` (manual)

Verifique env no shell atual:
```bash
echo "$SSL_CERT_FILE"
test -f "$SSL_CERT_FILE" && echo OK || echo MISSING
```

### `dial tcp 127.0.0.1:4569: connect: connection refused`

Sidecar TLS não está up. `docker-compose ps localstack-tls`.

### Cert expirado ou CN não cobre `localhost`

Regenere em `localstack-tls/certs/` (mantenha `localhost` em CN/SAN).
Se já usou `trust-cert.sh`, rode `./trust-cert.sh remove` antes da regeneração.
