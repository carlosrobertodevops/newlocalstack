# Serverless Framework + LocalStack

Como usar o **Serverless Framework v3** contra a emulação multi-cloud do LocalStack — AWS, Azure e GCP.

Exemplos: [`examples/serverless/`](../examples/serverless/).

## Status por provider

| Provider | Plugin                              | Cobertura |
|----------|-------------------------------------|-----------|
| AWS      | `serverless-localstack`             | Alta — paridade próxima de cloud real |
| Azure    | `serverless-azure-functions`        | Parcial — HTTP triggers + storage account ARM |
| GCP      | `serverless-google-cloudfunctions`  | Parcial — Cloud Functions Gen 1 HTTP |

## Pré-requisitos

```bash
docker-compose up -d
npm install -g serverless@3
```

## AWS

```bash
cd examples/serverless/aws
npm install serverless-localstack
serverless deploy --stage dev
```

O plugin `serverless-localstack` reescreve transparentemente cada SDK call para `http://localhost:4566`. Configuração em `custom.localstack`:

```yaml
custom:
  localstack:
    stages: [dev]
    host: http://localhost
    edgePort: 4566
```

Resources como `AWS::DynamoDB::Table` definidos em `resources.Resources` são processados via CloudFormation contra o emulador.

Invocar:

```bash
serverless invoke --function hello --stage dev
# ou via API Gateway endpoint exposto
curl http://localhost:4566/restapis/<id>/dev/_user_request_/hello
```

## Azure

Status: **parcial**. O plugin `serverless-azure-functions` é third-party e foi descontinuado pela vendor. Cobertura no LocalStack:

- HTTP triggers: OK
- ARM resource (Microsoft.Web/sites): provisionamento OK
- Bindings de storage/queue/blob/eventgrid: **não implementados** no `serverless-azure-functions` para endpoints customizados

Setup (uma vez por máquina):

```bash
make setup-azure-tls     # mkcert + cert TLS sidecar
```

Variáveis (em `env.sh`):

```bash
export AZURE_CLIENT_ID=00000000-0000-0000-0000-000000000001
export AZURE_CLIENT_SECRET=test-secret
export AZURE_TENANT_ID=localstack-tenant
export AZURE_SUBSCRIPTION_ID=00000000-0000-0000-0000-000000000000
export ARM_METADATA_HOST=localhost:4569
export NODE_EXTRA_CA_CERTS="$(mkcert -CAROOT)/rootCA.pem"
```

Deploy:

```bash
cd examples/serverless/azure
npm install serverless-azure-functions
source env.sh
serverless deploy --stage dev
```

### Alternativa para fluxos completos

Para functions com triggers não-HTTP, use **Azure Functions Core Tools** (`func`) direto:

```bash
# Provisione function app via Terraform
cd examples/terraform/azure && terraform apply -auto-approve

# Deploy do código
cd /seu/projeto/functions
func azure functionapp publish <name> --target-host localhost:4569
```

`func` lida melhor com os bindings nativos do runtime.

## GCP

Status: **parcial**. `serverless-google-cloudfunctions` assume Cloud Build (não emulado), mas o upload direto para Cloud Functions Gen 1 via endpoint override funciona para HTTP triggers.

Setup:

```bash
cd examples/serverless/gcp
npm install serverless-google-cloudfunctions
```

Crie `key.json` dummy (template em [`examples/serverless/gcp/README.md`](../examples/serverless/gcp/README.md)).

Deploy:

```bash
export CLOUDSDK_API_ENDPOINT_OVERRIDES_CLOUDFUNCTIONS=http://localhost:4566/
export GOOGLE_OAUTH_ACCESS_TOKEN=dummy-token
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/key.json
serverless deploy --stage dev
```

Cobertura:

- HTTP triggers: OK
- Pub/Sub triggers: tópico provisionado, mas `eventarc` não dispara end-to-end
- Storage triggers: idem

## Verificar via console

Após qualquer deploy, abra **<Provider> → Stack (Em ação)**:

- AWS: aparece Lambda + tabela + filas/buckets
- Azure: aparece Microsoft.Web (function app) + Microsoft.Storage
- GCP: aparece functions registry

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

Ação **isolada por cloud**.

## Pointers

- Visão geral multi-cloud: [`docs/multi-cloud-stack.md`](multi-cloud-stack.md)
- Console: [`docs/console-stack-view.md`](console-stack-view.md)
- Plugins:
  - https://github.com/localstack/serverless-localstack
  - https://github.com/serverless/serverless-azure-functions
  - https://github.com/serverless/serverless-google-cloudfunctions
