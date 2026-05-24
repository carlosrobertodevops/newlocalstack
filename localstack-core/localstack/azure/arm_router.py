"""WSGI router exposing the Azure Resource Manager subset over HTTP."""

from __future__ import annotations

import json
import re
from typing import Any, Callable

from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response

# Real Azure ARM treats subscription path segments case-insensitively.
# Werkzeug routing is case-sensitive, so we normalize a few well-known
# segments before matching so /resourcegroups, /resourcegroups/, /SUBSCRIPTIONS,
# etc. all hit the registered routes.
_PATH_NORMALIZATIONS = (
    (re.compile(r"/subscriptions/", re.IGNORECASE), "/subscriptions/"),
    (re.compile(r"/resourcegroups(/|$)", re.IGNORECASE), r"/resourceGroups\1"),
    (re.compile(r"/providers/", re.IGNORECASE), "/providers/"),
)


def _normalize_path(path: str) -> str:
    for pattern, repl in _PATH_NORMALIZATIONS:
        path = pattern.sub(repl, path)
    return path


# Deterministic dummy 64-byte base64 keys for storage account listKeys.
_STORAGE_DUMMY_KEY_1 = (
    "TG9jYWxTdGFja0R1bW15U3RvcmFnZUtleTFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9"
)
_STORAGE_DUMMY_KEY_2 = (
    "TG9jYWxTdGFja0R1bW15U3RvcmFnZUtleTJBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9"
)

from localstack.azure.arm_serializers import (
    deserialize_resource_body,
    deserialize_resource_group_body,
    serialize_resource,
    serialize_resource_group,
    serialize_resource_group_list,
    serialize_resource_list,
)
from localstack.azure.exceptions import AzureInvalidRequest, AzureNotFound
from localstack.azure.resource_manager import ResourceManagerProvider
from localstack.azure.scope import AzureScope


def _json_response(payload: dict[str, Any], status: int = 200) -> Response:
    return Response(json.dumps(payload), status=status, mimetype="application/json")


def _error(code: str, message: str, status: int) -> Response:
    return _json_response({"error": {"code": code, "message": message}}, status=status)


