# Azure CLI demo (curl-based)

Exercises LocalStack's Azure emulation via the HTTP edge at `http://localhost:4566`.

## Why curl, not `az`

- `az` has no equivalent of `aws --endpoint-url` for arbitrary services.
- Driving `az` against a local emulator requires `az cloud register` plus
  Keychain trust for the TLS sidecar's self-signed cert on macOS — a setup
  step we deliberately avoid here.
- Plain `curl` against `:4566` (HTTP) sidesteps both problems.

## Prerequisites

- LocalStack running: `docker compose up -d localstack`
- `curl` and `bash`

## Run

```bash
./demo.sh
```

## What it exercises

| Service | Path |
| --- | --- |
| Entra (OAuth2 token) | `POST /{tenant}/oauth2/v2.0/token` |
| ARM resource group | `PUT/GET/LIST /subscriptions/{sub}/resourceGroups/{rg}` |
| ARM storage account | `PUT /subscriptions/.../providers/Microsoft.Storage/storageAccounts/{name}` |
| Blob container | `PUT /{account}/{container}?restype=container` (via `Host: <acct>.blob.core.windows.net`) |
| Blob upload/list/download | same host + path |

All requests carry a dummy `Authorization: Bearer localstack-dummy` token; the LocalStack edge accepts any bearer.
