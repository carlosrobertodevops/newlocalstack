/**
 * Cloud-specific visual tokens — see docs/multi-cloud-console-plan.md §6.
 *
 * `applySkin(name)` sets CSS variables on the document root. The tokens are
 * read by Tailwind via `tailwind.config.ts` (skin-bg-top / skin-accent /
 * skin-sidebar / font-skin / shadow-skin).
 */

export type CloudName = "aws" | "azure" | "gcp";

export interface SkinTokens {
  bgTop: string;
  accent: string;
  sidebar: string;
  sidebarText: string;
  sidebarHover: string;
  sidebarMuted: string;
  fontFamily: string;
  shadow: string;
  textOnBg: string;
}

export const SKINS: Record<CloudName, SkinTokens> = {
  aws: {
    bgTop: "#232f3e",
    accent: "#ff9900",
    sidebar: "#1b2330",
    sidebarText: "#ffffff",
    sidebarHover: "rgba(255,255,255,0.08)",
    sidebarMuted: "rgba(255,255,255,0.6)",
    fontFamily: "'Amazon Ember', 'Inter', system-ui, sans-serif",
    shadow: "none",
    textOnBg: "#ffffff",
  },
  azure: {
    bgTop: "#0078d4",
    accent: "#50e6ff",
    sidebar: "#f3f2f1",
    sidebarText: "#201f1e",
    sidebarHover: "rgba(0,0,0,0.06)",
    sidebarMuted: "#605e5c",
    fontFamily: "'Segoe UI', system-ui, sans-serif",
    shadow: "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)",
    textOnBg: "#ffffff",
  },
  gcp: {
    bgTop: "#1a73e8",
    accent: "#34a853",
    sidebar: "#202124",
    sidebarText: "#ffffff",
    sidebarHover: "rgba(255,255,255,0.08)",
    sidebarMuted: "rgba(255,255,255,0.6)",
    fontFamily: "'Google Sans', 'Roboto', system-ui, sans-serif",
    shadow: "0 1px 2px 0 rgba(60,64,67,0.302), 0 1px 3px 1px rgba(60,64,67,0.149)",
    textOnBg: "#ffffff",
  },
};

export function applySkin(name: CloudName, root: HTMLElement = document.documentElement) {
  const skin = SKINS[name];
  root.style.setProperty("--bg-top", skin.bgTop);
  root.style.setProperty("--accent", skin.accent);
  root.style.setProperty("--sidebar", skin.sidebar);
  root.style.setProperty("--sidebar-text", skin.sidebarText);
  root.style.setProperty("--sidebar-hover", skin.sidebarHover);
  root.style.setProperty("--sidebar-muted", skin.sidebarMuted);
  root.style.setProperty("--font-family", skin.fontFamily);
  root.style.setProperty("--shadow", skin.shadow);
  root.style.setProperty("--text-on-bg", skin.textOnBg);
  root.dataset.cloud = name;
}
