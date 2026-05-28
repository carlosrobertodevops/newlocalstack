# make/compose.mk — docker compose lifecycle (D3: entrypoint único `make start`)

COMPOSE_FILE ?= docker/compose.yml

.PHONY: setup start stop logs reset

setup:                    ## One-shot bootstrap: install deps, build image, setup console
	@./scripts/start.sh

start:                    ## Start the docker compose stack (localstack + console UI)
	docker compose -f $(COMPOSE_FILE) up -d localstack localstack-ui

stop:                     ## Stop the docker compose stack
	docker compose -f $(COMPOSE_FILE) down

logs:                     ## Tail docker compose logs
	docker compose -f $(COMPOSE_FILE) logs -f

reset:                    ## Wipe containers + volumes + local cache (.cache/)
	docker compose -f $(COMPOSE_FILE) down -v
	rm -rf .cache/
