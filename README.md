# omada-cli

Typed Python SDK for a TP-Link Omada SDN controller's Open API, generated
from the controller's own live OpenAPI spec, plus a thin auth shim for
Omada's non-standard client-credentials + `Authorization: AccessToken=`
flow (the spec declares no `securitySchemes`, so this has to be wired by
hand).

## Layout

- `src/omada_client/` — generated SDK (2446 operations). Don't hand-edit;
  regenerate instead.
- `src/omada_cli/auth.py` — `OmadaSession`: fetches `omadacId`, fetches and
  caches an access token, and builds an `AuthenticatedClient` for the
  generated SDK.
- `openapi/controller-spec.json` — the spec snapshot generation runs
  against, fetched from `https://<controller>:8043/v3/api-docs/00%20All`
  (no auth required).
- `scripts/regenerate.sh` — regenerate `src/omada_client` from the spec.
- `examples/get_radio_config.py` — minimal end-to-end example.

## Setup

```bash
uv sync
```

Credentials come from `OMADA_CLIENT_ID` / `OMADA_CLIENT_SECRET` (env, or a
`~/.omada.env` file as fallback) — see Settings → Open API in the Omada
controller UI to create a client-credentials app.

## Usage

```python
from omada_cli.auth import OmadaSession
from omada_client.api.ap import get_radios_config

session = OmadaSession(base_url="https://your-controller.local:8043", verify_ssl=False)
with session.client() as client:
    resp = get_radios_config.sync_detailed(
        omadac_id=session.omadac_id, site_id="...", ap_mac="...", client=client
    )
```

`OmadaSession` resolves `*.local` hostnames to IPv4 explicitly — httpx has
no happy-eyeballs fallback, and link-local IPv6 advertised over mDNS is
often unroutable.

## Regenerating the SDK

If the controller firmware changes:

```bash
curl -sk "https://your-controller.local:8043/v3/api-docs/00%20All" -o openapi/controller-spec.json
./scripts/regenerate.sh
```

## Tests

```bash
uv run python tests/test_auth.py
```
