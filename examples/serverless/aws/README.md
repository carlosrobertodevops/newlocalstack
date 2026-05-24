# Serverless Framework — AWS contra LocalStack

Deploy de uma Lambda Python (HTTP + S3 trigger) + tabela DynamoDB.

## Setup

```bash
npm install serverless-localstack
```

LocalStack rodando em `:4566`.

## Deploy

```bash
serverless deploy --stage dev
```

O plugin `serverless-localstack` reescreve todos os endpoints AWS para `http://localhost:4566`.

## Invocar

```bash
serverless invoke -f hello
# ou via API Gateway exposto pelo LocalStack
curl http://localhost:4566/restapis/<id>/dev/_user_request_/hello
```

## Verificar via console

Aba **AWS → Stack (Em ação)** mostra a função Lambda + tabela DynamoDB.

## Cleanup

```bash
serverless remove --stage dev
```

Ou reset total AWS:

```bash
curl -X POST http://localhost:4566/_localstack/clouds/aws/stack/reset \
  -H 'Content-Type: application/json' -d '{"confirm": true}'
```
