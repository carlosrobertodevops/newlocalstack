## LocalStack Makefile — refactored for modularity
## Includes 9 modular .mk files from make/ directory

## Variable definitions (inherited by all includes)
VENV_BIN     ?= python3
VENV_DIR     ?= .venv
VENV_ACTIVATE := $(VENV_DIR)/bin/activate
VENV_RUN      := . $(VENV_ACTIVATE) &&
PIP_CMD       := $(VENV_BIN) -m pip
IMAGE_NAME    ?= localstack/localstack-custom
DEFAULT_TAG   ?= latest
PLATFORM      ?= $(shell uname -m | sed 's/arm64/arm64/g; s/x86_64/amd64/g')

TEST_PATH                ?= .
PYTEST_LOGLEVEL          ?= warning
PYTEST_ARGS              ?=
COVERAGE_FILE            ?= .coverage
JUNIT_REPORTS_FILE       ?= target/reports/junit.xml
TINYBIRD_PYTEST_ARGS     ?=
TINYBIRD_DATASOURCE      ?=
TINYBIRD_TOKEN           ?=
TINYBIRD_URL             ?=
CI_REPOSITORY_NAME       ?=
CI_WORKFLOW_NAME         ?=
CI_COMMIT_BRANCH         ?=
CI_COMMIT_SHA            ?=
CI_JOB_URL               ?=
CI_JOB_NAME              ?=
CI_JOB_ID                ?=
CI                       ?=
TEST_AWS_REGION_NAME     ?=
TEST_AWS_ACCESS_KEY_ID   ?=
TEST_AWS_ACCOUNT_ID      ?=
DEBUG                    ?= 0

.DEFAULT_GOAL := usage

## Include modular Makefiles
include make/help.mk
include make/install.mk
include make/console.mk
include make/dist.mk
include make/test.mk
include make/lint.mk
include make/asf.mk
include make/docker.mk
include make/setup.mk
include make/clean.mk
