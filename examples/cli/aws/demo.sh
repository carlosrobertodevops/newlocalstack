#!/usr/bin/env bash
# AWS CLI demo against LocalStack
# Requires: aws-cli v2, jq
# Run: ./demo.sh

set -e

# LocalStack credentials (test defaults)
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_DEFAULT_REGION=us-east-1

ENDPOINT="http://localhost:4566"

echo "=== S3 ==="
aws s3 mb s3://demo-bucket --endpoint-url="$ENDPOINT" 2>/dev/null || true
echo "hello world" | aws s3 cp - s3://demo-bucket/file.txt --endpoint-url="$ENDPOINT"
aws s3 ls s3://demo-bucket --endpoint-url="$ENDPOINT"

echo "=== IAM ==="
aws iam create-role \
  --role-name demo-role \
  --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}' \
  --endpoint-url="$ENDPOINT" 2>/dev/null || true
aws iam attach-role-policy \
  --role-name demo-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
  --endpoint-url="$ENDPOINT"
aws iam list-roles --endpoint-url="$ENDPOINT" | jq '.Roles[0].RoleName'

echo "=== DynamoDB ==="
aws dynamodb create-table \
  --table-name demo-table \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --endpoint-url="$ENDPOINT" 2>/dev/null || true
aws dynamodb put-item \
  --table-name demo-table \
  --item '{"id":{"S":"item1"},"data":{"S":"test"}}' \
  --endpoint-url="$ENDPOINT"
aws dynamodb scan --table-name demo-table --endpoint-url="$ENDPOINT" | jq '.Items[0]'

echo "=== SQS ==="
QUEUE_URL=$(aws sqs create-queue --queue-name demo-queue --endpoint-url="$ENDPOINT" 2>/dev/null | jq -r '.QueueUrl' || echo "http://localhost:4566/000000000000/demo-queue")
aws sqs send-message --queue-url "$QUEUE_URL" --message-body "test message" --endpoint-url="$ENDPOINT"
aws sqs receive-message --queue-url "$QUEUE_URL" --endpoint-url="$ENDPOINT" | jq '.Messages[0].Body'

echo "=== SNS ==="
TOPIC_ARN=$(aws sns create-topic --name demo-topic --endpoint-url="$ENDPOINT" 2>/dev/null | jq -r '.TopicArn' || echo "arn:aws:sns:us-east-1:000000000000:demo-topic")
aws sns publish --topic-arn "$TOPIC_ARN" --message "test notification" --endpoint-url="$ENDPOINT"
aws sns list-topics --endpoint-url="$ENDPOINT" | jq '.Topics[0].TopicArn'

echo "=== Done ==="
