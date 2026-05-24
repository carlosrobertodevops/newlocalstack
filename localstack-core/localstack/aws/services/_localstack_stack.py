"""Multi-cloud "stack em ação" endpoints.

Exposes per-cloud inventory + reset operations consumed by the console's
Stack page:

    GET    /_localstack/clouds/<cloud>/stack
    DELETE /_localstack/clouds/<cloud>/stack/services/<service>
    POST   /_localstack/clouds/<cloud>/stack/reset

Resets are isolated per cloud — wiping Azure does not touch AWS / GCP state.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from localstack.platform.http import Request, Response

LOG = logging.getLogger(__name__)


def _json(payload: dict[str, Any] | list[Any], status: int = 200) -> Response:
    return Response(json.dumps(payload), status=status, mimetype="application/json")


def _err(message: str, status: int = 400) -> Response:
    return _json({"error": message}, status=status)


def _normalize(cloud: str | None) -> str:
    return (cloud or "").strip().lower()


# ---------------------------------------------------------------------------
# AWS inventory + reset
# ---------------------------------------------------------------------------


def _aws_inventory() -> list[dict[str, Any]]:
    """Best-effort inventory derived from Moto backends — one entry per service."""
    services: dict[str, dict[str, Any]] = {}
    try:
        from moto import backends as moto_backends
    except Exception:
        LOG.debug("moto not available; AWS stack inventory empty")
        return []

    try:
        backend_iter = moto_backends.list_all_backends()
    except Exception:
        # Older moto: list_backends() iterator returns (service, backend) pairs.
        try:
            backend_iter = moto_backends.list_backends()
        except Exception:
            LOG.exception("unable to enumerate moto backends")
            return []

    for entry in backend_iter:
        # Newer moto: (service_name, BackendDict)
        # Older moto: (service_name, account_dict)
        try:
            name, backend = entry
        except (TypeError, ValueError):
            continue
        try:
            count = _count_moto_resources(backend)
        except Exception:
            count = 0
        services[name] = {
            "service": name,
            "resource_count": count,
        }
    return sorted(services.values(), key=lambda s: s["service"])


def _count_moto_resources(backend: Any) -> int:
    """Walk one Moto backend dict and count `regions * resources_per_region` heuristically."""
    total = 0
    # backend is typically a {account_id: {region: BaseBackend}} mapping
    try:
        for account_value in backend.values():
            if not hasattr(account_value, "values"):
                continue
            for region_backend in account_value.values():
                total += _count_region_resources(region_backend)
    except Exception:
        return total
    return total


def _count_region_resources(region_backend: Any) -> int:
    candidates = (
        "buckets",
        "queues",
        "topics",
        "tables",
        "functions",
        "instances",
        "log_groups",
        "users",
        "secrets",
        "keys",
        "stacks",
        "repositories",
        "hosted_zones",
        "rest_apis",
        "state_machines",
        "event_buses",
        "streams",
        "parameters",
        "clusters",
        "db_instances",
        "vpcs",
    )
    seen = 0
    for attr in candidates:
        try:
            value = getattr(region_backend, attr, None)
        except Exception:
            continue
        if value is None:
            continue
        try:
            seen += len(value)
        except TypeError:
            continue
    return seen


def _aws_reset_service(service: str) -> dict[str, Any]:
    try:
        from moto import backends as moto_backends
    except Exception:
        return {"reset": [], "error": "moto unavailable"}

    cleared = 0
    try:
        backend_dict = moto_backends.get_backend(service)
    except Exception:
        return {"reset": [], "error": f"unknown moto backend: {service}"}

    cleared += _reset_backend_dict(backend_dict)
    return {"reset": [service], "regions_cleared": cleared}


def _aws_reset_all() -> dict[str, Any]:
    try:
        from moto import backends as moto_backends
    except Exception:
        return {"reset": [], "error": "moto unavailable"}

    services: list[str] = []
    regions_cleared = 0
    try:
        for name, backend in moto_backends.list_all_backends():
            services.append(name)
            regions_cleared += _reset_backend_dict(backend)
    except Exception:
        LOG.exception("AWS reset_all failed")
    # Native LocalStack services that maintain their own stores
    regions_cleared += _aws_reset_native_stores()
    return {"reset": sorted(services), "regions_cleared": regions_cleared}


def _reset_backend_dict(backend_dict: Any) -> int:
    cleared = 0
    try:
        for account_value in backend_dict.values():
            if not hasattr(account_value, "values"):
                continue
            for region_backend in account_value.values():
                try:
                    region_backend.reset()
                    cleared += 1
                except Exception:
                    continue
    except Exception:
        pass
    return cleared


def _aws_reset_native_stores() -> int:
    """Best-effort reset for LocalStack-native AWS services (Lambda, SQS native, etc.)."""
    cleared = 0
    try:
        from localstack.aws.services.plugins import SERVICE_PLUGINS

        for name, _state in SERVICE_PLUGINS.get_states().items():
            try:
                container = SERVICE_PLUGINS.get_service_container(name)
                provider = getattr(container, "provider", None)
                if provider is None:
                    continue
                before = getattr(provider, "on_before_state_reset", None)
                after = getattr(provider, "on_after_state_reset", None)
                if callable(before):
                    before()
                # Clear all visible stores attribute names.
                for attr in dir(provider):
                    if not attr.endswith("_stores") and attr != "stores":
                        continue
                    try:
                        target = getattr(provider, attr)
                        clear = getattr(target, "reset", None) or getattr(target, "clear", None)
                        if callable(clear):
                            clear()
                            cleared += 1
                    except Exception:
                        continue
                if callable(after):
                    after()
            except Exception:
                continue
    except Exception:
        LOG.debug("native AWS reset skipped", exc_info=True)
    return cleared


# ---------------------------------------------------------------------------
# Azure / GCP inventory + reset (delegated to their gateways)
# ---------------------------------------------------------------------------


def _get_cloud_gateway(cloud: str):
    from localstack.cloud.builtin import register_builtins
    from localstack.cloud.registry import registry

    if len(registry) == 0:
        register_builtins(registry)
    provider = registry.get(cloud)
    if provider is None:
        return None
    try:
        return provider.build_gateway()
    except Exception:
        LOG.exception("failed to build gateway for cloud %s", cloud)
        return None


def _azure_inventory(gateway: Any) -> list[dict[str, Any]]:
    if gateway is None:
        return []
    out: list[dict[str, Any]] = []

    rg_total = 0
    res_by_type: dict[str, int] = {}
    try:
        subs = getattr(gateway.stores, "_subscriptions", None)
        if subs is not None:
            for sub_store in subs.values():
                rg_total += len(getattr(sub_store, "resource_groups", {}) or {})
                for r in (getattr(sub_store, "resources", {}) or {}).values():
                    rtype = getattr(r, "type", "Microsoft.Unknown") or "Microsoft.Unknown"
                    res_by_type[rtype] = res_by_type.get(rtype, 0) + 1
    except Exception:
        pass

    if rg_total:
        out.append({"service": "Microsoft.Resources", "resource_count": rg_total})
    for rtype, count in res_by_type.items():
        ns = rtype.split("/", 1)[0]
        out.append({"service": ns, "resource_count": count, "azure_type": rtype})

    storage_data = getattr(getattr(gateway, "storage_provider", None), "data_store", None)
    if storage_data is not None:
        try:
            n = len(storage_data.containers) + len(storage_data.queues)  # type: ignore[attr-defined]
            if n:
                out.append({"service": "Storage.DataPlane", "resource_count": n})
        except Exception:
            pass

    fr = getattr(gateway, "functions_registry", None)
    if fr is not None:
        try:
            n = len(getattr(fr, "_apps", {}) or {})
            if n:
                out.append({"service": "Microsoft.Web.Functions", "resource_count": n})
        except Exception:
            pass

    return sorted(out, key=lambda s: s["service"])


def _azure_reset_service(gateway: Any, service: str) -> dict[str, Any]:
    if gateway is None:
        return {"reset": [], "error": "azure gateway unavailable"}
    cleared = 0
    subs = getattr(gateway.stores, "_subscriptions", None)
    if subs is not None:
        for sub_store in subs.values():
            if service == "Microsoft.Resources":
                cleared += len(sub_store.resource_groups)
                sub_store.resource_groups.clear()
            elif service.startswith("Microsoft."):
                # delete resources whose type's namespace matches `service`
                to_drop = [
                    k
                    for k, v in (sub_store.resources or {}).items()
                    if (getattr(v, "type", "") or "").startswith(service)
                ]
                cleared += len(to_drop)
                for k in to_drop:
                    sub_store.resources.pop(k, None)
    return {"reset": [service], "items_cleared": cleared}


def _azure_reset_all(gateway: Any) -> dict[str, Any]:
    if gateway is None:
        return {"reset": [], "error": "azure gateway unavailable"}
    services: list[str] = []
    try:
        gateway.stores.clear()
        services.append("Microsoft.Resources")
    except Exception:
        LOG.exception("azure stores clear failed")
    for attr, name in (
        ("storage_provider", "Storage.DataPlane"),
        ("cosmos_provider", "Microsoft.DocumentDB"),
    ):
        prov = getattr(gateway, attr, None)
        if prov is None:
            continue
        data = getattr(prov, "data_store", None)
        if data is None:
            continue
        try:
            for clear_attr in ("containers", "queues", "tables", "blobs", "databases"):
                target = getattr(data, clear_attr, None)
                if target is None:
                    continue
                try:
                    target.clear()
                except Exception:
                    continue
            services.append(name)
        except Exception:
            continue
    fr = getattr(gateway, "functions_registry", None)
    if fr is not None:
        try:
            getattr(fr, "_apps", {}).clear()
            services.append("Microsoft.Web.Functions")
        except Exception:
            pass
    return {"reset": services}


def _gcp_inventory(gateway: Any) -> list[dict[str, Any]]:
    if gateway is None:
        return []
    out: list[dict[str, Any]] = []
    projects = getattr(gateway.stores, "_projects", None)
    if projects is not None:
        by_type: dict[str, int] = {}
        for proj_store in projects.values():
            for r in (getattr(proj_store, "resources", {}) or {}).values():
                rtype = getattr(r, "resource_type", "unknown") or "unknown"
                by_type[rtype] = by_type.get(rtype, 0) + 1
        for rtype, count in by_type.items():
            out.append({"service": rtype, "resource_count": count})

    for attr, label in (
        ("storage_provider", "storage"),
        ("pubsub_provider", "pubsub"),
        ("firestore_provider", "firestore"),
        ("iam_provider", "iam"),
    ):
        prov = getattr(gateway, attr, None)
        data = getattr(prov, "data", None) if prov else None
        if data is None:
            continue
        n = 0
        for collection_attr in (
            "buckets",
            "topics",
            "subscriptions",
            "databases",
            "service_accounts",
            "keys",
        ):
            value = getattr(data, collection_attr, None)
            if value is None:
                continue
            try:
                n += len(value)
            except TypeError:
                continue
        if n:
            out.append({"service": label, "resource_count": n})

    fp = getattr(gateway, "functions_provider", None)
    if fp is not None:
        reg = getattr(fp, "registry", None)
        if reg is not None:
            try:
                n = len(reg)
                if n:
                    out.append({"service": "functions", "resource_count": n})
            except TypeError:
                pass

    return sorted(out, key=lambda s: s["service"])


def _gcp_reset_service(gateway: Any, service: str) -> dict[str, Any]:
    if gateway is None:
        return {"reset": [], "error": "gcp gateway unavailable"}
    cleared = 0
    projects = getattr(gateway.stores, "_projects", None)
    if projects is not None:
        for proj_store in projects.values():
            to_drop = [
                k
                for k, v in (proj_store.resources or {}).items()
                if (getattr(v, "resource_type", "") or "") == service
            ]
            cleared += len(to_drop)
            for k in to_drop:
                proj_store.resources.pop(k, None)
    # data-plane providers keyed by short name
    attr_map = {
        "storage": "storage_provider",
        "pubsub": "pubsub_provider",
        "firestore": "firestore_provider",
        "iam": "iam_provider",
    }
    prov_attr = attr_map.get(service)
    if prov_attr:
        prov = getattr(gateway, prov_attr, None)
        data = getattr(prov, "data", None) if prov else None
        if data is not None:
            for collection_attr in (
                "buckets",
                "topics",
                "subscriptions",
                "databases",
                "service_accounts",
                "keys",
            ):
                target = getattr(data, collection_attr, None)
                if target is None:
                    continue
                try:
                    cleared += len(target)
                    target.clear()
                except Exception:
                    continue
    return {"reset": [service], "items_cleared": cleared}


def _gcp_reset_all(gateway: Any) -> dict[str, Any]:
    if gateway is None:
        return {"reset": [], "error": "gcp gateway unavailable"}
    services: list[str] = []
    try:
        gateway.stores.clear()
        services.append("resources")
    except Exception:
        LOG.exception("gcp stores clear failed")
    for attr, label in (
        ("storage_provider", "storage"),
        ("pubsub_provider", "pubsub"),
        ("firestore_provider", "firestore"),
        ("iam_provider", "iam"),
    ):
        prov = getattr(gateway, attr, None)
        data = getattr(prov, "data", None) if prov else None
        if data is None:
            continue
        for collection_attr in (
            "buckets",
            "topics",
            "subscriptions",
            "databases",
            "service_accounts",
            "keys",
        ):
            target = getattr(data, collection_attr, None)
            if target is None:
                continue
            try:
                target.clear()
            except Exception:
                continue
        services.append(label)
    fp = getattr(gateway, "functions_provider", None)
    if fp is not None:
        reg = getattr(fp, "registry", None)
        if reg is not None:
            try:
                reg.clear()
                services.append("functions")
            except Exception:
                pass
    return {"reset": services}


# ---------------------------------------------------------------------------
# Resource classes wired into the localstack-internal router
# ---------------------------------------------------------------------------


class CloudStackResource:
    """GET /_localstack/clouds/<cloud>/stack — list services with resource counts."""

    def on_get(self, request: Request, cloud: str):
        cloud = _normalize(cloud)
        if cloud == "aws":
            services = _aws_inventory()
        elif cloud in ("azure", "gcp"):
            gw = _get_cloud_gateway(cloud)
            services = _azure_inventory(gw) if cloud == "azure" else _gcp_inventory(gw)
        else:
            return _err(f"unknown cloud: {cloud}", 404)

        total = sum(s.get("resource_count", 0) for s in services)
        return _json(
            {
                "cloud": cloud,
                "services": services,
                "total_resources": total,
                "total_services": len(services),
            }
        )


class CloudStackServiceResource:
    """DELETE /_localstack/clouds/<cloud>/stack/services/<service> — wipe one service."""

    def on_delete(self, request: Request, cloud: str, service: str):
        cloud = _normalize(cloud)
        if not service:
            return _err("service required", 400)
        if cloud == "aws":
            result = _aws_reset_service(service)
        elif cloud == "azure":
            gw = _get_cloud_gateway("azure")
            result = _azure_reset_service(gw, service)
        elif cloud == "gcp":
            gw = _get_cloud_gateway("gcp")
            result = _gcp_reset_service(gw, service)
        else:
            return _err(f"unknown cloud: {cloud}", 404)

        result.setdefault("cloud", cloud)
        result.setdefault("service", service)
        return _json(result)


class CloudStackResetResource:
    """POST /_localstack/clouds/<cloud>/stack/reset — wipe everything for one cloud."""

    def on_post(self, request: Request, cloud: str):
        cloud = _normalize(cloud)
        # Defensive: require an explicit confirm flag in the body to discourage
        # accidental destructive calls (the console always passes {"confirm": true}).
        try:
            body = request.get_json(force=True, silent=True) or {}
        except Exception:
            body = {}
        if not body.get("confirm"):
            return _err(
                "reset refused — body must include {\"confirm\": true}",
                status=400,
            )

        if cloud == "aws":
            result = _aws_reset_all()
        elif cloud == "azure":
            gw = _get_cloud_gateway("azure")
            result = _azure_reset_all(gw)
        elif cloud == "gcp":
            gw = _get_cloud_gateway("gcp")
            result = _gcp_reset_all(gw)
        else:
            return _err(f"unknown cloud: {cloud}", 404)

        result.setdefault("cloud", cloud)
        return _json(result)
