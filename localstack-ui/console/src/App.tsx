import { useEffect } from "react";
import { Outlet, useRouterState } from "@tanstack/react-router";
import { TopBar } from "@/components/shell/TopBar";
import { Sidebar } from "@/components/shell/Sidebar";
import { Breadcrumbs } from "@/components/shell/Breadcrumbs";
import { IacInlineDrawer } from "@/components/iac/IacInlineDrawer";
import { CloudShellButton } from "@/components/cloud-shell/CloudShellDrawer";
import { useCloud } from "@/lib/cloud-context";
import type { CloudName } from "@/lib/skins";

const CLOUDS: ReadonlyArray<CloudName> = ["aws", "azure", "gcp"];

function isCloudName(value: string): value is CloudName {
  return (CLOUDS as ReadonlyArray<string>).includes(value);
}

export function App() {
  const { cloud, setCloud } = useCloud();
  const pathname = useRouterState({ select: (s) => s.location.pathname });

  useEffect(() => {
    const segment = pathname.split("/")[1] ?? "";
    if (isCloudName(segment) && segment !== cloud) {
      setCloud(segment);
    }
  }, [pathname, cloud, setCloud]);

  return (
    <div className="flex flex-col h-screen">
      <TopBar />
      <div className="flex flex-1 min-h-0">
        <Sidebar />
        <main className="flex-1 min-w-0 overflow-y-auto bg-background">
          <Breadcrumbs />
          <Outlet />
        </main>
      </div>
      <IacInlineDrawer />
      <CloudShellButton />
    </div>
  );
}
