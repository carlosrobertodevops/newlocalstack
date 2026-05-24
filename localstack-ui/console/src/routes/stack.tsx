import { useState } from "react";
import { Link } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import { ChevronRight, RefreshCw } from "lucide-react";
import { ServiceIcon } from "@/lib/service-icons";
import { awsApi } from "@/lib/api/aws";
import { azureApi } from "@/lib/api/azure";
import { gcpApi } from "@/lib/api/gcp";
import { useCloud } from "@/lib/cloud-context";
import { SERVICES_BY_CLOUD } from "@/routes/registry";
import type { CloudName } from "@/lib/skins";

type Lister = () => Promise<unknown[]>;

const AWS_LISTERS: Record<string, { fn: Lister; resourceType: string }> = {
  s3: { fn: awsApi.listBuckets, resourceType: "Bucket" },
  sqs: { fn: awsApi.listQueues, resourceType: "Queue" },
  sns: { fn: awsApi.listTopics, resourceType: "Topic" },
  dynamodb: { fn: awsApi.listTables, resourceType: "Table" },
  lambda: { fn: awsApi.listFunctions, resourceType: "Function" },
  logs: { fn: awsApi.listLogGroups, resourceType: "LogGroup" },
  ec2: { fn: awsApi.listInstances, resourceType: "Instance" },
  vpc: { fn: awsApi.listVpcs, resourceType: "VPC" },
  iam: { fn: awsApi.listIamUsers, resourceType: "User" },
  secretsmanager: { fn: awsApi.listSecrets, resourceType: "Secret" },
  kms: { fn: awsApi.listKmsKeys, resourceType: "Key" },
  cloudformation: { fn: awsApi.listStacks, resourceType: "Stack" },
  ecr: { fn: awsApi.listEcrRepos, resourceType: "Repository" },
  route53: { fn: awsApi.listHostedZones, resourceType: "HostedZone" },
  apigateway: { fn: awsApi.listRestApis, resourceType: "RestApi" },
  stepfunctions: { fn: awsApi.listStateMachines, resourceType: "StateMachine" },
  events: { fn: awsApi.listEventBuses, resourceType: "EventBus" },
  kinesis: { fn: awsApi.listKinesisStreams, resourceType: "Stream" },
  ssm: { fn: awsApi.listSsmParameters, resourceType: "Parameter" },
  eks: { fn: awsApi.listEksClusters, resourceType: "Cluster" },
  ecs: { fn: awsApi.listEcsClusters, resourceType: "Cluster" },
  rds: { fn: awsApi.listDbInstances, resourceType: "DBInstance" },
};

const AZURE_GENERIC: Record<string, { ns: string; rtype: string; apiVersion: string; resourceType: string }> = {
  "Microsoft.DocumentDB": { ns: "Microsoft.DocumentDB", rtype: "databaseAccounts", apiVersion: "2023-04-15", resourceType: "DatabaseAccount" },
  "Microsoft.EventGrid": { ns: "Microsoft.EventGrid", rtype: "topics", apiVersion: "2022-06-15", resourceType: "Topic" },
  "Microsoft.KeyVault": { ns: "Microsoft.KeyVault", rtype: "vaults", apiVersion: "2023-07-01", resourceType: "Vault" },
  "Microsoft.ServiceBus": { ns: "Microsoft.ServiceBus", rtype: "namespaces", apiVersion: "2022-10-01-preview", resourceType: "Namespace" },
  "Microsoft.Storage.Tables": { ns: "Microsoft.Storage", rtype: "storageAccounts/tableServices", apiVersion: "2022-09-01", resourceType: "TableService" },
  "Microsoft.ContainerService": { ns: "Microsoft.ContainerService", rtype: "managedClusters", apiVersion: "2023-10-01", resourceType: "ManagedCluster" },
  "Microsoft.Sql": { ns: "Microsoft.Sql", rtype: "servers", apiVersion: "2022-11-01-preview", resourceType: "Server" },
};

const AZURE_NATIVE_TYPE: Record<string, string> = {
  "Microsoft.Resources": "ResourceGroup",
  "Microsoft.Storage": "StorageAccount",
  "Microsoft.Network": "VirtualNetwork",
  "Microsoft.Web": "AppService",
  "Microsoft.ContainerRegistry": "Registry",
  "Microsoft.OperationalInsights": "Workspace",
  "Microsoft.Cache": "Redis",
};

const GCP_TYPE: Record<string, string> = {
  storage: "Bucket",
  pubsub: "Topic",
  firestore: "Database",
  functions: "Function",
  bigquery: "Dataset",
  run: "Service",
  secretmanager: "Secret",
  "gcp-iam": "ServiceAccount",
  "gcp-kms": "KeyRing",
  dns: "Zone",
  "compute-networks": "Network",
  compute: "Instance",
  sqladmin: "DBInstance",
  spanner: "Instance",
  monitoring: "Metric",
  cloudscheduler: "Job",
  container: "Cluster",
};

