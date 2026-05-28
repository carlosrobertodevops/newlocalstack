.PHONY: asf-regenerate

asf-regenerate:           ## Regenerate ASF APIs
	$(VENV_RUN); python -m localstack.aws.scaffold upgrade
	@echo 'Removing unused imports from generated modules'
	$(VENV_RUN); python -m ruff check --select F401 --unsafe-fixes --fix localstack-core/localstack/aws/api/ --config "lint.preview = true"
	$(VENV_RUN); python -m ruff check --output-format=full --fix localstack-core/localstack/aws/api/
	$(VENV_RUN); python -m ruff format localstack-core/localstack/aws/api/
