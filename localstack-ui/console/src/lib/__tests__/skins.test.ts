import { describe, it, expect, beforeEach } from "vitest";
import { applySkin, SKINS } from "@/lib/skins";

function root() {
  return document.documentElement;
}

describe("applySkin", () => {
  beforeEach(() => {
    root().removeAttribute("style");
    root().removeAttribute("data-cloud");
  });

  it("sets AWS skin CSS variables", () => {
    applySkin("aws");
    expect(root().style.getPropertyValue("--bg-top")).toBe(SKINS.aws.bgTop);
    expect(root().style.getPropertyValue("--accent")).toBe(SKINS.aws.accent);
    expect(root().dataset.cloud).toBe("aws");
  });

  it("switching to azure changes --bg-top", () => {
    applySkin("aws");
    const awsBg = root().style.getPropertyValue("--bg-top");
    applySkin("azure");
    expect(root().style.getPropertyValue("--bg-top")).not.toBe(awsBg);
    expect(root().style.getPropertyValue("--bg-top")).toBe(SKINS.azure.bgTop);
    expect(root().dataset.cloud).toBe("azure");
  });

  it("switching to gcp uses gcp tokens", () => {
    applySkin("gcp");
    expect(root().style.getPropertyValue("--accent")).toBe(SKINS.gcp.accent);
    expect(root().style.getPropertyValue("--sidebar")).toBe(SKINS.gcp.sidebar);
  });
});
