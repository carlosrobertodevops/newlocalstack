#!/usr/bin/env bash
# One-time: install the LocalStack TLS cert into the system trust store so
# `terraform`, `az`, `tflocal`, etc., trust https://localhost:4569 without
# any per-shell SSL_CERT_FILE juggling.
#
# Usage:
#   ./trust-cert.sh       # add  (sudo required)
#   ./trust-cert.sh remove
#
# Supports macOS keychain + Linux update-ca-certificates.
set -eu

ACTION="${1:-add}"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-$0}" )" && pwd )"
REPO_ROOT="$( cd "${SCRIPT_DIR}/../../.." && pwd )"
CERT_PATH="${REPO_ROOT}/localstack-tls/certs/cert.pem"

if [ ! -f "${CERT_PATH}" ]; then
  echo "ERROR: cert not found at ${CERT_PATH}" >&2
  exit 1
fi

case "$(uname -s)" in
  Darwin)
    if [ "${ACTION}" = "remove" ]; then
      sudo security delete-certificate -c "localhost" /Library/Keychains/System.keychain || true
      echo "[trust-cert] removed from System.keychain"
    else
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain "${CERT_PATH}"
      echo "[trust-cert] installed in System.keychain. tflocal/terraform/az should now trust :4569"
    fi
    ;;
  Linux)
    DST="/usr/local/share/ca-certificates/localstack.crt"
    if [ "${ACTION}" = "remove" ]; then
      sudo rm -f "${DST}"
      sudo update-ca-certificates --fresh
      echo "[trust-cert] removed from system trust"
    else
      sudo cp "${CERT_PATH}" "${DST}"
      sudo update-ca-certificates
      echo "[trust-cert] installed in system trust"
    fi
    ;;
  *)
    echo "ERROR: unsupported OS $(uname -s). Use SSL_CERT_FILE env via setup-env.sh." >&2
    exit 1
    ;;
esac
