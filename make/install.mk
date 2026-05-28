.PHONY: venv freeze upgrade-pinned-dependencies install-basic install-runtime install-test install-dev install-dev-types install-s3 install entrypoints

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
	$(VENV_RUN); $(PIP_CMD) install -r requirements-basic.txt
	$(VENV_RUN); $(PIP_CMD) install $(PIP_OPTS) -e .

install-runtime: venv     ## Install dependencies for the localstack runtime into venv
	$(VENV_RUN); $(PIP_CMD) install -r requirements-runtime.txt
	$(VENV_RUN); $(PIP_CMD) install $(PIP_OPTS) -e ".[runtime]"

install-test: venv        ## Install requirements to run tests into venv
	$(VENV_RUN); $(PIP_CMD) install -r requirements-test.txt
	$(VENV_RUN); $(PIP_CMD) install $(PIP_OPTS) -e ".[test]"

install-dev: venv         ## Install developer requirements into venv
	$(VENV_RUN); $(PIP_CMD) install -r requirements-dev.txt
	$(VENV_RUN); $(PIP_CMD) install $(PIP_OPTS) -e ".[dev]"

install-dev-types: venv   ## Install developer requirements incl. type hints into venv
	$(VENV_RUN); $(PIP_CMD) install -r requirements-typehint.txt
	$(VENV_RUN); $(PIP_CMD) install $(PIP_OPTS) -e ".[typehint]"

install-s3: venv          ## Install dependencies for the localstack runtime for s3-only into venv
	$(VENV_RUN); $(PIP_CMD) install -r requirements-base-runtime.txt
	$(VENV_RUN); $(PIP_CMD) install $(PIP_OPTS) -e ".[base-runtime]"

install: install-dev      ## Install full dependencies into venv

entrypoints: install-dev  ## Regenerate plux.ini entry points
	$(VENV_RUN); python -m plux entrypoints
	@# make sure that the plux.ini file with the entrypoints has correctly been created
	@test -s plux.ini || (echo "Entrypoints were not correctly created! Aborting!" && exit 1)
