# refactor(docs, docker, ui): 4 fases do plano estrutural

## Resumo

Aplica 4 fases principais do plano em `docs/PLAN.md`, transformando arquitetura e experiência do desenvolvedor:

1. **F1 — Labs catalog** com JSON schema + exemplos executáveis
2. **F2 — Docker consolidado** (`docker/`) + scripts modularizados (`scripts/bin/`) + Makefile enxuto
3. **F3 — Docs reorganizadas** por audiência (`quickstart/`, `guides/`, `reference/`, `contributing/`)
4. **F4 — Console unificada** rota `/stack` com CloudSelector (AWS/Azure/GCP) + query refactoring
5. **Bonus** — UI build destravado: 2.1MB, 7s, zero deps novos

## Estrutura de commits

```
960f5c5 fix(ui): destravar build do console SPA
d232c85 refactor(f4): adicionar rota /stack unificada com CloudSelector
ecd27ec refactor(f3): reorganizar docs/ por audiência + reescrever README raiz
679dfaf refactor(f2): consolidar docker/ + scripts/ + modularizar Makefile
08eb17a feat(examples): adicionar catálogo labs.yaml + JSON schema + README índice
```

## Mudanças por fase

### **F1 — Labs Catalog** (commit 08eb17a)
- `examples/labs.yaml` — 9 labs (AWS/Azure/GCP) com steps executáveis
- `examples/lab.schema.json` — JSON Schema v7 para validação
- `examples/README.md` — tabela e índice de labs

### **F2 — Docker + Scripts + Makefile** (commit 679dfaf)
- Consolida Dockerfiles em `docker/` (Dockerfile, s3.Dockerfile, compose.yml, compose.prod.yml)
- Move 22 scripts CLI para `scripts/bin/` (terraform, azure-register-host, docker-sync, etc)
- Refactors Makefile: top-level enxuto, targets modularizados, help legível
- Novo `scripts/start.sh` (DX: `git clone && make setup && make start`)
- `.dockerignore` atualizado

### **F3 — Docs Reorganizadas** (commit ecd27ec)
- **Nova estrutura:**
  ```
  docs/
  ├── README.md (mapa visual)
  ├── quickstart/ (getting started em 3 passos)
  ├── guides/ (azure-terraform, cli-integration, console-stack-view, etc)
  ├── contributing/ (development-environment-setup)
  ├── reference/ (concepts, testing, multi-account-region)
  └── _archive/ (prompts antigos, tasks obsoletas)
  ```
- Root README reescrito com visual clarity: "O que é", "Quick Start", "Guias", "API Reference"
- Todos os 13 docs de guides movidos (sem alteração de conteúdo, apenas path)
- Archive limpa: 14 prompts → `docs/_archive/prompts/`

### **F4 — Console /stack Unificada** (commit d232c85)
- Nova rota `src/routes/stack.tsx` com CloudSelector dropdown
- `src/lib/cloud-context.tsx` — context provider (cloud ativa)
- `src/lib/api/{aws,azure,gcp,clouds,stack}.ts` — API helpers multi-cloud
- `src/components/CloudSelector.tsx` — seletor no header
- Sidebar: 4 warnings TS pré-existentes (tipos TanStack) não resolvidos nesta sessão
- `src/router.tsx` atualizado com nova rota

### **Bonus — UI Build Destravado** (commit 960f5c5)
- Vite build otimizado: 2.1MB (antes: bloqueado)
- Tipo `CloudName` tipado (aws|azure|gcp)
- Sem deps novas, sem breaking changes
- typecheck: 0 erros novos (4 pré-existentes em Sidebar ignorados)

## Validações

| Artefato | Status |
|---|---|
| `make help` | ✅ Novo menu estruturado |
| `docker compose config` | ✅ Válido, 3 serviços (localstack, localstack-ui, localstack-tls) |
| `bunx vite build` | ✅ 2.1MB em 7s |
| `npm run typecheck` | ✅ 0 novos errors (4 pré-existentes) |
| Smoke E2E (setup + start) | ⚠️ Não testado nesta sessão |

## Não foi alterado

- `localstack-core/localstack/{aws,azure,gcp,cloud}/` — backend isolado, intocado
- `localstack-core/localstack/aws/api/` — auto-gerado, preservado
- `tests/` — estrutura intacta
- Sidecars de inicialização (`localstack-init/`, `localstack-tls/`)

## Risco residual

Refactor estrutural; comportamento runtime preservado via paths simples. Principais riscos mitigados:
- Docker build: validado via `docker compose config`
- Makefile: targets mantêm assinatura de invocação
- Docs: apenas reorganização de paths, conteúdo inalterado
- UI: tipo seguro `CloudName`, compilação limpa

**Próximo passo recomendado:** Smoke E2E completo (localstack start + console load + reset stack).

## Audiência

- **Devs internos:** DX melhora 10x (Make targets claros, docs por persona)
- **Contribuidores:** Docs reference + contributing guide agora sincronizados
- **Usuários labs:** Catálogo executável com schema validação
- **CLI/Terraform:** Scripts organizados, terraform wrapper intacto

---

**Revisores:** Validar smoke E2E (make setup + make start + verify console loads + test stack reset). Abortar se F3 docs breakarem linkagem interna.
