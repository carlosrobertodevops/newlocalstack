import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { awsApi } from "@/lib/api/aws";
import { useI18n } from "@/lib/i18n";
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

// ---------------- VPC ----------------
export function VpcList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const vpcs = useQuery({ queryKey: ["vpc", "vpcs"], queryFn: awsApi.listVpcs });
  const subnets = useQuery({
    queryKey: ["vpc", "subnets"],
    queryFn: awsApi.listSubnets,
  });
  const [cidr, setCidr] = useState("10.0.0.0/16");
  const [subCidr, setSubCidr] = useState("10.0.1.0/24");
  const [subVpc, setSubVpc] = useState("");

  const createVpc = useMutation({
    mutationFn: () => awsApi.createVpc(cidr),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["vpc"] }),
    onError: err,
  });
  const removeVpc = useMutation({
    mutationFn: (id: string) => awsApi.deleteVpc(id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["vpc"] }),
    onError: err,
  });
  const createSubnet = useMutation({
    mutationFn: () => awsApi.createSubnet(subVpc, subCidr),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["vpc", "subnets"] }),
    onError: err,
  });
  const removeSubnet = useMutation({
    mutationFn: (id: string) => awsApi.deleteSubnet(id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["vpc", "subnets"] }),
    onError: err,
  });

  return (
    <ResourcePage
      title="VPC · Networks & Subnets"
      onRefresh={() => {
        vpcs.refetch();
        subnets.refetch();
      }}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="vpc-cidr">{t("col.vpc_cidr")}</Label>
            <Input
              id="vpc-cidr"
              value={cidr}
              onChange={(e) => setCidr(e.target.value)}
            />
          </div>
          <Button onClick={() => createVpc.mutate()} disabled={!cidr}>
            {t("common.create_vpc")}
          </Button>
        </div>
      }
    >
      <div className="space-y-6">
        <div>
          <h3 className="text-sm font-semibold mb-2">VPCs</h3>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>{t("col.id")}</TableHead>
                <TableHead>{t("col.cidr")}</TableHead>
                <TableHead>{t("col.state")}</TableHead>
                <TableHead className="w-24" />
              </TableRow>
            </TableHeader>
            <TableBody>
              {(vpcs.data ?? []).map((v) => (
                <TableRow key={v.VpcId}>
                  <TableCell className="font-mono text-xs">{v.VpcId}</TableCell>
                  <TableCell>{v.CidrBlock}</TableCell>
                  <TableCell>{v.State}</TableCell>
                  <TableCell>
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() => removeVpc.mutate(v.VpcId!)}
                    >
                      Delete
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
        <div>
          <h3 className="text-sm font-semibold mb-2">Subnets</h3>
          <div className="flex gap-2 items-end mb-2">
            <div>
              <Label htmlFor="sub-vpc">{t("col.id")}</Label>
              <Input
                id="sub-vpc"
                value={subVpc}
                onChange={(e) => setSubVpc(e.target.value)}
                placeholder="vpc-…"
              />
            </div>
            <div>
              <Label htmlFor="sub-cidr">{t("col.subnet_cidr")}</Label>
              <Input
                id="sub-cidr"
                value={subCidr}
                onChange={(e) => setSubCidr(e.target.value)}
              />
            </div>
            <Button
              onClick={() => createSubnet.mutate()}
              disabled={!subVpc || !subCidr}
            >
              {t("common.create_subnet")}
            </Button>
          </div>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>{t("col.id")}</TableHead>
                <TableHead>VPC</TableHead>
                <TableHead>{t("col.cidr")}</TableHead>
                <TableHead>{t("col.az")}</TableHead>
                <TableHead className="w-24" />
              </TableRow>
            </TableHeader>
            <TableBody>
              {(subnets.data ?? []).map((s) => (
                <TableRow key={s.SubnetId}>
                  <TableCell className="font-mono text-xs">{s.SubnetId}</TableCell>
                  <TableCell className="font-mono text-xs">{s.VpcId}</TableCell>
                  <TableCell>{s.CidrBlock}</TableCell>
                  <TableCell>{s.AvailabilityZone}</TableCell>
                  <TableCell>
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() => removeSubnet.mutate(s.SubnetId!)}
                    >
                      Delete
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </div>
    </ResourcePage>
  );
}

// ---------------- Route 53 ----------------
export function Route53List() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["route53"],
    queryFn: awsApi.listHostedZones,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createHostedZone(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["route53"] });
    },
    onError: err,
  });
  const remove = useMutation({
    mutationFn: (id: string) => awsApi.deleteHostedZone(id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["route53"] }),
    onError: err,
  });
  return (
    <ResourcePage
      title="Route 53 · Hosted Zones"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="r53-n">{t("col.domain_name")}</Label>
            <Input
              id="r53-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="example.com"
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name}>
            {t("common.create")}
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>ID</TableHead>
            <TableHead>{t("col.records")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((z) => (
            <TableRow key={z.Id}>
              <TableCell>{z.Name}</TableCell>
              <TableCell className="font-mono text-xs">{z.Id}</TableCell>
              <TableCell>{z.ResourceRecordSetCount}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() => remove.mutate(z.Id!)}
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

// ---------------- API Gateway ----------------
export function ApiGatewayList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["apigw"],
    queryFn: awsApi.listRestApis,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createRestApi(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["apigw"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="API Gateway · REST APIs"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="api-n">{t("col.api_name")}</Label>
            <Input
              id="api-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name}>
            {t("common.create")}
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.id")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((a) => (
            <TableRow key={a.id}>
              <TableCell>{a.name}</TableCell>
              <TableCell className="font-mono text-xs">{a.id}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteRestApi(a.id!)
                      .then(() => qc.invalidateQueries({ queryKey: ["apigw"] }))
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

// ---------------- Step Functions ----------------
const PASS_DEF = JSON.stringify({
  Comment: "Hello",
  StartAt: "Pass",
  States: { Pass: { Type: "Pass", End: true } },
});

export function StepFunctionsList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["sfn"],
    queryFn: awsApi.listStateMachines,
  });
  const [name, setName] = useState("");
  const [role, setRole] = useState(
    "arn:aws:iam::000000000000:role/sfn-role",
  );
  const create = useMutation({
    mutationFn: () => awsApi.createStateMachine(name, PASS_DEF, role),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["sfn"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Step Functions · State Machines"
      description="Creates a no-op Pass state machine."
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sm-n">{t("col.name")}</Label>
            <Input
              id="sm-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div>
            <Label htmlFor="sm-r">{t("col.role_arn")}</Label>
            <Input
              id="sm-r"
              value={role}
              onChange={(e) => setRole(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name || !role}>
            Create
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.arn")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((s) => (
            <TableRow key={s.stateMachineArn}>
              <TableCell>{s.name}</TableCell>
              <TableCell className="font-mono text-[10px]">
                {s.stateMachineArn}
              </TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteStateMachine(s.stateMachineArn!)
                      .then(() => qc.invalidateQueries({ queryKey: ["sfn"] }))
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

// ---------------- EventBridge ----------------
export function EventBridgeList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["events", "buses"],
    queryFn: awsApi.listEventBuses,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createEventBus(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["events"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="EventBridge · Event Buses"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="eb-n">{t("col.bus_name")}</Label>
            <Input
              id="eb-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name}>
            {t("common.create")}
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.arn")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((b) => (
            <TableRow key={b.Arn}>
              <TableCell>{b.Name}</TableCell>
              <TableCell className="font-mono text-[10px]">{b.Arn}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteEventBus(b.Name!)
                      .then(() => qc.invalidateQueries({ queryKey: ["events"] }))
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

// ---------------- Kinesis ----------------
export function KinesisList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["kinesis"],
    queryFn: awsApi.listKinesisStreams,
  });
  const [name, setName] = useState("");
  const [shards, setShards] = useState("1");
  const create = useMutation({
    mutationFn: () =>
      awsApi.createKinesisStream(name, Number(shards) || 1),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["kinesis"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Kinesis · Streams"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="ks-n">{t("col.name")}</Label>
            <Input
              id="ks-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div>
            <Label htmlFor="ks-s">{t("col.shards")}</Label>
            <Input
              id="ks-s"
              type="number"
              min="1"
              value={shards}
              onChange={(e) => setShards(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name}>
            {t("common.create")}
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
          {(data ?? []).map((s) => (
            <TableRow key={s}>
              <TableCell className="font-mono text-xs">{s}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteKinesisStream(s)
                      .then(() => qc.invalidateQueries({ queryKey: ["kinesis"] }))
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

// ---------------- SSM Parameter Store ----------------
export function SsmList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["ssm"],
    queryFn: awsApi.listSsmParameters,
  });
  const [name, setName] = useState("");
  const [value, setValue] = useState("");
  const [secure, setSecure] = useState(false);
  const create = useMutation({
    mutationFn: () =>
      awsApi.putSsmParameter(name, value, secure ? "SecureString" : "String"),
    onSuccess: () => {
      setName("");
      setValue("");
      qc.invalidateQueries({ queryKey: ["ssm"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="SSM · Parameter Store"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="ssm-n">{t("col.name")}</Label>
            <Input
              id="ssm-n"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="/app/db/url"
            />
          </div>
          <div>
            <Label htmlFor="ssm-v">{t("col.value")}</Label>
            <Input
              id="ssm-v"
              type={secure ? "password" : "text"}
              value={value}
              onChange={(e) => setValue(e.target.value)}
            />
          </div>
          <label className="flex items-center gap-1 text-xs">
            <input
              type="checkbox"
              checked={secure}
              onChange={(e) => setSecure(e.target.checked)}
            />
            secure
          </label>
          <Button onClick={() => create.mutate()} disabled={!name || !value}>
            {t("common.put")}
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.type")}</TableHead>
            <TableHead>Version</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((p) => (
            <TableRow key={p.Name}>
              <TableCell className="font-mono text-xs">{p.Name}</TableCell>
              <TableCell>{p.Type}</TableCell>
              <TableCell>{p.Version}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteSsmParameter(p.Name!)
                      .then(() => qc.invalidateQueries({ queryKey: ["ssm"] }))
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
