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

// ---------------- SNS ----------------
export function SnsList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["sns", "topics"],
    queryFn: awsApi.listTopics,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createTopic(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["sns"] });
    },
    onError: err,
  });
  const remove = useMutation({
    mutationFn: (arn: string) => awsApi.deleteTopic(arn),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["sns"] }),
    onError: err,
  });
  return (
    <ResourcePage
      title="SNS · Topics"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sns-name">{t("col.topic_name")}</Label>
            <Input
              id="sns-name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="my-topic"
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
            <TableHead>{t("col.arn")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((tp) => (
            <TableRow key={tp.TopicArn}>
              <TableCell className="font-mono text-xs">{tp.TopicArn}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() => remove.mutate(tp.TopicArn!)}
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={2} className="text-center text-muted-foreground">
                {t("common.empty")}
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- CloudWatch Logs ----------------
export function LogsList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["logs", "groups"],
    queryFn: awsApi.listLogGroups,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createLogGroup(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["logs"] });
    },
    onError: err,
  });
  const remove = useMutation({
    mutationFn: (n: string) => awsApi.deleteLogGroup(n),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["logs"] }),
    onError: err,
  });
  return (
    <ResourcePage
      title="CloudWatch Logs · Log Groups"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="lg-name">{t("col.group_name")}</Label>
            <Input
              id="lg-name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="/aws/lambda/my-fn"
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
            <TableHead>{t("col.retention")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((g) => (
            <TableRow key={g.logGroupName}>
              <TableCell className="font-mono text-xs">{g.logGroupName}</TableCell>
              <TableCell>{g.retentionInDays ?? "—"}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() => remove.mutate(g.logGroupName!)}
                >
                  {t("common.delete")}
                </Button>
              </TableCell>
            </TableRow>
          ))}
          {(data ?? []).length === 0 && (
            <TableRow>
              <TableCell colSpan={3} className="text-center text-muted-foreground">
                {t("common.empty")}
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </ResourcePage>
  );
}

