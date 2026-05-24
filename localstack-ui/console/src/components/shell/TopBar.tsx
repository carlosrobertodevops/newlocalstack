import { useNavigate } from "@tanstack/react-router";
import { useCloud } from "@/lib/cloud-context";
import { useTheme } from "@/lib/theme-context";
import { useI18n, type Lang } from "@/lib/i18n";
import type { CloudName } from "@/lib/skins";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { ServiceIcon } from "@/lib/service-icons";
import { Cloud, Moon, Sun } from "lucide-react";

const CLOUDS: { id: CloudName; label: string }[] = [
  { id: "aws", label: "AWS" },
  { id: "azure", label: "Azure" },
  { id: "gcp", label: "GCP" },
];

const LANGS: { id: Lang; label: string }[] = [
  { id: "en", label: "English" },
  { id: "pt-BR", label: "Português" },
  { id: "es", label: "Español" },
];

export function TopBar() {
  const { cloud, setCloud, region, endpoint } = useCloud();
  const { theme, toggle: toggleTheme } = useTheme();
  const { lang, setLang, t } = useI18n();
  const navigate = useNavigate();

  const handleSwitch = (next: CloudName) => {
    if (next === cloud) return;
    setCloud(next);
    navigate({ to: `/${next}` });
  };

  const currentLang = LANGS.find((l) => l.id === lang) ?? LANGS[0];

  return (
    <header
      className="flex h-12 items-center justify-between px-4 text-white"
      style={{ background: "var(--bg-top)" }}
    >
      <div className="flex items-center gap-3">
        <Cloud className="h-5 w-5" style={{ color: "var(--accent)" }} />
        <span className="font-semibold tracking-tight">{t("app.brand")}</span>
      </div>
      <nav className="flex items-center gap-1">
        {CLOUDS.map((c) => (
          <Button
            key={c.id}
            size="sm"
            variant="ghost"
            onClick={() => handleSwitch(c.id)}
            className={cn(
              "text-white hover:bg-white/10 inline-flex items-center gap-1.5",
              cloud === c.id && "ring-1 ring-white/40 bg-white/10",
            )}
          >
            <ServiceIcon id="cloud" cloud={c.id} style={{ width: 14, height: 14 }} />
            {c.label}
          </Button>
        ))}
      </nav>
      <div className="flex items-center gap-2 text-xs">
        <Select value={lang} onValueChange={(v) => setLang(v as Lang)}>
          <SelectTrigger
            aria-label={t("topbar.language")}
            className="h-7 w-[7.5rem] border-white/30 bg-transparent text-white text-[11px] px-2 py-0 hover:bg-white/10"
          >
            <SelectValue>{currentLang.label}</SelectValue>
          </SelectTrigger>
          <SelectContent>
            {LANGS.map((l) => (
              <SelectItem key={l.id} value={l.id} className="text-xs">
                {l.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
        <Button
          size="sm"
          variant="ghost"
          onClick={toggleTheme}
          aria-label={t("topbar.theme.toggle")}
          title={
            theme === "dark"
              ? t("topbar.theme.light")
              : t("topbar.theme.dark")
          }
          className="text-white hover:bg-white/10 h-7 w-7 p-0"
        >
          {theme === "dark" ? (
            <Sun className="h-4 w-4" />
          ) : (
            <Moon className="h-4 w-4" />
          )}
        </Button>
        <span className="opacity-80">{region}</span>
        <span className="hidden md:inline opacity-80">{endpoint}</span>
      </div>
    </header>
  );
}
