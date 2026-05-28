# PLAN — Refactor newlocalstack inspirado em 0x3-cl0ud-l4bs

**Data:** 2026-05-28
**Referência externa:** https://github.com/carlosrobertodevops/0x3-cl0ud-l4bs
**Escopo:** simplicidade estrutural — sem mexer em lógica de provider/runtime.

---

## Insight central do 0x3-cl0ud-l4bs

- Depth ≤ 2 no top-level.
- 1 Makefile + 1 `start.sh` = entrypoint único (`make lab`).
- Multi-cloud é **runtime** (dropdown UI), não filesystem.
- Labs vivem em catálogo único (`labs/`), não em pastas por cloud × ferramenta.
- README único de 18KB com tabela de capacidades + quickstart de 3 comandos.

Aplicar parcialmente: preservar o que já é forte no newlocalstack (isolamento de stores por cloud), simplificar o que não é (poluição top-level, duplicação UI, docs por tema).

---

## 1. Reorganização do Top-Level

Hoje: 30+ entradas top-level, 2 Dockerfiles, 2 composes, `bin/` + `scripts/` duplicados, artefatos auto-gerados visíveis (`graphify-out/`, `diagram/`, `prompts/`, `target/`, `dist/`, `volume/`).

**Movimentos:**

| De                                                                                             | Para                                                                                   |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `Dockerfile`, `Dockerfile.s3`, `docker-compose.yml`, `docker-compose-pro.yml`, `.dockerignore` | `docker/` (renomear: `Dockerfile`, `s3.Dockerfile`, `compose.yml`, `compose.prod.yml`) |
| `bin/`, `start.sh`, `setup-azure-tls`                                                          | `scripts/` (merge `bin/` → `scripts/bin/`)                                             |
| `graphify-out/`, `target/`, `dist/`, `volume/`                                                 | `.cache/` (gitignored)                                                                 |
| `diagram/`, `prompts/`, `tasks/`                                                               | `docs/_archive/`                                                                       |

**Top-level final (≤ 15 entradas):**

```
newlocalstack/
├── docker/            # Dockerfiles + composes
├── scripts/           # start.sh + bin/ + helpers
├── localstack-core/   # backend Python
├── localstack-ui/     # console SPA
├── localstack-init/
├── localstack-tls/
├── examples/
├── tests/
├── docs/
├── Makefile
├── pyproject.toml
├── plux.ini
├── README.md
├── CLAUDE.md
└── LICENSE.txt
```

`.gitignore` ganha `.cache/` e `docker/.dockerignore`.

---

## 2. Unificação de examples/ como Labs

Hoje: `examples/{terraform,serverless,cli}/{aws,azure,gcp}/` = 9 pastas físicas.

**Opção A (recomendada, baixo risco)** — manter pastas + adicionar catálogo:

- `examples/labs.yaml` — registro único de todos os labs (id, cloud, tool, title, steps, cleanup, readme).
- `examples/README.md` — tabela gerada do YAML (substitui navegação por 9 pastas).
- `examples/lab.schema.json` — validação em CI.
- Endpoint futuro `/api/_localstack/labs` consome o YAML — gancho para UI interativa.

Exemplo de entrada:

```yaml
labs:
  - id: terraform-aws
    cloud: aws
    tool: terraform
    title: "Terraform + AWS"
    steps: ["Define VPC", "Deploy Lambda", "Verify via awslocal"]
    cleanup: "terraform destroy"
    readme: terraform/aws/README.md
```

**Opção B (futura, agressiva)** — migrar para `labs/` com `lab_server.py` + dropdown na console UI. YAML da opção A é portável — habilita B sem refactor.

---

## 3. Simplificação de DX (Makefile + start.sh)

Hoje: Makefile monolítico com ~40 targets. `start.sh` já idempotente (5 passos).

**Makefile raiz reduzido a ~30 linhas + includes:**

```makefile
.PHONY: help setup start stop logs reset test lint format clean

help:
	@echo "newlocalstack — multi-cloud emulator"
	@echo ""
	@echo "Quick start:"
	@echo "  make setup        Install deps, build docker, setup console"
	@echo "  make start        Start docker-compose stack"
	@echo "  make stop         Stop all services"
	@echo "  make logs         Tail docker-compose logs"
	@echo "  make reset        Wipe all containers & volumes"
	@echo ""
	@echo "Development:"
	@echo "  make test         Run test suite"
	@echo "  make lint         Lint + format check"
	@echo "  make format       Auto-format code"
	@echo "  make clean        Remove .venv, build artifacts"

setup:
	@./scripts/start.sh

start:
	docker compose -f docker/compose.yml up -d

stop:
	docker compose -f docker/compose.yml down

logs:
	docker compose -f docker/compose.yml logs -f

reset:
	docker compose -f docker/compose.yml down -v
	rm -rf .venv plux.ini .cache/

test:
	@. .venv/bin/activate && pytest $(TEST_PATH)

include make/lint.mk
include make/console.mk
include make/docker.mk
include make/install.mk
```

**Includes** (`make/*.mk`):

- `lint.mk` — `lint`, `format`, `typecheck`
- `console.mk` — `console-install`, `console-build`, `console-dev`
- `docker.mk` — `docker-build`, `docker-push`
- `install.mk` — variantes granulares de install

**3 comandos end-to-end:** `git clone` → `make setup` → `make start`.

---

## 4. Consolidação de Documentação

Hoje: docs organizadas por tema (`development-environment-setup/`, `testing/`, `localstack-concepts/`, `superpowers/`) com guias multi-cloud soltos no raiz. README upstream genérico.

**Reorganizar por audiência:**

