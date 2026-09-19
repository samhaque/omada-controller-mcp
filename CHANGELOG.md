# Changelog

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project follows [Semantic Versioning](https://semver.org/).

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
