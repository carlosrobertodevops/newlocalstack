# Serverless Framework — GCP contra LocalStack

Status: **parcial**. O plugin `serverless-google-cloudfunctions` aceita endpoint override via env vars, mas a deploy pipeline assume Cloud Build (não emulado). HTTP triggers funcionam; eventos Pub/Sub aparecem como recursos provisionados mas o trigger não dispara end-to-end.

## Setup

```bash
npm install serverless-google-cloudfunctions
```

LocalStack rodando em `:4566`.

## Variáveis

```bash
export CLOUDSDK_API_ENDPOINT_OVERRIDES_CLOUDFUNCTIONS=http://localhost:4566/
export GOOGLE_OAUTH_ACCESS_TOKEN=dummy-token
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/key.json
```

Crie um `key.json` dummy:

```json
{
  "type": "service_account",
  "project_id": "localstack-project",
  "private_key_id": "key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...IDAQAB\n-----END PRIVATE KEY-----\n",
  "client_email": "test@localstack.iam.gserviceaccount.com",
  "client_id": "test-client",
  "auth_uri": "http://localhost:4566/oauth2/token",
  "token_uri": "http://localhost:4566/oauth2/token"
}
```

## Deploy

```bash
serverless deploy --stage dev
```

## Verificar via console

Aba **GCP → Stack (Em ação)** lista a função criada.

## Cleanup

```bash
serverless remove --stage dev
# OU
curl -X POST http://localhost:4566/_localstack/clouds/gcp/stack/reset \
  -H 'Content-Type: application/json' -d '{"confirm": true}'
```
