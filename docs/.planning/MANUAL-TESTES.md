# Manual de Testes — newlocalstack (pós-PLAN.md)

**Data:** 2026-05-28
**Escopo:** roteiro passo a passo para validar o projeto após o refactor descrito em `docs/.planning/PLAN.md` (decisões D1–D6).
**Pré-leitura:** `docs/.planning/PLAN.md` (decisões) · este manual (verificação).

## Status de implementação do PLAN

| Dec    | Resumo                                                 | Status                                                                                                                             |
| ------ | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **D1** | docker/ + scripts/ consolidados; artefatos → `.cache/` | ✅ docker/scripts; ✅ `graphify-out/`+`volume/`→`.cache/`; ⚠️ `dist/`/`target/` ficam no raiz (gitignored, acoplados a publish/CI) |
| **D2** | catálogo `examples/labs.yaml` + schema + README        | ✅ completo (9 labs)                                                                                                               |
| **D3** | Makefile em includes + targets DX                      | ✅ 11 includes; ✅ `setup/start/stop/logs/reset` (make/compose.mk); `start` antigo → `start-runtime`                               |
| **D4** | docs/ por audiência + README reescrito                 | ✅ (⚠️ sem `CONTRIBUTING.md` standalone)                                                                                           |
| **D5** | rota `/stack` unificada + CloudSelector                | ✅ (⚠️ sem redirect HTTP real; wrappers cobrem compat)                                                                             |
| **D6** | backend aws/azure/gcp/cloud preservado                 | ✅ tudo intacto                                                                                                                    |

Critério de avanço entre fases (PLAN): verde em `tests/aws/` + `tests/azure/` + `make lint` + smoke de `start.sh`.

---

## 1. Pré-requisitos e bootstrap

**Dependências:** Docker + `docker compose` v2 · Python >= 3.10 · Bun (console) · Make. Plataforma: macOS, Linux ou WSL2 (Windows nativo não suportado).

```bash
cd /Users/carlosroberto/Workspace/Projetos/newlocalstack

make install            # cria .venv/, deps dev (ruff, mypy, pytest, pre-commit)
make entrypoints        # regenera plux.ini — rodar se adicionou/renomeou plugin
make lint               # ruff check + ruff format --check + openapi-spec-validator + mypy + deptry
make check-aws-markers  # valida markers em tests/aws/
```

✅ **esperado:** `make install` cria `.venv/`; `make entrypoints` → `plux.ini` não-vazio; `make lint` sai sem warnings (rode `make format` p/ auto-fix); `check-aws-markers` verde.

**3 comandos end-to-end (DX do PLAN):** `git clone` → `make setup` (= `./scripts/start.sh`) → `make start`.

---

## 2. Suites de backend e isolamento multi-cloud (D6)

Diretórios: `tests/unit/`, `tests/aws/services/<service>/`, `tests/azure/`, `tests/gcp/`, `tests/bootstrap/`, `tests/integration/`. Testes de cloud nunca se misturam — reset de uma cloud não vaza estado p/ outra.

```bash
make test TEST_PATH=tests/unit                   # suite unit
make test TEST_PATH=tests/aws/services/s3        # amostra parity AWS
. .venv/bin/activate && pytest tests/azure -q    # Azure isolado
. .venv/bin/activate && pytest tests/gcp -q      # GCP isolado
```

Parity contra AWS real (refresh snapshots):

```bash
TEST_TARGET=AWS_CLOUD AWS_PROFILE=<profile> SNAPSHOT_UPDATE=1 pytest tests/aws/services/<service> -v
```

✅ **esperado:** verde em unit + aws + azure + gcp. Confirma D6 (stores isolados por cloud).

---

## 3. Subir e gerenciar a stack (D3)

### 3.1 Via Docker Compose (recomendado)

