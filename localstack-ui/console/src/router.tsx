import {
  createRootRoute,
  createRoute,
  createRouter,
  Outlet,
} from "@tanstack/react-router";
import { App } from "@/App";
import { HomeIndex } from "@/routes/HomeIndex";
import { AwsOverview } from "@/routes/aws/overview";
import { AzureOverview } from "@/routes/azure/overview";
import { GcpOverview } from "@/routes/gcp/overview";
import {
  S3List,
  SqsList,
  DynamoList,
  LambdaList,
  GenericDetail,
} from "@/routes/aws/services";
import {
  SnsList,
  LogsList,
  IamList,
  SecretsList,
  Ec2List,
  KmsList as AwsKmsList,
  CfnList,
  EcrList,
} from "@/routes/aws/services-ext";
import {
  VpcList,
  Route53List,
  ApiGatewayList,
  StepFunctionsList,
  EventBridgeList,
  KinesisList,
  SsmList,
} from "@/routes/aws/services-network";
import {
  EksList,
  EcsList,
  RdsList,
} from "@/routes/aws/services-managed";
import {
  ResourceGroupsList,
  StorageAccountsList,
} from "@/routes/azure/services";
import {
  VnetList,
  AppServiceList,
  ContainerRegistryList,
  MonitorList,
  RedisList,
} from "@/routes/azure/services-ext";
import { StorageList, PubSubList } from "@/routes/gcp/services";
import {
  BigQueryList,
  FunctionsList as GcpFunctionsList,
  RunList,
  SecretManagerList,
  GcpIamList,
  FirestoreList,
  KmsList as GcpKmsList,
  DnsList,
} from "@/routes/gcp/services-ext";
import {
  VpcNetworksList,
  ComputeList,
  SqlList,
  SpannerList,
  MonitoringList,
  SchedulerList,
  GkeList,
} from "@/routes/gcp/services-compute";
import { AzureGenericList } from "@/routes/azure/services-generic";

const rootRoute = createRootRoute({ component: App });

const indexRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/",
  component: HomeIndex,
});

const cloudLayout = (path: "aws" | "azure" | "gcp") =>
  createRoute({
    getParentRoute: () => rootRoute,
    path,
    component: () => <Outlet />,
  });

const awsRoute = cloudLayout("aws");
const azureRoute = cloudLayout("azure");
const gcpRoute = cloudLayout("gcp");

const awsIndex = createRoute({ getParentRoute: () => awsRoute, path: "/", component: HomeIndex });
const azureIndex = createRoute({ getParentRoute: () => azureRoute, path: "/", component: HomeIndex });
const gcpIndex = createRoute({ getParentRoute: () => gcpRoute, path: "/", component: HomeIndex });

const route = (
  parent: typeof awsRoute | typeof azureRoute | typeof gcpRoute,
  path: string,
  Component: React.ComponentType,
) =>
  createRoute({ getParentRoute: () => parent, path, component: Component });

const azureGeneric = (
  path: string,
  title: string,
  ns: string,
  rtype: string,
  apiVersion: string,
  extraBody?: Record<string, unknown>,
) =>
  createRoute({
    getParentRoute: () => azureRoute,
    path,
    component: () => (
      <AzureGenericList
        title={title}
        ns={ns}
        rtype={rtype}
        apiVersion={apiVersion}
        extraBody={extraBody}
      />
    ),
  });

// AWS functional
const s3 = route(awsRoute, "s3", S3List);
const s3Detail = createRoute({
  getParentRoute: () => awsRoute,
  path: "s3/$bucket",
  component: () => <GenericDetail service="S3" paramKey="bucket" />,
});
const sqs = route(awsRoute, "sqs", SqsList);
const sqsDetail = createRoute({
  getParentRoute: () => awsRoute,
  path: "sqs/$queue",
  component: () => <GenericDetail service="SQS" paramKey="queue" />,
});
const dynamo = route(awsRoute, "dynamodb", DynamoList);
const dynamoDetail = createRoute({
  getParentRoute: () => awsRoute,
  path: "dynamodb/$table",
  component: () => <GenericDetail service="DynamoDB" paramKey="table" />,
});
const lambda = route(awsRoute, "lambda", LambdaList);
const lambdaDetail = createRoute({
  getParentRoute: () => awsRoute,
  path: "lambda/$fn",
  component: () => <GenericDetail service="Lambda" paramKey="fn" />,
});
const awsSns = route(awsRoute, "sns", SnsList);
const awsLogs = route(awsRoute, "logs", LogsList);
const awsEc2 = route(awsRoute, "ec2", Ec2List);
const awsVpc = route(awsRoute, "vpc", VpcList);
const awsIam = route(awsRoute, "iam", IamList);
const awsSecrets = route(awsRoute, "secretsmanager", SecretsList);
const awsKms = route(awsRoute, "kms", AwsKmsList);
const awsCfn = route(awsRoute, "cloudformation", CfnList);
const awsEcr = route(awsRoute, "ecr", EcrList);
const awsRoute53 = route(awsRoute, "route53", Route53List);
const awsApiGw = route(awsRoute, "apigateway", ApiGatewayList);
const awsSfn = route(awsRoute, "stepfunctions", StepFunctionsList);
const awsEvents = route(awsRoute, "events", EventBridgeList);
const awsKinesis = route(awsRoute, "kinesis", KinesisList);
const awsSsm = route(awsRoute, "ssm", SsmList);
const awsEks = route(awsRoute, "eks", EksList);
const awsEcs = route(awsRoute, "ecs", EcsList);
const awsRds = route(awsRoute, "rds", RdsList);

