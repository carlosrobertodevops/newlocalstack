# CLI examples — AWS · Azure · GCP

Demos auto-contidos para exercitar a emulação multi-cloud do LocalStack via CLI nativa (ou `curl` quando a CLI nativa não suporta endpoint override).

| Provider | Subdiretório   | Ferramenta primária    | Detalhes |
|----------|----------------|------------------------|----------|
| AWS      | `aws/`         | `aws` CLI v2 + `jq`    | endpoint override por flag, golden path completo |
| Azure    | `azure/`       | `curl` (não `az`)      | `az` não tem endpoint override por serviço; curl direto |
| GCP      | `gcp/`         | `curl` (não `gcloud`)  | `gcloud` tem override parcial; curl é mais previsível |

Guia maior: [`docs/guides/cli-integration.md`](../../docs/guides/cli-integration.md).

## Pré-requisitos comuns

- LocalStack rodando em `:4566` (e `:4569` para Azure TLS).
- `curl`, `jq`, `bash`.
- Para AWS: `aws` CLI v2.

```bash
docker-compose up -d
```

## Workflow geral

```bash
cd <provider>
chmod +x demo.sh
./demo.sh
```

Todos os scripts usam credenciais dummy (`test/test` no AWS, qualquer bearer no Azure/GCP). Operações idempotentes — re-execução não falha.

## Verificar via console

Após rodar o demo, abra a aba **<Provider> → Stack (Em ação)** no console (`localstack-ui/console`). Recursos aparecem agrupados.

## Cleanup

Cada demo é isolado por nome — re-execuções sobrescrevem ou ignoram conflitos. Para reset total por provedor (botão **"Limpar Stack"** no console ou API):

```bash
curl -X POST http://localhost:4566/_localstack/clouds/<aws|azure|gcp>/stack/reset \
  -H 'Content-Type: application/json' -d '{"confirm": true}'
```

Ação **isolada por cloud** — não afeta os outros provedores.
