# Serverless Framework + LocalStack

Exemplos de deploy do **Serverless Framework v3** contra a emulação multi-cloud do LocalStack.

| Provider | Subdiretório   | Plugin                             | Status   |
|----------|----------------|------------------------------------|----------|
| AWS      | `aws/`         | `serverless-localstack`            | OK — paridade alta |
| Azure    | `azure/`       | `serverless-azure-functions`       | Parcial — HTTP triggers |
| GCP      | `gcp/`         | `serverless-google-cloudfunctions` | Parcial — HTTP triggers |

Guia detalhado: [`docs/serverless-framework.md`](../../docs/serverless-framework.md).

## Pré-requisitos comuns

```bash
docker-compose up -d           # raiz do repo
npm install -g serverless@3
```

## AWS

```bash
cd aws
npm install serverless-localstack
serverless deploy --stage dev
serverless invoke --function hello --stage dev
```

O plugin reescreve todos os SDKs AWS para `http://localhost:4566`.

## Azure

```bash
cd azure
npm install serverless-azure-functions
source env.sh         # vars descritas em serverless.yml
serverless deploy --stage dev
```

Cobertura hoje: HTTP triggers + provisionamento de Storage Account via ARM. Outros bindings (queue, blob, eventgrid) exigem extensões ainda não wired no provider Azure do LocalStack — use Azure Functions Core Tools (`func`) para fluxos completos.

## GCP

```bash
cd gcp
npm install serverless-google-cloudfunctions
export CLOUDSDK_API_ENDPOINT_OVERRIDES_CLOUDFUNCTIONS=http://localhost:4566/
export GOOGLE_OAUTH_ACCESS_TOKEN=dummy
serverless deploy --stage dev
```

Cobertura: Cloud Functions Gen 1 com HTTP trigger. Triggers Pub/Sub funcionam se o tópico for criado antes (`gcloud pubsub topics create ... --endpoint=...`).

## Verificar via console

Aba **<Provider> → Stack (Em ação)** lista funções e recursos auxiliares.

## Cleanup

Por exemplo:

```bash
serverless remove --stage dev
```

Reset total por provedor (botão **"Limpar Stack"** no console, ou API):

```bash
curl -X POST http://localhost:4566/_localstack/clouds/<aws|azure|gcp>/stack/reset \
  -H 'Content-Type: application/json' -d '{"confirm": true}'
```

A ação é **isolada por cloud** — limpar AWS não afeta Azure/GCP.
