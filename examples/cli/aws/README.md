# AWS CLI LocalStack Demo

Demonstrates AWS service interactions against LocalStack using the AWS CLI.

## Prerequisites

- LocalStack running on `localhost:4566`
- AWS CLI v2
- `jq` for JSON processing

## Quick Start

```bash
chmod +x demo.sh
./demo.sh
```

## What It Demonstrates

- **S3**: Create bucket, copy object, list contents
- **IAM**: Create role with trust policy, attach policy, list roles
- **DynamoDB**: Create table, put item, scan table
- **SQS**: Create queue, send message, receive message
- **SNS**: Create topic, publish message, list topics

Uses LocalStack endpoint (`http://localhost:4566`) with test credentials (`test/test`). Operations are idempotent and safe to re-run.
