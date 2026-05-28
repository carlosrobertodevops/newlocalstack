.PHONY: console-install console-dev console-build console-lint console-test console-test-e2e console-bridge console-bridge-install

console-install:          ## Install console SPA dependencies (bun)
	@if [ -z "$(FORCE)" ] && [ -d localstack-ui/console/node_modules ]; then \
		echo "✓ console deps já instaladas (FORCE=1 make console-install para reinstalar)"; \
	else \
		cd localstack-ui/console && bun install; \
	fi

console-dev:              ## Run Vite dev server on :5173
	cd localstack-ui/console && bun run dev

console-build:            ## Build the console SPA into dist/
	cd localstack-ui/console && bun run build

console-lint:             ## Lint + typecheck the console SPA
	cd localstack-ui/console && bun run lint && bun run typecheck

console-test:             ## Run console SPA tests (vitest)
	cd localstack-ui/console && bun run test

console-test-e2e:         ## Run console SPA e2e tests (playwright)
	cd localstack-ui/console && bun run test:e2e

console-bridge:           ## Run the host-side CLI bridge worker on :4578
	./scripts/bin/console-cli-bridge

console-bridge-install:   ## Install the bridge worker requirements
	@if [ -z "$(FORCE)" ] && [ -f .cache/.stamp-bridge ]; then \
		echo "✓ console-bridge-install já instalado (FORCE=1 make console-bridge-install para reinstalar)"; \
	else \
		$(PIP_CMD) install -r scripts/bin/console-cli-bridge.requirements.txt \
			&& mkdir -p .cache && touch .cache/.stamp-bridge; \
	fi
