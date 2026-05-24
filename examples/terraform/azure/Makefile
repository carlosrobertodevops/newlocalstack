# Makefile that always invokes terraform with the LocalStack TLS env.
# Use this when you don't want to rely on direnv or remember to source env.

.PHONY: setup trust init plan apply destroy env clean

setup: trust
	@./tflocal-azure init

trust:
	@./trust-cert.sh add

init:
	@./tflocal-azure init

plan:
	@./tflocal-azure plan

apply:
	@./tflocal-azure apply -auto-approve

destroy:
	@./tflocal-azure destroy -auto-approve

env:
	@./setup-env.sh

clean:
	@rm -rf .terraform .terraform.lock.hcl terraform.tfstate*
