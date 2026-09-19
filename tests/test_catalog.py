"""Self-check for omada_mcp.catalog: build_catalog / search / build_request_path.

Run: uv run python tests/test_catalog.py
"""

from __future__ import annotations

import httpx

from omada_mcp import catalog as cat

FAKE_SPEC = {
    "info": {"version": "6.3.0.45"},
    "components": {
        "schemas": {
            "ClientPatch": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
            },
            "Node": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "children": {"type": "array", "items": {"$ref": "#/components/schemas/Node"}},
                },
            },
        }
    },
    "paths": {
        "/openapi/v1/{omadacId}/sites": {
            "get": {
                "operationId": "getSites",
                "summary": "List sites",
                "parameters": [
                    {"name": "omadacId", "in": "path", "required": True, "schema": {"type": "string"}},
                    {"name": "page", "in": "query", "required": True, "schema": {"type": "integer"}},
                ],
            }
        },
        "/openapi/v1/{omadacId}/site-list": {
            "get": {
                "operationId": "siteList",
                "summary": "Site list, alternate endpoint",
                "parameters": [
                    {"name": "omadacId", "in": "path", "required": True, "schema": {"type": "string"}}
                ],
            }
        },
        "/openapi/v1/{omadacId}/sites/{siteId}/clients/{clientMac}": {
            "patch": {
                "operationId": "patchClient",
                "summary": "Rename a client",
                "parameters": [
                    {"name": "omadacId", "in": "path", "required": True, "schema": {"type": "string"}},
                    {"name": "siteId", "in": "path", "required": True, "schema": {"type": "string"}},
                    {"name": "clientMac", "in": "path", "required": True, "schema": {"type": "string"}},
                ],
                "requestBody": {
                    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ClientPatch"}}}
                },
            }
        },
        "/openapi/v1/{omadacId}/sites/{siteId}/clients/{clientMac}/legacy": {
            "get": {"operationId": "legacyGetClient", "summary": "Old", "deprecated": True, "parameters": []}
        },
        "/openapi/v1/{omadacId}/topology/tree": {
            "post": {
                "operationId": "postTree",
                "summary": "Self-referencing topology tree",
                "parameters": [],
                "requestBody": {
                    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Node"}}}
                },
            }
        },
        "/openapi/v1/{omadacId}/firmware/upload": {
            "post": {
                "operationId": "uploadFirmware",
                "summary": "Non-JSON body",
                "parameters": [],
                "requestBody": {"content": {"multipart/form-data": {"schema": {"type": "string"}}}},
            }
        },
        "/openapi/v1/{omadacId}/no-id": {
            "get": {"summary": "Missing operationId, must be excluded", "parameters": []}
        },
        "/openapi/v1/msp/{mspId}/sites": {
            "get": {"operationId": "mspGetSites", "summary": "MSP sites", "parameters": []}
        },
        "/api/info": {"get": {"operationId": "getInfo", "summary": "unscoped, excluded", "parameters": []}},
    },
}


def test_build_catalog_filters_and_dereferences() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test")
    assert set(catalog.operations) == {
        "getSites",
        "siteList",
        "patchClient",
        "postTree",
        "uploadFirmware",
    }, "deprecated, MSP, unscoped, and operationId-less ops excluded"
    assert catalog.version == "6.3.0.45"

    patch = catalog.operations["patchClient"]
    assert patch.request_body_schema == {"type": "object", "properties": {"name": {"type": "string"}}}
    assert {p["name"] for p in patch.parameters} == {"siteId", "clientMac"}, "omadacId excluded (auto-filled)"


def test_build_catalog_include_deprecated() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test", include_deprecated=True)
    assert "legacyGetClient" in catalog.operations


def test_build_catalog_resolves_circular_ref_without_recursing_forever() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test")
    schema = catalog.operations["postTree"].request_body_schema
    assert schema is not None
    children_items = schema["properties"]["children"]["items"]
    assert children_items.get("note", "").startswith("circular"), "self-ref must terminate, not recurse forever"


def test_build_catalog_non_json_body_has_no_schema() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test")
    assert catalog.operations["uploadFirmware"].request_body_schema is None


def test_search_ranks_operation_id_match_first() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test")
    hits = cat.search(catalog, "client")
    assert [h["operation_id"] for h in hits] == ["patchClient"]

    # Three matches for "site": siteList's operationId starts with the query
    # (ranks first); getSites and patchClient both only match in path, tied
    # on that, so the second tie-break (shorter path first) decides between
    # them - proves both levels of the comparator, not just that search finds something.
    hits = cat.search(catalog, "site")
    assert [h["operation_id"] for h in hits] == ["siteList", "getSites", "patchClient"]


def test_build_request_path_fills_omadac_id_and_validates() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test")
    op = catalog.operations["patchClient"]
    path = cat.build_request_path(op, "OC123", {"siteId": "s1", "clientMac": "aa:bb"})
    assert path == "/openapi/v1/OC123/sites/s1/clients/aa%3Abb"

    try:
        cat.build_request_path(op, "OC123", {"siteId": "s1"})
        raise AssertionError("expected ValueError for missing clientMac")
    except ValueError as e:
        assert "clientMac" in str(e)


def test_build_request_path_rejects_traversal() -> None:
    catalog = cat.build_catalog(FAKE_SPEC, "test")
    op = catalog.operations["patchClient"]
    path = cat.build_request_path(
        op, "OC123", {"siteId": "../../msp/1/sites", "clientMac": "aa:bb"}
    )
    assert "%2F" in path, "the '/' in the malicious siteId must be percent-encoded, not a literal separator"
    # The real proof: build the actual request httpx would send and confirm
    # its resolved path still starts inside this operation's own template -
    # not e.g. "/openapi/authorize/token" or an MSP path.
    request = httpx.Client(base_url="https://controller.test").build_request("PATCH", path)
    assert str(request.url.path).startswith("/openapi/v1/OC123/sites/"), request.url


def test_build_request_path_unknown_path_param_in_template() -> None:
    # op.parameters doesn't declare siteId (malformed/mismatched spec), and
    # the caller doesn't supply it either, so the "missing required" check
    # (which only knows about declared params) doesn't catch it - .format()
    # must still fail clearly instead of raising a raw KeyError.
    op = cat.Operation(
        operation_id="broken",
        method="GET",
        path="/openapi/v1/{omadacId}/sites/{siteId}",
        summary="",
        deprecated=False,
        parameters=[],
        request_body_schema=None,
    )
    try:
        cat.build_request_path(op, "OC123", {})
        raise AssertionError("expected ValueError: path references {siteId} with no value supplied")
    except ValueError as e:
        assert "siteId" in str(e)


def test_build_call_kwargs() -> None:
    assert cat.build_call_kwargs(None, None) == {}
    assert cat.build_call_kwargs({}, None) == {}
    assert cat.build_call_kwargs(None, {}) == {"json": {}}, "body={} is meaningful, must not be dropped"
    assert cat.build_call_kwargs({"page": 1}, {"name": "x"}) == {"params": {"page": 1}, "json": {"name": "x"}}


def test_bundled_spec_loads_and_builds() -> None:
    path = cat._bundled_spec_path()
    assert path is not None, "expected to find openapi/controller-spec.json from the repo root"
    spec = cat._load_bundled_spec()
    assert spec is not None
    catalog = cat.build_catalog(spec, "bundled")
    assert len(catalog.operations) > 1000, "sanity check against the real controller spec"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok  {name}")
    print("all tests passed")