class ArmRouter:
    """Minimal ARM REST surface for resource groups + generic resources."""

    def __init__(self, provider: ResourceManagerProvider) -> None:
        self.provider = provider
        self.url_map = Map(
            [
                Rule(
                    "/subscriptions/<sub>",
                    endpoint="subscription",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions",
                    endpoint="subscriptions",
                    methods=["GET"],
                ),
                Rule(
                    "/tenants",
                    endpoint="tenants",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/providers",
                    endpoint="providers",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/providers/<ns>",
                    endpoint="provider",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/providers/<ns>/register",
                    endpoint="provider_register",
                    methods=["POST"],
                ),
                Rule(
                    "/subscriptions/<sub>/providers/<ns>/unregister",
                    endpoint="provider_register",
                    methods=["POST"],
                ),
                Rule(
                    "/subscriptions/<sub>/locations",
                    endpoint="locations",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/resourceGroups",
                    endpoint="resource_groups",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/resourceGroups/<rg>",
                    endpoint="resource_group",
                    methods=["PUT", "GET", "DELETE"],
                ),
                Rule(
                    "/subscriptions/<sub>/providers/<ns>/<rtype>",
                    endpoint="resources_by_subscription",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/resourceGroups/<rg>/providers/<ns>/<rtype>",
                    endpoint="resources_by_type",
                    methods=["GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/resourceGroups/<rg>/providers/<ns>/<rtype>/<name>",
                    endpoint="resource",
                    methods=["PUT", "GET", "DELETE"],
                ),
                Rule(
                    "/subscriptions/<sub>/resourceGroups/<rg>/providers/<ns>/<rtype>/<name>/<action>",
                    endpoint="resource_action",
                    methods=["POST", "GET"],
                ),
                Rule(
                    "/subscriptions/<sub>/resourceGroups/<rg>/providers/<ns>/<rtype>/<name>/<sub_type>/<sub_name>",
                    endpoint="sub_resource",
                    methods=["GET", "PUT", "DELETE"],
                ),
            ]
        )

    # WSGI entrypoint
    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        original = environ.get("PATH_INFO", "")
        normalized = _normalize_path(original)
        if normalized != original:
            environ = {**environ, "PATH_INFO": normalized}
            request = Request(environ)
        adapter = self.url_map.bind_to_environ(environ)
        try:
            endpoint, values = adapter.match()
        except HTTPException as exc:
            return exc(environ, start_response)
        handler: Callable[..., Response] = getattr(self, f"_handle_{endpoint}")
        try:
            response = handler(request, **values)
        except AzureNotFound as exc:
            response = _error(self._notfound_code(exc), str(exc), 404)
        except AzureInvalidRequest as exc:
            response = _error("BadRequest", str(exc), 400)
        except json.JSONDecodeError as exc:
            response = _error("InvalidJson", f"request body is not valid JSON: {exc.msg}", 400)
        except NotFound:
            response = _error("NotFound", "route not found", 404)
        return response(environ, start_response)

    # -- handlers --

    _DEFAULT_LOCATIONS = (
        ("eastus", "East US"),
        ("eastus2", "East US 2"),
        ("westus", "West US"),
        ("westus2", "West US 2"),
        ("westus3", "West US 3"),
        ("westeurope", "West Europe"),
        ("northeurope", "North Europe"),
        ("brazilsouth", "Brazil South"),
    )

    def _serialize_provider(self, sub: str, spec_namespace: str, types: list) -> dict:
        return {
            "id": f"/subscriptions/{sub}/providers/{spec_namespace}",
            "namespace": spec_namespace,
            "registrationState": "Registered",
            "registrationPolicy": "RegistrationRequired",
            "resourceTypes": types,
        }

    def _all_providers(self, sub: str) -> list[dict]:
        by_ns: dict[str, list[dict]] = {}
        for spec in self.provider.registry.all():
            by_ns.setdefault(spec.namespace, []).append(
                {
                    "resourceType": spec.resource_type,
                    "locations": list(spec.locations) or [name for name, _ in self._DEFAULT_LOCATIONS],
                    "apiVersions": list(spec.api_versions),
                    "defaultApiVersion": spec.api_versions[0] if spec.api_versions else None,
                    "capabilities": "None",
                }
            )
        return [self._serialize_provider(sub, ns, types) for ns, types in by_ns.items()]

    def _handle_subscriptions(self, request: Request) -> Response:
        return _json_response({"value": [self._subscription_obj("00000000-0000-0000-0000-000000000000")]})

    def _handle_tenants(self, request: Request) -> Response:
        return _json_response(
            {
                "value": [
                    {
                        "id": "/tenants/00000000-0000-0000-0000-000000000002",
                        "tenantId": "00000000-0000-0000-0000-000000000002",
                        "displayName": "LocalStack Tenant",
                        "countryCode": "US",
                        "tenantCategory": "Home",
                    }
                ]
            }
        )

    def _subscription_obj(self, sub: str) -> dict:
        return {
            "id": f"/subscriptions/{sub}",
            "subscriptionId": sub,
            "tenantId": "00000000-0000-0000-0000-000000000002",
            "displayName": "LocalStack Subscription",
            "state": "Enabled",
            "subscriptionPolicies": {
                "locationPlacementId": "Public_2014-09-01",
                "quotaId": "Internal_2014-09-01",
                "spendingLimit": "Off",
            },
            "authorizationSource": "RoleBased",
        }

    def _handle_subscription(self, request: Request, *, sub: str) -> Response:
        return _json_response(self._subscription_obj(sub))

    def _handle_locations(self, request: Request, *, sub: str) -> Response:
        value = [
            {
                "id": f"/subscriptions/{sub}/locations/{name}",
                "subscriptionId": sub,
                "name": name,
                "displayName": display,
                "regionalDisplayName": f"(US) {display}",
                "metadata": {"regionType": "Physical", "regionCategory": "Recommended"},
            }
            for name, display in self._DEFAULT_LOCATIONS
        ]
        return _json_response({"value": value})

    def _handle_providers(self, request: Request, *, sub: str) -> Response:
        return _json_response({"value": self._all_providers(sub)})

    def _handle_provider(self, request: Request, *, sub: str, ns: str) -> Response:
        for prov in self._all_providers(sub):
            if prov["namespace"].lower() == ns.lower():
                return _json_response(prov)
        return _error("InvalidResourceNamespace", f"namespace {ns} not registered", 404)

    def _handle_provider_register(self, request: Request, *, sub: str, ns: str) -> Response:
        for prov in self._all_providers(sub):
            if prov["namespace"].lower() == ns.lower():
                return _json_response(prov)
        return _error("InvalidResourceNamespace", f"namespace {ns} not registered", 404)

    def _handle_resource_groups(self, request: Request, *, sub: str) -> Response:
        scope = AzureScope.for_subscription(sub)
        return _json_response(serialize_resource_group_list(self.provider.list_resource_groups(scope)))

    def _handle_resource_group(self, request: Request, *, sub: str, rg: str) -> Response:
        scope = AzureScope.for_subscription(sub)
        if request.method == "PUT":
            body = self._json_body(request)
            params = deserialize_resource_group_body(body)
            group = self.provider.create_or_update_resource_group(scope, rg, params)
            return _json_response(serialize_resource_group(group))
        if request.method == "GET":
            return _json_response(serialize_resource_group(self.provider.get_resource_group(scope, rg)))
        if request.method == "DELETE":
            self.provider.delete_resource_group(scope, rg)
            return Response(status=204)
        raise NotFound()

    def _handle_resources_by_type(
        self, request: Request, *, sub: str, rg: str, ns: str, rtype: str
    ) -> Response:
        scope = AzureScope.for_subscription(sub)
        type_filter = f"{ns}/{rtype}".lower()
        all_resources = self.provider.list_resources(scope, resource_group=rg)
        filtered = [r for r in all_resources if r.type.lower() == type_filter]
        return _json_response(serialize_resource_list(filtered))

    def _handle_resources_by_subscription(
        self, request: Request, *, sub: str, ns: str, rtype: str
    ) -> Response:
        scope = AzureScope.for_subscription(sub)
        type_filter = f"{ns}/{rtype}".lower()
        all_resources = self.provider.list_resources(scope)
        filtered = [r for r in all_resources if r.type.lower() == type_filter]
        return _json_response(serialize_resource_list(filtered))

    _STORAGE_SUB_DEFAULTS = {
        "fileservices": {
            "protocolSettings": {
                "smb": {
                    "versions": "SMB2.1;SMB3.0;SMB3.1.1",
                    "authenticationMethods": "NTLMv2;Kerberos",
                    "kerberosTicketEncryption": "RC4-HMAC;AES-256",
                    "channelEncryption": "AES-128-CCM;AES-128-GCM;AES-256-GCM",
                }
            },
            "cors": {"corsRules": []},
            "shareDeleteRetentionPolicy": {"enabled": False, "days": 0},
        },
        "blobservices": {
            "cors": {"corsRules": []},
            "deleteRetentionPolicy": {"enabled": False},
            "containerDeleteRetentionPolicy": {"enabled": False},
            "isVersioningEnabled": False,
            "changeFeed": {"enabled": False},
            "restorePolicy": {"enabled": False},
            "lastAccessTimeTrackingPolicy": {"enable": False},
        },
        "queueservices": {"cors": {"corsRules": []}},
        "tableservices": {"cors": {"corsRules": []}},
    }

    def _handle_sub_resource(
        self,
        request: Request,
        *,
        sub: str,
        rg: str,
        ns: str,
        rtype: str,
        name: str,
        sub_type: str,
        sub_name: str,
    ) -> Response:
        sub_lower = sub_type.lower()
        if (
            ns.lower() == "microsoft.storage"
            and rtype.lower() == "storageaccounts"
            and sub_lower in self._STORAGE_SUB_DEFAULTS
            and sub_name.lower() == "default"
        ):
            defaults = self._STORAGE_SUB_DEFAULTS[sub_lower]
            if request.method == "PUT":
                try:
                    body = self._json_body(request)
                except json.JSONDecodeError:
                    body = {}
                merged_props = {**defaults, **(body.get("properties") or {})}
            else:
                merged_props = defaults
            return _json_response(
                {
                    "id": (
                        f"/subscriptions/{sub}/resourceGroups/{rg}/providers/{ns}/{rtype}/{name}/{sub_type}/{sub_name}"
                    ),
                    "name": sub_name,
                    "type": f"{ns}/{rtype}/{sub_type}",
                    "properties": merged_props,
                }
            )
        if request.method == "DELETE":
            return Response(status=204)
        return _error("NotFound", f"sub-resource {sub_type}/{sub_name} not emulated", 404)

    def _handle_resource_action(
        self,
        request: Request,
        *,
        sub: str,
        rg: str,
        ns: str,
        rtype: str,
        name: str,
        action: str,
    ) -> Response:
        """Generic POST sub-action dispatcher (listKeys, regenerateKey, listAccountSas, ...)."""
        type_lower = f"{ns}/{rtype}".lower()
        action_lower = action.lower()

        if type_lower == "microsoft.storage/storageaccounts":
            if action_lower in ("listkeys", "regeneratekey"):
                return _json_response(
                    {
                        "keys": [
                            {
                                "keyName": "key1",
                                "value": _STORAGE_DUMMY_KEY_1,
                                "permissions": "FULL",
                                "creationTime": "2024-01-01T00:00:00.0000000Z",
                            },
                            {
                                "keyName": "key2",
                                "value": _STORAGE_DUMMY_KEY_2,
                                "permissions": "FULL",
                                "creationTime": "2024-01-01T00:00:00.0000000Z",
                            },
                        ]
                    }
                )
            if action_lower == "listaccountsas":
                return _json_response(
                    {
                        "accountSasToken": "?sv=2023-01-01&ss=bfqt&srt=sco&sp=rwdlacupx&se=2099-01-01T00:00:00Z&sig=localstack",
                    }
                )
            if action_lower == "listservicesas":
                return _json_response(
                    {
                        "serviceSasToken": "?sv=2023-01-01&sr=b&sp=r&se=2099-01-01T00:00:00Z&sig=localstack",
                    }
                )

        return _error("InvalidAction", f"action {action} not supported for {ns}/{rtype}", 404)

    def _handle_resource(
        self, request: Request, *, sub: str, rg: str, ns: str, rtype: str, name: str
    ) -> Response:
        scope = AzureScope.for_subscription(sub)
        resource_id = (
            f"/subscriptions/{sub}/resourceGroups/{rg}/providers/{ns}/{rtype}/{name}"
        )
        if request.method == "PUT":
            body = self._json_body(request)
            params = deserialize_resource_body(body)
            res = self.provider.create_or_update_resource(scope, resource_id, params)
            return _json_response(serialize_resource(res))
        if request.method == "GET":
            return _json_response(serialize_resource(self.provider.get_resource(scope, resource_id)))
        if request.method == "DELETE":
            self.provider.delete_resource(scope, resource_id)
            return Response(status=204)
        raise NotFound()

    # -- helpers --

    @staticmethod
    def _json_body(request: Request) -> dict[str, Any]:
        raw = request.get_data(as_text=True) or "{}"
        return json.loads(raw)

    @staticmethod
    def _notfound_code(exc: AzureNotFound) -> str:
        msg = str(exc).lower()
        if "resource group" in msg:
            return "ResourceGroupNotFound"
        return "ResourceNotFound"
