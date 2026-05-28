import { useQuery } from "@tanstack/react-query";
import { Link } from "@tanstack/react-router";
import { cloudsApi, type CloudHealth } from "@/lib/api/clouds";
import { useCloud } from "@/lib/cloud-context";
import { useI18n } from "@/lib/i18n";
import { Badge } from "@/components/ui/badge";
import { ServiceIcon } from "@/lib/service-icons";
import { SERVICES_BY_CLOUD } from "@/routes/registry";

export function Sidebar() {
  const { cloud } = useCloud();
  const { t } = useI18n();
  const { data, isLoading, error } = useQuery<CloudHealth>({
    queryKey: ["cloud-health", cloud],
    queryFn: () => cloudsApi.health(cloud),
    refetchInterval: 15_000,
  });

  const states = data?.services ?? {};
  const services = SERVICES_BY_CLOUD[cloud] ?? [];

  return (
    <aside
      className="w-64 shrink-0 overflow-y-auto p-3 text-sm"
      style={{ background: "var(--sidebar)", color: "var(--sidebar-text)" }}
    >
      <div
        className="px-2 pb-2 text-xs uppercase tracking-wider"
        style={{ color: "var(--sidebar-muted)" }}
      >
        {t("sidebar.services", { cloud: cloud.toUpperCase() })}
      </div>
      {isLoading && (
        <div className="px-2 text-xs" style={{ color: "var(--sidebar-muted)" }}>
          {t("sidebar.loading")}
        </div>
      )}
      {error && (
        <div className="px-2 text-xs" style={{ color: "var(--sidebar-muted)" }}>
          {t("sidebar.health_offline") ?? "health offline"}
        </div>
      )}
      <ul className="space-y-0.5 mb-2">
        <li>
          <Link
            to="/stack"
            search={{ cloud }}
            className="group flex items-center justify-between rounded-md px-2 py-1.5 sidebar-link font-semibold"
            activeProps={{ className: "sidebar-link-active" }}
          >
            <span className="flex items-center gap-2 min-w-0">
              <ServiceIcon id="cloud" cloud={cloud} />
              <span className="truncate">{t("sidebar.multi_cloud_stack") ?? "Multi-Cloud Stack"}</span>
            </span>
          </Link>
        </li>
        <li>
          <Link
            to="/overview"
            params={{}}
            className="group flex items-center justify-between rounded-md px-2 py-1.5 sidebar-link font-semibold"
            activeProps={{ className: "sidebar-link-active" }}
          >
            <span className="flex items-center gap-2 min-w-0">
              <ServiceIcon id="cloud" cloud={cloud} />
              <span className="truncate">{t("sidebar.all_clouds_overview")}</span>
            </span>
          </Link>
        </li>
        <li>
          <Link
            to={`/${cloud}/overview`}
            params={{}}
            className="group flex items-center justify-between rounded-md px-2 py-1.5 sidebar-link font-medium"
            activeProps={{ className: "sidebar-link-active" }}
          >
            <span className="flex items-center gap-2 min-w-0">
              <ServiceIcon id="cloud" cloud={cloud} />
              <span className="truncate">{t("sidebar.overview")}</span>
            </span>
          </Link>
        </li>
        <li>
          <Link
            to={`/${cloud}/stack`}
            params={{}}
            className="group flex items-center justify-between rounded-md px-2 py-1.5 sidebar-link font-medium"
            activeProps={{ className: "sidebar-link-active" }}
          >
            <span className="flex items-center gap-2 min-w-0">
              <ServiceIcon id="cloud" cloud={cloud} />
              <span className="truncate">{t("sidebar.stack")}</span>
            </span>
          </Link>
        </li>
      </ul>
      <ul className="space-y-0.5">
        {services.map((s) => {
          const raw = states[s.healthId ?? s.id];
          const state = raw ?? "ready";
          const variant =
            state === "available" || state === "running" || state === "ready"
              ? "success"
              : state === "disabled"
                ? "warn"
                : "muted";
          return (
            <li key={s.id}>
              <Link
                to={s.path}
                params={{}}
                className="group flex items-center justify-between rounded-md px-2 py-1.5 sidebar-link"
                activeProps={{ className: "sidebar-link-active" }}
              >
                <span className="flex items-center gap-2 min-w-0">
                  <ServiceIcon id={s.id} cloud={cloud} />
                  <span className="truncate">{s.label}</span>
                </span>
                <Badge variant={variant} className="text-[10px] py-0">
                  {t(`state.${state}`)}
                </Badge>
              </Link>
            </li>
          );
        })}
      </ul>
    </aside>
  );
}
