import { ResourcePage } from "@/components/resource-page/ResourcePage";
import { Badge } from "@/components/ui/badge";
import { ServiceIcon } from "@/lib/service-icons";
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
  return (
    <ResourcePage
      title={label}
      description={
        reason ??
        "Backend not available in this LocalStack distribution. Requires LocalStack Pro or a future community provider."
      }
    >
      <div className="flex flex-col items-center justify-center gap-3 py-10 text-center">
        <ServiceIcon id={id} cloud={cloud} style={{ width: 48, height: 48 }} />
        <div className="text-sm text-muted-foreground max-w-md">
          {reason ??
            "This service requires a paid provider tier. The UI is wired and ready — once the backend ships, it will work automatically."}
        </div>
        <Badge variant="warn">pro / not yet available</Badge>
      </div>
    </ResourcePage>
  );
}
