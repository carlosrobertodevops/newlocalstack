import { ResourcePage } from "@/components/resource-page/ResourcePage";
import { Badge } from "@/components/ui/badge";
import { ServiceIcon } from "@/lib/service-icons";
import { useI18n } from "@/lib/i18n";
import type { CloudName } from "@/lib/skins";

export function PreviewService({
  cloud,
  id,
  label,
  description,
}: {
  cloud: CloudName;
  id: string;
  label: string;
  description?: string;
}) {
  const { t } = useI18n();
  return (
    <ResourcePage
      title={label}
      description={description ?? t("preview.description", { service: label })}
    >
      <div className="flex flex-col items-center justify-center gap-3 py-10 text-center">
        <ServiceIcon id={id} cloud={cloud} style={{ width: 48, height: 48 }} />
        <div className="text-sm text-muted-foreground">
          {t("preview.ui_ready")}
        </div>
        <Badge variant="warn">{t("badge.preview")}</Badge>
      </div>
    </ResourcePage>
  );
}
