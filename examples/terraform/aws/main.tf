terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# AWS provider pointed at LocalStack.
# All commands use http://localhost:4566 instead of real AWS APIs.
provider "aws" {
  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"
  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3             = "http://localhost:4566"
    sqs            = "http://localhost:4566"
    sns            = "http://localhost:4566"
    dynamodb       = "http://localhost:4566"
    lambda         = "http://localhost:4566"
    iam            = "http://localhost:4566"
    sts            = "http://localhost:4566"
    cloudwatch     = "http://localhost:4566"
    cloudwatchlogs = "http://localhost:4566"
    secretsmanager = "http://localhost:4566"
    ssm            = "http://localhost:4566"
    kms            = "http://localhost:4566"
    apigateway     = "http://localhost:4566"
    events         = "http://localhost:4566"
    kinesis        = "http://localhost:4566"
    firehose       = "http://localhost:4566"
    stepfunctions  = "http://localhost:4566"
    ec2            = "http://localhost:4566"
    route53        = "http://localhost:4566"
    cloudformation = "http://localhost:4566"
    eks            = "http://localhost:4566"
    ecs            = "http://localhost:4566"
    rds            = "http://localhost:4566"
    ecr            = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "demo" {
  bucket = "tf-localstack-aws-demo"
}

resource "aws_sqs_queue" "demo" {
  name = "tf-localstack-queue"
}

resource "aws_dynamodb_table" "demo" {
  name         = "tf-localstack-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_ecr_repository" "demo" {
  name                 = "tf-localstack-ecr"
  image_tag_mutability = "MUTABLE"
  force_delete         = true
}

resource "aws_ecs_cluster" "demo" {
  name = "tf-localstack-ecs"
}

resource "aws_iam_role" "eks" {
  name = "tf-localstack-eks-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "eks.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_vpc" "demo" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "demo_a" {
  vpc_id            = aws_vpc.demo.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_subnet" "demo_b" {
  vpc_id            = aws_vpc.demo.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"
}

resource "aws_eks_cluster" "demo" {
  name     = "tf-localstack-eks"
  role_arn = aws_iam_role.eks.arn
  version  = "1.29"
  vpc_config {
    subnet_ids = [aws_subnet.demo_a.id, aws_subnet.demo_b.id]
  }
}

resource "aws_db_subnet_group" "demo" {
  name       = "tf-localstack-rds-sng"
  subnet_ids = [aws_subnet.demo_a.id, aws_subnet.demo_b.id]
}

resource "aws_db_instance" "demo" {
  identifier             = "tf-localstack-rds"
  engine                 = "postgres"
  engine_version         = "15"
  instance_class         = "db.t3.micro"
  allocated_storage      = 20
  username               = "admin"
  password               = "Password1!"
  db_subnet_group_name   = aws_db_subnet_group.demo.name
  skip_final_snapshot    = true
  publicly_accessible    = false
}

output "bucket" { value = aws_s3_bucket.demo.bucket }
output "queue"  { value = aws_sqs_queue.demo.url }
output "table"  { value = aws_dynamodb_table.demo.name }
output "ecr"    { value = aws_ecr_repository.demo.repository_url }
output "ecs"    { value = aws_ecs_cluster.demo.name }
output "eks"    { value = aws_eks_cluster.demo.name }
output "rds"    { value = aws_db_instance.demo.endpoint }
output "vpc"    { value = aws_vpc.demo.id }
