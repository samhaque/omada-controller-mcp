# Security and trust model

## Who can drive the Omada API through this server

`call_operation` can reach every cataloged operation, including destructive ones (device reboot, config changes). It does this using this server's own client-credentials session; it doesn't ask the MCP client to re-authenticate per call.

So: whoever can reach this server can drive the whole Omada API.

- **stdio** (local `uv run omada-mcp`): that's whoever can run this process. Same trust boundary as running the CLI/SDK directly.
- **HTTP** (the Docker/`docker compose` deployment): the container binds `0.0.0.0:8000`, so other machines on the LAN can reach it. That's the point, agents running elsewhere on your network can use it.

Without `OMADA_MCP_AUTH_TOKEN` set, that port is unauthenticated. Anything on the same LAN segment (a compromised IoT device, an unisolated guest-WiFi client) can drive the whole Omada API with no credential of its own.

Set `OMADA_MCP_AUTH_TOKEN` (see `.env.example`) before exposing this beyond `localhost`. `docker-compose.yml` refuses to start without it. It's a single shared-secret bearer token, not OAuth: enough to stop opportunistic LAN access, not a substitute for network segmentation if your LAN itself isn't trusted.

## Zero trust on an untrusted LAN

Don't trust the network. Verify every request. Log everything. Built in, on the HTTP transport:

- **Bearer token**, above. Constant-time comparison, so timing attacks don't leak it.
- **Rate limiting** (`RateLimitingMiddleware`), against brute force and request floods. Tune with `OMADA_MCP_RATE_LIMIT` (default 20 req/s).
- **DNS-rebinding / Host header protection**, FastMCP's built-in `host_origin_protection="auto"`, stops a malicious webpage's JS from using your browser as a proxy into your LAN. Lock it down further with `OMADA_MCP_ALLOWED_HOSTS`.
- **Audit logging** (`StructuredLoggingMiddleware`), every tool call with arguments goes to stderr as structured JSON.

Not built in: **transport encryption**. This server speaks plain HTTP, so the bearer token travels in cleartext unless you add TLS yourself:

- **Reverse proxy** (Caddy, nginx, Traefik) in front of it, terminating TLS. Caddy gets you automatic HTTPS in about 3 lines of Caddyfile.
- **Overlay network** (Tailscale, WireGuard) instead of exposing port 8000 to the LAN at all. Then "untrusted LAN" stops being the threat model.

Pick one if your LAN has devices you don't fully trust. On a small, single-user home network, the bearer token alone is a reasonable floor, not the ceiling.

## Credentials

Never hardcode `OMADA_CLIENT_ID` / `OMADA_CLIENT_SECRET`, and never pass them as CLI args (visible in `ps`/process listings). In priority order:

1. `OMADA_CLIENT_ID` / `OMADA_CLIENT_SECRET` env vars.
2. `OMADA_CLIENT_ID_FILE` / `OMADA_CLIENT_SECRET_FILE`, pointing at a file: the Docker/Kubernetes secrets convention, also works with a Vault agent or anything else that mounts a file.
3. `~/.omada.env`, as a last-resort local-dev fallback.

## Supply chain

CI runs a dependency scan (`pip-audit`) and a container image scan (Trivy, fails on fixable HIGH/CRITICAL) before every push to Docker Hub. See `.github/workflows/ci.yml`.

The Docker image doesn't install packages at build time. `scripts/build_venv_for_docker.sh` resolves and locks dependencies first, and the image ships exactly what was scanned.
