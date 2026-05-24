"""Minimal Microsoft Graph mock for terraform-provider-azurerm.

The provider hits `GET /v1.0/servicePrincipals?$filter=appId eq '<client_id>'`
right after authentication to discover the object ID of the authenticated SP.
We synthesize a deterministic object ID per client_id so the lookup succeeds
without persisting any state.

Only the endpoints the provider actually depends on are implemented:
  * GET /v1.0/me
  * GET /v1.0/servicePrincipals?$filter=appId eq '<uuid>'
  * GET /v1.0/applications?$filter=appId eq '<uuid>'
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any
from urllib.parse import unquote

from werkzeug.wrappers import Request, Response

_FILTER_APPID_RE = re.compile(
    r"appId\s+eq\s+'(?P<app_id>[^']+)'", re.IGNORECASE
)
_BEARER_APPID_RE = re.compile(r'"appid"\s*:\s*"(?P<app_id>[^"]+)"')


def _json_response(payload: dict[str, Any], status: int = 200) -> Response:
    return Response(json.dumps(payload), status=status, mimetype="application/json")


def _object_id_for(app_id: str) -> str:
    """Deterministic v4-shaped UUID derived from app_id (so re-auth returns same id)."""
    digest = hashlib.sha256(app_id.encode()).hexdigest()
    return (
        f"{digest[0:8]}-{digest[8:12]}-{digest[12:16]}-"
        f"{digest[16:20]}-{digest[20:32]}"
    )


def _app_id_from_token(request: Request) -> str | None:
    auth = request.headers.get("Authorization", "")
    if not auth.lower().startswith("bearer "):
        return None
    token = auth[7:]
    parts = token.split(".")
    if len(parts) < 2:
        return None
    payload = parts[1]
    # base64url decode (add padding)
    payload += "=" * (-len(payload) % 4)
    try:
        import base64
        decoded = base64.urlsafe_b64decode(payload.encode()).decode("utf-8", "ignore")
    except Exception:
        return None
    m = _BEARER_APPID_RE.search(decoded)
    return m.group("app_id") if m else None


def _filter_app_id(query_string: str) -> str | None:
    qs = unquote(query_string or "")
    m = _FILTER_APPID_RE.search(qs)
    return m.group("app_id") if m else None


def _service_principal(app_id: str) -> dict[str, Any]:
    object_id = _object_id_for(app_id)
    return {
        "id": object_id,
        "appId": app_id,
        "displayName": f"LocalStack SP {app_id[:8]}",
        "servicePrincipalType": "Application",
        "accountEnabled": True,
        "appOwnerOrganizationId": "00000000-0000-0000-0000-000000000002",
        "appRoleAssignmentRequired": False,
        "servicePrincipalNames": [app_id, f"https://localstack/{app_id}"],
        "tags": [],
    }


def _application(app_id: str) -> dict[str, Any]:
    object_id = _object_id_for("app:" + app_id)
    return {
        "id": object_id,
        "appId": app_id,
        "displayName": f"LocalStack App {app_id[:8]}",
        "signInAudience": "AzureADMyOrg",
        "publisherDomain": "localstack.local",
    }


def _odata_list(kind: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "@odata.context": f"https://graph.microsoft.com/v1.0/$metadata#{kind}",
        "value": items,
    }


class GraphRouter:
    """WSGI handler for `/v1.0/*` and `/beta/*` Microsoft Graph paths."""

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self._dispatch(request)
        return response(environ, start_response)

    def _dispatch(self, request: Request) -> Response:
        path = request.path
        # Strip /v1.0 or /beta prefix.
        for prefix in ("/v1.0", "/beta"):
            if path.startswith(prefix + "/") or path == prefix:
                path = path[len(prefix):] or "/"
                break

        if path in ("/me", "/me/"):
            app_id = _app_id_from_token(request) or "00000000-0000-0000-0000-000000000001"
            return _json_response(
                {
                    "id": _object_id_for("user:" + app_id),
                    "displayName": "LocalStack User",
                    "userPrincipalName": f"localstack@{app_id[:8]}.onmicrosoft.com",
                }
            )

        if path in ("/servicePrincipals", "/servicePrincipals/"):
            app_id = _filter_app_id(request.query_string.decode("ascii", "ignore"))
            if not app_id:
                app_id = _app_id_from_token(request)
            items = [_service_principal(app_id)] if app_id else []
            return _json_response(_odata_list("servicePrincipals", items))

        if path in ("/applications", "/applications/"):
            app_id = _filter_app_id(request.query_string.decode("ascii", "ignore"))
            if not app_id:
                app_id = _app_id_from_token(request)
            items = [_application(app_id)] if app_id else []
            return _json_response(_odata_list("applications", items))

        # Single-object lookups like /servicePrincipals/{id}
        m = re.match(r"^/servicePrincipals/(?P<oid>[^/]+)$", path)
        if m:
            app_id = _app_id_from_token(request) or "00000000-0000-0000-0000-000000000001"
            sp = _service_principal(app_id)
            sp["id"] = m.group("oid")
            return _json_response(sp)

        m = re.match(r"^/applications/(?P<oid>[^/]+)$", path)
        if m:
            app_id = _app_id_from_token(request) or "00000000-0000-0000-0000-000000000001"
            app = _application(app_id)
            app["id"] = m.group("oid")
            return _json_response(app)

        return _json_response(
            {
                "error": {
                    "code": "Request_ResourceNotFound",
                    "message": f"graph endpoint {request.path} not emulated",
                }
            },
            status=404,
        )
