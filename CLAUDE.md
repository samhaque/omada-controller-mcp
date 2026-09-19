# CLAUDE.md

## Commands
- Tests (no pytest, plain assert scripts): `uv run python tests/test_auth.py` and `uv run python tests/test_catalog.py`
- Local dev: `uv sync`, then `uv run omada-mcp`
- Docker: `./scripts/build_venv_for_docker.sh` must run before `docker build` or `docker compose up --build`. The Dockerfile has no install step by design, it only copies `.venv-docker/lib/python3.14/site-packages` in. Skipping this step fails the build with "site-packages not found."
- Regenerate the SDK: `./scripts/regenerate.sh` (after refetching `openapi/controller-spec.json` from a live controller)

## Architecture
- `src/omada_client/` is machine-generated (openapi-python-client). Never hand-edit it, regenerate instead.
- `src/omada_mcp/server.py` exposes meta-tools (search/inspect/call/refresh/info) instead of one MCP tool per Omada operation (there are 2000+). Don't add per-endpoint tools.
- The operation catalog is built from the controller's live OpenAPI spec at startup, falling back to the bundled `openapi/controller-spec.json` only if the controller is unreachable.
- `.venv-docker` (built by `scripts/build_venv_for_docker.sh`) is always linux/amd64, even when built on macOS. Don't confuse it with the native `.venv` used for local dev.

## Environment
- Needs `OMADA_CLIENT_ID` / `OMADA_CLIENT_SECRET` (or their `_FILE` variants, or `~/.omada.env`) to run against a real controller. Without one reachable, the server falls back to the bundled spec snapshot, expected in a sandboxed environment, not a bug.
- `OMADA_MCP_AUTH_TOKEN` is required for the HTTP transport; unset is fine for stdio.

## Conventions
- Changelog: Keep a Changelog format in `CHANGELOG.md`, semver tags (`vX.Y.Z`).
