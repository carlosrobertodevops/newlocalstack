/**
 * Terraform / Serverless snippet generators. Each returns the *resource
 * block only* — the backend wraps it with a provider configuration that
 * points at LocalStack. See docs/multi-cloud-console-plan.md §3.4.
 */

const tf = String.raw;

function sanitize(name: string): string {
  return name.replace(/[^A-Za-z0-9_]/g, "_");
}

export function genTerraformS3Bucket(name: string): string {
  const id = sanitize(name) || "bucket";
  return tf`resource "aws_s3_bucket" "${id}" {
  bucket        = "${name}"
  force_destroy = true
}`;
}

export function genTerraformSqsQueue(name: string, attrs?: { fifo?: boolean }): string {
  const id = sanitize(name) || "queue";
  return tf`resource "aws_sqs_queue" "${id}" {
  name${attrs?.fifo ? "        = \"" + name + ".fifo\"\n  fifo_queue = true" : "       = \"" + name + "\""}
}`;
}

export function genTerraformDynamoTable(
  name: string,
  partitionKey: string,
  sortKey?: string,
): string {
  const id = sanitize(name) || "table";
  const sortBlock = sortKey
    ? `\n  range_key   = "${sortKey}"\n  attribute {\n    name = "${sortKey}"\n    type = "S"\n  }`
    : "";
  return tf`resource "aws_dynamodb_table" "${id}" {
  name         = "${name}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "${partitionKey}"
  attribute {
    name = "${partitionKey}"
    type = "S"
  }${sortBlock}
}`;
}

export function genTerraformLambdaFunction(
  name: string,
  runtime: string,
  handler: string,
): string {
  const id = sanitize(name) || "fn";
  return tf`resource "aws_lambda_function" "${id}" {
  function_name = "${name}"
  runtime       = "${runtime}"
  handler       = "${handler}"
  role          = "arn:aws:iam::000000000000:role/lambda-role"
  filename      = "${name}.zip"
}`;
}

export function genTerraformAzureRg(name: string, location: string): string {
  const id = sanitize(name) || "rg";
  return tf`resource "azurerm_resource_group" "${id}" {
  name     = "${name}"
  location = "${location}"
}`;
}

export function genTerraformAzureStorageAccount(
  name: string,
  rg: string,
  location: string,
): string {
  const id = sanitize(name) || "sa";
  return tf`resource "azurerm_storage_account" "${id}" {
  name                     = "${name}"
  resource_group_name      = "${rg}"
  location                 = "${location}"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}`;
}

export function genTerraformGcsBucket(name: string, project: string): string {
  const id = sanitize(name) || "bucket";
  return tf`resource "google_storage_bucket" "${id}" {
  name     = "${name}"
  project  = "${project}"
  location = "US"
}`;
}

export function genTerraformPubSubTopic(name: string, project: string): string {
  const id = sanitize(name) || "topic";
  return tf`resource "google_pubsub_topic" "${id}" {
  name    = "${name}"
  project = "${project}"
}`;
}

export function genServerlessLambdaFunction(
  name: string,
  runtime: string,
  handler: string,
): string {
  return `service: ${sanitize(name) || "svc"}
provider:
  name: aws
  runtime: ${runtime}
  region: us-east-1
functions:
  ${sanitize(name)}:
    handler: ${handler}
    name: ${name}
`;
}
