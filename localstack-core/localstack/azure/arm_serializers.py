"""Serialize/deserialize Azure resources to/from ARM-style REST JSON."""

from __future__ import annotations

from typing import Any

from localstack.azure.exceptions import AzureInvalidRequest
from localstack.azure.stores import AzureGenericResource, AzureResourceGroup

RESOURCE_GROUP_TYPE = "Microsoft.Resources/resourceGroups"
_DEFAULT_PROVISIONING_STATE = {"provisioningState": "Succeeded"}
STORAGE_ACCOUNT_TYPE = "Microsoft.Storage/storageAccounts"


def _storage_primary_endpoints(account_name: str) -> dict[str, str]:
    # Host-based endpoints. Provider parses `<account>.<service>.<suffix>`
    # and expects "core.windows.net". Real DNS would point those hostnames
    # at Azure; locally we serve them via the TLS sidecar and a /etc/hosts
    # registration step (see bin/azure-register-host).
    return {
        "blob": f"https://{account_name}.blob.core.windows.net/",
        "queue": f"https://{account_name}.queue.core.windows.net/",
        "table": f"https://{account_name}.table.core.windows.net/",
        "file": f"https://{account_name}.file.core.windows.net/",
        "web": f"https://{account_name}.z13.web.core.windows.net/",
        "dfs": f"https://{account_name}.dfs.core.windows.net/",
        "internetEndpoints": {
            "blob": f"https://{account_name}.blob.core.windows.net/",
            "file": f"https://{account_name}.file.core.windows.net/",
            "web": f"https://{account_name}.z13.web.core.windows.net/",
            "dfs": f"https://{account_name}.dfs.core.windows.net/",
        },
        "microsoftEndpoints": {
            "blob": f"https://{account_name}.blob.core.windows.net/",
            "queue": f"https://{account_name}.queue.core.windows.net/",
            "table": f"https://{account_name}.table.core.windows.net/",
            "file": f"https://{account_name}.file.core.windows.net/",
            "web": f"https://{account_name}.z13.web.core.windows.net/",
            "dfs": f"https://{account_name}.dfs.core.windows.net/",
        },
    }


def _storage_account_defaults(account_name: str) -> dict[str, Any]:
    """Fields azurerm v3.x reads from `properties` for `azurerm_storage_account`."""
    endpoints = _storage_primary_endpoints(account_name)
    return {
        "primaryEndpoints": endpoints,
        "secondaryEndpoints": endpoints,
        "primaryLocation": "eastus",
        "secondaryLocation": "westus",
        "statusOfPrimary": "available",
        "statusOfSecondary": "available",
        "creationTime": "2024-01-01T00:00:00.000000Z",
        "accessTier": "Hot",
        "supportsHttpsTrafficOnly": True,
        "minimumTlsVersion": "TLS1_2",
        "allowBlobPublicAccess": True,
        "allowSharedKeyAccess": True,
        "allowCrossTenantReplication": False,
        "defaultToOAuthAuthentication": False,
        "publicNetworkAccess": "Enabled",
        "isHnsEnabled": False,
        "isLocalUserEnabled": True,
        "isNfsV3Enabled": False,
        "isSftpEnabled": False,
        "encryption": {
            "services": {
                "blob": {"enabled": True, "keyType": "Account"},
                "file": {"enabled": True, "keyType": "Account"},
                "queue": {"enabled": True, "keyType": "Service"},
                "table": {"enabled": True, "keyType": "Service"},
            },
            "keySource": "Microsoft.Storage",
            "requireInfrastructureEncryption": False,
        },
        "networkAcls": {
            "bypass": "AzureServices",
            "virtualNetworkRules": [],
            "ipRules": [],
            "defaultAction": "Allow",
        },
    }


def serialize_resource_group(rg: AzureResourceGroup) -> dict[str, Any]:
    return {
        "id": rg.id,
        "name": rg.name,
        "type": RESOURCE_GROUP_TYPE,
        "location": rg.location,
        "tags": dict(rg.tags),
        "properties": {**_DEFAULT_PROVISIONING_STATE, **rg.properties},
    }


def serialize_resource_group_list(items: list[AzureResourceGroup]) -> dict[str, Any]:
    return {"value": [serialize_resource_group(i) for i in items]}


def serialize_resource(res: AzureGenericResource) -> dict[str, Any]:
    body: dict[str, Any] = {
        "id": res.id,
        "name": res.name,
        "type": res.type,
        "tags": dict(res.tags),
        "properties": {**_DEFAULT_PROVISIONING_STATE, **res.properties},
    }
    if res.location is not None:
        body["location"] = res.location

    if res.type.lower() == STORAGE_ACCOUNT_TYPE.lower():
        # azurerm v3 reads sku/kind/identity from top-level on the response.
        defaults = _storage_account_defaults(res.name)
        body["properties"] = {**defaults, **body["properties"]}
        body.setdefault(
            "sku",
            res.properties.get("sku") or {"name": "Standard_LRS", "tier": "Standard"},
        )
        body.setdefault("kind", res.properties.get("kind") or "StorageV2")
        body.setdefault(
            "identity",
            res.properties.get("identity") or {"type": "None"},
        )

    return body


def serialize_resource_list(items: list[AzureGenericResource]) -> dict[str, Any]:
    return {"value": [serialize_resource(i) for i in items]}


def deserialize_resource_group_body(body: dict[str, Any]) -> dict[str, Any]:
    if not body or "location" not in body:
        raise AzureInvalidRequest("Resource group body requires 'location'")
    return {
        "location": body["location"],
        "tags": dict(body.get("tags") or {}),
        "properties": dict(body.get("properties") or {}),
    }


def deserialize_resource_body(body: dict[str, Any]) -> dict[str, Any]:
    if not body or "location" not in body:
        raise AzureInvalidRequest("Resource body requires 'location'")
    return {
        "location": body["location"],
        "tags": dict(body.get("tags") or {}),
        "properties": dict(body.get("properties") or {}),
    }
