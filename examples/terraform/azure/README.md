# Terraform + LocalStack Azure

Cria resource group, storage account e storage container contra a emulação Azure do LocalStack — sem `az login` nem env vars.

Guia completo em [`docs/azure-terraform.md`](../../../docs/azure-terraform.md).

## Setup único

```bash
# raiz do repo
make setup-azure-tls
docker-compose up -d
bin/azure-register-host tflocalstackstor
```

## Rodar

```bash
terraform init
terraform plan
terraform apply -auto-approve
```

`main.tf` já é auto-suficiente: credenciais dummy embutidas, `metadata_host = "localhost:4569"`, `use_cli/msi/oidc = false`.

## Limpar

```bash
terraform destroy -auto-approve
```

Reset total do provider Azure (isolado):

```bash
curl -X POST http://localhost:4566/_localstack/clouds/azure/stack/reset \
  -H 'Content-Type: application/json' \
  -d '{"confirm": true}'
```

Equivalente ao botão **"Limpar Stack"** na aba Azure do console.

## Troubleshooting

Erros comuns + mitigação em [`docs/azure-terraform.md`](../../../docs/azure-terraform.md#troubleshooting).
