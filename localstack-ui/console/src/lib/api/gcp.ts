const GCP = "http://localhost:4566";

async function gcp<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${GCP}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
  });
  if (!res.ok) {
    const t = await res.text().catch(() => "");
    throw new Error(`${path} → ${res.status}: ${t}`);
  }
  if (res.status === 204) return undefined as T;
  return (await res.json()) as T;
}

interface Bucket {
  id?: string;
  name: string;
  location?: string;
  storageClass?: string;
}

interface BucketObject {
  name: string;
  size?: string;
  updated?: string;
  contentType?: string;
}

interface Topic {
  name: string;
}

interface Subscription {
  name: string;
  topic: string;
}

interface Dataset {
  datasetReference: { datasetId: string; projectId: string };
  location?: string;
}

interface CloudFunction {
  name: string;
  state?: string;
  buildConfig?: { runtime?: string };
}

interface CloudRunService {
  name: string;
  uri?: string;
  creator?: string;
}

interface Secret {
  name: string;
}

interface ServiceAccount {
  email: string;
  displayName?: string;
  uniqueId?: string;
}

interface KeyRing {
  name: string;
}

interface CryptoKey {
  name: string;
  purpose?: string;
}

interface ManagedZone {
  name: string;
  dnsName?: string;
  description?: string;
}

interface FirestoreDatabase {
  name: string;
  type?: string;
  locationId?: string;
}

interface ComputeNetwork {
  id?: string;
  name: string;
  selfLink?: string;
  autoCreateSubnetworks?: boolean;
}

interface ComputeInstance {
  id?: string;
  name: string;
  machineType?: string;
  status?: string;
  zone?: string;
}

interface SqlInstance {
  name: string;
  databaseVersion?: string;
  region?: string;
  state?: string;
}

interface SpannerInstance {
  name: string;
  displayName?: string;
  state?: string;
}

interface MetricDescriptor {
  name: string;
  type?: string;
  metricKind?: string;
}

interface SchedulerJob {
  name: string;
  schedule?: string;
  state?: string;
}

