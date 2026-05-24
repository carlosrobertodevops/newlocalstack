import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { gcpApi } from "@/lib/api/gcp";
import { useCloud } from "@/lib/cloud-context";
import { ResourcePage } from "@/components/resource-page/ResourcePage";
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

function err(e: unknown) {
  toast.error(e instanceof Error ? e.message : String(e));
}

// ---------------- BigQuery ----------------
export function BigQueryList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "bigquery", project],
    queryFn: () => gcpApi.listDatasets(project),
  });
  const [id, setId] = useState("");
  const create = useMutation({
    mutationFn: () => gcpApi.createDataset(project, id),
    onSuccess: () => {
      setId("");
      qc.invalidateQueries({ queryKey: ["gcp", "bigquery"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="BigQuery · Datasets"
      description={`project ${project}`}
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="bq-id">Dataset ID</Label>
            <Input id="bq-id" value={id} onChange={(e) => setId(e.target.value)} />
          </div>
          <Button onClick={() => create.mutate()} disabled={!id}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Dataset</TableHead>
            <TableHead>Location</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((d) => (
            <TableRow key={d.datasetReference.datasetId}>
              <TableCell>{d.datasetReference.datasetId}</TableCell>
              <TableCell>{d.location ?? "—"}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    gcpApi
                      .deleteDataset(project, d.datasetReference.datasetId)
                      .then(() => qc.invalidateQueries({ queryKey: ["gcp", "bigquery"] }))
                      .catch(err)
                  }
                >
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={3} className="text-center text-muted-foreground">
                No datasets.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Cloud Functions ----------------
export function FunctionsList() {
  const { project } = useCloud();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "functions", project],
    queryFn: () => gcpApi.listFunctions(project),
  });
  return (
    <ResourcePage
      title="Cloud Functions"
      description={`project ${project}`}
      onRefresh={refetch}
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>Runtime</TableHead>
            <TableHead>State</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((f) => (
            <TableRow key={f.name}>
              <TableCell className="font-mono text-xs">{f.name}</TableCell>
              <TableCell>{f.buildConfig?.runtime ?? "—"}</TableCell>
              <TableCell>{f.state ?? "—"}</TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={3} className="text-center text-muted-foreground">
                No functions. Deploy via gcloud.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Cloud Run ----------------
export function RunList() {
  const { project } = useCloud();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "run", project],
    queryFn: () => gcpApi.listRunServices(project),
  });
  return (
    <ResourcePage
      title="Cloud Run · Services"
      description={`project ${project}`}
      onRefresh={refetch}
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>URI</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((s) => (
            <TableRow key={s.name}>
              <TableCell className="font-mono text-xs">{s.name}</TableCell>
              <TableCell className="font-mono text-xs">{s.uri ?? "—"}</TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={2} className="text-center text-muted-foreground">
                No services.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Secret Manager ----------------
export function SecretManagerList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "secrets", project],
    queryFn: () => gcpApi.listSecrets(project),
  });
  const [id, setId] = useState("");
  const create = useMutation({
    mutationFn: () => gcpApi.createSecret(project, id),
    onSuccess: () => {
      setId("");
      qc.invalidateQueries({ queryKey: ["gcp", "secrets"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Secret Manager"
      description={`project ${project}`}
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sm-id">Secret ID</Label>
            <Input id="sm-id" value={id} onChange={(e) => setId(e.target.value)} />
          </div>
          <Button onClick={() => create.mutate()} disabled={!id}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((s) => {
            const id = s.name.split("/").pop()!;
            return (
              <TableRow key={s.name}>
                <TableCell>{id}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() =>
                      gcpApi
                        .deleteSecret(project, id)
                        .then(() => qc.invalidateQueries({ queryKey: ["gcp", "secrets"] }))
                        .catch(err)
                    }
                  >
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- IAM Service Accounts ----------------
export function GcpIamList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "iam", project],
    queryFn: () => gcpApi.listServiceAccounts(project),
  });
  const [id, setId] = useState("");
  const create = useMutation({
    mutationFn: () => gcpApi.createServiceAccount(project, id),
    onSuccess: () => {
      setId("");
      qc.invalidateQueries({ queryKey: ["gcp", "iam"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="IAM · Service Accounts"
      description={`project ${project}`}
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sa-id">Account ID</Label>
            <Input id="sa-id" value={id} onChange={(e) => setId(e.target.value)} />
          </div>
          <Button onClick={() => create.mutate()} disabled={!id}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Email</TableHead>
            <TableHead>Display Name</TableHead>
            <TableHead>Unique ID</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((a) => (
            <TableRow key={a.uniqueId ?? a.email}>
              <TableCell className="font-mono text-xs">{a.email}</TableCell>
              <TableCell>{a.displayName ?? "—"}</TableCell>
              <TableCell className="font-mono text-xs">{a.uniqueId ?? "—"}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Firestore ----------------
export function FirestoreList() {
  const { project } = useCloud();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "firestore", project],
    queryFn: () => gcpApi.listFirestoreDatabases(project),
  });
  return (
    <ResourcePage
      title="Firestore · Databases"
      description={`project ${project}`}
      onRefresh={refetch}
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>Type</TableHead>
            <TableHead>Location</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((d) => (
            <TableRow key={d.name}>
              <TableCell className="font-mono text-xs">{d.name}</TableCell>
              <TableCell>{d.type ?? "—"}</TableCell>
              <TableCell>{d.locationId ?? "—"}</TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={3} className="text-center text-muted-foreground">
                No databases.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- KMS ----------------
export function KmsList() {
  const { project } = useCloud();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "kms", project],
    queryFn: () => gcpApi.listKeyRings(project),
  });
  return (
    <ResourcePage
      title="Cloud KMS · Key Rings"
      description={`project ${project} · location global`}
      onRefresh={refetch}
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Key Ring</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((k) => (
            <TableRow key={k.name}>
              <TableCell className="font-mono text-xs">{k.name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- DNS ----------------
export function DnsList() {
  const { project } = useCloud();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "dns", project],
    queryFn: () => gcpApi.listZones(project),
  });
  return (
    <ResourcePage
      title="Cloud DNS · Managed Zones"
      description={`project ${project}`}
      onRefresh={refetch}
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>DNS Name</TableHead>
            <TableHead>Description</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((z) => (
            <TableRow key={z.name}>
              <TableCell>{z.name}</TableCell>
              <TableCell className="font-mono text-xs">{z.dnsName ?? "—"}</TableCell>
              <TableCell>{z.description ?? "—"}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}
