# Changelog

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed
- `list_devices` returned HTTP 400 on a real controller: it called `GET /openapi/v1/{omadacId}/devices`, which is `searchGlobalDevice` and requires a `searchKey` query param. It now walks every site (paged) and calls `getDeviceList` per site with `page`/`pageSize`, tagging each device with `siteId` and `siteName`.
- `OmadaSession.request()` raised a bare `httpx.HTTPStatusError` on a 4xx/5xx, hiding the controller's own error. It now raises `RuntimeError` with the controller's `errorCode`, HTTP status, and `msg` (e.g. "Omada API error -1001 (HTTP 400) on <path>: Invalid request parameters."), or "HTTP <code>, non-JSON body" when the response isn't JSON. Never includes the access token.
- `build_request_path()` let a caller-supplied `omadacId` in `path_params` override the session's own id. An agent passing `omadacId=""` got "-7131 Controller ID not exist." It now always fills `omadacId` from the session.

## [0.1.0] - 2026-09-19

Initial release.

### Added
- MCP server exposing the Omada Open API via 7 meta-tools (`search_operations`, `get_operation_schema`, `call_operation`, `refresh_catalog`, `server_info`, `list_sites`, `list_devices`), instead of one tool per operation.
- Operation catalog built from the controller's own live OpenAPI spec at startup, with a bundled fallback snapshot.
- Typed Python SDK (`omada_client`), generated from the same spec.
- Auth shim (`omada_auth`) for Omada's non-standard client-credentials flow, with env var, `*_FILE` (Docker/K8s secrets), and `~/.omada.env` credential sources.
- Zero-trust controls on the HTTP transport: bearer token auth, rate limiting, DNS-rebinding/Host header protection, structured audit logging.
- Docker image with no install step at build time (dependencies resolved and scanned ahead of time).
- CI: tests, dependency scan (`pip-audit`), container image scan (Trivy), push to Docker Hub.
- MIT license.

[0.1.0]: https://github.com/samhaque/omada-controller-mcp/releases/tag/v0.1.0
