import type { CloudName } from "@/lib/skins";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const CLOUDS: { id: CloudName; label: string; color: string }[] = [
  { id: "aws", label: "AWS", color: "#ff9900" },
  { id: "azure", label: "Azure", color: "#0078d4" },
  { id: "gcp", label: "GCP", color: "#1a73e8" },
];

interface CloudSelectorProps {
  value: CloudName;
  onChange: (cloud: CloudName) => void;
}

export function CloudSelector({ value, onChange }: CloudSelectorProps) {
  return (
    <Select value={value} onValueChange={(v) => onChange(v as CloudName)}>
      <SelectTrigger className="w-40">
        <SelectValue />
      </SelectTrigger>
      <SelectContent>
        {CLOUDS.map((c) => (
          <SelectItem key={c.id} value={c.id}>
            <span className="inline-flex items-center gap-2">
              <span className="size-2 rounded-full" style={{ backgroundColor: c.color }} />
              {c.label}
            </span>
          </SelectItem>
        ))}
      </SelectContent>
    </Select>
  );
}
