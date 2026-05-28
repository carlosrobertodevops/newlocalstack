import { useSyncExternalStore } from "react";

export type IacTool = "terraform" | "serverless";

export interface IacDrawerState {
  open: boolean;
  tool: IacTool;
  snippet: string;
  title?: string;
}

const initial: IacDrawerState = {
  open: false,
  tool: "terraform",
  snippet: "",
};

let state: IacDrawerState = initial;
const listeners = new Set<() => void>();

function emit() {
  for (const fn of listeners) fn();
}

export function openIacDrawer(input: {
  tool: IacTool;
  snippet: string;
  title?: string;
}) {
  state = { open: true, ...input };
  emit();
}

export function closeIacDrawer() {
  state = { ...state, open: false };
  emit();
}

export function setIacSnippet(snippet: string) {
  state = { ...state, snippet };
  emit();
}

function subscribe(listener: () => void) {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function useIacDrawer(): IacDrawerState {
  return useSyncExternalStore(subscribe, () => state);
}
