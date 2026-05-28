import type { CloudName } from "@/lib/skins";

export interface ServiceMeta {
  id: string;
  label: string;
  path: string;
  healthId?: string;
  pro?: boolean;
  preview?: boolean;
}

export const SERVICES_BY_CLOUD: Record<CloudName, ServiceMeta[]> = {
  aws: [
    { id: "s3", label: "S3", path: "/aws/s3" },
    { id: "sqs", label: "SQS", path: "/aws/sqs" },
    { id: "sns", label: "SNS", path: "/aws/sns" },
    { id: "dynamodb", label: "DynamoDB", path: "/aws/dynamodb" },
    { id: "lambda", label: "Lambda", path: "/aws/lambda" },
    { id: "logs", label: "CloudWatch Logs", path: "/aws/logs" },
    { id: "ec2", label: "EC2", path: "/aws/ec2" },
    { id: "vpc", label: "VPC", path: "/aws/vpc", healthId: "ec2" },
    { id: "iam", label: "IAM", path: "/aws/iam" },
    { id: "secretsmanager", label: "Secrets Manager", path: "/aws/secretsmanager" },
    { id: "kms", label: "KMS", path: "/aws/kms" },
    { id: "cloudformation", label: "CloudFormation", path: "/aws/cloudformation" },
    { id: "ecr", label: "ECR", path: "/aws/ecr" },
    { id: "route53", label: "Route 53", path: "/aws/route53" },
    { id: "apigateway", label: "API Gateway", path: "/aws/apigateway" },
    { id: "stepfunctions", label: "Step Functions", path: "/aws/stepfunctions" },
    { id: "events", label: "EventBridge", path: "/aws/events" },
    { id: "kinesis", label: "Kinesis", path: "/aws/kinesis" },
    { id: "ssm", label: "SSM Parameters", path: "/aws/ssm" },
    { id: "eks", label: "EKS", path: "/aws/eks" },
    { id: "ecs", label: "ECS", path: "/aws/ecs" },
    { id: "rds", label: "RDS", path: "/aws/rds" },
  ],
  azure: [
    { id: "Microsoft.Resources", label: "Resource Groups", path: "/azure/resource-groups" },
    { id: "Microsoft.Storage", label: "Storage Accounts", path: "/azure/storage-accounts" },
    { id: "Microsoft.Network", label: "Virtual Network", path: "/azure/vnet" },
    { id: "Microsoft.Web", label: "App Service", path: "/azure/appservice" },
    { id: "Microsoft.ContainerRegistry", label: "Container Registry", path: "/azure/acr" },
    { id: "Microsoft.OperationalInsights", label: "Log Analytics", path: "/azure/monitor" },
    { id: "Microsoft.Cache", label: "Redis Cache", path: "/azure/redis" },
    { id: "Microsoft.DocumentDB", label: "Cosmos DB", path: "/azure/cosmos" },
    { id: "Microsoft.EventGrid", label: "Event Grid", path: "/azure/eventgrid" },
    { id: "Microsoft.KeyVault", label: "Key Vault", path: "/azure/keyvault" },
    { id: "Microsoft.ServiceBus", label: "Service Bus", path: "/azure/servicebus" },
    { id: "Microsoft.Storage.Tables", label: "Table Storage", path: "/azure/tablestorage" },
    { id: "Microsoft.ContainerService", label: "AKS", path: "/azure/aks" },
    { id: "Microsoft.Sql", label: "SQL Database", path: "/azure/sql" },
  ],
  gcp: [
    { id: "storage", label: "Cloud Storage", path: "/gcp/storage" },
    { id: "pubsub", label: "Pub/Sub", path: "/gcp/pubsub" },
    { id: "firestore", label: "Firestore", path: "/gcp/firestore" },
    { id: "functions", label: "Cloud Functions", path: "/gcp/functions" },
    { id: "bigquery", label: "BigQuery", path: "/gcp/bigquery" },
    { id: "run", label: "Cloud Run", path: "/gcp/run" },
    { id: "secretmanager", label: "Secret Manager", path: "/gcp/secretmanager" },
    { id: "gcp-iam", label: "IAM", path: "/gcp/iam" },
    { id: "gcp-kms", label: "Cloud KMS", path: "/gcp/kms" },
    { id: "dns", label: "Cloud DNS", path: "/gcp/dns" },
    { id: "compute-networks", label: "VPC Networks", path: "/gcp/vpc" },
    { id: "compute", label: "Compute Engine", path: "/gcp/compute" },
    { id: "sqladmin", label: "Cloud SQL", path: "/gcp/sql" },
    { id: "spanner", label: "Spanner", path: "/gcp/spanner" },
    { id: "monitoring", label: "Monitoring", path: "/gcp/monitoring" },
    { id: "cloudscheduler", label: "Cloud Scheduler", path: "/gcp/scheduler" },
    { id: "container", label: "GKE", path: "/gcp/gke" },
  ],
};
