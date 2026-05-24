import { useRouterState, Link } from "@tanstack/react-router";
import { ChevronRight } from "lucide-react";
import { useI18n } from "@/lib/i18n";

export function Breadcrumbs() {
  const { t } = useI18n();
  const { location } = useRouterState();
  const segments = location.pathname.split("/").filter(Boolean);
  let accum = "";
  return (
    <nav className="flex items-center gap-1 px-4 py-2 text-xs text-muted-foreground">
      <Link to="/" className="hover:text-foreground">
        {t("breadcrumbs.home")}
      </Link>
      {segments.map((seg) => {
        accum += "/" + seg;
        return (
          <span key={accum} className="flex items-center gap-1">
            <ChevronRight className="h-3 w-3" />
            <Link to={accum} className="hover:text-foreground">
              {seg}
            </Link>
          </span>
        );
      })}
    </nav>
  );
}
