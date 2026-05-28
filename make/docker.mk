.PHONY: docker-build docker-run-tests docker-run-tests-s3-only docker-cp-coverage

docker-build:             ## Build the LocalStack Docker image
	IMAGE_NAME=$(IMAGE_NAME) PLATFORM=$(PLATFORM) ./scripts/bin/docker-helper.sh build

docker-run-tests:         ## Initializes the test environment and runs the tests in a docker container
	docker run -e LOCALSTACK_INTERNAL_TEST_COLLECT_METRIC=1 -e DOCKERHUB_USERNAME -e DOCKERHUB_PASSWORD --entrypoint= -v `pwd`/.git:/opt/code/localstack/.git -v `pwd`/requirements-test.txt:/opt/code/localstack/requirements-test.txt -v `pwd`/.test_durations:/opt/code/localstack/.test_durations -v `pwd`/tests/:/opt/code/localstack/tests/ -v `pwd`/dist/:/opt/code/localstack/dist/ -v `pwd`/target/:/opt/code/localstack/target/ -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/localstack:/var/lib/localstack  \
		$(IMAGE_NAME):$(DEFAULT_TAG) \
	    bash -c "make install-test && DEBUG=$(DEBUG) PYTEST_LOGLEVEL=$(PYTEST_LOGLEVEL) PYTEST_ARGS='$(PYTEST_ARGS)' COVERAGE_FILE='$(COVERAGE_FILE)' JUNIT_REPORTS_FILE=$(JUNIT_REPORTS_FILE) TEST_PATH='$(TEST_PATH)' LAMBDA_IGNORE_ARCHITECTURE=1 LAMBDA_INIT_POST_INVOKE_WAIT_MS=50 TINYBIRD_PYTEST_ARGS='$(TINYBIRD_PYTEST_ARGS)' TINYBIRD_DATASOURCE='$(TINYBIRD_DATASOURCE)' TINYBIRD_TOKEN='$(TINYBIRD_TOKEN)' TINYBIRD_URL='$(TINYBIRD_URL)' CI_REPOSITORY_NAME='$(CI_REPOSITORY_NAME)' CI_WORKFLOW_NAME='$(CI_WORKFLOW_NAME)' CI_COMMIT_BRANCH='$(CI_COMMIT_BRANCH)' CI_COMMIT_SHA='$(CI_COMMIT_SHA)' CI_JOB_URL='$(CI_JOB_URL)' CI_JOB_NAME='$(CI_JOB_NAME)' CI_JOB_ID='$(CI_JOB_ID)' CI='$(CI)' TEST_AWS_REGION_NAME='${TEST_AWS_REGION_NAME}' TEST_AWS_ACCESS_KEY_ID='${TEST_AWS_ACCESS_KEY_ID}' TEST_AWS_ACCOUNT_ID='${TEST_AWS_ACCOUNT_ID}' make test-coverage"

docker-run-tests-s3-only: ## Initializes the test environment and runs the tests in a docker container for the S3 only image
	docker run -e LOCALSTACK_INTERNAL_TEST_COLLECT_METRIC=1 --entrypoint= -v `pwd`/.git:/opt/code/localstack/.git -v `pwd`/requirements-test.txt:/opt/code/localstack/requirements-test.txt -v `pwd`/tests/:/opt/code/localstack/tests/ -v `pwd`/target/:/opt/code/localstack/target/ -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/localstack:/var/lib/localstack \
		$(IMAGE_NAME):$(DEFAULT_TAG) \
	    bash -c "apt-get update && apt-get install -y g++ git && make install-test && apt-get install -y --no-install-recommends gnupg && mkdir -p /etc/apt/keyrings && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && echo \"deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_18.x nodistro main\" > /etc/apt/sources.list.d/nodesource.list && apt-get update && apt-get install -y --no-install-recommends nodejs && DEBUG=$(DEBUG) PYTEST_LOGLEVEL=$(PYTEST_LOGLEVEL) PYTEST_ARGS='$(PYTEST_ARGS)' TEST_PATH='$(TEST_PATH)' TINYBIRD_PYTEST_ARGS='$(TINYBIRD_PYTEST_ARGS)' TINYBIRD_DATASOURCE='$(TINYBIRD_DATASOURCE)' TINYBIRD_TOKEN='$(TINYBIRD_TOKEN)' TINYBIRD_URL='$(TINYBIRD_URL)' CI_COMMIT_BRANCH='$(CI_COMMIT_BRANCH)' CI_COMMIT_SHA='$(CI_COMMIT_SHA)' CI_JOB_URL='$(CI_JOB_URL)' CI_JOB_NAME='$(CI_JOB_NAME)' CI_JOB_ID='$(CI_JOB_ID)' CI='$(CI)' make test"

docker-cp-coverage:       ## Extract .coverage file from Docker image
	@echo 'Extracting .coverage file from Docker image'; \
		id=$$(docker create localstack/localstack); \
		docker cp $$id:/opt/code/localstack/.coverage .coverage; \
		docker rm -v $$id
