# Terraform + LocalStack GCP

Guia end-to-end para usar `hashicorp/google` (v5.30+) contra a emulação GCP do LocalStack — sem service account real nem `gcloud auth`.

Exemplo: [`examples/terraform/gcp/main.tf`](../examples/terraform/gcp/main.tf).

## O que funciona hoje

| Recurso                          | Status |
|----------------------------------|--------|
| `google_storage_bucket`          | OK     |
| `google_pubsub_topic`            | OK     |
| `google_pubsub_subscription`     | OK     |
| `google_secret_manager_secret`   | parcial |
| `google_cloudfunctions2_function`| parcial |
| `google_bigquery_dataset`        | parcial |

## Setup

```bash
docker-compose up -d
```

Não precisa de mkcert nem `/etc/hosts` — GCP roda em HTTP em `:4566`.

## Rodar

```bash
cd examples/terraform/gcp
terraform init
terraform plan
terraform apply -auto-approve
```

Provider block (em `main.tf`):

```hcl
provider "google" {
  project = "localstack-project"
  region  = "us-central1"
  zone    = "us-central1-a"

  access_token = "localstack-dummy-token"

  storage_custom_endpoint         = "http://localhost:4566/storage/v1/"
  pubsub_custom_endpoint          = "http://localhost:4566/"
  firestore_custom_endpoint       = "http://localhost:4566/"
  cloud_functions_custom_endpoint = "http://localhost:4566/"
  iam_custom_endpoint             = "http://localhost:4566/"
  big_query_custom_endpoint       = "http://localhost:4566/bigquery/v2/"
  # ... ver main.tf completo
}
```

Sem `GOOGLE_APPLICATION_CREDENTIALS`, sem `gcloud auth login`.

## Como funciona

### 1. Token bearer

O LocalStack aceita **qualquer** bearer no header `Authorization`. O provider passa `access_token` direto no provider block → evita ADC (Application Default Credentials), que tenta `oauth2.googleapis.com` (shimado, mas o ADC falha primeiro porque procura JSON local).

### 2. Endpoint override por serviço

`hashicorp/google` aceita `*_custom_endpoint` em cada API. Cada um vira override no SDK Go gerado a partir do discovery doc. LocalStack roteia por path-prefix:

- `/storage/v1/...` → `localstack.gcp.services.storage.StorageJsonRouter`
- `/v1/projects/<id>/topics/...` → `localstack.gcp.services.pubsub.PubSubRouter`
- `/bigquery/v2/...` → `localstack.gcp.services.bigquery.BigQueryRouter`

Roteamento detectado em `localstack-core/localstack/aws/handlers/multi_cloud.py:_looks_like_gcp_v1_projects()`.

### 3. Per-project state

Os recursos vivem em `GcpStores._projects[project_id]` (case-insensitive). Cada `provider.project` produz um namespace independente.

## Troubleshooting

**`google: could not find default credentials`** — Você está exportando `GOOGLE_APPLICATION_CREDENTIALS` apontando para arquivo inexistente. Remova essa env var; deixe o provider usar `access_token` inline.

**`Unauthenticated`** — Falta o `access_token` no provider block. Adicione `access_token = "localstack-dummy-token"`.

**`bucket already exists`** — Estado GCP persistido. Reset via:

```bash
curl -X POST http://localhost:4566/_localstack/clouds/gcp/stack/reset \
  -H 'Content-Type: application/json' -d '{"confirm": true}'
```

**`connection refused`** — LocalStack offline. Suba com `docker-compose up -d`.

## Limites conhecidos

- IAM bindings (`google_project_iam_binding`) parcial — aceito mas não enforced.
- Cloud Run revisions: deploy reconhecido, mas o runtime não executa containers.
- BigQuery: estrutura de datasets/tabelas existe, sem query engine.

## Pointers

- Gateway GCP: `localstack-core/localstack/gcp/gateway.py`
- Stores: `localstack-core/localstack/gcp/stores.py`
- Reset isolado: ver [`docs/guides/multi-cloud-stack.md`](../guides/multi-cloud-stack.md#5-isolamento-entre-provedores)
