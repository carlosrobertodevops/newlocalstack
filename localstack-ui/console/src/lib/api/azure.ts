const ARM = "http://localhost:4566";
const HEADERS = {
  Authorization: "Bearer dev-token",
  "Content-Type": "application/json",
};

async function arm<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${ARM}${path}`, {
    ...init,
    headers: { ...HEADERS, ...(init?.headers ?? {}) },
  });
  if (!res.ok) {
    const t = await res.text().catch(() => "");
    throw new Error(`${path} → ${res.status}: ${t}`);
  }
  if (res.status === 204) return undefined as T;
  return (await res.json()) as T;
}

interface RG {
  id: string;
  name: string;
  location: string;
  properties?: { provisioningState?: string };
}

interface StorageAccount {
  id: string;
  name: string;
  location: string;
  kind?: string;
}

interface VirtualNetwork {
  id: string;
  name: string;
  location: string;
  properties?: { addressSpace?: { addressPrefixes?: string[] } };
}

interface AppService {
  id: string;
  name: string;
  location: string;
  kind?: string;
}

interface ContainerRegistry {
  id: string;
  name: string;
  location: string;
  sku?: { name?: string };
}

interface LogAnalyticsWorkspace {
  id: string;
  name: string;
  location: string;
}

interface RedisCache {
  id: string;
  name: string;
  location: string;
  properties?: { sku?: { name?: string } };
}

const rgPath = (sub: string, rg: string) =>
  `/subscriptions/${sub}/resourceGroups/${encodeURIComponent(rg)}`;

async function ensureRg(sub: string, rg: string, location: string) {
  await arm<RG>(
    `/subscriptions/${sub}/resourceGroups/${encodeURIComponent(rg)}?api-version=2021-04-01`,
    { method: "PUT", body: JSON.stringify({ location }) },
  );
}

export const azureApi = {
  ensureResourceGroup: ensureRg,
  listResourceGroups: async (sub: string) => {
    const body = await arm<{ value: RG[] }>(
      `/subscriptions/${sub}/resourceGroups?api-version=2021-04-01`,
    );
    return body.value;
  },
  createResourceGroup: (sub: string, name: string, location: string) =>
    arm<RG>(
      `/subscriptions/${sub}/resourceGroups/${encodeURIComponent(name)}?api-version=2021-04-01`,
      { method: "PUT", body: JSON.stringify({ location }) },
    ),
  deleteResourceGroup: (sub: string, name: string) =>
    arm<void>(
      `/subscriptions/${sub}/resourceGroups/${encodeURIComponent(name)}?api-version=2021-04-01`,
      { method: "DELETE" },
    ),

  // Storage Accounts
  listStorageAccounts: async (sub: string) => {
    const body = await arm<{ value: StorageAccount[] }>(
      `/subscriptions/${sub}/providers/Microsoft.Storage/storageAccounts?api-version=2023-05-01`,
    );
    return body.value;
  },
  createStorageAccount: async (
    sub: string,
    rg: string,
    name: string,
    location: string,
  ) => {
    await ensureRg(sub, rg, location);
    return arm<StorageAccount>(
      `${rgPath(sub, rg)}/providers/Microsoft.Storage/storageAccounts/${encodeURIComponent(name)}?api-version=2023-05-01`,
      {
        method: "PUT",
        body: JSON.stringify({
          location,
          sku: { name: "Standard_LRS" },
          kind: "StorageV2",
          properties: {},
        }),
      },
    );
  },
  deleteStorageAccount: (sub: string, rg: string, name: string) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/Microsoft.Storage/storageAccounts/${encodeURIComponent(name)}?api-version=2023-05-01`,
      { method: "DELETE" },
    ),

  // Virtual Network
  listVirtualNetworks: async (sub: string) => {
    const body = await arm<{ value: VirtualNetwork[] }>(
      `/subscriptions/${sub}/providers/Microsoft.Network/virtualNetworks?api-version=2023-09-01`,
    );
    return body.value;
  },
  createVirtualNetwork: async (
    sub: string,
    rg: string,
    name: string,
    location: string,
    cidr = "10.0.0.0/16",
  ) => {
    await ensureRg(sub, rg, location);
    return arm<VirtualNetwork>(
      `${rgPath(sub, rg)}/providers/Microsoft.Network/virtualNetworks/${encodeURIComponent(name)}?api-version=2023-09-01`,
      {
        method: "PUT",
        body: JSON.stringify({
          location,
          properties: { addressSpace: { addressPrefixes: [cidr] } },
        }),
      },
    );
  },
  deleteVirtualNetwork: (sub: string, rg: string, name: string) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/Microsoft.Network/virtualNetworks/${encodeURIComponent(name)}?api-version=2023-09-01`,
      { method: "DELETE" },
    ),

  // App Service (Microsoft.Web/sites)
  listAppServices: async (sub: string) => {
    const body = await arm<{ value: AppService[] }>(
      `/subscriptions/${sub}/providers/Microsoft.Web/sites?api-version=2022-03-01`,
    );
    return body.value;
  },
  createAppService: async (sub: string, rg: string, name: string, location: string) => {
    await ensureRg(sub, rg, location);
    return arm<AppService>(
      `${rgPath(sub, rg)}/providers/Microsoft.Web/sites/${encodeURIComponent(name)}?api-version=2022-03-01`,
      {
        method: "PUT",
        body: JSON.stringify({ location, properties: {} }),
      },
    );
  },
  deleteAppService: (sub: string, rg: string, name: string) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/Microsoft.Web/sites/${encodeURIComponent(name)}?api-version=2022-03-01`,
      { method: "DELETE" },
    ),

  // Container Registry
  listContainerRegistries: async (sub: string) => {
    const body = await arm<{ value: ContainerRegistry[] }>(
      `/subscriptions/${sub}/providers/Microsoft.ContainerRegistry/registries?api-version=2023-07-01`,
    );
    return body.value;
  },
  createContainerRegistry: async (
    sub: string,
    rg: string,
    name: string,
    location: string,
  ) => {
    await ensureRg(sub, rg, location);
    return arm<ContainerRegistry>(
      `${rgPath(sub, rg)}/providers/Microsoft.ContainerRegistry/registries/${encodeURIComponent(name)}?api-version=2023-07-01`,
      {
        method: "PUT",
        body: JSON.stringify({
          location,
          sku: { name: "Basic" },
          properties: { adminUserEnabled: false },
        }),
      },
    );
  },
  deleteContainerRegistry: (sub: string, rg: string, name: string) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/Microsoft.ContainerRegistry/registries/${encodeURIComponent(name)}?api-version=2023-07-01`,
      { method: "DELETE" },
    ),

  // Log Analytics (Monitor)
  listLogAnalyticsWorkspaces: async (sub: string) => {
    const body = await arm<{ value: LogAnalyticsWorkspace[] }>(
      `/subscriptions/${sub}/providers/Microsoft.OperationalInsights/workspaces?api-version=2022-10-01`,
    );
    return body.value;
  },
  createLogAnalyticsWorkspace: async (
    sub: string,
    rg: string,
    name: string,
    location: string,
  ) => {
    await ensureRg(sub, rg, location);
    return arm<LogAnalyticsWorkspace>(
      `${rgPath(sub, rg)}/providers/Microsoft.OperationalInsights/workspaces/${encodeURIComponent(name)}?api-version=2022-10-01`,
      {
        method: "PUT",
        body: JSON.stringify({
          location,
          properties: { sku: { name: "PerGB2018" } },
        }),
      },
    );
  },
  deleteLogAnalyticsWorkspace: (sub: string, rg: string, name: string) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/Microsoft.OperationalInsights/workspaces/${encodeURIComponent(name)}?api-version=2022-10-01`,
      { method: "DELETE" },
    ),

  // Redis Cache
  listRedisCaches: async (sub: string) => {
    const body = await arm<{ value: RedisCache[] }>(
      `/subscriptions/${sub}/providers/Microsoft.Cache/redis?api-version=2023-08-01`,
    );
    return body.value;
  },
  createRedisCache: async (
    sub: string,
    rg: string,
    name: string,
    location: string,
  ) => {
    await ensureRg(sub, rg, location);
    return arm<RedisCache>(
      `${rgPath(sub, rg)}/providers/Microsoft.Cache/redis/${encodeURIComponent(name)}?api-version=2023-08-01`,
      {
        method: "PUT",
        body: JSON.stringify({
          location,
          properties: {
            sku: { name: "Basic", family: "C", capacity: 0 },
            enableNonSslPort: true,
          },
        }),
      },
    );
  },
  deleteRedisCache: (sub: string, rg: string, name: string) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/Microsoft.Cache/redis/${encodeURIComponent(name)}?api-version=2023-08-01`,
      { method: "DELETE" },
    ),

  // ---- Generic ARM CRUD (for any ns/rtype) ----
  listGeneric: async (sub: string, ns: string, rtype: string, apiVersion: string) => {
    const body = await arm<{ value: Array<{ id: string; name: string; location?: string; properties?: Record<string, unknown> }> }>(
      `/subscriptions/${sub}/providers/${ns}/${rtype}?api-version=${apiVersion}`,
    );
    return body.value;
  },
  createGeneric: async (
    sub: string,
    rg: string,
    ns: string,
    rtype: string,
    name: string,
    location: string,
    apiVersion: string,
    extra: Record<string, unknown> = {},
  ) => {
    await ensureRg(sub, rg, location);
    return arm<{ id: string; name: string; location?: string }>(
      `${rgPath(sub, rg)}/providers/${ns}/${rtype}/${encodeURIComponent(name)}?api-version=${apiVersion}`,
      {
        method: "PUT",
        body: JSON.stringify({ location, ...extra }),
      },
    );
  },
  deleteGeneric: (
    sub: string,
    rg: string,
    ns: string,
    rtype: string,
    name: string,
    apiVersion: string,
  ) =>
    arm<void>(
      `${rgPath(sub, rg)}/providers/${ns}/${rtype}/${encodeURIComponent(name)}?api-version=${apiVersion}`,
      { method: "DELETE" },
    ),
};

export type {
  RG,
  StorageAccount,
  VirtualNetwork,
  AppService,
  ContainerRegistry,
  LogAnalyticsWorkspace,
  RedisCache,
};
