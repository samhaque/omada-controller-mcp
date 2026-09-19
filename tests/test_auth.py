"""Self-check for the auth shim, no live controller required.

Run directly: uv run python tests/test_auth.py
"""

from __future__ import annotations

import httpx

from omada_cli.auth import OmadaSession

FAKE_OMADAC_ID = "7e2ec518acbd6bb74282eafcb4ce7aab"
FAKE_TOKEN = "AT-fake-token"


def _fake_handler(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/api/info":
        return httpx.Response(200, json={"errorCode": 0, "msg": "Success.", "result": {"omadacId": FAKE_OMADAC_ID}})
    if request.url.path == "/openapi/authorize/token":
        assert request.url.params["grant_type"] == "client_credentials"
        return httpx.Response(
            200,
            json={
                "errorCode": 0,
                "msg": "Open API Get Access Token successfully.",
                "result": {"accessToken": FAKE_TOKEN, "tokenType": "bearer", "expiresIn": 7200},
            },
        )
    raise AssertionError(f"unexpected request: {request.url}")


def _session() -> OmadaSession:
    session = OmadaSession.__new__(OmadaSession)
    session.base_url = "https://controller.test"
    session.verify_ssl = True
    session.client_id = "id"
    session.client_secret = "secret"
    session._omadac_id = None
    session._token = None
    session._token_expires_at = 0.0
    session._raw_client = lambda: httpx.Client(  # type: ignore[method-assign]
        base_url=session.base_url, transport=httpx.MockTransport(_fake_handler)
    )
    return session


def test_omadac_id_and_token():
    session = _session()
    assert session.omadac_id == FAKE_OMADAC_ID
    assert session.token == FAKE_TOKEN
    # cached, no re-fetch needed within expiry window
    assert session.token == FAKE_TOKEN


def test_authenticated_client_header():
    session = _session()
    client = session.client()
    assert client._base_url == "https://controller.test"
    headers = client.get_httpx_client().headers
    assert headers["Authorization"] == f"AccessToken={FAKE_TOKEN}"


if __name__ == "__main__":
    test_omadac_id_and_token()
    test_authenticated_client_header()
    print("ok")
