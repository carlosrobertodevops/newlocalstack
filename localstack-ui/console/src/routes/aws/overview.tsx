import { Link } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import { ServiceIcon } from "@/lib/service-icons";
import { awsApi } from "@/lib/api/aws";
import { SERVICES_BY_CLOUD } from "@/routes/registry";

type Lister = () => Promise<unknown[]>;

const LISTERS: Record<string, Lister> = {
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

function nameOf(item: unknown): string {
  if (typeof item === "string") return item;
  if (!item || typeof item !== "object") return String(item);
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

export function AwsOverview() {
  const services = SERVICES_BY_CLOUD.aws;
  const queries = useQueries({
    queries: services.map((s) => ({
      queryKey: ["aws", "overview", s.id],
      queryFn: async () => {
        const fn = LISTERS[s.healthId ?? s.id];
        if (!fn) return [];
        try {
          const out = await fn();
          return Array.isArray(out) ? out : [];
        } catch {
          return [];
        }
      },
      staleTime: 10_000,
      refetchInterval: 15_000,
    })),
  });

  const totalResources = queries.reduce((acc, q) => acc + ((q.data as unknown[])?.length ?? 0), 0);
  const liveServices = queries.filter((q) => ((q.data as unknown[])?.length ?? 0) > 0).length;

  return (
    <div className="p-6 space-y-6">
      <header className="space-y-1">
        <h1 className="text-2xl font-semibold">AWS · Overview</h1>
        <p className="text-sm text-muted-foreground">
          Resources created via CLI, Terraform, Serverless or this console.
          Live total: <strong>{totalResources}</strong> across <strong>{liveServices}</strong> services.
        </p>
      </header>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
        {services.map((s, i) => {
          const q = queries[i];
          const items = (q.data as unknown[]) ?? [];
          const count = items.length;
          const loading = q.isLoading;
          const err = q.isError;
          return (
            <Link
              key={s.id}
              to={s.path}
              className="group rounded-lg border bg-card p-4 hover:border-primary hover:shadow-sm transition"
            >
              <div className="flex items-center gap-2 mb-2">
                <ServiceIcon id={s.id} cloud="aws" />
                <span className="font-medium text-sm flex-1 truncate">{s.label}</span>
                <span
                  className={`text-xs px-2 py-0.5 rounded ${
                    count > 0
                      ? "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300"
                      : err
                        ? "bg-rose-500/15 text-rose-700 dark:text-rose-300"
                        : "bg-muted text-muted-foreground"
                  }`}
                >
                  {loading ? "…" : err ? "err" : count}
                </span>
              </div>
              {count > 0 && (
                <ul className="text-xs text-muted-foreground space-y-0.5 max-h-24 overflow-hidden">
                  {items.slice(0, 5).map((it, idx) => (
                    <li key={idx} className="truncate">
                      {nameOf(it)}
                    </li>
                  ))}
                  {count > 5 && <li className="text-[10px]">+ {count - 5} more</li>}
                </ul>
              )}
            </Link>
          );
        })}
      </div>
    </div>
  );
}
