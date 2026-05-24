import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { ResourcePage } from "@/components/resource-page/ResourcePage";
import { azureApi } from "@/lib/api/azure";
import { useCloud } from "@/lib/cloud-context";
import { useI18n } from "@/lib/i18n";

function err(e: unknown) {
  toast.error(e instanceof Error ? e.message : String(e));
}

interface CreateFields {
  name: string;
  rg: string;
  location: string;
}

function useCreateFields(): [
  CreateFields,
  (next: Partial<CreateFields>) => void,
  () => void,
] {
  const [f, setF] = useState<CreateFields>({
    name: "",
    rg: "default",
    location: "eastus",
  });
  return [
    f,
    (next) => setF((prev) => ({ ...prev, ...next })),
    () => setF({ name: "", rg: "default", location: "eastus" }),
  ];
}

function ActionsBar({
  fields,
  set,
  onCreate,
  disabled,
}: {
  fields: CreateFields;
  set: (n: Partial<CreateFields>) => void;
  onCreate: () => void;
  disabled?: boolean;
}) {
  const { t } = useI18n();
  return (
    <div className="flex items-end gap-2 flex-wrap">
      <div>
        <Label className="text-xs">{t("col.name")}</Label>
        <Input
          value={fields.name}
          onChange={(e) => set({ name: e.target.value })}
          className="h-8 w-40"
        />
      </div>
      <div>
        <Label className="text-xs">{t("col.resource_group")}</Label>
        <Input
          value={fields.rg}
          onChange={(e) => set({ rg: e.target.value })}
          className="h-8 w-32"
        />
      </div>
      <div>
        <Label className="text-xs">{t("col.location")}</Label>
        <Input
          value={fields.location}
          onChange={(e) => set({ location: e.target.value })}
          className="h-8 w-28"
        />
      </div>
      <Button
        size="sm"
        variant="skin"
        disabled={!fields.name || disabled}
        onClick={onCreate}
      >
        {t("common.create")}
      </Button>
    </div>
  );
}