// Azure functional
const azRgs = route(azureRoute, "resource-groups", ResourceGroupsList);
const azSa = route(azureRoute, "storage-accounts", StorageAccountsList);
const azVnet = route(azureRoute, "vnet", VnetList);
const azApp = route(azureRoute, "appservice", AppServiceList);
const azAcr = route(azureRoute, "acr", ContainerRegistryList);
const azMonitor = route(azureRoute, "monitor", MonitorList);
const azRedis = route(azureRoute, "redis", RedisList);
const azCosmos = azureGeneric(
  "cosmos",
  "Azure · Cosmos DB Accounts",
  "Microsoft.DocumentDB",
  "databaseAccounts",
  "2023-11-15",
  {
    kind: "GlobalDocumentDB",
    properties: {
      databaseAccountOfferType: "Standard",
      locations: [{ locationName: "eastus", failoverPriority: 0 }],
    },
  },
);
const azEventgrid = azureGeneric(
  "eventgrid",
  "Azure · Event Grid Topics",
  "Microsoft.EventGrid",
  "topics",
  "2022-06-15",
);
const azKeyvault = azureGeneric(
  "keyvault",
  "Azure · Key Vaults",
  "Microsoft.KeyVault",
  "vaults",
  "2023-07-01",
  {
    properties: {
      sku: { family: "A", name: "standard" },
      tenantId: "00000000-0000-0000-0000-000000000000",
      accessPolicies: [],
    },
  },
);
const azServicebus = azureGeneric(
  "servicebus",
  "Azure · Service Bus Namespaces",
  "Microsoft.ServiceBus",
  "namespaces",
  "2022-10-01-preview",
  { sku: { name: "Standard", tier: "Standard" } },
);
const azTables = azureGeneric(
  "tablestorage",
  "Azure · Table Storage",
  "Microsoft.Storage",
  "storageAccounts",
  "2023-05-01",
  { sku: { name: "Standard_LRS" }, kind: "StorageV2" },
);
const azAks = azureGeneric(
  "aks",
  "Azure · AKS Clusters",
  "Microsoft.ContainerService",
  "managedClusters",
  "2023-10-01",
  {
    properties: {
      dnsPrefix: "aks",
      agentPoolProfiles: [
        { name: "agentpool", count: 1, vmSize: "Standard_DS2_v2", mode: "System" },
      ],
    },
  },
);
const azSql = azureGeneric(
  "sql",
  "Azure · SQL Servers",
  "Microsoft.Sql",
  "servers",
  "2022-05-01-preview",
  {
    properties: {
      administratorLogin: "sqladmin",
      administratorLoginPassword: "Password1!",
      version: "12.0",
    },
  },
);

// GCP functional
const gcpStorage = route(gcpRoute, "storage", StorageList);
const gcpPubsub = route(gcpRoute, "pubsub", PubSubList);
const gcpFirestore = route(gcpRoute, "firestore", FirestoreList);
const gcpFunctions = route(gcpRoute, "functions", GcpFunctionsList);
const gcpBigquery = route(gcpRoute, "bigquery", BigQueryList);
const gcpRun = route(gcpRoute, "run", RunList);
const gcpSecret = route(gcpRoute, "secretmanager", SecretManagerList);
const gcpIam = route(gcpRoute, "iam", GcpIamList);
const gcpKms = route(gcpRoute, "kms", GcpKmsList);
const gcpDns = route(gcpRoute, "dns", DnsList);
const gcpVpc = route(gcpRoute, "vpc", VpcNetworksList);
const gcpCompute = route(gcpRoute, "compute", ComputeList);
const gcpSql = route(gcpRoute, "sql", SqlList);
const gcpSpanner = route(gcpRoute, "spanner", SpannerList);
const gcpMonitoring = route(gcpRoute, "monitoring", MonitoringList);
const gcpScheduler = route(gcpRoute, "scheduler", SchedulerList);
const gcpGke = route(gcpRoute, "gke", GkeList);

const awsOverview = route(awsRoute, "overview", AwsOverview);
const azureOverview = route(azureRoute, "overview", AzureOverview);
const gcpOverview = route(gcpRoute, "overview", GcpOverview);

const routeTree = rootRoute.addChildren([
  indexRoute,
  awsRoute.addChildren([
    awsIndex,
    awsOverview,
    s3,
    s3Detail,
    sqs,
    sqsDetail,
    dynamo,
    dynamoDetail,
    lambda,
    lambdaDetail,
    awsSns,
    awsLogs,
    awsEc2,
    awsVpc,
    awsIam,
    awsSecrets,
    awsKms,
    awsCfn,
    awsEcr,
    awsRoute53,
    awsApiGw,
    awsSfn,
    awsEvents,
    awsKinesis,
    awsSsm,
    awsEks,
    awsEcs,
    awsRds,
  ]),
  azureRoute.addChildren([
    azureIndex,
    azureOverview,
    azRgs,
    azSa,
    azVnet,
    azApp,
    azAcr,
    azMonitor,
    azRedis,
    azCosmos,
    azEventgrid,
    azKeyvault,
    azServicebus,
    azTables,
    azAks,
    azSql,
  ]),
  gcpRoute.addChildren([
    gcpIndex,
    gcpOverview,
    gcpStorage,
    gcpPubsub,
    gcpFirestore,
    gcpFunctions,
    gcpBigquery,
    gcpRun,
    gcpSecret,
    gcpIam,
    gcpKms,
    gcpDns,
    gcpVpc,
    gcpCompute,
    gcpSql,
    gcpSpanner,
    gcpMonitoring,
    gcpScheduler,
    gcpGke,
  ]),
]);

export const router = createRouter({ routeTree });

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}