```
docs/
├── quickstart/          # 5 min para subir local
├── guides/              # terraform, serverless, multi-cloud, console
├── reference/           # concepts/, testing/, guides/cli-integration
├── contributing/        # CONTRIBUTING.md + dev-env-setup
└── superpowers/         # roadmap (preservado)
```

**Movimentos:**

- `azure-terraform.md`, `gcp-terraform.md`, `serverless-framework.md`, `multi-cloud-stack.md`, `multi-cloud-console-local-testing.md`, `console-stack-view.md` → `docs/guides/`
- `localstack-concepts/` → `docs/reference/concepts/`
- `testing/` → `docs/reference/testing/`
- `development-environment-setup/` → `docs/contributing/`

**README.md top-level reescrito:** intro 2 linhas + quickstart 3 comandos + tabela serviços×clouds + links para `docs/`.

Cada `examples/<tool>/<cloud>/README.md` linka para guide correspondente; guides linkam de volta a exemplo pronto.

---

## 5. Estratégia Multi-Cloud — Filesystem vs Runtime

**Princípio:** providers em filesystem isolado, seleção em runtime.

**Backend (sem mudança):** `aws/`, `azure/`, `gcp/` continuam pastas físicas. `CloudRegistry` + `CloudProvider` já discoveram via plux entry points. Stores isolados (moto.backends p/ AWS, próprios p/ Azure/GCP). Endpoints `/_localstack/clouds/<cloud>/...` já refletem padrão 0x3.

**Frontend (refactor):** console UI hoje tem 3 rotas separadas com componentes duplicados:

- `/stack/aws` → `<AwsStack />`
- `/stack/azure` → `<AzureStack />`
- `/stack/gcp` → `<GcpStack />`

Lógica idêntica (listar serviços, reset, inventory) — só muda URL de backend.

**Proposta:**

- 1 rota única `/stack` com `<CloudSelector>` dropdown no header.
- Estado via `useSearchParams()` → `?cloud=aws|azure|gcp`.
- `<StackView>` reusa `<ServiceTable />` e `<ResetButton />` para qualquer cloud.
- Redirects `/stack/aws` → `/stack?cloud=aws` para compat.

Resultado: ~200 LOC removidas, UX consistente, paralelo direto com 0x3 (uma view, múltiplas visões).

---

## 6. Prós, Contras e Riscos

| Mudança                                  | Prós                                                                            | Contras                                                                         | Risco      | Mitigação                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------- |
| **1. Consolidar `docker/` + `scripts/`** | Reduz top-level 30→15; centraliza deploy artifacts; CI mais claro               | Move 20+ arquivos; refs internas podem quebrar; docs externos com paths antigos | **Alto**   | Grep+regex pré-move; testar CI local; atualizar `.github/workflows` + docs                  |
| **2. `examples/labs.yaml` catálogo**     | Aditivo (zero quebra); descobribilidade instant; gancho UI futuro; valida em CI | YAML duplica metadados dos READMEs; manutenção em 2 lugares; baixa urgência     | **Baixo**  | YAML como source-of-truth, READMEs gerados ou validados via bot                             |
| **3. Makefile includes (`make/*.mk`)**   | Raiz legível ≤30 linhas; subsistemas auto-contidos; onboarding claro            | Overhead de includes; precisa enumerar targets em help; sensível a paths        | **Médio**  | Estrutura simples; `make help` em CI; manter targets canônicos estáveis                     |
| **4. Reorganizar `docs/` por audiência** | Navegação por perfil; onboarding segmentado; contribuidor acha guia rápido      | Refactor 30+ MDs; links internos quebram; TOC reconstruir                       | **Médio**  | Script grep validador de links pós-move; testar build de docs em CI; manter `docs/index.md` |
| **5. Unificar `/stack` na UI**           | Remove duplicação ~200 LOC; UX consistente; alinhado com 0x3                    | Refactor React; pode quebrar bookmarks antigos; teste E2E precisa atualizar     | **Médio**  | Redirects HTTP `/stack/aws` → `/stack?cloud=aws`; feature flag p/ rollout; E2E pré/pós      |
| **6. Backend providers — sem mudança**   | Zero risco; isolamento preservado; roadmap futuro (OCI etc) claro               | Nenhum (decisão de NÃO fazer)                                                   | **Mínimo** | Rodar `tests/aws/` + `tests/azure/` pós-refactor confirma isolamento                        |

---

## Ordem de Execução Recomendada

**F1 (Semana 1) — risco zero/baixo:**

- D6: validar baseline (rodar suites AWS + Azure).
- D2: adicionar `examples/labs.yaml` + schema (aditivo).

**F2 (Semana 2) — infra/DX:**

- D3: quebrar Makefile em includes (`make/*.mk`).
- D1: consolidar `docker/` + `scripts/`.

**F3 (Semana 3) — documentação:**

- D4: reorganizar `docs/` por audiência + reescrever README top-level.

**F4 (Semana 4) — UI:**

- D5: unificar rotas `/stack` com `<CloudSelector>`, feature flag opcional.

**Critério de avanço entre fases:** suite verde em `tests/aws/` + `tests/azure/` + `make lint` + smoke test do `start.sh`.

---

## O que NÃO mexer

- `localstack-core/localstack/{aws,azure,gcp,cloud}/` — separação correta, isolamento de stores.
- `localstack-core/localstack/aws/api/` — auto-gerado (`make asf-regenerate`).
- Plux entry points (`plux.ini`) — regenerados via `make entrypoints`.
- Estrutura de `tests/` — categorização por tipo já funciona.
- `localstack-init/`, `localstack-tls/` — sidecars com função clara.
