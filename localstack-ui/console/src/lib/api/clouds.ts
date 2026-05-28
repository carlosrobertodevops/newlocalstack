/** Meta endpoints exposed by the LocalStack edge gateway. */

export interface CloudSummary {
  name: string;
  display_name: string;
  package: string;
  services_count: number;
}

export interface CloudHealth {
  cloud: string;
  display_name?: string;
  edition?: string;
  version?: string;
  services: Record<string, string>;
  error?: string;
}

export interface CloudInfo {
  cloud: string;
  display_name: string;
  package: string;
  edge_hosts: string[];
  services_count: number;
  scope_terms?: Record<string, unknown>;
  auth?: Record<string, unknown>;
  id_format?: Record<string, unknown>;
  version?: string;
  edition?: string;
}

function base(): string {
  return import.meta.env.DEV ? "" : "";
}

async function getJSON<T>(path: string): Promise<T> {
  const res = await fetch(`${base()}${path}`, { mode: "cors" });
  if (!res.ok) throw new Error(`${path} → HTTP ${res.status}`);
  return res.json() as Promise<T>;
}

export const cloudsApi = {
  list: () => getJSON<{ clouds: CloudSummary[] }>("/_localstack/clouds"),
  health: (cloud: string) =>
    getJSON<CloudHealth>(`/_localstack/clouds/${cloud}/health`),
  info: (cloud: string) =>
    getJSON<CloudInfo>(`/_localstack/clouds/${cloud}/info`),
};
