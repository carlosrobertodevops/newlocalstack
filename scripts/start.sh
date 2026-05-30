#!/usr/bin/env bash
# LocalStack fork — bootstrap idempotente.
# Cada passo só roda se o artefato correspondente ainda não existir.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

IMAGE_NAME="${IMAGE_NAME:-localstack/localstack-custom}"
COMPOSE_FILE="${COMPOSE_FILE:-docker/compose.yml}"
COMPOSE_SERVICES=(localstack localstack-ui)

step()  { printf '\n\033[1;36m▶ %s\033[0m\n' "$*"; }
skip()  { printf '\033[1;33m↷ %s\033[0m\n' "$*"; }
done_() { printf '\033[1;32m✓ %s\033[0m\n' "$*"; }
fail()  { printf '\033[1;31m✗ %s\033[0m\n' "$*" >&2; exit 1; }

require_docker() {
  docker info >/dev/null 2>&1 \
    || fail "Docker daemon não está rodando. Inicie o OrbStack/Docker Desktop e tente de novo."
}

# Verdadeiro só se TUDO já estiver instalado E a stack no ar e saudável.
# Qualquer requisito ausente → retorna 1 → bootstrap segue o fluxo normal.
setup_complete() {
  [ -f .venv/bin/activate ]                                      || return 1
  [ -s plux.ini ]                                                || return 1
  { [ -d localstack-ui/console/dist ] \
      && [ -n "$(ls -A localstack-ui/console/dist 2>/dev/null || true)" ]; } || return 1
  docker info >/dev/null 2>&1                                    || return 1
  docker image inspect "${IMAGE_NAME}:latest" >/dev/null 2>&1    || return 1
  local running
  running="$(docker compose -f "$COMPOSE_FILE" ps --services --filter status=running 2>/dev/null \
    | grep -Ec "^($(IFS='|'; echo "${COMPOSE_SERVICES[*]}"))$" || true)"
  [ "${running}" -eq "${#COMPOSE_SERVICES[@]}" ]                 || return 1
  curl -fsS "http://localhost:4566/_localstack/health" >/dev/null 2>&1 || return 1
  return 0
}

# ── Guard idempotente: já instalado e rodando? nada a fazer ───────────────────
if setup_complete; then
  done_ "Setup já instalado e rodando — nada a fazer."
  skip  "venv + plux.ini + imagem '${IMAGE_NAME}' + console + containers (${COMPOSE_SERVICES[*]}) presentes e no ar."
  echo
  echo "   • Console UI:   http://localhost:4577"
  echo "   • LocalStack:   http://localhost:4566"
  echo "   • Saúde:        curl -s http://localhost:4566/_localstack/health | jq"
  exit 0
fi

# ── 1. venv + deps Python (make install) ──────────────────────────────────────
step "1/5 Python venv + dependências (make install)"
if [ -f .venv/bin/activate ]; then
  skip "venv já existe em .venv/ — pulando 'make install'"
else
  echo "criando venv e instalando dependências de dev…"
  make install
  done_ "venv pronto"
fi

# ── 2. plux entrypoints (make entrypoints) ────────────────────────────────────
step "2/5 plux.ini (make entrypoints)"
if [ -s plux.ini ]; then
  skip "plux.ini já existe e não está vazio — pulando 'make entrypoints'"
else
  echo "gerando plux.ini a partir dos plugins…"
  make entrypoints
  done_ "plux.ini gerado"
fi

# ── 3. imagem Docker do fork (make docker-build) ──────────────────────────────
step "3/5 imagem Docker '${IMAGE_NAME}' (make docker-build)"
require_docker
if docker image inspect "${IMAGE_NAME}:latest" >/dev/null 2>&1; then
  skip "imagem '${IMAGE_NAME}:latest' já existe localmente — pulando build"
else
  echo "construindo imagem '${IMAGE_NAME}' (pode demorar)…"
  IMAGE_NAME="${IMAGE_NAME}" make docker-build
  done_ "imagem '${IMAGE_NAME}' construída"
fi

# ── 4a. console deps (make console-install) ───────────────────────────────────
step "4/5 console SPA — dependências (make console-install)"
if [ -d localstack-ui/console/node_modules ] && [ -f localstack-ui/console/bun.lock ]; then
  skip "node_modules + bun.lock já presentes — pulando 'make console-install'"
else
  echo "instalando dependências do console com bun…"
  make console-install
  done_ "deps do console instaladas"
fi

# ── 4b. console build (make console-build) ────────────────────────────────────
step "4/5 console SPA — build (make console-build)"
if [ -d localstack-ui/console/dist ] && [ -n "$(ls -A localstack-ui/console/dist 2>/dev/null || true)" ]; then
  skip "localstack-ui/console/dist/ já populado — pulando 'make console-build'"
else
  echo "construindo bundle do console…"
  make console-build
  done_ "console buildado"
fi

# ── 5. subir stack via docker compose ─────────────────────────────────────────
step "5/5 subindo stack (docker compose up -d ${COMPOSE_SERVICES[*]})"
require_docker
running_count="$(docker compose -f "$COMPOSE_FILE" ps --services --filter status=running 2>/dev/null \
  | grep -Ec "^($(IFS='|'; echo "${COMPOSE_SERVICES[*]}"))$" || true)"
if [ "${running_count}" -eq "${#COMPOSE_SERVICES[@]}" ]; then
  skip "todos os serviços (${COMPOSE_SERVICES[*]}) já estão Up — pulando 'docker compose up'"
else
  echo "iniciando containers em background…"
  docker compose -f "$COMPOSE_FILE" up -d "${COMPOSE_SERVICES[@]}"
  done_ "stack no ar"
fi

printf '\n\033[1;32m✅ Bootstrap concluído.\033[0m\n'
echo "   • Console UI:   http://localhost:4577"
echo "   • LocalStack:   http://localhost:4566"
echo "   • Saúde:        curl -s http://localhost:4566/_localstack/health | jq"
