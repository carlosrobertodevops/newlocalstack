# Console — Stack (Em ação)

Página do console que consolida o inventário de recursos ativos por provedor de cloud, com controles destrutivos por serviço e botão de reset total isolado.

## Onde fica

Rotas no console (`localstack-ui/console`):

- `/aws/stack` — `AwsStack`
- `/azure/stack` — `AzureStack`
- `/gcp/stack` — `GcpStack`

Arquivo: `localstack-ui/console/src/routes/stack.tsx`. Os três componentes apenas chamam `CloudStack` com o `cloud` correspondente.

## O que mostra

Para cada provedor selecionado:

- **Header**: contagem total de recursos + nome do provedor + chip "Em ação".
- **Lista de serviços** com recursos ativos (serviços sem recursos são ocultados):
  - Ícone do serviço, label, tipo de recurso, contagem em badge.
  - Linha expansível listando nomes de cada recurso.
  - Link "Open <serviço> →" para a página dedicada de gestão.
- **Botão "Refresh"** — invalida a cache react-query e força refetch.
- **Botão vermelho "Limpar Stack"** — abre modal de confirmação para reset total.

## Controles destrutivos

### Botão "Remover" por linha

Em cada linha de serviço (canto direito), há um botão vermelho `Trash2` + "Remover":

1. Click → modal: *"Esta ação remove TODOS os recursos do serviço <X> em <CLOUD>. É irreversível e não afeta os outros provedores."*
2. Confirma → `DELETE /_localstack/clouds/<cloud>/stack/services/<service>`
3. Refetch automático

### Botão "Limpar Stack" (CT vermelho)

Header da página, ao lado do Refresh, em `bg-red-600`:

1. Click → modal: *"Esta ação remove TODOS os recursos ativos em <CLOUD> (reset completo). Não afeta os outros provedores. Ação irreversível."*
2. Confirma → `POST /_localstack/clouds/<cloud>/stack/reset` com body `{"confirm": true}`
3. Refetch automático

O campo `confirm: true` é obrigatório no body — proteção server-side. Sem ele, a API responde `400 reset refused`.

## Auto-refresh

React-query refetch a cada **20 segundos** (`refetchInterval: 20_000`). Recursos criados via Terraform / Serverless / CLI aparecem em < 20s sem ação do usuário.

`staleTime: 10_000` evita refetch redundante quando se navega entre páginas.

## Wiring backend ↔ frontend

```
DELETE /_localstack/clouds/<cloud>/stack/services/<service>
       ↓
localstack-core/localstack/aws/services/_localstack_stack.py
  CloudStackServiceResource.on_delete()
       ↓
{aws|azure|gcp}_reset_service(...)
```

Mapeamento de IDs entre frontend e backend:

- AWS: o `service.id` do registry já corresponde ao nome do backend Moto (`s3`, `sqs`, `dynamodb`, …).
- Azure: o `service.id` é o namespace ARM (`Microsoft.Storage`, `Microsoft.Resources`, …).
- GCP: ajustes em `SERVICE_REMOTE_ID["gcp"]` para os casos onde o id da UI difere do `resource_type` do store (`gcp-iam` → `iam`, etc).

## Isolamento entre clouds

Princípio: limpar uma cloud **nunca** toca as outras.

- AWS reset itera `moto.backends.list_all_backends()` + stores nativos LocalStack do módulo `aws/`.
- Azure reset chama `AzureGateway.stores.clear()` + clear dos data planes (`storage_provider.data_store`, `cosmos_provider.data_store`, `functions_registry._apps`).
- GCP reset chama `GcpGateway.stores.clear()` + clear dos data planes (storage / pubsub / firestore / iam) + `functions_provider.registry`.

Cada gateway tem stores próprios — não há global compartilhado. Detalhes em [`docs/multi-cloud-stack.md`](multi-cloud-stack.md#5-isolamento-entre-provedores).

## Pointers

- Backend: `localstack-core/localstack/aws/services/_localstack_stack.py`
- Frontend page: `localstack-ui/console/src/routes/stack.tsx`
- API helpers: `localstack-ui/console/src/lib/api/stack.ts`
- Doc geral: [`docs/multi-cloud-stack.md`](multi-cloud-stack.md)
