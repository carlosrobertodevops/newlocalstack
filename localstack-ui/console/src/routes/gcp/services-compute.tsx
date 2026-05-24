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

function err(e: unknown) {
  toast.error(e instanceof Error ? e.message : String(e));
}

// ---------------- VPC Networks ----------------
export function VpcNetworksList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "networks", project],
    queryFn: () => gcpApi.listNetworks(project),
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => gcpApi.createNetwork(project, name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["gcp", "networks"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="GCP · VPC Networks"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="vpc-n">Name</Label>
            <Input
              id="vpc-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
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
            <TableHead>Auto subnets</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((n) => (
            <TableRow key={n.name}>
              <TableCell className="font-mono">{n.name}</TableCell>
              <TableCell>{n.autoCreateSubnetworks ? "yes" : "no"}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    gcpApi
                      .deleteNetwork(project, n.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["gcp", "networks"] }),
                      )
                      .catch(err)
                  }
                >
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Compute Engine Instances ----------------
export function ComputeList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const [zone, setZone] = useState("us-central1-a");
  const [name, setName] = useState("");
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "instances", project, zone],
    queryFn: () => gcpApi.listInstances(project, zone),
  });
  const create = useMutation({
    mutationFn: () => gcpApi.createInstance(project, zone, name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["gcp", "instances"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="GCP · Compute Engine"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="ce-z">Zone</Label>
            <Input
              id="ce-z"
              value={zone}
              onChange={(e) => setZone(e.target.value)}
              className="w-36"
            />
          </div>
          <div>
            <Label htmlFor="ce-n">Name</Label>
            <Input
              id="ce-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name || !zone}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Type</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((i) => (
            <TableRow key={i.name}>
              <TableCell className="font-mono">{i.name}</TableCell>
              <TableCell>{i.status}</TableCell>
              <TableCell className="font-mono text-xs">
                {i.machineType?.split("/").pop()}
              </TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    gcpApi
                      .deleteInstance(project, zone, i.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["gcp", "instances"] }),
                      )
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
              <TableCell colSpan={4} className="text-center text-muted-foreground">
                No instances in {zone}.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Cloud SQL ----------------
export function SqlList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const [name, setName] = useState("");
  const [region, setRegion] = useState("us-central1");
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "sql", project],
    queryFn: () => gcpApi.listSqlInstances(project),
  });
  const create = useMutation({
    mutationFn: () => gcpApi.createSqlInstance(project, name, region),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["gcp", "sql"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="GCP · Cloud SQL"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sql-n">Name</Label>
            <Input
              id="sql-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div>
            <Label htmlFor="sql-r">Region</Label>
            <Input
              id="sql-r"
              value={region}
              onChange={(e) => setRegion(e.target.value)}
              className="w-32"
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
            <TableHead>Version</TableHead>
            <TableHead>Region</TableHead>
            <TableHead>State</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((i) => (
            <TableRow key={i.name}>
              <TableCell className="font-mono">{i.name}</TableCell>
              <TableCell>{i.databaseVersion}</TableCell>
              <TableCell>{i.region}</TableCell>
              <TableCell>{i.state}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    gcpApi
                      .deleteSqlInstance(project, i.name)
                      .then(() =>
                        qc.invalidateQueries({ queryKey: ["gcp", "sql"] }),
                      )
                      .catch(err)
                  }
                >
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Spanner ----------------
export function SpannerList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const [name, setName] = useState("");
  const [display, setDisplay] = useState("");
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "spanner", project],
    queryFn: () => gcpApi.listSpannerInstances(project),
  });
  const create = useMutation({
    mutationFn: () =>
      gcpApi.createSpannerInstance(project, name, display || name),
    onSuccess: () => {
      setName("");
      setDisplay("");
      qc.invalidateQueries({ queryKey: ["gcp", "spanner"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="GCP · Spanner Instances"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sp-id">Instance ID</Label>
            <Input
              id="sp-id"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div>
            <Label htmlFor="sp-d">Display name</Label>
            <Input
              id="sp-d"
              value={display}
              onChange={(e) => setDisplay(e.target.value)}
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
            <TableHead>Display</TableHead>
            <TableHead>State</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((i) => {
            const id = i.name.split("/").pop()!;
            return (
              <TableRow key={i.name}>
                <TableCell className="font-mono text-xs">{i.name}</TableCell>
                <TableCell>{i.displayName}</TableCell>
                <TableCell>{i.state}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() =>
                      gcpApi
                        .deleteSpannerInstance(project, id)
                        .then(() =>
                          qc.invalidateQueries({ queryKey: ["gcp", "spanner"] }),
                        )
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

// ---------------- Monitoring ----------------
export function MonitoringList() {
  const { project } = useCloud();
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "monitoring", project],
    queryFn: () => gcpApi.listMonitoringMetrics(project),
  });
  return (
    <ResourcePage title="GCP · Monitoring · Metric Descriptors" onRefresh={refetch}>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Type</TableHead>
            <TableHead>Kind</TableHead>
            <TableHead>Name</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).slice(0, 200).map((m) => (
            <TableRow key={m.name}>
              <TableCell className="font-mono text-xs">{m.type}</TableCell>
              <TableCell>{m.metricKind}</TableCell>
              <TableCell className="font-mono text-[10px]">{m.name}</TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={3} className="text-center text-muted-foreground">
                No metrics.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- GKE ----------------
export function GkeList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const [location, setLocation] = useState("us-central1");
  const [name, setName] = useState("");
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "gke", project, location],
    queryFn: () => gcpApi.listGkeClusters(project, location),
  });
  const create = useMutation({
    mutationFn: () => gcpApi.createGkeCluster(project, location, name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["gcp", "gke"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="GCP · GKE Clusters"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="gke-l">Location</Label>
            <Input
              id="gke-l"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className="w-32"
            />
          </div>
          <div>
            <Label htmlFor="gke-n">Cluster name</Label>
            <Input
              id="gke-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
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
            <TableHead>Location</TableHead>
            <TableHead>Status</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((c) => (
            <TableRow key={c.name}>
              <TableCell className="font-mono">{c.name}</TableCell>
              <TableCell>{c.location}</TableCell>
              <TableCell>{c.status}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    gcpApi
                      .deleteGkeCluster(project, location, c.name)
                      .then(() => qc.invalidateQueries({ queryKey: ["gcp", "gke"] }))
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
              <TableCell colSpan={4} className="text-center text-muted-foreground">
                No clusters in {location}.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- Cloud Scheduler ----------------
export function SchedulerList() {
  const { project } = useCloud();
  const qc = useQueryClient();
  const [location, setLocation] = useState("us-central1");
  const [jobId, setJobId] = useState("");
  const [schedule, setSchedule] = useState("*/5 * * * *");
  const [url, setUrl] = useState("https://example.com/ping");
  const { data, refetch } = useQuery({
    queryKey: ["gcp", "scheduler", project, location],
    queryFn: () => gcpApi.listSchedulerJobs(project, location),
  });
  const create = useMutation({
    mutationFn: () =>
      gcpApi.createSchedulerJob(project, location, jobId, schedule, url),
    onSuccess: () => {
      setJobId("");
      qc.invalidateQueries({ queryKey: ["gcp", "scheduler"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="GCP · Cloud Scheduler"
      onRefresh={refetch}
      actions={
        <div className="flex flex-wrap gap-2 items-end">
          <div>
            <Label htmlFor="sch-l">Location</Label>
            <Input
              id="sch-l"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className="w-32"
            />
          </div>
          <div>
            <Label htmlFor="sch-id">Job ID</Label>
            <Input
              id="sch-id"
              value={jobId}
              onChange={(e) => setJobId(e.target.value)}
            />
          </div>
          <div>
            <Label htmlFor="sch-s">Schedule</Label>
            <Input
              id="sch-s"
              value={schedule}
              onChange={(e) => setSchedule(e.target.value)}
              className="w-32"
            />
          </div>
          <div>
            <Label htmlFor="sch-u">Target URL</Label>
            <Input
              id="sch-u"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!jobId}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>Schedule</TableHead>
            <TableHead>State</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((j) => {
            const id = j.name.split("/").pop()!;
            return (
              <TableRow key={j.name}>
                <TableCell className="font-mono text-xs">{j.name}</TableCell>
                <TableCell className="font-mono">{j.schedule}</TableCell>
                <TableCell>{j.state}</TableCell>
                <TableCell>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() =>
                      gcpApi
                        .deleteSchedulerJob(project, location, id)
                        .then(() =>
                          qc.invalidateQueries({ queryKey: ["gcp", "scheduler"] }),
                        )
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
