import { useQuery } from "@tanstack/react-query";
import { Link } from "@tanstack/react-router";
import { useCloud } from "@/lib/cloud-context";
import { useI18n } from "@/lib/i18n";
import { cloudsApi } from "@/lib/api/clouds";
import { SERVICES_BY_CLOUD } from "@/routes/registry";
import { ServiceIcon } from "@/lib/service-icons";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export function HomeIndex() {
  const { cloud } = useCloud();
  const { t } = useI18n();
  const { data } = useQuery({
    queryKey: ["cloud-health", cloud],
    queryFn: () => cloudsApi.health(cloud),
  });
  const states = data?.services ?? {};
  const services = SERVICES_BY_CLOUD[cloud] ?? [];

  return (
    <div className="p-4">
      <h1 className="text-xl font-semibold mb-3">
        {t("home.title", { cloud: cloud.toUpperCase() })}
      </h1>
      <p className="text-sm text-muted-foreground mb-4">{t("home.subtitle")}</p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
        {services.map((s) => {
          const raw = states[s.healthId ?? s.id];
          const state = s.pro
            ? "pro"
            : s.preview
              ? "preview"
              : (raw ?? "ready");
          const variant =
            state === "available" || state === "running" || state === "ready"
              ? "success"
              : state === "disabled" || state === "pro"
                ? "warn"
                : "muted";
          return (
            <Link key={s.id} to={s.path}>
              <Card className="hover:bg-accent transition-colors cursor-pointer">
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle className="flex items-center gap-2">
                      <ServiceIcon
                        id={s.id}
                        cloud={cloud}
                        style={{ width: 18, height: 18 }}
                      />
                      <span>{s.label}</span>
                    </CardTitle>
                    <Badge variant={variant}>{state}</Badge>
                  </div>
                  <CardDescription className="text-xs">{s.id}</CardDescription>
                </CardHeader>
                <CardContent />
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
