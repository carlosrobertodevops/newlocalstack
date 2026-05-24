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
import { gcpApi } from "@/lib/api/gcp";
import { useCloud } from "@/lib/cloud-context";
import { useI18n } from "@/lib/i18n";
import {
  genTerraformGcsBucket,
  genTerraformPubSubTopic,
} from "@/lib/iac/generators";

export function StorageList() {
  const { project } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [name, setName] = useState("");

  const { data, isLoading, refetch } = useQuery({
    queryKey: ["gcp", "buckets", project],
    queryFn: () => gcpApi.listBuckets(project),
  });
  const create = useMutation({
    mutationFn: () => gcpApi.createBucket(project, name),
    onSuccess: () => {
      toast.success("bucket created");
      setName("");
      qc.invalidateQueries({ queryKey: ["gcp", "buckets"] });
    },
    onError: (e: Error) => toast.error(e.message),
  });
  const del = useMutation({
    mutationFn: (n: string) => gcpApi.deleteBucket(n),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["gcp", "buckets"] }),
  });

  return (
    <ResourcePage
      title="GCP · Cloud Storage"
      description={`project ${project}`}
      onRefresh={() => refetch()}
      iac={{
        tool: "terraform",
        snippet: genTerraformGcsBucket(name || "my-bucket", project),
      }}
      actions={
        <div className="flex items-end gap-2">
          <div>
            <Label className="text-xs">{t("col.bucket")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="h-8 w-48"
              placeholder="my-bucket"
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
      {isLoading ? (
        <div className="p-3 text-sm text-muted-foreground">{t("sidebar.loading")}</div>
      ) : !data || data.length === 0 ? (
        <div className="p-3 text-sm text-muted-foreground">{t("common.empty")}</div>
      ) : (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>{t("col.name")}</TableHead>
              <TableHead>{t("col.location")}</TableHead>
              <TableHead>{t("col.class")}</TableHead>
              <TableHead className="w-20" />
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((b) => (
              <TableRow key={b.name}>
                <TableCell className="font-mono">{b.name}</TableCell>
                <TableCell>{b.location ?? "—"}</TableCell>
                <TableCell>{b.storageClass ?? "—"}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => del.mutate(b.name)}
                  >
                    {t("common.delete")}
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      )}
    </ResourcePage>
  );
}

export function PubSubList() {
  const { project } = useCloud();
  const { t } = useI18n();
  const qc = useQueryClient();
  const [name, setName] = useState("");

  const { data, isLoading, refetch } = useQuery({
    queryKey: ["gcp", "topics", project],
    queryFn: () => gcpApi.listTopics(project),
  });
  const create = useMutation({
    mutationFn: () => gcpApi.createTopic(project, name),
    onSuccess: () => {
      toast.success("topic created");
      setName("");
      qc.invalidateQueries({ queryKey: ["gcp", "topics"] });
    },
    onError: (e: Error) => toast.error(e.message),
  });
  const del = useMutation({
    mutationFn: (n: string) => gcpApi.deleteTopic(project, n),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["gcp", "topics"] }),
  });

  return (
    <ResourcePage
      title="GCP · Pub/Sub Topics"
      description={`project ${project}`}
      onRefresh={() => refetch()}
      iac={{
        tool: "terraform",
        snippet: genTerraformPubSubTopic(name || "my-topic", project),
      }}
      actions={
        <div className="flex items-end gap-2">
          <div>
            <Label className="text-xs">{t("col.topic")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="h-8 w-48"
              placeholder="my-topic"
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
      {isLoading ? (
        <div className="p-3 text-sm text-muted-foreground">{t("sidebar.loading")}</div>
      ) : !data || data.length === 0 ? (
        <div className="p-3 text-sm text-muted-foreground">{t("common.empty")}</div>
      ) : (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>{t("col.name")}</TableHead>
              <TableHead className="w-20" />
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((tp) => {
              const short = tp.name.split("/").pop() ?? tp.name;
              return (
                <TableRow key={tp.name}>
                  <TableCell className="font-mono">{tp.name}</TableCell>
                  <TableCell>
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() => del.mutate(short)}
                    >
                      {t("common.delete")}
                    </Button>
                  </TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      )}
    </ResourcePage>
  );
}
