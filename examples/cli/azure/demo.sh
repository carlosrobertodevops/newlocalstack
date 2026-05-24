#!/usr/bin/env bash
# Azure REST demo against LocalStack via the HTTP edge.
#
# `az` itself cannot drive LocalStack cleanly (no per-API endpoint override,
# and login.microsoftonline.com calls require Keychain trust for the local
# self-signed cert). This demo uses plain `curl` against :4566, mirroring
# examples/cli/gcp/demo.sh.
#
# LocalStack's Azure gateway routes by Host header for data-plane services:
#   *.blob.core.windows.net   -> blob router
#   *.queue.core.windows.net  -> queue router
#   *.documents.azure.com     -> cosmos router
# ARM control plane is path-based (/subscriptions/...). OAuth token is
# path-based (/{tenant}/oauth2/v2.0/token).
set -euo pipefail

EDGE="${EDGE:-http://localhost:4566}"
SUB="${SUB:-00000000-0000-0000-0000-000000000000}"
TENANT="${TENANT:-common}"
TOKEN="${TOKEN:-localstack-dummy}"
ACCT="${ACCT:-demoaccount}"
API="api-version=2021-04-01"

ARM() { curl -fsS -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" "$@" || true; }
BLOB() { curl -fsS -H "Host: ${ACCT}.blob.core.windows.net" "$@" || true; }

echo "== 1. Entra OAuth2 token =="
curl -fsS -X POST "${EDGE}/${TENANT}/oauth2/v2.0/token" \
  -d "grant_type=client_credentials&client_id=demo&client_secret=demo&scope=https://management.azure.com/.default" \
  | head -c 200; echo

echo "== 2. Resource group: create =="
ARM -X PUT "${EDGE}/subscriptions/${SUB}/resourceGroups/demo-rg?${API}" \
  -d '{"location":"eastus","tags":{"env":"demo"}}' | head -c 200; echo

echo "== 3. Resource group: get =="
ARM "${EDGE}/subscriptions/${SUB}/resourceGroups/demo-rg?${API}" | head -c 200; echo

echo "== 4. Storage account (ARM) =="
ARM -X PUT \
  "${EDGE}/subscriptions/${SUB}/resourceGroups/demo-rg/providers/Microsoft.Storage/storageAccounts/${ACCT}?api-version=2023-01-01" \
  -d '{"location":"eastus","sku":{"name":"Standard_LRS"},"kind":"StorageV2","properties":{}}' | head -c 200; echo

echo "== 5. Blob container: create =="
BLOB -X PUT "${EDGE}/demo-container?restype=container" \
  -w "  HTTP %{http_code}\n" -o /dev/null

echo "== 6. Blob upload =="
BLOB -X PUT \
  -H "x-ms-blob-type: BlockBlob" \
  -H "Content-Type: text/plain" \
  --data-binary "hello from localstack-azure" \
  "${EDGE}/demo-container/hello.txt" \
  -w "  HTTP %{http_code}\n" -o /dev/null

echo "== 7. Blob list =="
BLOB "${EDGE}/demo-container?restype=container&comp=list" | head -c 400; echo

echo "== 8. Blob download =="
BLOB "${EDGE}/demo-container/hello.txt"; echo

echo "== 9. Resource groups: list =="
ARM "${EDGE}/subscriptions/${SUB}/resourceGroups?${API}" | head -c 400; echo

echo "done."
