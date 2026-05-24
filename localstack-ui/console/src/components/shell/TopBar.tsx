import { useNavigate } from "@tanstack/react-router";
import { useCloud } from "@/lib/cloud-context";
import { useTheme } from "@/lib/theme-context";
import { useI18n, type Lang } from "@/lib/i18n";
import type { CloudName } from "@/lib/skins";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Cloud, Moon, Sun } from "lucide-react";

const CLOUDS: { id: CloudName; label: string }[] = [
  { id: "aws", label: "AWS" },
  { id: "azure", label: "Azure" },
  { id: "gcp", label: "GCP" },
];

const LANGS: { id: Lang; label: string }[] = [
  { id: "en", label: "EN" },
  { id: "pt-BR", label: "PT-BR" },
  { id: "es", label: "ES" },
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
              "text-white hover:bg-white/10",
              cloud === c.id && "ring-1 ring-white/40 bg-white/10",
            )}
          >
            {c.label}
          </Button>
        ))}
      </nav>
      <div className="flex items-center gap-2 text-xs">
        <div
          className="flex items-center rounded-md ring-1 ring-white/30 overflow-hidden"
          role="group"
          aria-label={t("topbar.language")}
        >
          {LANGS.map((l) => (
            <button
              key={l.id}
              type="button"
              onClick={() => setLang(l.id)}
              className={cn(
                "px-2 py-1 text-[11px] font-medium",
                lang === l.id
                  ? "bg-white/20 text-white"
                  : "text-white/80 hover:bg-white/10",
              )}
            >
              {l.label}
            </button>
          ))}
        </div>
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