function nameOf(item: unknown): string {
  if (typeof item === "string") return item;
  if (!item || typeof item !== "object") return String(item ?? "");
  const o = item as Record<string, unknown>;
  return (
    (o.Name as string) ??
    (o.name as string) ??
    (o.BucketName as string) ??
    (o.FunctionName as string) ??
    (o.TopicArn as string) ??
    (o.QueueUrl as string) ??
    (o.repositoryName as string) ??
    (o.RepositoryName as string) ??
    (o.id as string) ??
    JSON.stringify(o).slice(0, 60)
  );
}

async function fetchAws(id: string): Promise<unknown[]> {
  const entry = AWS_LISTERS[id];
  if (!entry) return [];
  try {
    const out = await entry.fn();
    return Array.isArray(out) ? out : [];
  } catch {
    return [];
  }
}

async function fetchAzure(id: string, sub: string): Promise<unknown[]> {
  try {
    switch (id) {
      case "Microsoft.Resources": return (await azureApi.listResourceGroups(sub)) ?? [];
      case "Microsoft.Storage": return (await azureApi.listStorageAccounts(sub)) ?? [];
      case "Microsoft.Network": return (await azureApi.listVirtualNetworks(sub)) ?? [];
      case "Microsoft.Web": return (await azureApi.listAppServices(sub)) ?? [];
      case "Microsoft.ContainerRegistry": return (await azureApi.listContainerRegistries(sub)) ?? [];
      case "Microsoft.OperationalInsights": return (await azureApi.listLogAnalyticsWorkspaces(sub)) ?? [];
      case "Microsoft.Cache": return (await azureApi.listRedisCaches(sub)) ?? [];
      default: {
        const cfg = AZURE_GENERIC[id];
        if (!cfg) return [];
        return (await azureApi.listGeneric(sub, cfg.ns, cfg.rtype, cfg.apiVersion)) ?? [];
      }
    }
  } catch {
    return [];
  }
}

async function fetchGcp(id: string, project: string): Promise<unknown[]> {
  try {
    switch (id) {
      case "storage": return (await gcpApi.listBuckets(project)) ?? [];
      case "pubsub": return (await gcpApi.listTopics(project)) ?? [];
      case "firestore": return (await gcpApi.listFirestoreDatabases(project)) ?? [];
      case "functions": return (await gcpApi.listFunctions(project)) ?? [];
      case "bigquery": return (await gcpApi.listDatasets(project)) ?? [];
      case "run": return (await gcpApi.listRunServices(project)) ?? [];
      case "secretmanager": return (await gcpApi.listSecrets(project)) ?? [];
      case "gcp-iam": return (await gcpApi.listServiceAccounts(project)) ?? [];
      case "gcp-kms": return (await gcpApi.listKeyRings(project)) ?? [];
      case "dns": return (await gcpApi.listZones(project)) ?? [];
      case "compute-networks": return (await gcpApi.listNetworks(project)) ?? [];
      case "compute": return (await gcpApi.listInstances(project, "us-central1-a")) ?? [];
      case "sqladmin": return (await gcpApi.listSqlInstances(project)) ?? [];
      case "spanner": return (await gcpApi.listSpannerInstances(project)) ?? [];
      case "monitoring": return (await gcpApi.listMonitoringMetrics(project)) ?? [];
      case "cloudscheduler": return (await gcpApi.listSchedulerJobs(project, "us-central1")) ?? [];
      case "container": return (await gcpApi.listGkeClusters(project)) ?? [];
      default: return [];
    }
  } catch {
    return [];
  }
}

function resourceTypeOf(cloud: CloudName, id: string): string {
  if (cloud === "aws") return AWS_LISTERS[id]?.resourceType ?? "Resource";
  if (cloud === "azure") return AZURE_NATIVE_TYPE[id] ?? AZURE_GENERIC[id]?.resourceType ?? "Resource";
  return GCP_TYPE[id] ?? "Resource";
}

const CLOUD_LABEL: Record<CloudName, string> = { aws: "AWS", azure: "Azure", gcp: "GCP" };
const CLOUD_SCOPE: Record<CloudName, { region: string; account: string }> = {
  aws: { region: "us-east-1", account: "000000000000" },
  azure: { region: "eastus", account: "subscription" },
  gcp: { region: "us-central1", account: "project" },
};

interface RowProps {
  cloud: CloudName;
  serviceId: string;
  serviceLabel: string;
  resourceType: string;
  items: unknown[];
  loading: boolean;
  error: boolean;
  path: string;
}

