# GCP LocalStack CLI Demo

Self-contained demo of GCP services (GCS, Pub/Sub, BigQuery, Cloud DNS) against LocalStack via REST/curl.

## Prerequisites

- LocalStack running: `localstack start` or `docker-compose up`
- `curl` and `jq` installed
- EDGE endpoint accessible (default: http://localhost:4566)

## Usage

```bash
chmod +x demo.sh
./demo.sh
```

Set custom endpoint/project/token via environment:
```bash
EDGE=http://localhost:4567 PROJECT=my-project TOKEN=custom-token ./demo.sh
```

## What It Shows

- **GCS**: bucket create, object upload, object list
- **Pub/Sub**: topic create, subscription create, publish, pull
- **BigQuery**: dataset create, dataset list
- **Cloud DNS**: managed zone create, zone list

## Why curl, Not gcloud?

`gcloud` CLI cannot override service endpoints uniformly across all GCP APIs via flags alone. Some services require config files or environment variables that gcloud may not respect when hitting a mock endpoint. **curl + REST is the reliable path** for LocalStack testing.

### Try gcloud (optional)

```bash
gcloud config configurations create localstack --no-user-output-enabled
gcloud config set --configuration=localstack core/project localstack-project
gcloud config set --configuration=localstack api_endpoint_override/storage http://localhost:4566
gcloud --configuration=localstack storage buckets list
```

This works for some APIs but not all. For full coverage and predictability, use the demo.sh script.
