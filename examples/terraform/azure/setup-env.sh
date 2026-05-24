#!/usr/bin/env bash
# Source me: `source ./setup-env.sh`
# Sets ARM_* + SSL_CERT_FILE so `terraform apply` talks to the LocalStack
# TLS sidecar on https://localhost:4569 without x509 errors.
#
# IMPORTANT — macOS:
#   Go's net/http on darwin reads the system Keychain ONLY and IGNORES
#   SSL_CERT_FILE/SSL_CERT_DIR. The azurerm provider is built with Go,
#   so on macOS the ONLY way to fix the x509 error is to install the cert
#   in the Keychain via `./trust-cert.sh`. Env vars are useless here.
#
# Linux:
#   Go honors SSL_CERT_FILE — exporting it is enough. Trust is optional.
#
# Optional: pass --trust to also install the cert system-wide (one-time,
# requires sudo).

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

# Detect trust via curl probe (works because curl uses LibreSSL/system store on macOS).
TRUSTED=unknown
if command -v curl >/dev/null 2>&1; then
  if curl -fs --max-time 2 https://localhost:4569/_localstack/health >/dev/null 2>&1; then
    TRUSTED=yes
  else
    TRUSTED=no
  fi
fi

OS=$(uname -s)
echo "[localstack-azure] env loaded"
echo "  OS                = ${OS}"
echo "  ARM_METADATA_HOST = ${ARM_METADATA_HOST}"
echo "  SSL_CERT_FILE     = ${SSL_CERT_FILE}"
echo "  Keychain trust    = ${TRUSTED}"

if [ "${OS}" = "Darwin" ] && [ "${TRUSTED}" != "yes" ]; then
  cat >&2 <<'WARN'

  ╔══════════════════════════════════════════════════════════════════╗
  ║ macOS WARNING: terraform will FAIL with x509 even with env vars. ║
  ║                                                                  ║
  ║ Go on darwin reads ONLY the Keychain. SSL_CERT_FILE is ignored.  ║
  ║                                                                  ║
  ║ Run ONCE to fix permanently:                                     ║
  ║                                                                  ║
  ║     ./trust-cert.sh                                              ║
  ║                                                                  ║
  ║ (sudo required — installs cert into /Library/Keychains/System.)  ║
  ╚══════════════════════════════════════════════════════════════════╝

WARN
elif [ "${TRUSTED}" = "no" ]; then
  echo "  TIP: run './setup-env.sh --trust' to install cert system-wide."
fi

echo "Next: terraform init && terraform apply -auto-approve"