```bash
make setup    # one-shot bootstrap (./scripts/start.sh)
make start    # docker compose -f docker/compose.yml up -d localstack localstack-ui
make logs     # docker compose ... logs -f
make stop     # docker compose ... down
make reset    # docker compose ... down -v  +  rm -rf .cache/
```

Build da imagem (se mexeu em `localstack-core/`):

```bash
IMAGE_NAME=localstack/localstack-custom make docker-build
```

Serviços (`docker/compose.yml`):

| Serviço          | Porta                  | Função              |
| ---------------- | ---------------------- | ------------------- |
| `localstack`     | `4566` (+ `4510-4559`) | edge gateway AWS    |
| `localstack-ui`  | `4577`                 | console SPA (nginx) |
| `localstack-tls` | `4569` + `443`         | Azure TLS sidecar   |

Volume persistente: `../.cache/volume` → `/var/lib/localstack` (movido de `../volume` no D1).

### 3.2 Via runtime in-process (sem docker)

```bash
make start-runtime    # python3 -m localstack.platform.runtime.main  (escuta :4566, Ctrl+C p/ parar)
```

> Sem UI nem TLS; bom p/ dev rápido / CI. (Era o `make start` antigo — renomeado no D3.)

### 3.3 Verificação

```bash
docker compose -f docker/compose.yml ps                 # 3 serviços Up
curl -s localhost:4566/_localstack/health | jq          # status: ok
```

✅ **esperado:** gateway `:4566` responde; console em `:4577`.

---

## 4. Endpoints multi-cloud e reset isolado (D6)

Handler: `localstack-core/localstack/aws/services/internal.py` + `_localstack_stack.py`.

| Método | Endpoint                                               | Descrição                                                                           |
| ------ | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| GET    | `/_localstack/clouds`                                  | lista clouds (aws, azure, gcp)                                                      |
| GET    | `/_localstack/clouds/<cloud>/health`                   | status dos serviços                                                                 |
| GET    | `/_localstack/clouds/<cloud>/info`                     | metadados do provider                                                               |
| GET    | `/_localstack/clouds/<cloud>/stack`                    | inventário `{services:[{service,resource_count}], total_resources, total_services}` |
| DELETE | `/_localstack/clouds/<cloud>/stack/services/<service>` | wipe 1 serviço                                                                      |
| POST   | `/_localstack/clouds/<cloud>/stack/reset`              | reset isolado, body `{"confirm": true}`                                             |

Teste de isolamento:

```bash
curl -s localhost:4566/_localstack/clouds | jq                       # 3 clouds
for c in aws azure gcp; do
  echo "== $c =="; curl -s localhost:4566/_localstack/clouds/$c/stack | jq '.total_resources'
done

aws --endpoint-url http://localhost:4566 s3 mb s3://test-bucket      # cria recurso AWS
curl -s localhost:4566/_localstack/clouds/aws/stack | jq '.total_resources'   # → 1

curl -s -XPOST localhost:4566/_localstack/clouds/aws/stack/reset \
  -H 'content-type: application/json' -d '{"confirm":true}'          # reset só AWS

curl -s localhost:4566/_localstack/clouds/aws/stack   | jq '.total_resources'  # → 0
curl -s localhost:4566/_localstack/clouds/azure/stack | jq '.total_resources'  # intacto
```

✅ **esperado:** reset AWS zera só AWS; Azure/GCP não mudam.

---

## 5. Catálogo de labs — examples/ (D2)

`examples/labs.yaml` (9 labs: terraform/serverless/cli × aws/azure/gcp), `examples/lab.schema.json` (draft-07), `examples/README.md` (tabela). Pastas `examples/{terraform,serverless,cli}/{aws,azure,gcp}/` preservadas.

```bash
. .venv/bin/activate
python -c "import yaml,json,jsonschema; \
d=yaml.safe_load(open('examples/labs.yaml')); \
s=json.load(open('examples/lab.schema.json')); \
jsonschema.validate(d,s); print('labs ok:',len(d['labs']))"
```

✅ **esperado:** `labs ok: 9`.

