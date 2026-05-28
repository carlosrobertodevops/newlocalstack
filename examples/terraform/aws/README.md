# Terraform + LocalStack AWS

Cria S3 bucket, fila SQS, tabela DynamoDB, ECR, ECS, EKS, RDS e VPC contra a emulação AWS do LocalStack — sem credenciais reais.

## Pré-requisitos

- LocalStack rodando (`docker-compose up -d` na raiz do repo) escutando em `:4566`.
- Terraform >= 1.5.

## Rodar

```bash
terraform init
terraform plan
terraform apply -auto-approve
```

Não precisa exportar `AWS_*` env vars — o provider está com credenciais dummy (`test`/`test`) e todos os endpoints apontados para `http://localhost:4566`.

## Verificar via console

Após o `apply`, abra a aba **AWS → Stack (Em ação)** no console (`localstack-ui/console`). Os recursos criados devem aparecer agrupados por serviço com contagem.

## Limpar

```bash
terraform destroy -auto-approve
```

Alternativa — reset total do provider AWS (não afeta Azure/GCP):

```bash
curl -X POST http://localhost:4566/_localstack/clouds/aws/stack/reset \
  -H 'Content-Type: application/json' \
  -d '{"confirm": true}'
```

Equivalente ao botão vermelho **"Limpar Stack"** no console.

## Troubleshooting

- `connection refused`: LocalStack offline. Suba com `docker-compose up -d`.
- `RDS / EKS lento`: alguns recursos de gestão demoram ao serem emulados pela primeira vez; reexecute o plan.
- Mais detalhes em `docs/guides/multi-cloud-stack.md`.
