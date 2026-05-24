#!/usr/bin/env bash
set -euo pipefail

# GCP LocalStack CLI demo (curl-based)
# Run: localstack start, then ./demo.sh

export EDGE="${EDGE:-http://localhost:4566}"
export PROJECT="${PROJECT:-localstack-project}"
export TOKEN="${TOKEN:-localstack-dummy}"
export BUCKET="demo-bucket-$(date +%s)"
export TOPIC="demo-topic"
export SUBSCRIPTION="demo-sub"
export DATASET="demo_dataset"
export ZONE="demo.example.com"
export ZONE_NAME="demo-zone"

echo "=== GCP LocalStack CLI Demo ==="
echo "EDGE: $EDGE"
echo "PROJECT: $PROJECT"
echo

# GCS bucket create
echo "--- GCS Bucket Create ---"
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$BUCKET\", \"project\": \"$PROJECT\"}" \
  "$EDGE/storage/v1/b?project=$PROJECT" | jq . || echo "Bucket may exist; continuing..."
echo

# GCS object upload (create empty object)
echo "--- GCS Object Upload ---"
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: text/plain" \
  --data "demo-content-$(date +%s)" \
  "$EDGE/upload/storage/v1/b/$BUCKET/o?uploadType=media&name=demo-object.txt" | jq . || echo "Upload may exist; continuing..."
echo

# GCS object list
echo "--- GCS Object List ---"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  "$EDGE/storage/v1/b/$BUCKET/o" | jq '.items[]?.name' || echo "No objects; continuing..."
echo

# Pub/Sub topic create
echo "--- Pub/Sub Topic Create ---"
curl -s -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{}" \
  "$EDGE/v1/projects/$PROJECT/topics/$TOPIC" | jq . || echo "Topic may exist; continuing..."
echo

# Pub/Sub subscription create
echo "--- Pub/Sub Subscription Create ---"
curl -s -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"topic\": \"projects/$PROJECT/topics/$TOPIC\"}" \
  "$EDGE/v1/projects/$PROJECT/subscriptions/$SUBSCRIPTION" | jq . || echo "Subscription may exist; continuing..."
echo

# Pub/Sub publish message
echo "--- Pub/Sub Publish Message ---"
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"messages\": [{\"data\": \"$(echo 'test message' | base64)\"}]}" \
  "$EDGE/v1/projects/$PROJECT/topics/$TOPIC:publish" | jq . || echo "Publish failed; continuing..."
echo

# Pub/Sub pull messages
echo "--- Pub/Sub Pull Messages ---"
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"maxMessages\": 10}" \
  "$EDGE/v1/projects/$PROJECT/subscriptions/$SUBSCRIPTION:pull" | jq . || echo "Pull returned empty; continuing..."
echo

# BigQuery dataset create
echo "--- BigQuery Dataset Create ---"
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"datasetReference\": {\"projectId\": \"$PROJECT\", \"datasetId\": \"$DATASET\"}, \"location\": \"US\"}" \
  "$EDGE/bigquery/v2/projects/$PROJECT/datasets" | jq . || echo "Dataset may exist; continuing..."
echo

# BigQuery dataset list
echo "--- BigQuery Dataset List ---"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  "$EDGE/bigquery/v2/projects/$PROJECT/datasets" | jq '.datasets[]?.datasetReference.datasetId' || echo "No datasets; continuing..."
echo

# Cloud DNS managed zone create
echo "--- Cloud DNS Managed Zone Create ---"
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$ZONE_NAME\", \"dnsName\": \"$ZONE.\"}" \
  "$EDGE/dns/v1/projects/$PROJECT/managedZones" | jq . || echo "Zone may exist; continuing..."
echo

# Cloud DNS zone list
echo "--- Cloud DNS Zone List ---"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  "$EDGE/dns/v1/projects/$PROJECT/managedZones" | jq '.managedZones[]?.name' || echo "No zones; continuing..."
echo

echo "=== Demo Complete ==="
