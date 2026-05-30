# make/compose.mk — docker compose lifecycle (D3: entrypoint único `make start`)

COMPOSE_FILE ?= docker/compose.yml

.PHONY: setup start stop logs reset _require-docker

_require-docker:
	@docker info >/dev/null 2>&1 || { \
		echo "✗ Docker daemon não está rodando. Inicie o OrbStack/Docker Desktop e tente de novo." >&2; \
		exit 1; }

setup:                    ## One-shot bootstrap: install deps, build image, setup console
	@./scripts/start.sh

start: _require-docker     ## Start the docker compose stack (localstack + console UI)
	@docker image inspect $(IMAGE_NAME):$(DEFAULT_TAG) >/dev/null 2>&1 || { \
		echo "▶ imagem local '$(IMAGE_NAME):$(DEFAULT_TAG)' ausente — buildando ($(MAKE) docker-build)…"; \
		$(MAKE) docker-build; }
	docker compose -f $(COMPOSE_FILE) up -d localstack localstack-ui

stop: _require-docker      ## Stop the docker compose stack
	docker compose -f $(COMPOSE_FILE) down

logs: _require-docker      ## Tail docker compose logs
	docker compose -f $(COMPOSE_FILE) logs -f

reset: _require-docker     ## Wipe containers + volumes + local cache (.cache/)
	docker compose -f $(COMPOSE_FILE) down -v
	rm -rf .cache/
