import { describe, it, expect, vi, beforeEach } from "vitest";
import { execCli, isAllowedCli, BRIDGE_URL } from "@/lib/cli-bridge";

describe("isAllowedCli", () => {
  it("accepts known clis", () => {
    expect(isAllowedCli("aws")).toBe(true);
    expect(isAllowedCli("az")).toBe(true);
    expect(isAllowedCli("gcloud")).toBe(true);
  });
  it("rejects others", () => {
    expect(isAllowedCli("rm")).toBe(false);
    expect(isAllowedCli("")).toBe(false);
    expect(isAllowedCli("aws ls")).toBe(false);
  });
});

describe("execCli", () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  it("rejects disallowed cli without calling fetch", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch");
    // @ts-expect-error — testing the runtime guard
    await expect(execCli("rm", [])).rejects.toThrow(/allowlist/);
    expect(fetchSpy).not.toHaveBeenCalled();
  });

  it("uses bridge URL when /health returns ok", async () => {
    const fetchMock = vi
      .spyOn(globalThis, "fetch")
      .mockImplementation((input) => {
        const url = typeof input === "string" ? input : input.toString();
        if (url.endsWith("/health")) {
          return Promise.resolve(
            new Response(JSON.stringify({ status: "ok" }), { status: 200 }),
          );
        }
        return Promise.resolve(
          new Response(
            JSON.stringify({
              session_id: "abc",
              exit_code: 0,
              stdout: "ok",
              stderr: "",
              duration_ms: 5,
            }),
            { status: 200 },
          ),
        );
      });

    const r = await execCli("aws", ["s3", "ls"]);
    expect(r.via).toBe("bridge");
    expect(r.stdout).toBe("ok");
    const calls = fetchMock.mock.calls.map((c) => c[0]);
    expect(calls.some((c) => String(c).startsWith(BRIDGE_URL))).toBe(true);
  });

  it("falls back to in-container endpoint when bridge unreachable", async () => {
    vi.spyOn(globalThis, "fetch").mockImplementation((input) => {
      const url = typeof input === "string" ? input : input.toString();
      if (url.endsWith("/health")) return Promise.reject(new Error("no bridge"));
      return Promise.resolve(
        new Response(
          JSON.stringify({
            session_id: "x",
            exit_code: 0,
            stdout: "fallback",
            stderr: "",
            duration_ms: 1,
          }),
          { status: 200 },
        ),
      );
    });

    const r = await execCli("aws", ["s3", "ls"]);
    expect(r.via).toBe("in-container");
    expect(r.stdout).toBe("fallback");
  });
});
