.PHONY: setup-azure-tls setup-azure-tls-uninstall init-precommit start

setup-azure-tls:          ## Bootstrap Azure TLS (one-time per machine). Installs mkcert local CA into OS trust store and issues a cert for localstack-tls signed by it, so Go binaries (terraform-provider-azurerm) trust https://localhost:4569 without any per-cert step. Required because Go on macOS reads only the system Keychain — no SSL_CERT_FILE bypass exists.
	@./scripts/bin/setup-azure-tls

setup-azure-tls-uninstall: ## Remove mkcert local CA from OS trust store.
	@./scripts/bin/setup-azure-tls --uninstall

init-precommit:           ## install te pre-commit hook into your local git repository
	($(VENV_RUN); pre-commit install)

start:                    ## Manually start the local infrastructure for testing
	($(VENV_RUN); python3 -m localstack.platform.runtime.main)
