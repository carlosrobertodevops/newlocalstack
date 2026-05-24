import { Link } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import { ServiceIcon } from "@/lib/service-icons";
import { azureApi } from "@/lib/api/azure";
import { useCloud } from "@/lib/cloud-context";
import { useI18n } from "@/lib/i18n";
import { SERVICES_BY_CLOUD } from "@/routes/registry";

const GENERIC_AZURE: Record<string, { ns: string; rtype: string; apiVersion: string }> = {
  "Microsoft.DocumentDB": { ns: "Microsoft.DocumentDB", rtype: "databaseAccounts", apiVersion: "2023-04-15" },
  "Microsoft.EventGrid": { ns: "Microsoft.EventGrid", rtype: "topics", apiVersion: "2022-06-15" },
  "Microsoft.KeyVault": { ns: "Microsoft.KeyVault", rtype: "vaults", apiVersion: "2023-07-01" },
  "Microsoft.ServiceBus": { ns: "Microsoft.ServiceBus", rtype: "namespaces", apiVersion: "2022-10-01-preview" },
  "Microsoft.Storage.Tables": { ns: "Microsoft.Storage", rtype: "storageAccounts/tableServices", apiVersion: "2022-09-01" },
  "Microsoft.ContainerService": { ns: "Microsoft.ContainerService", rtype: "managedClusters", apiVersion: "2023-10-01" },
  "Microsoft.Sql": { ns: "Microsoft.Sql", rtype: "servers", apiVersion: "2022-11-01-preview" },
};

function nameOf(item: unknown): string {
  if (!item || typeof item !== "object") return String(item ?? "");
  const o = item as Record<string, unknown>;
  return (o.name as string) ?? (o.id as string) ?? JSON.stringify(o).slice(0, 60);
}

export function AzureOverview() {
  const { t } = useI18n();
  const { subscription } = useCloud();
  const services = SERVICES_BY_CLOUD.azure;

  const queries = useQueries({
    queries: services.map((s) => ({
      queryKey: ["azure", "overview", s.id, subscription],
      queryFn: async () => {
        try {
          switch (s.id) {
            case "Microsoft.Resources":
              return (await azureApi.listResourceGroups(subscription)) ?? [];
            case "Microsoft.Storage":
              return (await azureApi.listStorageAccounts(subscription)) ?? [];
            case "Microsoft.Network":
              return (await azureApi.listVirtualNetworks(subscription)) ?? [];
            case "Microsoft.Web":
              return (await azureApi.listAppServices(subscription)) ?? [];
            case "Microsoft.ContainerRegistry":
              return (await azureApi.listContainerRegistries(subscription)) ?? [];
            case "Microsoft.OperationalInsights":
              return (await azureApi.listLogAnalyticsWorkspaces(subscription)) ?? [];
            case "Microsoft.Cache":
              return (await azureApi.listRedisCaches(subscription)) ?? [];
            default: {
              const cfg = GENERIC_AZURE[s.id];
              if (!cfg) return [];
              return (await azureApi.listGeneric(subscription, cfg.ns, cfg.rtype, cfg.apiVersion)) ?? [];
            }
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
        <h1 className="text-2xl font-semibold">{t("overview.title.cloud", { cloud: "Azure" })}</h1>
        <p className="text-sm text-muted-foreground">
          {t("overview.subtitle.azure", {
            scope: subscription,
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
                <ServiceIcon id={s.id} cloud="azure" />
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
