import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import { applySkin, type CloudName } from "./skins";

interface CloudState {
  cloud: CloudName;
  region: string;
  endpoint: string;
  tlsEndpoint: string;
  project: string;
  subscription: string;
}

interface CloudContextValue extends CloudState {
  setCloud: (c: CloudName) => void;
  setRegion: (r: string) => void;
}

const DEFAULT_REGION: Record<CloudName, string> = {
  aws: "us-east-1",
  azure: "eastus",
  gcp: "us-central1",
};

const STORAGE_KEY = "localstack-console:cloud-state";

const initial: CloudState = {
  cloud: "aws",
  region: "us-east-1",
  endpoint: "http://localhost:4566",
  tlsEndpoint: "https://localhost:4569",
  project: "localstack-project",
  subscription: "00000000-0000-0000-0000-000000000000",
};

function load(): CloudState {
  if (typeof localStorage === "undefined") return initial;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return initial;
    return { ...initial, ...(JSON.parse(raw) as Partial<CloudState>) };
  } catch {
    return initial;
  }
}

const CloudContext = createContext<CloudContextValue | null>(null);

export function CloudProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<CloudState>(() => load());

  useEffect(() => {
    applySkin(state.cloud);
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch {
      /* ignore */
    }
  }, [state]);

  const value = useMemo<CloudContextValue>(
    () => ({
      ...state,
      setCloud: (cloud) =>
        setState((s) => ({ ...s, cloud, region: DEFAULT_REGION[cloud] })),
      setRegion: (region) => setState((s) => ({ ...s, region })),
    }),
    [state],
  );

  return <CloudContext.Provider value={value}>{children}</CloudContext.Provider>;
}

export function useCloud(): CloudContextValue {
  const ctx = useContext(CloudContext);
  if (!ctx) throw new Error("useCloud must be used within CloudProvider");
  return ctx;
}
