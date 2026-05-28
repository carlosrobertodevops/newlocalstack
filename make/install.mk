.PHONY: venv freeze upgrade-pinned-dependencies install-basic install-runtime install-test install-dev install-dev-types install-s3 install entrypoints

## Idempotência: cada install-* grava $(VENV_DIR)/.stamp-<alvo> ao concluir.
## Re-rodar informa e pula. Reinstalar à força: FORCE=1 make install-<alvo>.
## `make clean` remove $(VENV_DIR) (e portanto os stamps).

$(VENV_ACTIVATE): pyproject.toml
	test -d $(VENV_DIR) || $(VENV_BIN) $(VENV_DIR)
	$(VENV_RUN); $(PIP_CMD) install --upgrade pip setuptools wheel
	touch $(VENV_ACTIVATE)

venv: $(VENV_ACTIVATE)    ## Create a new (empty) virtual environment

freeze:                   ## Run pip freeze -l in the virtual environment
	@$(VENV_RUN); pip freeze -l

upgrade-pinned-dependencies: venv
	# TODO: Avoid pip 26.0 for now due to https://github.com/jazzband/pip-tools/issues/2319
	$(VENV_RUN); $(PIP_CMD) install --upgrade "pip<26.0" pip-tools pre-commit
	$(VENV_RUN); pip-compile --strip-extras --upgrade -o requirements-basic.txt pyproject.toml
	$(VENV_RUN); pip-compile --strip-extras --upgrade --extra runtime -o requirements-runtime.txt pyproject.toml
	$(VENV_RUN); pip-compile --strip-extras --upgrade --extra test -o requirements-test.txt pyproject.toml
	$(VENV_RUN); pip-compile --strip-extras --upgrade --extra dev -o requirements-dev.txt pyproject.toml
	$(VENV_RUN); pip-compile --strip-extras --upgrade --extra typehint -o requirements-typehint.txt pyproject.toml
	$(VENV_RUN); pip-compile --strip-extras --upgrade --extra base-runtime -o requirements-base-runtime.txt pyproject.toml
	$(VENV_RUN); pre-commit autoupdate

install-basic: venv       ## Install basic dependencies for CLI usage into venv
	@if [ -z "$(FORCE)" ] && [ -f "$(VENV_DIR)/.stamp-basic" ]; then \
		echo "✓ install-basic já instalado (FORCE=1 make install-basic para reinstalar)"; \
	else \
		$(VENV_RUN) && $(PIP_CMD) install -r requirements-basic.txt \
			&& $(PIP_CMD) install $(PIP_OPTS) -e . \
			&& touch $(VENV_DIR)/.stamp-basic; \
	fi

install-runtime: venv     ## Install dependencies for the localstack runtime into venv
	@if [ -z "$(FORCE)" ] && [ -f "$(VENV_DIR)/.stamp-runtime" ]; then \
		echo "✓ install-runtime já instalado (FORCE=1 make install-runtime para reinstalar)"; \
	else \
		$(VENV_RUN) && $(PIP_CMD) install -r requirements-runtime.txt \
			&& $(PIP_CMD) install $(PIP_OPTS) -e ".[runtime]" \
			&& touch $(VENV_DIR)/.stamp-runtime; \
	fi

install-test: venv        ## Install requirements to run tests into venv
	@if [ -z "$(FORCE)" ] && [ -f "$(VENV_DIR)/.stamp-test" ]; then \
		echo "✓ install-test já instalado (FORCE=1 make install-test para reinstalar)"; \
	else \
		$(VENV_RUN) && $(PIP_CMD) install -r requirements-test.txt \
			&& $(PIP_CMD) install $(PIP_OPTS) -e ".[test]" \
			&& touch $(VENV_DIR)/.stamp-test; \
	fi

install-dev: venv         ## Install developer requirements into venv
	@if [ -z "$(FORCE)" ] && [ -f "$(VENV_DIR)/.stamp-dev" ]; then \
		echo "✓ install-dev já instalado (FORCE=1 make install-dev para reinstalar)"; \
	else \
		$(VENV_RUN) && $(PIP_CMD) install -r requirements-dev.txt \
			&& $(PIP_CMD) install $(PIP_OPTS) -e ".[dev]" \
			&& touch $(VENV_DIR)/.stamp-dev; \
	fi

install-dev-types: venv   ## Install developer requirements incl. type hints into venv
	@if [ -z "$(FORCE)" ] && [ -f "$(VENV_DIR)/.stamp-dev-types" ]; then \
		echo "✓ install-dev-types já instalado (FORCE=1 make install-dev-types para reinstalar)"; \
	else \
		$(VENV_RUN) && $(PIP_CMD) install -r requirements-typehint.txt \
			&& $(PIP_CMD) install $(PIP_OPTS) -e ".[typehint]" \
			&& touch $(VENV_DIR)/.stamp-dev-types; \
	fi

install-s3: venv          ## Install dependencies for the localstack runtime for s3-only into venv
	@if [ -z "$(FORCE)" ] && [ -f "$(VENV_DIR)/.stamp-s3" ]; then \
		echo "✓ install-s3 já instalado (FORCE=1 make install-s3 para reinstalar)"; \
	else \
		$(VENV_RUN) && $(PIP_CMD) install -r requirements-base-runtime.txt \
			&& $(PIP_CMD) install $(PIP_OPTS) -e ".[base-runtime]" \
			&& touch $(VENV_DIR)/.stamp-s3; \
	fi

install: install-dev      ## Install full dependencies into venv

entrypoints: install-dev  ## Regenerate plux.ini entry points
	$(VENV_RUN); python -m plux entrypoints
	@# make sure that the plux.ini file with the entrypoints has correctly been created
	@test -s plux.ini || (echo "Entrypoints were not correctly created! Aborting!" && exit 1)
