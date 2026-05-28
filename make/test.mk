.PHONY: test test-coverage check-aws-markers

test:                     ## Run automated tests
	($(VENV_RUN); $(TEST_EXEC) pytest --durations=10 --log-cli-level=$(PYTEST_LOGLEVEL) --junitxml=$(JUNIT_REPORTS_FILE) $(PYTEST_ARGS) $(TEST_PATH))

test-coverage: LOCALSTACK_INTERNAL_TEST_COLLECT_METRIC = 1
test-coverage: TEST_EXEC = python -m coverage run $(COVERAGE_ARGS) -m
test-coverage: test       ## Run automated tests and create coverage report

check-aws-markers:        ## Lightweight check to ensure all AWS tests have proper compatibility markers set
	($(VENV_RUN); python -m pytest --co tests/aws/)
