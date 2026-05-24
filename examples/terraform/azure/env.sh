# Source this file before running terraform: `source env.sh`
#
# LocalStack Azure auth (service principal — no `az login` needed).
export ARM_CLIENT_ID=00000000-0000-0000-0000-000000000001
export ARM_CLIENT_SECRET=test-secret
export ARM_TENANT_ID=localstack-tenant
export ARM_SUBSCRIPTION_ID=00000000-0000-0000-0000-000000000000
export ARM_METADATA_HOST=localhost:4569

# Path to the self-signed cert the TLS sidecar serves.
TF_AZURE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
CERT_PATH="${TF_AZURE_DIR}/../../../localstack-tls/certs/cert.pem"

if [ ! -f "${CERT_PATH}" ]; then
  echo "error: cert not found at ${CERT_PATH}" >&2
  return 1 2>/dev/null || exit 1
fi

export SSL_CERT_FILE="${CERT_PATH}"
export SSL_CERT_DIR="$(dirname "${CERT_PATH}")"

# Go's crypto/x509 on macOS uses Security.framework and ignores SSL_CERT_FILE
# unless this fallback is enabled. Linux Go reads SSL_CERT_FILE natively.
export GODEBUG="x509usefallbackroots=1${GODEBUG:+,${GODEBUG}}"

echo "azure terraform env loaded"
echo "  SSL_CERT_FILE=${SSL_CERT_FILE}"
echo "  GODEBUG=${GODEBUG}"