// ---------------- Virtual Network ----------------
export function VnetList() {
  const { subscription } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [f, set, reset] = useCreateFields();
  const { data, refetch } = useQuery({
    queryKey: ["azure", "vnet", subscription],
    queryFn: () => azureApi.listVirtualNetworks(subscription),
  });
  const create = useMutation({
    mutationFn: () =>
      azureApi.createVirtualNetwork(subscription, f.rg, f.name, f.location),
    onSuccess: () => {
      reset();
      qc.invalidateQueries({ queryKey: ["azure", "vnet"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Azure · Virtual Networks"
      onRefresh={() => refetch()}
      actions={
        <ActionsBar
          fields={f}
          set={set}
          onCreate={() => create.mutate()}
          disabled={create.isPending}
        />
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.location")}</TableHead>
            <TableHead>{t("col.cidr")}</TableHead>
            <TableHead className="w-20" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((v) => (
            <TableRow key={v.id}>
              <TableCell className="font-mono">{v.name}</TableCell>
              <TableCell>{v.location}</TableCell>
              <TableCell className="font-mono text-xs">
                {v.properties?.addressSpace?.addressPrefixes?.join(", ") ?? "—"}
              </TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    azureApi
                      .deleteVirtualNetwork(subscription, f.rg, v.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["azure", "vnet"] }),
                      )
                      .catch(err)
                  }
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={4} className="text-center text-muted-foreground">
                {t("common.empty")}
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- App Service ----------------
export function AppServiceList() {
  const { subscription } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [f, set, reset] = useCreateFields();
  const { data, refetch } = useQuery({
    queryKey: ["azure", "appservice", subscription],
    queryFn: () => azureApi.listAppServices(subscription),
  });
  const create = useMutation({
    mutationFn: () =>
      azureApi.createAppService(subscription, f.rg, f.name, f.location),
    onSuccess: () => {
      reset();
      qc.invalidateQueries({ queryKey: ["azure", "appservice"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Azure · App Services"
      onRefresh={() => refetch()}
      actions={
        <ActionsBar
          fields={f}
          set={set}
          onCreate={() => create.mutate()}
          disabled={create.isPending}
        />
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.location")}</TableHead>
            <TableHead>{t("col.kind")}</TableHead>
            <TableHead className="w-20" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((a) => (
            <TableRow key={a.id}>
              <TableCell className="font-mono">{a.name}</TableCell>
              <TableCell>{a.location}</TableCell>
              <TableCell>{a.kind ?? "—"}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    azureApi
                      .deleteAppService(subscription, f.rg, a.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["azure", "appservice"] }),
                      )
                      .catch(err)
                  }
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={4} className="text-center text-muted-foreground">
                {t("common.empty")}
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Container Registry ----------------
export function ContainerRegistryList() {
  const { subscription } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [f, set, reset] = useCreateFields();
  const { data, refetch } = useQuery({
    queryKey: ["azure", "acr", subscription],
    queryFn: () => azureApi.listContainerRegistries(subscription),
  });
  const create = useMutation({
    mutationFn: () =>
      azureApi.createContainerRegistry(subscription, f.rg, f.name, f.location),
    onSuccess: () => {
      reset();
      qc.invalidateQueries({ queryKey: ["azure", "acr"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Azure · Container Registries"
      onRefresh={() => refetch()}
      actions={
        <ActionsBar
          fields={f}
          set={set}
          onCreate={() => create.mutate()}
          disabled={create.isPending}
        />
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.location")}</TableHead>
            <TableHead>{t("col.sku")}</TableHead>
            <TableHead className="w-20" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((r) => (
            <TableRow key={r.id}>
              <TableCell className="font-mono">{r.name}</TableCell>
              <TableCell>{r.location}</TableCell>
              <TableCell>{r.sku?.name ?? "—"}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    azureApi
                      .deleteContainerRegistry(subscription, f.rg, r.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["azure", "acr"] }),
                      )
                      .catch(err)
                  }
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Log Analytics (Monitor) ----------------
export function MonitorList() {
  const { subscription } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [f, set, reset] = useCreateFields();
  const { data, refetch } = useQuery({
    queryKey: ["azure", "monitor", subscription],
    queryFn: () => azureApi.listLogAnalyticsWorkspaces(subscription),
  });
  const create = useMutation({
    mutationFn: () =>
      azureApi.createLogAnalyticsWorkspace(subscription, f.rg, f.name, f.location),
    onSuccess: () => {
      reset();
      qc.invalidateQueries({ queryKey: ["azure", "monitor"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Azure · Log Analytics Workspaces"
      onRefresh={() => refetch()}
      actions={
        <ActionsBar
          fields={f}
          set={set}
          onCreate={() => create.mutate()}
          disabled={create.isPending}
        />
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.location")}</TableHead>
            <TableHead className="w-20" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((w) => (
            <TableRow key={w.id}>
              <TableCell className="font-mono">{w.name}</TableCell>
              <TableCell>{w.location}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    azureApi
                      .deleteLogAnalyticsWorkspace(subscription, f.rg, w.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["azure", "monitor"] }),
                      )
                      .catch(err)
                  }
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Redis Cache ----------------
export function RedisList() {
  const { subscription } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [f, set, reset] = useCreateFields();
  const { data, refetch } = useQuery({
    queryKey: ["azure", "redis", subscription],
    queryFn: () => azureApi.listRedisCaches(subscription),
  });
  const create = useMutation({
    mutationFn: () =>
      azureApi.createRedisCache(subscription, f.rg, f.name, f.location),
    onSuccess: () => {
      reset();
      qc.invalidateQueries({ queryKey: ["azure", "redis"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Azure · Redis Caches"
      onRefresh={() => refetch()}
      actions={
        <ActionsBar
          fields={f}
          set={set}
          onCreate={() => create.mutate()}
          disabled={create.isPending}
        />
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.location")}</TableHead>
            <TableHead>{t("col.sku")}</TableHead>
            <TableHead className="w-20" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((r) => (
            <TableRow key={r.id}>
              <TableCell className="font-mono">{r.name}</TableCell>
              <TableCell>{r.location}</TableCell>
              <TableCell>{r.properties?.sku?.name ?? "—"}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    azureApi
                      .deleteRedisCache(subscription, f.rg, r.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["azure", "redis"] }),
                      )
                      .catch(err)
                  }
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}
