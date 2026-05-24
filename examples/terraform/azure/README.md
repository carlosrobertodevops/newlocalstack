# Terraform · Azure on LocalStack

Provisiona Resource Group + Storage Account + Container via `azurerm` provider
apontando para o gateway TLS local (`https://localhost:4569`).

## ⚠ macOS: trust-cert.sh é OBRIGATÓRIO

Go (que roda dentro do `terraform-provider-azurerm`) em **macOS lê APENAS o Keychain
do sistema** e ignora `SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`.
Em macOS env vars NÃO resolvem o `x509: certificate signed by unknown authority`.

Solução única em macOS — rode **uma vez**:

```bash
cd examples/terraform/azure
./trust-cert.sh                 # sudo: instala cert no /Library/Keychains/System.keychain
```

Depois disso, `terraform plan` funciona em qualquer shell.

Linux: env vars (`source ./setup-env.sh`) bastam — Go honra `SSL_CERT_FILE`.

## Pré-requisitos

1. LocalStack + sidecar TLS rodando:
   ```bash
   docker-compose up -d localstack localstack-tls
   ```
2. Terraform >= 1.5.
3. (Opcional) `tflocal`: `pip install terraform-local`.

## Fluxo recomendado (qualquer SO)

```bash
cd examples/terraform/azure
make setup        # roda trust-cert.sh + terraform init
make plan
make apply
make destroy
```

`make setup` instala cert + inicializa. Depois `plan/apply/destroy` funcionam direto.

## Caminhos alternativos

### Sem Makefile (qualquer SO depois de `./trust-cert.sh`)

```bash
export ARM_CLIENT_ID="00000000-0000-0000-0000-000000000001"
export ARM_CLIENT_SECRET="test-secret"
export ARM_TENANT_ID="localstack-tenant"
export ARM_SUBSCRIPTION_ID="00000000-0000-0000-0000-000000000000"
export ARM_METADATA_HOST="localhost:4569"
terraform init && terraform plan
```

### Wrapper local (somente Linux ou macOS pós-trust)

```bash
./tflocal-azure init
./tflocal-azure apply -auto-approve
```

### direnv (Linux ou macOS pós-trust)

```bash
direnv allow
tflocal apply -auto-approve     # PATH_add . resolve wrapper local
```

## Troubleshoot

### `tls: failed to verify certificate: x509: certificate signed by unknown authority`

| OS    | Fix                                                                        |
|-------|----------------------------------------------------------------------------|
| macOS | `./trust-cert.sh` (única via — Go ignora `SSL_CERT_FILE` em darwin)        |
| Linux | `./trust-cert.sh` OU `export SSL_CERT_FILE=$(pwd)/../../../localstack-tls/certs/cert.pem` |

Verificar trust:
```bash
curl -fsv https://localhost:4569/_localstack/health 2>&1 | grep -i "verify\|ok"
```

### `dial tcp 127.0.0.1:4569: connect: connection refused`

Sidecar TLS não está up: `docker-compose ps localstack-tls`.

### Cert expirado ou CN não cobre `localhost`

Regenere em `localstack-tls/certs/` (mantenha `localhost` em CN/SAN).
Se já usou `trust-cert.sh`, rode `./trust-cert.sh remove` antes da regeneração.

### Remover trust depois

```bash
./trust-cert.sh remove
```
