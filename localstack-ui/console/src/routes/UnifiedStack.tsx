import { useNavigate, useSearch } from "@tanstack/react-router";
import type { CloudName } from "@/lib/skins";
import { CloudSelector } from "@/components/CloudSelector";
import { CloudStack } from "@/routes/stack";

const VALID_CLOUDS: CloudName[] = ["aws", "azure", "gcp"];

export function UnifiedStack() {
  const search = useSearch({ strict: false }) as { cloud?: string };
  const navigate = useNavigate();

  const cloud: CloudName = (VALID_CLOUDS as string[]).includes(search.cloud ?? "")
    ? (search.cloud as CloudName)
    : "aws";

  const handleCloudChange = (nextCloud: CloudName) => {
    navigate({ to: "/stack", search: { cloud: nextCloud } });
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">Multi-Cloud Stack</h1>
        <CloudSelector value={cloud} onChange={handleCloudChange} />
      </div>
      <CloudStack cloud={cloud} />
    </div>
  );
}
