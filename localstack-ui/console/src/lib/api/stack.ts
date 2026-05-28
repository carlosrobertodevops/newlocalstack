// Helpers for the multi-cloud "Stack em ação" REST endpoints exposed by
// localstack-core/localstack/aws/services/_localstack_stack.py.

const LOCALSTACK_BASE = "http://localhost:4566";

export type CloudName = "aws" | "azure" | "gcp";

export interface StackService {
  service: string;
  resource_count: number;
  azure_type?: string;
}

export interface StackInventory {
  cloud: CloudName;
  services: StackService[];
  total_resources: number;
  total_services: number;
}

async function jsonOrThrow(res: Response): Promise<unknown> {
  if (!res.ok) {
    const body = await res.text().catch(() => "");
    throw new Error(`HTTP ${res.status}: ${body || res.statusText}`);
  }
  return res.json().catch(() => ({}));
}

export const stackApi = {
  inventory: async (cloud: CloudName): Promise<StackInventory> =>
    jsonOrThrow(
      await fetch(`${LOCALSTACK_BASE}/_localstack/clouds/${cloud}/stack`, {
        method: "GET",
        headers: { Accept: "application/json" },
      }),
    ) as Promise<StackInventory>,

  remove: async (cloud: CloudName, service: string): Promise<unknown> =>
    jsonOrThrow(
      await fetch(
        `${LOCALSTACK_BASE}/_localstack/clouds/${cloud}/stack/services/${encodeURIComponent(service)}`,
        {
          method: "DELETE",
          headers: { Accept: "application/json" },
        },
      ),
    ),

  resetAll: async (cloud: CloudName): Promise<unknown> =>
    jsonOrThrow(
      await fetch(`${LOCALSTACK_BASE}/_localstack/clouds/${cloud}/stack/reset`, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ confirm: true }),
      }),
    ),
};
