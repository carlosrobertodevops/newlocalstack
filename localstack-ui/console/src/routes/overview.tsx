import { Link } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import { ServiceIcon } from "@/lib/service-icons";
import { awsApi } from "@/lib/api/aws";
import { azureApi } from "@/lib/api/azure";
import { gcpApi } from "@/lib/api/gcp";
import { useCloud } from "@/lib/cloud-context";
import { SERVICES_BY_CLOUD } from "@/routes/registry";
import type { CloudName } from "@/lib/skins";

type Lister = () => Promise<unknown[]>;

const AWS_LISTERS: Record<string, Lister> = {
  s3: awsApi.listBuckets,
  sqs: awsApi.listQueues,
  sns: awsApi.listTopics,
  dynamodb: awsApi.listTables,
  lambda: awsApi.listFunctions,
  logs: awsApi.listLogGroups,
  ec2: awsApi.listInstances,
  vpc: awsApi.listVpcs,
  iam: awsApi.listIamUsers,
  secretsmanager: awsApi.listSecrets,
  kms: awsApi.listKmsKeys,
  cloudformation: awsApi.listStacks,
  ecr: awsApi.listEcrRepos,
  route53: awsApi.listHostedZones,
  apigateway: awsApi.listRestApis,
  stepfunctions: awsApi.listStateMachines,
  events: awsApi.listEventBuses,
  kinesis: awsApi.listKinesisStreams,
  ssm: awsApi.listSsmParameters,
  eks: awsApi.listEksClusters,
  ecs: awsApi.listEcsClusters,
  rds: awsApi.listDbInstances,
};

const AZURE_GENERIC: Record<string, { ns: string; rtype: string; apiVersion: string }> = {
  "Microsoft.DocumentDB": { ns: "Microsoft.DocumentDB", rtype: "databaseAccounts", apiVersion: "2023-04-15" },
  "Microsoft.EventGrid": { ns: "Microsoft.EventGrid", rtype: "topics", apiVersion: "2022-06-15" },
  "Microsoft.KeyVault": { ns: "Microsoft.KeyVault", rtype: "vaults", apiVersion: "2023-07-01" },
  "Microsoft.ServiceBus": { ns: "Microsoft.ServiceBus", rtype: "namespaces", apiVersion: "2022-10-01-preview" },
  "Microsoft.Storage.Tables": { ns: "Microsoft.Storage", rtype: "storageAccounts/tableServices", apiVersion: "2022-09-01" },
  "Microsoft.ContainerService": { ns: "Microsoft.ContainerService", rtype: "managedClusters", apiVersion: "2023-10-01" },
  "Microsoft.Sql": { ns: "Microsoft.Sql", rtype: "servers", apiVersion: "2022-11-01-preview" },
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
  const fn = AWS_LISTERS[id];
  if (!fn) return [];
  try {
    const out = await fn();
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

const CLOUD_LABEL: Record<CloudName, string> = { aws: "AWS", azure: "Azure", gcp: "GCP" };

export function UnifiedOverview() {
  const { subscription, project } = useCloud();
  const all = (["aws", "azure", "gcp"] as CloudName[]).flatMap((cloud) =>
    SERVICES_BY_CLOUD[cloud].map((s) => ({ cloud, ...s })),
  );

  const queries = useQueries({
    queries: all.map((s) => ({
      queryKey: ["unified-overview", s.cloud, s.id, subscription, project],
      queryFn: () =>
        s.cloud === "aws"
          ? fetchAws(s.healthId ?? s.id)
          : s.cloud === "azure"
            ? fetchAzure(s.id, subscription)
            : fetchGcp(s.id, project),
      staleTime: 10_000,
      refetchInterval: 20_000,
    })),
  });

  const totalsByCloud: Record<CloudName, number> = { aws: 0, azure: 0, gcp: 0 };
  const liveByCloud: Record<CloudName, number> = { aws: 0, azure: 0, gcp: 0 };
  queries.forEach((q, i) => {
    const items = (q.data as unknown[]) ?? [];
    totalsByCloud[all[i].cloud] += items.length;
    if (items.length > 0) liveByCloud[all[i].cloud] += 1;
  });
  const grandTotal = totalsByCloud.aws + totalsByCloud.azure + totalsByCloud.gcp;

  return (
    <div className="p-6 space-y-6">
      <header className="space-y-1">
        <h1 className="text-2xl font-semibold">Unified Overview · All Clouds</h1>
        <p className="text-sm text-muted-foreground">
          Resources created via CLI (aws/az/gcloud), Terraform, Serverless Framework or the
          New LocalStack Console. <strong>{grandTotal}</strong> resources total.
        </p>
        <div className="flex gap-3 pt-2 text-xs">
          {(Object.keys(totalsByCloud) as CloudName[]).map((c) => (
            <span key={c} className="rounded-md border px-2 py-1">
              <strong>{CLOUD_LABEL[c]}</strong>: {totalsByCloud[c]} resources · {liveByCloud[c]} live services
            </span>
          ))}
        </div>
      </header>

      {(["aws", "azure", "gcp"] as CloudName[]).map((cloud) => {
        const items = all
          .map((s, i) => ({ s, q: queries[i] }))
          .filter(({ s }) => s.cloud === cloud);
        return (
          <section key={cloud} className="space-y-2">
            <h2 className="text-lg font-semibold flex items-center gap-2">
              <ServiceIcon id="cloud" cloud={cloud} />
              {CLOUD_LABEL[cloud]}
              <span className="text-xs font-normal text-muted-foreground">
                ({totalsByCloud[cloud]} resources)
              </span>
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
              {items.map(({ s, q }) => {
                const data = (q.data as unknown[]) ?? [];
                const count = data.length;
                return (
                  <Link
                    key={`${cloud}-${s.id}`}
                    to={s.path}
                    className="group rounded-lg border bg-card p-3 hover:border-primary hover:shadow-sm transition"
                  >
                    <div className="flex items-center gap-2 mb-1">
                      <ServiceIcon id={s.id} cloud={cloud} />
                      <span className="font-medium text-sm flex-1 truncate">{s.label}</span>
                      <span
                        className={`text-xs px-2 py-0.5 rounded ${
                          count > 0
                            ? "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300"
                            : q.isError
                              ? "bg-rose-500/15 text-rose-700 dark:text-rose-300"
                              : "bg-muted text-muted-foreground"
                        }`}
                      >
                        {q.isLoading ? "…" : q.isError ? "err" : count}
                      </span>
                    </div>
                    {count > 0 && (
                      <ul className="text-[11px] text-muted-foreground space-y-0.5 max-h-20 overflow-hidden">
                        {data.slice(0, 4).map((it, idx) => (
                          <li key={idx} className="truncate">
                            {nameOf(it)}
                          </li>
                        ))}
                        {count > 4 && <li className="text-[10px]">+ {count - 4} more</li>}
                      </ul>
                    )}
                  </Link>
                );
              })}
            </div>
          </section>
        );
      })}
    </div>
  );
}
