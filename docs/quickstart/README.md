# Quickstart — newlocalstack

Stack multi-cloud (AWS + Azure + GCP) em 3 comandos.

## Pré-requisitos

- Docker + Docker Compose
- Python 3.10+
- make
- (Opcional) bun para a Console UI

## Passos

```bash
git clone <repo> && cd newlocalstack
make setup    # instala venv, builds imagem Docker, console SPA
make start    # sobe docker compose
```

A stack expõe:
- LocalStack gateway: http://localhost:4566
- Console UI: http://localhost:4577
- TLS gateway (Azure): https://localhost:4569

## Próximos passos

- Guias por tecnologia: [docs/guides/](../guides/)
- Conceitos do core: [docs/reference/concepts/](../reference/concepts/)
- Testes: [docs/reference/testing/](../reference/testing/)
- Exemplos prontos: [examples/](../../examples/)

## Setup Azure TLS (opcional)

```bash
make setup-azure-tls   # uma vez por máquina
```
