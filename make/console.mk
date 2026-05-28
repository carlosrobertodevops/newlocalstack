.PHONY: console-install console-dev console-build console-lint console-test console-test-e2e console-bridge console-bridge-install

console-install:          ## Install console SPA dependencies (bun)
	cd localstack-ui/console && bun install

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
	$(PIP_CMD) install -r scripts/bin/console-cli-bridge.requirements.txt
