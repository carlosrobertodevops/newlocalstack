# LocalStack — Multi-Cloud Emulator

Emula AWS, Azure, e GCP localmente. Rode aplicações em nuvem no seu laptop sem conectar a provedores reais.

## Quickstart

```bash
git clone https://github.com/localstack/localstack.git
cd localstack

make install          # Setup completo (venv + deps)
make setup            # Setup completo (venv + deps)
make start            # Inicia LocalStack + console UI
```

Endpoints:

- **Gateway (AWS):** `http://localhost:4566`
- **Console UI:** `http://localhost:4577`
- **TLS (Azure):** `https://localhost:4569` (requer `make setup-azure-tls`)

## Cloud Support

| Cloud     | Status       | Gateway          | Features                                       |
| --------- | ------------ | ---------------- | ---------------------------------------------- |
| **AWS**   | Stable       | `localhost:4566` | 100+ serviços (Lambda, S3, DynamoDB, IAM, ...) |
| **Azure** | Experimental | `localhost:4569` | Storage (Blob/Queue), Entra (OAuth2), ARM API  |
| **GCP**   | Experimental | `localhost:4566` | Storage, Pub/Sub, Firestore, IAM, Functions    |

## Documentation

- [Architecture & Concepts](docs/reference/concepts/README.md)
- [Testing Guide](docs/reference/testing/README.md)
- [Azure + Terraform](docs/guides/azure-terraform.md)
- [GCP + Terraform](docs/guides/gcp-terraform.md)
- [Serverless Framework](docs/guides/serverless-framework.md)
- [Multi-Cloud Stack Management](docs/guides/multi-cloud-stack.md)
- [Console UI](docs/guides/console-stack-view.md)

## Development

```bash
make lint              # Ruff + mypy + deptry
make test TEST_PATH=<path>
make entrypoints       # Regen plux.ini após novo plugin

# Docker
make docker-build
docker-compose up
```

Veja [PLAN.md](docs/PLAN.md) para roadmap e fases de desenvolvimento.

## License

Apache License 2.0. Veja [LICENSE](LICENSE.txt).
