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

interface Props {
  title: string;
  ns: string;
  rtype: string;
  apiVersion: string;
  extraBody?: Record<string, unknown>;
}

export function AzureGenericList({
  title,
  ns,
  rtype,
  apiVersion,
  extraBody = {},
}: Props) {
  const { subscription } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const key = ["azure", "generic", ns, rtype, subscription];
  const { data, refetch } = useQuery({
    queryKey: key,
    queryFn: () => azureApi.listGeneric(subscription, ns, rtype, apiVersion),
  });
  const [name, setName] = useState("");
  const [rg, setRg] = useState("default");
  const [location, setLocation] = useState("eastus");
  const create = useMutation({
    mutationFn: () =>
      azureApi.createGeneric(
        subscription,
        rg,
        ns,
        rtype,
        name,
        location,
        apiVersion,
        extraBody,
      ),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["azure", "generic", ns, rtype] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title={title}
      description={`${ns}/${rtype}`}
      onRefresh={() => refetch()}
      actions={
        <div className="flex gap-2 items-end flex-wrap">
          <div>
            <Label className="text-xs">{t("col.name")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="h-8 w-40"
            />
          </div>
          <div>
            <Label className="text-xs">{t("col.resource_group")}</Label>
            <Input
              value={rg}
              onChange={(e) => setRg(e.target.value)}
              className="h-8 w-32"
            />
          </div>
          <div>
            <Label className="text-xs">{t("col.location")}</Label>
            <Input
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className="h-8 w-28"
            />
          </div>
          <Button
            size="sm"
            variant="skin"
            disabled={!name || create.isPending}
            onClick={() => create.mutate()}
          >
            {t("common.create")}
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.location")}</TableHead>
            <TableHead>{t("col.resource_id")}</TableHead>
            <TableHead className="w-20" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((r) => {
            const segs = r.id.split("/");
            const rgFromId = segs[segs.indexOf("resourceGroups") + 1] ?? rg;
            return (
              <TableRow key={r.id}>
                <TableCell className="font-mono">{r.name}</TableCell>
                <TableCell>{r.location ?? "—"}</TableCell>
                <TableCell className="font-mono text-[10px] truncate max-w-[420px]">
                  {r.id}
                </TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() =>
                      azureApi
                        .deleteGeneric(subscription, rgFromId, ns, rtype, r.name, apiVersion)
                        .then(() =>
                          qc.invalidateQueries({
                            queryKey: ["azure", "generic", ns, rtype],
                          }),
                        )
                        .catch(err)
                    }
                  >
                    {t("common.delete")}
                  </Button>
                </TableCell>
              </TableRow>
            );
          })}
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