// ---------------- IAM ----------------
export function IamList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const users = useQuery({ queryKey: ["iam", "users"], queryFn: awsApi.listIamUsers });
  const roles = useQuery({ queryKey: ["iam", "roles"], queryFn: awsApi.listIamRoles });
  const [u, setU] = useState("");
  const [r, setR] = useState("");
  const createUser = useMutation({
    mutationFn: () => awsApi.createIamUser(u),
    onSuccess: () => {
      setU("");
      qc.invalidateQueries({ queryKey: ["iam", "users"] });
    },
    onError: err,
  });
  const createRole = useMutation({
    mutationFn: () => awsApi.createIamRole(r),
    onSuccess: () => {
      setR("");
      qc.invalidateQueries({ queryKey: ["iam", "roles"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="IAM · Users & Roles"
      description="Users and roles in the local IAM provider."
      onRefresh={() => {
        users.refetch();
        roles.refetch();
      }}
    >
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <div className="flex items-end gap-2 mb-2">
            <div className="flex-1">
              <Label htmlFor="iam-u">{t("col.user_name")}</Label>
              <Input
                id="iam-u"
                value={u}
                onChange={(e) => setU(e.target.value)}
                placeholder="alice"
              />
            </div>
            <Button onClick={() => createUser.mutate()} disabled={!u}>
              Create
            </Button>
          </div>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>{t("col.user")}</TableHead>
                <TableHead>{t("col.arn")}</TableHead>
                <TableHead className="w-20" />
              </TableRow>
            </TableHeader>
            <TableBody>
              {(users.data ?? []).map((x) => (
                <TableRow key={x.Arn}>
                  <TableCell>{x.UserName}</TableCell>
                  <TableCell className="font-mono text-[10px]">{x.Arn}</TableCell>
                  <TableCell>
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() =>
                        awsApi
                          .deleteIamUser(x.UserName!)
                          .then(() => qc.invalidateQueries({ queryKey: ["iam", "users"] }))
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
        </div>
        <div>
          <div className="flex items-end gap-2 mb-2">
            <div className="flex-1">
              <Label htmlFor="iam-r">{t("col.role_name")}</Label>
              <Input
                id="iam-r"
                value={r}
                onChange={(e) => setR(e.target.value)}
                placeholder="lambda-role"
              />
            </div>
            <Button onClick={() => createRole.mutate()} disabled={!r}>
              Create
            </Button>
          </div>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>{t("col.role")}</TableHead>
                <TableHead>{t("col.arn")}</TableHead>
                <TableHead className="w-20" />
              </TableRow>
            </TableHeader>
            <TableBody>
              {(roles.data ?? []).map((x) => (
                <TableRow key={x.Arn}>
                  <TableCell>{x.RoleName}</TableCell>
                  <TableCell className="font-mono text-[10px]">{x.Arn}</TableCell>
                  <TableCell>
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() =>
                        awsApi
                          .deleteIamRole(x.RoleName!)
                          .then(() => qc.invalidateQueries({ queryKey: ["iam", "roles"] }))
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
        </div>
      </div>
    </ResourcePage>
  );
}

// ---------------- Secrets Manager ----------------
export function SecretsList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["secrets"],
    queryFn: awsApi.listSecrets,
  });
  const [name, setName] = useState("");
  const [value, setValue] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createSecret(name, value),
    onSuccess: () => {
      setName("");
      setValue("");
      qc.invalidateQueries({ queryKey: ["secrets"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="Secrets Manager"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="sec-n">{t("col.name")}</Label>
            <Input id="sec-n" value={name} onChange={(e) => setName(e.target.value)} />
          </div>
          <div>
            <Label htmlFor="sec-v">{t("col.value")}</Label>
            <Input
              id="sec-v"
              type="password"
              value={value}
              onChange={(e) => setValue(e.target.value)}
            />
          </div>
          <Button onClick={() => create.mutate()} disabled={!name || !value}>
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
            <TableRow key={s.ARN}>
              <TableCell>{s.Name}</TableCell>
              <TableCell className="font-mono text-[10px]">{s.ARN}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteSecret(s.ARN!)
                      .then(() => qc.invalidateQueries({ queryKey: ["secrets"] }))
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

// ---------------- EC2 ----------------
export function Ec2List() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["ec2", "instances"],
    queryFn: awsApi.listInstances,
  });
  const [ami, setAmi] = useState("ami-12345678");
  const run = useMutation({
    mutationFn: () => awsApi.runInstance(ami),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["ec2"] }),
    onError: err,
  });
  return (
    <ResourcePage
      title="EC2 · Instances"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="ami">{t("col.ami")}</Label>
            <Input id="ami" value={ami} onChange={(e) => setAmi(e.target.value)} />
          </div>
          <Button onClick={() => run.mutate()} disabled={!ami}>
            {t("common.run_instance")}
          </Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>ID</TableHead>
            <TableHead>{t("col.type")}</TableHead>
            <TableHead>{t("col.state")}</TableHead>
            <TableHead>AMI</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((i) => (
            <TableRow key={i.InstanceId}>
              <TableCell className="font-mono text-xs">{i.InstanceId}</TableCell>
              <TableCell>{i.InstanceType}</TableCell>
              <TableCell>{i.State?.Name}</TableCell>
              <TableCell className="font-mono text-xs">{i.ImageId}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .terminateInstance(i.InstanceId!)
                      .then(() => qc.invalidateQueries({ queryKey: ["ec2"] }))
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

// ---------------- KMS ----------------
export function KmsList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["kms"],
    queryFn: awsApi.listKmsKeys,
  });
  const [desc, setDesc] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createKmsKey(desc || "Key created from console"),
    onSuccess: () => {
      setDesc("");
      qc.invalidateQueries({ queryKey: ["kms"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="KMS · Keys"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="kms-d">{t("col.description")}</Label>
            <Input id="kms-d" value={desc} onChange={(e) => setDesc(e.target.value)} />
          </div>
          <Button onClick={() => create.mutate()}>{t("common.create")}</Button>
        </div>
      }
    >
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.id")}</TableHead>
            <TableHead>ARN</TableHead>
            <TableHead className="w-32" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((k) => (
            <TableRow key={k.KeyId}>
              <TableCell className="font-mono text-xs">{k.KeyId}</TableCell>
              <TableCell className="font-mono text-[10px]">{k.KeyArn}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .scheduleKmsKeyDeletion(k.KeyId!)
                      .then(() => qc.invalidateQueries({ queryKey: ["kms"] }))
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

// ---------------- CloudFormation ----------------
export function CfnList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["cfn", "stacks"],
    queryFn: awsApi.listStacks,
  });
  return (
    <ResourcePage title="CloudFormation · Stacks" onRefresh={refetch}>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>{t("col.name")}</TableHead>
            <TableHead>{t("col.state")}</TableHead>
            <TableHead>{t("col.created")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((s) => (
            <TableRow key={s.StackId}>
              <TableCell>{s.StackName}</TableCell>
              <TableCell>{s.StackStatus}</TableCell>
              <TableCell>{s.CreationTime?.toISOString().slice(0, 19)}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteStack(s.StackName!)
                      .then(() => qc.invalidateQueries({ queryKey: ["cfn"] }))
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

// ---------------- ECR ----------------
export function EcrList() {
  const qc = useQueryClient();
  const { t } = useI18n();
  const { data, refetch } = useQuery({
    queryKey: ["ecr"],
    queryFn: awsApi.listEcrRepos,
  });
  const [name, setName] = useState("");
  const create = useMutation({
    mutationFn: () => awsApi.createEcrRepo(name),
    onSuccess: () => {
      setName("");
      qc.invalidateQueries({ queryKey: ["ecr"] });
    },
    onError: err,
  });
  return (
    <ResourcePage
      title="ECR · Repositories"
      onRefresh={refetch}
      actions={
        <div className="flex gap-2 items-end">
          <div>
            <Label htmlFor="ecr-n">{t("col.repo_name")}</Label>
            <Input id="ecr-n" value={name} onChange={(e) => setName(e.target.value)} />
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
            <TableHead>{t("col.uri")}</TableHead>
            <TableHead className="w-24" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {(data ?? []).map((r) => (
            <TableRow key={r.repositoryArn}>
              <TableCell>{r.repositoryName}</TableCell>
              <TableCell className="font-mono text-xs">{r.repositoryUri}</TableCell>
              <TableCell>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() =>
                    awsApi
                      .deleteEcrRepo(r.repositoryName!)
                      .then(() => qc.invalidateQueries({ queryKey: ["ecr"] }))
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
