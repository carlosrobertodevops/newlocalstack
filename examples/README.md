# LocalStack Examples & Labs Catalog

Catálogo de 9 labs demonstrando LocalStack across 3 cloud providers (AWS, Azure, GCP) com 3 ferramentas (Terraform, Serverless Framework, CLI).

## Lab Catalog

| ID | Cloud | Ferramenta | Steps | Cleanup | Docs |
|---|---|---|---|---|---|
| terraform-aws | AWS | Terraform | init, plan, apply | destroy | [README](terraform/aws/README.md) |
| terraform-azure | Azure | Terraform | init, plan, apply | destroy | [README](terraform/azure/README.md) |
| terraform-gcp | GCP | Terraform | init, plan, apply | destroy | [README](terraform/gcp/README.md) |
| serverless-aws | AWS | Serverless | install, deploy, invoke | remove | [README](serverless/aws/README.md) |
| serverless-azure | Azure | Serverless | setup-tls, install, deploy | remove | [README](serverless/azure/README.md) |
| serverless-gcp | GCP | Serverless | install, deploy, invoke | remove | [README](serverless/gcp/README.md) |
| cli-aws | AWS | CLI | bash demo.sh | stack reset | [README](cli/aws/README.md) |
| cli-azure | Azure | CLI | bash demo.sh | stack reset | [README](cli/azure/README.md) |
| cli-gcp | GCP | CLI | bash demo.sh | stack reset | [README](cli/gcp/README.md) |

## Como usar

1. Consulte o README correspondente no link "Docs" acima.
2. Siga os passos listados (init/plan/apply para Terraform, etc).
3. Execute cleanup quando terminar (destroy/remove/stack reset).

## Validação

O catálogo completo está em `labs.yaml`. Para validar a estrutura:

```bash
# usando JSON Schema (lab.schema.json):
python -m jsonschema -i labs.yaml lab.schema.json
```

A estrutura de cada lab segue: `id`, `cloud`, `tool`, `title`, `description`, `steps[]`, `cleanup`, `readme`.

## Notas

- **Catálogo é source-of-truth**: consulte `labs.yaml` para estrutura canonical.
- **Azure TLS**: labs Serverless Azure requerem `make setup-azure-tls` (uma vez por máquina).
- **Stack reset**: cada cloud pode ser resetado isoladamente via endpoints `/_localstack/clouds/<cloud>/stack/reset`.
- **Sem credenciais reais**: todos os labs usam credenciais dummy (test/test) e endpoints localhost (:4566).
