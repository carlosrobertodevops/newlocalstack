# Terraform + LocalStack GCP

Cria bucket Cloud Storage, tópico Pub/Sub e subscription contra a emulação GCP do LocalStack — sem service account real.

## Pré-requisitos

- LocalStack rodando (`docker-compose up -d`) escutando em `:4566`.
- Terraform >= 1.5.

## Rodar

```bash
terraform init
terraform plan
terraform apply -auto-approve
```

O provider está configurado com `access_token = "localstack-dummy-token"` (o gateway aceita qualquer bearer) e cada API GCP aponta para `http://localhost:4566`. Evite `GOOGLE_APPLICATION_CREDENTIALS` — usaríamos um round-trip a `oauth2.googleapis.com` que já é shimado, mas ADC tende a falhar primeiro.

Variáveis úteis (opcional):

```bash
export GOOGLE_PROJECT=localstack-project
export GOOGLE_OAUTH_ACCESS_TOKEN=dummy-token
```

## Verificar via console

Aba **GCP → Stack (Em ação)** mostra bucket, topic e subscription com contagem.

## Limpar

```bash
terraform destroy -auto-approve
```

Reset total do provider GCP (isolado dos outros provedores):

```bash
curl -X POST http://localhost:4566/_localstack/clouds/gcp/stack/reset \
  -H 'Content-Type: application/json' \
  -d '{"confirm": true}'
```

## Recursos suportados hoje

| Recurso                          | Status |
|----------------------------------|--------|
| `google_storage_bucket`          | OK     |
| `google_pubsub_topic`            | OK     |
| `google_pubsub_subscription`     | OK     |
| `google_secret_manager_secret`   | parcial |
| `google_cloudfunctions2_function`| parcial |

Mais detalhes: `docs/multi-cloud-stack.md`.
