import { ResourcePage } from "@/components/resource-page/ResourcePage";
import { Badge } from "@/components/ui/badge";
import { ServiceIcon } from "@/lib/service-icons";
import { useI18n } from "@/lib/i18n";
import type { CloudName } from "@/lib/skins";

export function ProService({
  cloud,
  id,
  label,
  reason,
}: {
  cloud: CloudName;
  id: string;
  label: string;
  reason?: string;
}) {
  const { t } = useI18n();
  return (
    <ResourcePage
      title={label}
      description={reason ?? t("pro.description")}
    >
      <div className="flex flex-col items-center justify-center gap-3 py-10 text-center">
        <ServiceIcon id={id} cloud={cloud} style={{ width: 48, height: 48 }} />
        <div className="text-sm text-muted-foreground max-w-md">
          {reason ?? t("pro.reason")}
        </div>
        <Badge variant="warn">{t("state.not_yet_available")}</Badge>
      </div>
    </ResourcePage>
  );
}