function StackRow({ cloud, serviceId, serviceLabel, resourceType, items, loading, error, path }: RowProps) {
  const [open, setOpen] = useState(false);
  const count = items.length;
  const scope = CLOUD_SCOPE[cloud];

  if (count === 0 && !loading && !error) return null;

  return (
    <div className="border rounded-md bg-card overflow-hidden">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="w-full flex items-center gap-3 px-4 py-3 hover:bg-muted/40 transition text-left"
      >
        <ChevronRight
          size={14}
          className={`transition-transform ${open ? "rotate-90" : ""}`}
        />
        <ServiceIcon id={serviceId} cloud={cloud} />
        <div className="flex items-center gap-2 flex-1 min-w-0">
          <span className="font-semibold">{serviceLabel}</span>
          <span className="text-sm text-muted-foreground">{resourceType}</span>
          <span className="bg-zinc-900 text-white text-[10px] font-bold rounded-full w-5 h-5 flex items-center justify-center">
            {loading ? "…" : error ? "!" : count}
          </span>
        </div>
        <span className="text-xs text-muted-foreground hidden sm:inline">1 region</span>
        <span className="text-xs text-muted-foreground hidden md:inline mr-2">1 account</span>
      </button>
      {open && count > 0 && (
        <div className="border-t bg-muted/20 px-4 py-2">
          <ul className="text-xs space-y-1">
            {items.map((it, idx) => (
              <li key={idx} className="flex items-center justify-between py-1 border-b last:border-0 border-border/40">
                <span className="truncate font-mono">{nameOf(it)}</span>
                <span className="text-muted-foreground text-[10px]">
                  {scope.region} · {scope.account}
                </span>
              </li>
            ))}
          </ul>
          <Link
            to={path}
            className="text-xs text-primary hover:underline inline-block mt-2"
          >
            Open {serviceLabel} →
          </Link>
        </div>
      )}
    </div>
  );
}

function CloudStack({ cloud }: { cloud: CloudName }) {
  const { subscription, project } = useCloud();
  const services = SERVICES_BY_CLOUD[cloud];
  const [tick, setTick] = useState(0);

  const queries = useQueries({
    queries: services.map((s) => ({
      queryKey: ["stack", cloud, s.id, subscription, project, tick],
      queryFn: () =>
        cloud === "aws"
          ? fetchAws(s.healthId ?? s.id)
          : cloud === "azure"
            ? fetchAzure(s.id, subscription)
            : fetchGcp(s.id, project),
      staleTime: 10_000,
      refetchInterval: 20_000,
    })),
  });

  const rows = services
    .map((s, i) => ({
      service: s,
      data: (queries[i].data as unknown[]) ?? [],
      loading: queries[i].isLoading,
      error: queries[i].isError,
    }))
    .filter((r) => r.data.length > 0 || r.loading);

  const total = rows.reduce((a, r) => a + r.data.length, 0);

  return (
    <div className="p-6 space-y-4 max-w-5xl mx-auto">
      <header className="flex items-center justify-between flex-wrap gap-3">
        <div>
          <h1 className="text-2xl font-semibold flex items-center gap-2">
            <ServiceIcon id="cloud" cloud={cloud} />
            {CLOUD_LABEL[cloud]} · Stack Overview
            <span className="text-xs px-2 py-0.5 rounded-full bg-violet-500/15 text-violet-700 dark:text-violet-300 font-medium">
              Em ação
            </span>
          </h1>
          <p className="text-sm text-muted-foreground">
            {total} resources across {rows.length} services. Created via CLI,
            Terraform, Serverless Framework or this console.
          </p>
        </div>
        <button
          type="button"
          onClick={() => setTick((t) => t + 1)}
          className="inline-flex items-center gap-1.5 text-xs px-3 py-2 rounded-md border bg-card hover:bg-muted transition"
        >
          <RefreshCw size={12} /> Refresh
        </button>
      </header>

      {rows.length === 0 ? (
        <div className="text-sm text-muted-foreground border rounded-md p-6 bg-card text-center">
          No {CLOUD_LABEL[cloud]} resources detected yet.
          <br />
          Create some via CLI, Terraform, Serverless Framework or the console — they'll appear here.
        </div>
      ) : (
        <div className="space-y-2">
          {rows.map(({ service, data, loading, error }) => (
            <StackRow
              key={service.id}
              cloud={cloud}
              serviceId={service.id}
              serviceLabel={service.label}
              resourceType={resourceTypeOf(cloud, service.id)}
              items={data}
              loading={loading}
              error={error}
              path={service.path}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export function AwsStack() {
  return <CloudStack cloud="aws" />;
}
export function AzureStack() {
  return <CloudStack cloud="azure" />;
}
export function GcpStack() {
  return <CloudStack cloud="gcp" />;
}
