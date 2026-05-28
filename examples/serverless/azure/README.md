# Serverless Framework — Azure contra LocalStack

Status: **parcial**. O plugin `serverless-azure-functions` é third-party e tem suporte limitado a endpoints customizados. Cobertura atual: HTTP triggers, sem bindings (storage, queue, eventgrid).

## Setup

```bash
make setup-azure-tls          # (raiz do repo) — uma vez por máquina
docker-compose up -d
npm install serverless-azure-functions
```

## Variáveis necessárias

Crie `env.sh` (ou exporte direto):

```bash
export AZURE_CLIENT_ID=00000000-0000-0000-0000-000000000001
export AZURE_CLIENT_SECRET=test-secret
export AZURE_TENANT_ID=localstack-tenant
export AZURE_SUBSCRIPTION_ID=00000000-0000-0000-0000-000000000000
export ARM_METADATA_HOST=localhost:4569
export NODE_EXTRA_CA_CERTS="$(mkcert -CAROOT)/rootCA.pem"
```

## Deploy

```bash
source env.sh
serverless deploy --stage dev
```

## Alternativa recomendada

Para fluxos completos (timers, queue triggers, blob triggers), use **Azure Functions Core Tools** (`func`) direto:

```bash
cd ../../terraform/azure
terraform apply -auto-approve   # provisiona function app
cd /seu/projeto/functions
func azure functionapp publish <name>
```

Detalhes: [`docs/guides/serverless-framework.md`](../../../docs/guides/serverless-framework.md#azure).

## Cleanup

```bash
serverless remove --stage dev
# OU
curl -X POST http://localhost:4566/_localstack/clouds/azure/stack/reset \
  -H 'Content-Type: application/json' -d '{"confirm": true}'
```
