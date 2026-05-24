import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useParams } from "@tanstack/react-router";
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
import { awsApi } from "@/lib/api/aws";
import { useI18n } from "@/lib/i18n";
import {
  genTerraformDynamoTable,
  genTerraformLambdaFunction,
  genTerraformS3Bucket,
  genTerraformSqsQueue,
} from "@/lib/iac/generators";

// ============================================================================
// S3
// ============================================================================
export function S3List() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const [name, setName] = useState("");
  const { data, isLoading, refetch } = useQuery({
    queryKey: ["aws", "s3", "buckets"],
    queryFn: awsApi.listBuckets,
  });
  const create = useMutation({
    mutationFn: (n: string) => awsApi.createBucket(n),
    onSuccess: () => {
      toast.success("bucket created");
      setName("");
      qc.invalidateQueries({ queryKey: ["aws", "s3", "buckets"] });
    },
    onError: (e: Error) => toast.error(e.message),
  });
  const del = useMutation({
    mutationFn: (n: string) => awsApi.deleteBucket(n),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["aws", "s3", "buckets"] }),
  });

  return (
    <ResourcePage
      title="S3 · Buckets"
      onRefresh={() => refetch()}
      iac={{
        tool: "terraform",
        snippet: genTerraformS3Bucket(name || "my-bucket"),
        title: "S3 Bucket — Terraform",
      }}
      actions={
        <div className="flex items-end gap-2">
          <div>
            <Label className="text-xs">{t("col.bucket_name")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="my-bucket"
              className="h-8 w-56"
            />
          </div>
          <Button
            size="sm"
            variant="skin"
            disabled={!name || create.isPending}
            onClick={() => create.mutate(name)}
          >
            {t("common.create")}
          </Button>
        </div>
      }
    >
      {isLoading ? (
        <div className="text-sm text-muted-foreground p-3">{t("sidebar.loading")}</div>
      ) : !data || data.length === 0 ? (
        <div className="text-sm text-muted-foreground p-3">{t("common.empty")}</div>
      ) : (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>{t("col.name")}</TableHead>
              <TableHead>{t("col.created")}</TableHead>
              <TableHead className="w-20" />
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((b) => (
              <TableRow key={b.Name}>
                <TableCell className="font-mono">{b.Name}</TableCell>
                <TableCell>
                  {b.CreationDate?.toISOString?.() ?? "—"}
                </TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => del.mutate(b.Name!)}
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

// ============================================================================
// SQS
// ============================================================================
export function SqsList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const [name, setName] = useState("");
  const { data, isLoading, refetch } = useQuery({
    queryKey: ["aws", "sqs", "queues"],
    queryFn: awsApi.listQueues,
  });
  const create = useMutation({
    mutationFn: (n: string) => awsApi.createQueue(n),
    onSuccess: () => {
      toast.success("queue created");
      setName("");
      qc.invalidateQueries({ queryKey: ["aws", "sqs", "queues"] });
    },
    onError: (e: Error) => toast.error(e.message),
  });
  const del = useMutation({
    mutationFn: (url: string) => awsApi.deleteQueue(url),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["aws", "sqs", "queues"] }),
  });

  return (
    <ResourcePage
      title="SQS · Queues"
      onRefresh={() => refetch()}
      iac={{
        tool: "terraform",
        snippet: genTerraformSqsQueue(name || "my-queue"),
      }}
      actions={
        <div className="flex items-end gap-2">
          <div>
            <Label className="text-xs">{t("col.queue_name")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="my-queue"
              className="h-8 w-56"
            />
          </div>
          <Button
            size="sm"
            variant="skin"
            disabled={!name || create.isPending}
            onClick={() => create.mutate(name)}
          >
            {t("common.create")}
          </Button>
        </div>
      }
    >
      {isLoading ? (
        <div className="text-sm text-muted-foreground p-3">{t("sidebar.loading")}</div>
      ) : !data || data.length === 0 ? (
        <div className="text-sm text-muted-foreground p-3">{t("common.empty")}</div>
      ) : (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>{t("col.url")}</TableHead>
              <TableHead className="w-32" />
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((url) => (
              <TableRow key={url}>
                <TableCell className="font-mono text-xs">{url}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => del.mutate(url)}
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

// ============================================================================
// DynamoDB
// ============================================================================
export function DynamoList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const [name, setName] = useState("");
  const [pk, setPk] = useState("id");
  const { data, isLoading, refetch } = useQuery({
    queryKey: ["aws", "dynamo", "tables"],
    queryFn: awsApi.listTables,
  });
  const create = useMutation({
    mutationFn: () => awsApi.createTable(name, pk),
    onSuccess: () => {
      toast.success("table created");
      setName("");
      qc.invalidateQueries({ queryKey: ["aws", "dynamo", "tables"] });
    },
    onError: (e: Error) => toast.error(e.message),
  });
  const del = useMutation({
    mutationFn: (n: string) => awsApi.deleteTable(n),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["aws", "dynamo", "tables"] }),
  });

  return (
    <ResourcePage
      title="DynamoDB · Tables"
      onRefresh={() => refetch()}
      iac={{
        tool: "terraform",
        snippet: genTerraformDynamoTable(name || "my-table", pk || "id"),
      }}
      actions={
        <div className="flex items-end gap-2">
          <div>
            <Label className="text-xs">{t("col.table")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="h-8 w-40"
              placeholder="my-table"
            />
          </div>
          <div>
            <Label className="text-xs">{t("col.partition_key")}</Label>
            <Input
              value={pk}
              onChange={(e) => setPk(e.target.value)}
              className="h-8 w-32"
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
        <div className="text-sm text-muted-foreground p-3">{t("sidebar.loading")}</div>
      ) : !data || data.length === 0 ? (
        <div className="text-sm text-muted-foreground p-3">{t("common.empty")}</div>
      ) : (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>{t("col.table")}</TableHead>
              <TableHead className="w-20" />
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((tbl) => (
              <TableRow key={tbl}>
                <TableCell className="font-mono">{tbl}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => del.mutate(tbl)}
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

// ============================================================================
// Lambda
// ============================================================================
const EMPTY_ZIP_BASE64 =
  "UEsDBBQAAAAIACiHQUkAAAAAAgAAAAAAAAAFAAAAaW5kZXjLLs1JzAEAAA==";
const NOOP_HANDLER = "index.handler";

export function LambdaList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const [name, setName] = useState("");
  const [runtime, setRuntime] = useState("nodejs20.x");
  const { data, isLoading, refetch } = useQuery({
    queryKey: ["aws", "lambda", "functions"],
    queryFn: awsApi.listFunctions,
  });
  const create = useMutation({
    mutationFn: () =>
      awsApi.createFunction(name, runtime, NOOP_HANDLER, EMPTY_ZIP_BASE64),
    onSuccess: () => {
      toast.success("function created");
      setName("");
      qc.invalidateQueries({ queryKey: ["aws", "lambda", "functions"] });
    },
    onError: (e: Error) => toast.error(e.message),
  });
  const del = useMutation({
    mutationFn: (n: string) => awsApi.deleteFunction(n),
    onSuccess: () =>
      qc.invalidateQueries({ queryKey: ["aws", "lambda", "functions"] }),
  });

  return (
    <ResourcePage
      title="Lambda · Functions"
      onRefresh={() => refetch()}
      iac={{
        tool: "terraform",
        snippet: genTerraformLambdaFunction(
          name || "my-fn",
          runtime,
          NOOP_HANDLER,
        ),
      }}
      actions={
        <div className="flex items-end gap-2">
          <div>
            <Label className="text-xs">{t("col.function")}</Label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="h-8 w-40"
              placeholder="my-fn"
            />
          </div>
          <div>
            <Label className="text-xs">{t("col.runtime")}</Label>
            <Input
              value={runtime}
              onChange={(e) => setRuntime(e.target.value)}
              className="h-8 w-32"
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
        <div className="text-sm text-muted-foreground p-3">{t("sidebar.loading")}</div>
      ) : !data || data.length === 0 ? (
        <div className="text-sm text-muted-foreground p-3">{t("common.empty")}</div>
      ) : (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>{t("col.function")}</TableHead>
              <TableHead>{t("col.runtime")}</TableHead>
              <TableHead className="w-20" />
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((f) => (
              <TableRow key={f.FunctionName}>
                <TableCell className="font-mono">{f.FunctionName}</TableCell>
                <TableCell>{f.Runtime}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => del.mutate(f.FunctionName!)}
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

// ============================================================================
// Detail views (stub) — show resource name + IaC button
// ============================================================================
export function GenericDetail({
  service,
  paramKey,
}: {
  service: string;
  paramKey: "bucket" | "queue" | "table" | "fn";
}) {
  const params = useParams({ strict: false });
  const id = (params as Record<string, string>)[paramKey];
  return (
    <ResourcePage
      title={`${service} · ${id}`}
      iac={{
        tool: "terraform",
        snippet: `# detail view for ${id}`,
        title: `${service} ${id} — Terraform`,
      }}
    >
      <pre className="text-xs">{JSON.stringify({ service, id }, null, 2)}</pre>
    </ResourcePage>
  );
}
