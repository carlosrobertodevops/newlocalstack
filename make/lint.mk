.PHONY: lint lint-modified format format-modified

lint:                     ## Run code linter to check code style, check if formatter would make changes and check if dependency pins need to be updated
	@[ -f localstack-core/localstack/__init__.py ] && echo "localstack-core/localstack/__init__.py will break packaging." && exit 1 || :
	($(VENV_RUN); python -m ruff check --output-format=full . && python -m ruff format --check --diff .)
	$(VENV_RUN); pre-commit run check-pinned-deps-for-needed-upgrade --files pyproject.toml
	$(VENV_RUN); openapi-spec-validator localstack-core/localstack/platform/openapi.yaml
	$(VENV_RUN); cd localstack-core && mypy --install-types --non-interactive
	$(VENV_RUN); deptry .

lint-modified:            ## Run code linter on modified files to check code style, check if formatter would make changes, and check if dependency pins need to be updated because of modified files
	($(VENV_RUN); python -m ruff check --output-format=full `git diff --diff-filter=d --name-only HEAD | grep '\.py$$' | xargs` && python -m ruff format --check `git diff --diff-filter=d --name-only HEAD | grep '\.py$$' | xargs`)
	$(VENV_RUN); pre-commit run check-pinned-deps-for-needed-upgrade --files $(git diff main --name-only)

format:                   ## Run ruff to format the whole codebase
	($(VENV_RUN); python -m ruff check --output-format=full --fix .; python -m ruff format .)

format-modified:          ## Run ruff to format only modified code
	($(VENV_RUN); \
	  python -m ruff check --output-format=full --fix `git diff --diff-filter=d --name-only HEAD | grep '\.py$$' | xargs`; \
	  python -m ruff format `git diff --diff-filter=d --name-only HEAD | grep '\.py$$' | xargs`)
