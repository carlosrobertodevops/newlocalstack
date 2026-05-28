# Multi-cloud Stack — guia geral

O LocalStack neste fork emula três provedores em paralelo: **AWS**, **Azure** e **GCP**. Todos os recursos criados ficam disponíveis simultaneamente e podem ser inventariados ou resetados de forma **isolada por provedor**.

Este documento cobre:

1. Portas e endpoints
2. Como criar recursos via cada caminho (CLI / Terraform / Serverless / console)
3. API REST de gestão (`/_localstack/clouds/...`) — listar, remover, resetar
4. Página "Stack (Em ação)" no console
5. Princípio de isolamento entre provedores

## 1. Portas e endpoints

| Cloud | Edge HTTP        | Edge HTTPS (TLS sidecar) | Observações |
|-------|------------------|--------------------------|-------------|
| AWS   | `:4566`          | —                        | Todos os SDKs apontam para `http://localhost:4566` |
| Azure | `:4569`          | `:443` (via sidecar `localstack-tls`) | TLS necessário para `terraform-provider-azurerm` (rejeita URLs com porta) |
| GCP   | `:4566`          | —                        | Compartilha o edge AWS via roteador multi-cloud |

`docker/compose.yml` já sobe ambos os contêineres (`localstack-main` + `localstack-tls`). O roteamento multi-cloud é decidido em `localstack-core/localstack/aws/handlers/multi_cloud.py`.

## 2. Caminhos de criação

### 2.1 Via CLI nativa de cada cloud

Exemplos em [`examples/cli/`](../examples/cli/). AWS usa `aws --endpoint-url`. Azure e GCP usam `curl` (CLIs nativas não têm endpoint override universal).

### 2.2 Via Terraform

Exemplos em [`examples/terraform/`](../examples/terraform/). Cada `main.tf` é auto-suficiente: credenciais dummy + endpoint overrides para LocalStack.

Guias específicos:

- [`docs/azure-terraform.md`](azure-terraform.md)
- [`docs/gcp-terraform.md`](gcp-terraform.md)

### 2.3 Via Serverless Framework

Exemplos em [`examples/serverless/`](../examples/serverless/). Cobertura variada — AWS é completo, Azure e GCP são parciais. Detalhes em [`docs/serverless-framework.md`](serverless-framework.md).

### 2.4 Via console

Aba **"<Provider> → Resources"** permite criar recursos via UI (formulários simples para cada serviço). A aba **"Stack (Em ação)"** mostra o inventário consolidado.

## 3. API REST de gestão

Implementada em `localstack-core/localstack/aws/services/_localstack_stack.py`, exposta pelo `LocalstackResources` router (`internal.py`).

### Listar provedores registrados

```bash
curl http://localhost:4566/_localstack/clouds
```

Retorna `{clouds: [{name, display_name, package, services_count}]}`.

### Health de um provedor

```bash
curl http://localhost:4566/_localstack/clouds/azure/health
```

### Info técnico de um provedor

```bash
curl http://localhost:4566/_localstack/clouds/gcp/info
```

### Inventário "Stack (Em ação)"

```bash
curl http://localhost:4566/_localstack/clouds/aws/stack
```

Retorna:

```json
{
  "cloud": "aws",
  "services": [
    {"service": "s3", "resource_count": 3},
    {"service": "sqs", "resource_count": 1}
  ],
  "total_resources": 4,
  "total_services": 2
}
```

Mesma forma para `azure` e `gcp` (campos `service` variam: `Microsoft.Storage`, `storage`, etc).

### Remover todos recursos de um serviço

```bash
curl -X DELETE \
  http://localhost:4566/_localstack/clouds/azure/stack/services/Microsoft.Storage
```

Retorna `{cloud, service, reset: [service], items_cleared|regions_cleared}`.

### Reset total de um provedor

```bash
curl -X POST http://localhost:4566/_localstack/clouds/aws/stack/reset \
  -H 'Content-Type: application/json' \
  -d '{"confirm": true}'
```

O campo `confirm: true` é **obrigatório** — proteção contra requisição acidental.

Retorna `{cloud, reset: [list of services cleared]}`.

## 4. Página "Stack (Em ação)" no console

Rotas:

- `/aws/stack`
- `/azure/stack`
- `/gcp/stack`

Layout:

- Header com contagem total de recursos + provedor selecionado.
- Lista de serviços (somente os que têm recursos ativos), cada um expansível para mostrar nomes individuais.
- Botão **"Remover"** por serviço (vermelho, ícone lixeira) → confirmação modal → chama `DELETE /_localstack/clouds/<cloud>/stack/services/<service>`.
- Botão **"Limpar Stack"** (vermelho, no header) → confirmação modal → chama `POST /_localstack/clouds/<cloud>/stack/reset`.
- Auto-refresh: react-query refetch a cada 20s.

Detalhes em [`docs/console-stack-view.md`](console-stack-view.md).

## 5. Isolamento entre provedores

**Princípio fundamental**: limpar a stack de um provedor **não afeta** os outros.

- `POST /_localstack/clouds/aws/stack/reset` zera apenas estado AWS (Moto backends + stores nativos LocalStack para serviços AWS).
- `POST /_localstack/clouds/azure/stack/reset` zera apenas a gateway Azure (`AzureStores`, storage data plane, cosmos data plane, functions registry).
- `POST /_localstack/clouds/gcp/stack/reset` zera apenas a gateway GCP (`GcpStores`, storage/pubsub/firestore/iam data planes, functions registry).

Cada implementação clear/reset vive no módulo do cloud correspondente (`localstack-core/localstack/{aws,azure,gcp}/`). Não há cross-talk acidental porque os stores são instâncias distintas por gateway.

## Pointers

- Arquitetura multi-cloud: `localstack-core/localstack/cloud/` (`registry.py`, `base.py`, `builtin.py`).
- Roteamento de requests: `localstack-core/localstack/aws/handlers/multi_cloud.py`.
- Endpoints stack: `localstack-core/localstack/aws/services/_localstack_stack.py`.
- Página console: `localstack-ui/console/src/routes/stack.tsx`.
- Helper TS: `localstack-ui/console/src/lib/api/stack.ts`.
