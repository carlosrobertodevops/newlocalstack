import { Link } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import { ServiceIcon } from "@/lib/service-icons";
import { gcpApi } from "@/lib/api/gcp";
import { useCloud } from "@/lib/cloud-context";
import { useI18n } from "@/lib/i18n";
import { SERVICES_BY_CLOUD } from "@/routes/registry";

function nameOf(item: unknown): string {
  if (typeof item === "string") return item;
  if (!item || typeof item !== "object") return String(item ?? "");
  const o = item as Record<string, unknown>;
  return (o.name as string) ?? (o.id as string) ?? JSON.stringify(o).slice(0, 60);
}

export function GcpOverview() {
  const { t } = useI18n();
  const { project } = useCloud();
  const services = SERVICES_BY_CLOUD.gcp;

  const queries = useQueries({
    queries: services.map((s) => ({
      queryKey: ["gcp", "overview", s.id, project],
      queryFn: async () => {
        try {
          switch (s.id) {
            case "storage":
              return (await gcpApi.listBuckets(project)) ?? [];
            case "pubsub":
              return (await gcpApi.listTopics(project)) ?? [];
            case "firestore":
              return (await gcpApi.listFirestoreDatabases(project)) ?? [];
            case "functions":
              return (await gcpApi.listFunctions(project)) ?? [];
            case "bigquery":
              return (await gcpApi.listDatasets(project)) ?? [];
            case "run":
              return (await gcpApi.listRunServices(project)) ?? [];
            case "secretmanager":
              return (await gcpApi.listSecrets(project)) ?? [];
            case "gcp-iam":
              return (await gcpApi.listServiceAccounts(project)) ?? [];
            case "gcp-kms":
              return (await gcpApi.listKeyRings(project)) ?? [];
            case "dns":
              return (await gcpApi.listZones(project)) ?? [];
            case "compute-networks":
              return (await gcpApi.listNetworks(project)) ?? [];
            case "compute":
              return (await gcpApi.listInstances(project, "us-central1-a")) ?? [];
            case "sqladmin":
              return (await gcpApi.listSqlInstances(project)) ?? [];
            case "spanner":
              return (await gcpApi.listSpannerInstances(project)) ?? [];
            case "monitoring":
              return (await gcpApi.listMonitoringMetrics(project)) ?? [];
            case "cloudscheduler":
              return (await gcpApi.listSchedulerJobs(project, "us-central1")) ?? [];
            case "container":
              return (await gcpApi.listGkeClusters(project)) ?? [];
            default:
              return [];
          }
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
        <h1 className="text-2xl font-semibold">{t("overview.title.cloud", { cloud: "GCP" })}</h1>
        <p className="text-sm text-muted-foreground">
          {t("overview.subtitle.gcp", {
            scope: project,
            total: totalResources,
            services: liveServices,
          })}
        </p>
      </header>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
        {services.map((s, i) => {
          const q = queries[i];
          const items = (q.data as unknown[]) ?? [];
          const count = items.length;
          return (
            <Link
              key={s.id}
              to={s.path}
              className="group rounded-lg border bg-card p-4 hover:border-primary hover:shadow-sm transition"
            >
              <div className="flex items-center gap-2 mb-2">
                <ServiceIcon id={s.id} cloud="gcp" />
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
                  {q.isLoading ? "…" : q.isError ? t("state.err") : count}
                </span>
              </div>
              {count > 0 && (
                <ul className="text-xs text-muted-foreground space-y-0.5 max-h-24 overflow-hidden">
                  {items.slice(0, 5).map((it, idx) => (
                    <li key={idx} className="truncate">
                      {nameOf(it)}
                    </li>
                  ))}
                  {count > 5 && (
                    <li className="text-[10px]">
                      {t("overview.more_count", { count: count - 5 })}
                    </li>
                  )}
                </ul>
              )}
            </Link>
          );
        })}
      </div>
    </div>
  );
}
