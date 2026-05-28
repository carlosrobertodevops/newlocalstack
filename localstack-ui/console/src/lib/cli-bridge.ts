/**
 * Tiny client for the host-side bridge worker (bin/console-cli-bridge).
 * Falls back to the in-container endpoint /_localstack/console/cli when
 * the bridge is unreachable.
 */

export const BRIDGE_URL =
  import.meta.env.VITE_CONSOLE_BRIDGE ?? "http://localhost:4578";

export interface ExecResult {
  session_id: string;
  exit_code: number;
  stdout: string;
  stderr: string;
  duration_ms: number;
  via: "bridge" | "in-container";
}

const ALLOWED_CLIS = ["aws", "az", "gcloud"] as const;
export type Cli = (typeof ALLOWED_CLIS)[number];

export function isAllowedCli(c: string): c is Cli {
  return (ALLOWED_CLIS as readonly string[]).includes(c);
}

async function bridgeHealthy(timeoutMs = 500): Promise<boolean> {
  try {
    const ac = new AbortController();
    const t = setTimeout(() => ac.abort(), timeoutMs);
    const res = await fetch(`${BRIDGE_URL}/health`, { signal: ac.signal });
    clearTimeout(t);
    return res.ok;
  } catch {
    return false;
  }
}

export async function execCli(
  cli: Cli,
  args: string[],
  env?: Record<string, string>,
): Promise<ExecResult> {
  if (!isAllowedCli(cli)) {
    throw new Error(`cli not in allowlist: ${cli}`);
  }

  const useBridge = await bridgeHealthy();
  const url = useBridge ? `${BRIDGE_URL}/exec` : "/_localstack/console/cli";

  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ cli, args, env }),
  });

  if (!res.ok) {
    const body = await res.text().catch(() => "");
    throw new Error(`${url} → HTTP ${res.status}: ${body}`);
  }

  const data = (await res.json()) as Omit<ExecResult, "via">;
  return { ...data, via: useBridge ? "bridge" : "in-container" };
}
