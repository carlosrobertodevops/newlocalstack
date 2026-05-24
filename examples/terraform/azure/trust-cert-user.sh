#!/usr/bin/env bash
# NO-SUDO alternative: install LocalStack TLS cert into the user's login keychain
# (~/Library/Keychains/login.keychain-db) so azurerm Go provider trusts https://localhost:4569
# without requiring sudo or system-wide elevation.
#
# macOS may prompt for user password on first run — this is normal macOS behavior,
# not sudo. Once added to login keychain, no further prompts needed.
#
# Usage:
#   ./trust-cert-user.sh       # add to login keychain (no sudo required)
#   ./trust-cert-user.sh remove
#
# Supports: macOS only (login keychain is Darwin-specific).
# For system-wide trust (requires sudo), use trust-cert.sh instead.

set -eu

ACTION="${1:-add}"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-$0}" )" && pwd )"
REPO_ROOT="$( cd "${SCRIPT_DIR}/../../.." && pwd )"
CERT_PATH="${REPO_ROOT}/localstack-tls/certs/cert.pem"
LOGIN_KEYCHAIN="$HOME/Library/Keychains/login.keychain-db"

if [ ! -f "${CERT_PATH}" ]; then
  echo "ERROR: cert not found at ${CERT_PATH}" >&2
  exit 1
fi

case "$(uname -s)" in
  Darwin)
    if [ "${ACTION}" = "remove" ]; then
      security delete-certificate -c "localhost" "${LOGIN_KEYCHAIN}" 2>/dev/null || true
      echo "[trust-cert-user] removed from login.keychain"
    else
      # trustAsRoot: accept self-signed cert as root CA for this user session (no sudo needed)
      security add-trusted-cert -d -r trustAsRoot -k "${LOGIN_KEYCHAIN}" "${CERT_PATH}"
      echo "[trust-cert-user] installed in login.keychain (no sudo required)"
      echo "  azurerm/terraform should now trust https://localhost:4569"
      echo "  If prompted for password: enter your macOS login password (normal behavior)"
    fi
    ;;
  *)
    echo "ERROR: login keychain trust is macOS-only. Use trust-cert.sh for other systems." >&2
    exit 1
    ;;
esac
