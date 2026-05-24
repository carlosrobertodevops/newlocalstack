import { ResourcePage } from "@/components/resource-page/ResourcePage";
import { Badge } from "@/components/ui/badge";
import { ServiceIcon } from "@/lib/service-icons";
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
  return (
    <ResourcePage
      title={label}
      description={description ?? `${label} (preview) — backend wiring in progress.`}
    >
      <div className="flex flex-col items-center justify-center gap-3 py-10 text-center">
        <ServiceIcon id={id} cloud={cloud} style={{ width: 48, height: 48 }} />
        <div className="text-sm text-muted-foreground">
          UI ready. Provider integration coming soon.
        </div>
        <Badge variant="warn">preview</Badge>
      </div>
    </ResourcePage>
  );
}
