"""Self-check for the auth shim, no live controller required.

Run directly: uv run python tests/test_auth.py
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

import httpx

from omada_auth.auth import OmadaSession, _env_or_file

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
    if request.url.path == "/openapi/v1/OC/sites":
        assert request.headers["Authorization"] == f"AccessToken={FAKE_TOKEN}"
        return httpx.Response(200, json={"errorCode": 0, "msg": "Success.", "result": {"siteList": []}})
    if request.url.path == "/openapi/v1/OC/fail":
        return httpx.Response(200, json={"errorCode": -1, "msg": "boom", "result": None})
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


def test_request_returns_result_and_raises_on_error_code():
    session = _session()
    result = session.request("GET", "/openapi/v1/OC/sites")
    assert result == {"siteList": []}

    try:
        session.request("GET", "/openapi/v1/OC/fail")
        raise AssertionError("expected RuntimeError for non-zero errorCode")
    except RuntimeError as e:
        assert "boom" in str(e)


def test_env_or_file_prefers_direct_env_var():
    os.environ["OMADA_TEST_SECRET"] = "direct-value"
    try:
        assert _env_or_file("OMADA_TEST_SECRET") == "direct-value"
    finally:
        del os.environ["OMADA_TEST_SECRET"]


def test_env_or_file_reads_file_when_direct_var_unset():
    os.environ.pop("OMADA_TEST_SECRET", None)
    with tempfile.TemporaryDirectory() as tmp:
        secret_path = Path(tmp) / "secret"
        secret_path.write_text("from-file-value\n")
        os.environ["OMADA_TEST_SECRET_FILE"] = str(secret_path)
        try:
            assert _env_or_file("OMADA_TEST_SECRET") == "from-file-value"
        finally:
            del os.environ["OMADA_TEST_SECRET_FILE"]


def test_session_reads_credentials_from_file_env_vars():
    with tempfile.TemporaryDirectory() as tmp:
        id_path = Path(tmp) / "client_id"
        secret_path = Path(tmp) / "client_secret"
        id_path.write_text("id-from-file\n")
        secret_path.write_text("secret-from-file\n")
        env_backup = {k: os.environ.get(k) for k in ("OMADA_CLIENT_ID", "OMADA_CLIENT_SECRET")}
        os.environ.pop("OMADA_CLIENT_ID", None)
        os.environ.pop("OMADA_CLIENT_SECRET", None)
        os.environ["OMADA_CLIENT_ID_FILE"] = str(id_path)
        os.environ["OMADA_CLIENT_SECRET_FILE"] = str(secret_path)
        try:
            session = OmadaSession(base_url="https://controller.test")
            assert session.client_id == "id-from-file"
            assert session.client_secret == "secret-from-file"
        finally:
            del os.environ["OMADA_CLIENT_ID_FILE"]
            del os.environ["OMADA_CLIENT_SECRET_FILE"]
            for k, v in env_backup.items():
                if v is not None:
                    os.environ[k] = v


if __name__ == "__main__":
    test_omadac_id_and_token()
    test_authenticated_client_header()
    test_request_returns_result_and_raises_on_error_code()
    test_env_or_file_prefers_direct_env_var()
    test_env_or_file_reads_file_when_direct_var_unset()
    test_session_reads_credentials_from_file_env_vars()
    print("ok")