---

## 6. Console UI — rota /stack unificada (D5)

Componentes (`localstack-ui/console`): `src/routes/UnifiedStack.tsx` (rota `/stack`), `src/components/CloudSelector.tsx` (dropdown), `src/routes/stack.tsx` (`CloudStack` reusa `ServiceTable` + `ResetButton`). API: `src/lib/api/{clouds,stack}.ts`. Estado via `useSearch()` → `?cloud=aws|azure|gcp` (default `aws`). Rotas legadas `/stack/{aws,azure,gcp}` = wrappers (sem redirect real).

```bash
make console-install    # bun
make console-lint       # tsc + eslint (max-warnings=0)
make console-build      # popula dist/
make console-test       # vitest
make console-dev        # vite :5173
```

Roteiro manual (browser):

1. `localhost:5173/stack` → dropdown CloudSelector visível no header.
2. Trocar cloud no dropdown → URL vira `?cloud=azure`, `ServiceTable` recarrega.
3. `?cloud=gcp` → tabela + botão "Limpar Stack" (`ResetButton`) com modal de confirmação.
4. Abrir `/stack/aws` legado → wrapper renderiza (compat).
5. Auto-refresh a cada 20s atualiza inventário.

| Contexto | URL                    | Servido por                                                         |
| -------- | ---------------------- | ------------------------------------------------------------------- |
| Dev      | `localhost:5173/stack` | Vite                                                                |
| Prod     | `localhost:4577/stack` | nginx (`localstack-ui`), proxy `/_localstack/*` → `localstack:4566` |

✅ **esperado:** seleção fluida; reset de uma cloud não afeta outra; sem erros de console.

---

## 7. Smoke E2E com examples

Stack precisa estar up (`:4566`). Configs self-contained, creds dummy.

```bash
cd examples/terraform/aws
terraform init && terraform apply -auto-approve && terraform destroy -auto-approve

cd ../../cli/aws && bash demo.sh        # golden-path awslocal
```

✅ **esperado:** apply/destroy verdes contra `:4566`.

---

## 8. Azure TLS (terraform-provider-azurerm)

```bash
make setup-azure-tls                              # mkcert CA + SANs *.blob/queue/table.core.windows.net... (one-time)
scripts/bin/azure-register-host devstoreaccount1  # sudo /etc/hosts
cd examples/terraform/azure && terraform init && terraform apply -auto-approve
```

Sidecar `localstack-tls` mapeia `127.0.0.1:443 → 4569`.

✅ **esperado:** `azurerm_resource_group` + `azurerm_storage_account` + `azurerm_storage_container` verdes.

---

## 9. Troubleshooting e gaps conhecidos

| Gap                                         | Status | Nota                                                                                                                                                   |
| ------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dist/`/`target/` não movidos p/ `.cache/`  | pós-D1 | gitignored, ausentes em clone limpo; acoplados a `publish`/twine, `docker-run-tests` mounts, `JUNIT_REPORTS_FILE`, cargo lambda — relocar quebraria CI |
| `graphify-out/`+`volume/` → `.cache/`       | ✅     | reset via `make reset`                                                                                                                                 |
| Sem `CONTRIBUTING.md` standalone            | pós-D4 | conteúdo em `docs/contributing/development-environment-setup/`                                                                                         |
| Sem redirect HTTP `/stack/aws`→`?cloud=aws` | pós-D5 | wrappers cobrem compat                                                                                                                                 |

**Dicas:**

- `make start` falha → conferir Docker rodando (`docker ps`) + porta `4566` livre.
- Console vazio → rodar `make console-build` antes de subir `localstack-ui`.
- Volume agora em `.cache/volume`; `make reset` limpa containers + volumes + `.cache/`.
- Certificado Azure expirado → rerun `make setup-azure-tls`.
- CORS/proxy → checar `localstack-ui/.../nginx.conf` + env `EXTRA_CORS_ALLOWED_ORIGINS`.
