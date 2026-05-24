import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { awsApi } from "@/lib/api/aws";
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

// ---------------- EKS ----------------
export function EksList() {
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["eks"],
    queryFn: awsApi.listEksClusters,
  });
  const [name, setName] = useState("");
  const [subnets, setSubnets] = useState("subnet-12345,subnet-67890");
  const create = useMutation({
    mutationFn: () =>
      awsApi.createEksCluster(
        name,
        subnets.split(",").map((s) => s.trim()).filter(Boolean),
      ),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["eks"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="EKS · Clusters"
      description="Emulated via Moto. Pre-provision subnets in VPC for a realistic flow."
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end flex-wrap">
          <div>
            <Label htmlFor="eks-n">Cluster name</Label>
            <Input id="eks-n" value={name} onChange={(e) => setName(e.target.value)} />
          </div>
          <div>
            <Label htmlFor="eks-s">Subnet IDs (comma-sep)</Label>
            <Input
              id="eks-s"
              value={subnets}
              onChange={(e) => setSubnets(e.target.value)}
              className="w-72"
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name}>
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
          {(data ?? []).map((c) => (
            <TableRow key={c}>
              <TableCell className="font-mono">{c}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteEksCluster(c)
                      .then(() => qc.invalidateQueries({ queryKey: ["eks"] }))
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
              <TableCell colSpan={2} className="text-center text-muted-foreground">
                No clusters.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- ECS ----------------
export function EcsList() {
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["ecs"],
    queryFn: awsApi.listEcsClusters,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createEcsCluster(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["ecs"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="ECS · Clusters"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="ecs-n">Cluster name</Label>
            <Input id="ecs-n" value={name} onChange={(e) => setName(e.target.value)} />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>ARN</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((arn) => {
            const short = arn.split("/").pop() ?? arn;
            return (
              <TableRow key={arn}>
                <TableCell className="font-mono text-xs">{arn}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() =>
                      awsApi
                        .deleteEcsCluster(short)
                        .then(() => qc.invalidateQueries({ queryKey: ["ecs"] }))
                        .catch(err)
                    }
                  >
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            );
          })}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={2} className="text-center text-muted-foreground">
                No clusters.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- RDS ----------------
export function RdsList() {
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["rds"],
    queryFn: awsApi.listDbInstances,
  });
  const [id, setId] = useState("");
  const [engine, setEngine] = useState("postgres");
  const create = useMutation({
    mutationFn: () => awsApi.createDbInstance(id, engine),
    onSuccess: () => {
      setId("");
      qc.invalidateQueries({ queryKey: ["rds"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="RDS · DB Instances"
      description="Master credentials default to admin / Password1!"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="rds-id">Instance ID</Label>
            <Input id="rds-id" value={id} onChange={(e) => setId(e.target.value)} />
          </div>
          <div>
            <Label htmlFor="rds-e">Engine</Label>
            <Input
              id="rds-e"
              value={engine}
              onChange={(e) => setEngine(e.target.value)}
              className="w-32"
            />
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
            <TableHead>ID</TableHead>
            <TableHead>Engine</TableHead>
            <TableHead>Class</TableHead>
            <TableHead>Status</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((db) => (
            <TableRow key={db.DBInstanceIdentifier}>
              <TableCell>{db.DBInstanceIdentifier}</TableCell>
              <TableCell>{db.Engine}</TableCell>
              <TableCell>{db.DBInstanceClass}</TableCell>
              <TableCell>{db.DBInstanceStatus}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteDbInstance(db.DBInstanceIdentifier!)
                      .then(() => qc.invalidateQueries({ queryKey: ["rds"] }))
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
              <TableCell colSpan={5} className="text-center text-muted-foreground">
                No instances.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}