export const gcpApi = {
  // Cloud Storage
  listBuckets: async (project: string) => {
    const body = await gcp<{ items?: Bucket[] }>(
      `/storage/v1/b?project=${encodeURIComponent(project)}`,
    );
    return body.items ?? [];
  },
  createBucket: (project: string, name: string) =>
    gcp<Bucket>(`/storage/v1/b?project=${encodeURIComponent(project)}`, {
      method: "POST",
      body: JSON.stringify({ name, location: "US" }),
    }),
  deleteBucket: (name: string) =>
    gcp<void>(`/storage/v1/b/${encodeURIComponent(name)}`, { method: "DELETE" }),
  listObjects: async (bucket: string) => {
    const body = await gcp<{ items?: BucketObject[] }>(
      `/storage/v1/b/${encodeURIComponent(bucket)}/o`,
    );
    return body.items ?? [];
  },

  // Pub/Sub
  listTopics: async (project: string) => {
    const body = await gcp<{ topics?: Topic[] }>(
      `/v1/projects/${encodeURIComponent(project)}/topics`,
    );
    return body.topics ?? [];
  },
  createTopic: (project: string, name: string) =>
    gcp<Topic>(
      `/v1/projects/${encodeURIComponent(project)}/topics/${encodeURIComponent(name)}`,
      { method: "PUT", body: JSON.stringify({}) },
    ),
  deleteTopic: (project: string, name: string) =>
    gcp<void>(
      `/v1/projects/${encodeURIComponent(project)}/topics/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),
  listSubscriptions: async (project: string) => {
    const body = await gcp<{ subscriptions?: Subscription[] }>(
      `/v1/projects/${encodeURIComponent(project)}/subscriptions`,
    );
    return body.subscriptions ?? [];
  },

  // BigQuery
  listDatasets: async (project: string) => {
    const body = await gcp<{ datasets?: Dataset[] }>(
      `/bigquery/v2/projects/${encodeURIComponent(project)}/datasets`,
    );
    return body.datasets ?? [];
  },
  createDataset: (project: string, datasetId: string) =>
    gcp<Dataset>(`/bigquery/v2/projects/${encodeURIComponent(project)}/datasets`, {
      method: "POST",
      body: JSON.stringify({
        datasetReference: { datasetId, projectId: project },
        location: "US",
      }),
    }),
  deleteDataset: (project: string, datasetId: string) =>
    gcp<void>(
      `/bigquery/v2/projects/${encodeURIComponent(project)}/datasets/${encodeURIComponent(datasetId)}`,
      { method: "DELETE" },
    ),

  // Cloud Functions (Gen 2)
  listFunctions: async (project: string) => {
    const body = await gcp<{ functions?: CloudFunction[] }>(
      `/v2/projects/${encodeURIComponent(project)}/locations/-/functions`,
    );
    return body.functions ?? [];
  },
  createFunction: (project: string, location: string, name: string, runtime = "nodejs20") =>
    gcp<CloudFunction>(
      `/v2/projects/${encodeURIComponent(project)}/locations/${location}/functions?functionId=${encodeURIComponent(name)}`,
      {
        method: "POST",
        body: JSON.stringify({
          buildConfig: { runtime, entryPoint: "handler" },
          serviceConfig: { ingressSettings: "ALLOW_ALL" },
        }),
      },
    ),
  deleteFunction: (project: string, location: string, name: string) =>
    gcp<void>(
      `/v2/projects/${encodeURIComponent(project)}/locations/${location}/functions/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),

  // Cloud Run
  listRunServices: async (project: string) => {
    const body = await gcp<{ services?: CloudRunService[] }>(
      `/v2/projects/${encodeURIComponent(project)}/locations/-/services`,
    );
    return body.services ?? [];
  },
  createRunService: (project: string, location: string, name: string, image: string) =>
    gcp<CloudRunService>(
      `/v2/projects/${encodeURIComponent(project)}/locations/${location}/services?serviceId=${encodeURIComponent(name)}`,
      {
        method: "POST",
        body: JSON.stringify({
          template: { containers: [{ image }] },
        }),
      },
    ),
  deleteRunService: (project: string, location: string, name: string) =>
    gcp<void>(
      `/v2/projects/${encodeURIComponent(project)}/locations/${location}/services/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),

  // Secret Manager
  listSecrets: async (project: string) => {
    const body = await gcp<{ secrets?: Secret[] }>(
      `/v1/projects/${encodeURIComponent(project)}/secrets`,
    );
    return body.secrets ?? [];
  },
  createSecret: (project: string, secretId: string) =>
    gcp<Secret>(
      `/v1/projects/${encodeURIComponent(project)}/secrets?secretId=${encodeURIComponent(secretId)}`,
      { method: "POST", body: JSON.stringify({ replication: { automatic: {} } }) },
    ),
  deleteSecret: (project: string, secretId: string) =>
    gcp<void>(
      `/v1/projects/${encodeURIComponent(project)}/secrets/${encodeURIComponent(secretId)}`,
      { method: "DELETE" },
    ),

  // IAM
  listServiceAccounts: async (project: string) => {
    const body = await gcp<{ accounts?: ServiceAccount[] }>(
      `/v1/projects/${encodeURIComponent(project)}/serviceAccounts`,
    );
    return body.accounts ?? [];
  },
  createServiceAccount: (project: string, accountId: string) =>
    gcp<ServiceAccount>(
      `/v1/projects/${encodeURIComponent(project)}/serviceAccounts`,
      {
        method: "POST",
        body: JSON.stringify({
          accountId,
          serviceAccount: { displayName: accountId },
        }),
      },
    ),
  deleteServiceAccount: (project: string, email: string) =>
    gcp<void>(
      `/v1/projects/${encodeURIComponent(project)}/serviceAccounts/${encodeURIComponent(email)}`,
      { method: "DELETE" },
    ),

  // KMS
  listKeyRings: async (project: string, location = "global") => {
    const body = await gcp<{ keyRings?: KeyRing[] }>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${location}/keyRings`,
    );
    return body.keyRings ?? [];
  },
  createKeyRing: (project: string, location: string, keyRingId: string) =>
    gcp<KeyRing>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${location}/keyRings?keyRingId=${encodeURIComponent(keyRingId)}`,
      { method: "POST", body: JSON.stringify({}) },
    ),
  listKmsKeys: async (keyRing: string) => {
    const body = await gcp<{ cryptoKeys?: CryptoKey[] }>(
      `/v1/${keyRing}/cryptoKeys`,
    );
    return body.cryptoKeys ?? [];
  },

  // DNS
  listZones: async (project: string) => {
    const body = await gcp<{ managedZones?: ManagedZone[] }>(
      `/dns/v1/projects/${encodeURIComponent(project)}/managedZones`,
    );
    return body.managedZones ?? [];
  },
  createZone: (project: string, name: string, dnsName: string) =>
    gcp<ManagedZone>(
      `/dns/v1/projects/${encodeURIComponent(project)}/managedZones`,
      {
        method: "POST",
        body: JSON.stringify({
          name,
          dnsName: dnsName.endsWith(".") ? dnsName : `${dnsName}.`,
          description: "console-created",
        }),
      },
    ),
  deleteZone: (project: string, name: string) =>
    gcp<void>(
      `/dns/v1/projects/${encodeURIComponent(project)}/managedZones/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),

  // Firestore
  listFirestoreDatabases: async (project: string) => {
    const body = await gcp<{ databases?: FirestoreDatabase[] }>(
      `/v1/projects/${encodeURIComponent(project)}/databases`,
    );
    return body.databases ?? [];
  },
  createFirestoreDatabase: (project: string, databaseId: string, locationId = "us-central1") =>
    gcp<FirestoreDatabase>(
      `/v1/projects/${encodeURIComponent(project)}/databases?databaseId=${encodeURIComponent(databaseId)}`,
      {
        method: "POST",
        body: JSON.stringify({ type: "FIRESTORE_NATIVE", locationId }),
      },
    ),

  // Compute (VPC)
  listNetworks: async (project: string) => {
    const body = await gcp<{ items?: ComputeNetwork[] }>(
      `/compute/v1/projects/${encodeURIComponent(project)}/global/networks`,
    );
    return body.items ?? [];
  },
  createNetwork: (project: string, name: string) =>
    gcp<ComputeNetwork>(
      `/compute/v1/projects/${encodeURIComponent(project)}/global/networks`,
      {
        method: "POST",
        body: JSON.stringify({ name, autoCreateSubnetworks: true }),
      },
    ),
  deleteNetwork: (project: string, name: string) =>
    gcp<void>(
      `/compute/v1/projects/${encodeURIComponent(project)}/global/networks/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),

  // Compute Engine instances (zone-scoped)
  listInstances: async (project: string, zone: string) => {
    const body = await gcp<{ items?: ComputeInstance[] }>(
      `/compute/v1/projects/${encodeURIComponent(project)}/zones/${encodeURIComponent(zone)}/instances`,
    );
    return body.items ?? [];
  },
  createInstance: (project: string, zone: string, name: string, machineType = "e2-small") =>
    gcp<ComputeInstance>(
      `/compute/v1/projects/${encodeURIComponent(project)}/zones/${encodeURIComponent(zone)}/instances`,
      {
        method: "POST",
        body: JSON.stringify({
          name,
          machineType: `zones/${zone}/machineTypes/${machineType}`,
          disks: [
            {
              boot: true,
              autoDelete: true,
              initializeParams: { sourceImage: "projects/debian-cloud/global/images/family/debian-12" },
            },
          ],
          networkInterfaces: [{ network: "global/networks/default" }],
        }),
      },
    ),
  deleteInstance: (project: string, zone: string, name: string) =>
    gcp<void>(
      `/compute/v1/projects/${encodeURIComponent(project)}/zones/${encodeURIComponent(zone)}/instances/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),

  // Cloud SQL
  listSqlInstances: async (project: string) => {
    const body = await gcp<{ items?: SqlInstance[] }>(
      `/sql/v1beta4/projects/${encodeURIComponent(project)}/instances`,
    );
    return body.items ?? [];
  },
  createSqlInstance: (project: string, name: string, region = "us-central1") =>
    gcp<SqlInstance>(
      `/sql/v1beta4/projects/${encodeURIComponent(project)}/instances`,
      {
        method: "POST",
        body: JSON.stringify({
          name,
          region,
          databaseVersion: "POSTGRES_15",
          settings: { tier: "db-f1-micro" },
        }),
      },
    ),
  deleteSqlInstance: (project: string, name: string) =>
    gcp<void>(
      `/sql/v1beta4/projects/${encodeURIComponent(project)}/instances/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),

  // Spanner
  listSpannerInstances: async (project: string) => {
    const body = await gcp<{ instances?: SpannerInstance[] }>(
      `/v1/projects/${encodeURIComponent(project)}/instances`,
    );
    return body.instances ?? [];
  },
  createSpannerInstance: (project: string, instanceId: string, displayName: string) =>
    gcp<SpannerInstance>(
      `/v1/projects/${encodeURIComponent(project)}/instances`,
      {
        method: "POST",
        body: JSON.stringify({
          instanceId,
          instance: {
            config: `projects/${project}/instanceConfigs/regional-us-central1`,
            displayName,
            nodeCount: 1,
          },
        }),
      },
    ),
  deleteSpannerInstance: (project: string, instanceId: string) =>
    gcp<void>(
      `/v1/projects/${encodeURIComponent(project)}/instances/${encodeURIComponent(instanceId)}`,
      { method: "DELETE" },
    ),

  // Monitoring
  listMonitoringMetrics: async (project: string) => {
    const body = await gcp<{ metricDescriptors?: MetricDescriptor[] }>(
      `/v3/projects/${encodeURIComponent(project)}/metricDescriptors`,
    );
    return body.metricDescriptors ?? [];
  },

  // Cloud Scheduler
  listSchedulerJobs: async (project: string, location: string) => {
    const body = await gcp<{ jobs?: SchedulerJob[] }>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${encodeURIComponent(location)}/jobs`,
    );
    return body.jobs ?? [];
  },
  createSchedulerJob: (
    project: string,
    location: string,
    jobId: string,
    schedule: string,
    targetUrl: string,
  ) =>
    gcp<SchedulerJob>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${encodeURIComponent(location)}/jobs`,
      {
        method: "POST",
        body: JSON.stringify({
          name: `projects/${project}/locations/${location}/jobs/${jobId}`,
          schedule,
          httpTarget: { uri: targetUrl, httpMethod: "GET" },
        }),
      },
    ),
  deleteSchedulerJob: (project: string, location: string, jobId: string) =>
    gcp<void>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${encodeURIComponent(location)}/jobs/${encodeURIComponent(jobId)}`,
      { method: "DELETE" },
    ),

  // GKE — Kubernetes Engine
  listGkeClusters: async (project: string, location = "-") => {
    const body = await gcp<{ clusters?: Array<{ name: string; location?: string; status?: string }> }>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${encodeURIComponent(location)}/clusters`,
    );
    return body.clusters ?? [];
  },
  createGkeCluster: (project: string, location: string, name: string) =>
    gcp<unknown>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${encodeURIComponent(location)}/clusters`,
      {
        method: "POST",
        body: JSON.stringify({
          cluster: {
            name,
            initialNodeCount: 1,
            nodeConfig: { machineType: "e2-small" },
          },
        }),
      },
    ),
  deleteGkeCluster: (project: string, location: string, name: string) =>
    gcp<void>(
      `/v1/projects/${encodeURIComponent(project)}/locations/${encodeURIComponent(location)}/clusters/${encodeURIComponent(name)}`,
      { method: "DELETE" },
    ),
};

export type {
  Bucket,
  BucketObject,
  Topic,
  Subscription,
  Dataset,
  CloudFunction,
  CloudRunService,
  Secret,
  ServiceAccount,
  KeyRing,
  CryptoKey,
  ManagedZone,
  FirestoreDatabase,
  ComputeNetwork,
  ComputeInstance,
  SqlInstance,
  SpannerInstance,
  MetricDescriptor,
  SchedulerJob,
};
