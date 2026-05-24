#!/usr/bin/env bash
# Source me: `source ./setup-env.sh`
# Sets ARM_* + SSL_CERT_FILE so `terraform apply` talks to the LocalStack
# TLS sidecar on https://localhost:4569 without x509 errors.
#
# Optional: pass --trust to also install the cert system-wide (one-time,
# requires sudo). After that, even `terraform` invoked outside this dir
# (or outside direnv) trusts https://localhost:4569.

set -eu

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-$0}" )" && pwd )"
REPO_ROOT="$( cd "${SCRIPT_DIR}/../../.." && pwd )"
CERT_PATH="${REPO_ROOT}/localstack-tls/certs/cert.pem"

if [ ! -f "${CERT_PATH}" ]; then
  echo "ERROR: cert not found at ${CERT_PATH}" >&2
  echo "       Start the TLS sidecar (docker-compose up localstack-tls) or" >&2
  echo "       regenerate certs in localstack-tls/certs/." >&2
  return 1 2>/dev/null || exit 1
fi

export ARM_CLIENT_ID="${ARM_CLIENT_ID:-00000000-0000-0000-0000-000000000001}"
export ARM_CLIENT_SECRET="${ARM_CLIENT_SECRET:-test-secret}"
export ARM_TENANT_ID="${ARM_TENANT_ID:-localstack-tenant}"
export ARM_SUBSCRIPTION_ID="${ARM_SUBSCRIPTION_ID:-00000000-0000-0000-0000-000000000000}"
export ARM_METADATA_HOST="${ARM_METADATA_HOST:-localhost:4569}"
export SSL_CERT_FILE="${SSL_CERT_FILE:-${CERT_PATH}}"
export REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${CERT_PATH}}"
export CURL_CA_BUNDLE="${CURL_CA_BUNDLE:-${CERT_PATH}}"
export SSL_CERT_DIR="${SSL_CERT_DIR:-${REPO_ROOT}/localstack-tls/certs}"

if [ "${1:-}" = "--trust" ]; then
  "${SCRIPT_DIR}/trust-cert.sh" add
fi

if command -v curl >/dev/null 2>&1; then
  if curl -fs --max-time 2 https://localhost:4569/_localstack/health >/dev/null 2>&1; then
    TRUSTED=yes
  else
    TRUSTED=no
  fi
else
  TRUSTED=unknown
fi

echo "[localstack-azure] env loaded"
echo "  ARM_METADATA_HOST = ${ARM_METADATA_HOST}"
echo "  SSL_CERT_FILE     = ${SSL_CERT_FILE}"
echo "  System trust      = ${TRUSTED}  (yes = terraform works in any shell)"
if [ "${TRUSTED}" = "no" ]; then
  echo
  echo "  TIP: run './setup-env.sh --trust' (or './trust-cert.sh') once to"
  echo "       install cert system-wide. Then 'terraform plan' works without"
  echo "       sourcing this script."
fi
echo "Next: terraform init && terraform apply -auto-approve"
