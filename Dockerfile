# syntax=docker/dockerfile:1
FROM python:3.12.11-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:0.12.0 /uv /uvx /bin/

ENV UV_PYTHON_DOWNLOADS=0
WORKDIR /app

# Dependencies first, cached separately from source changes.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

COPY pyproject.toml uv.lock README.md ./
COPY src/ src/
COPY openapi/controller-spec.json openapi/controller-spec.json

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable

FROM python:3.12.11-slim

RUN groupadd --system omada && useradd --system --gid omada --home /app omada
WORKDIR /app

COPY --from=builder --chown=omada:omada /app/.venv /app/.venv
COPY --from=builder --chown=omada:omada /app/openapi/controller-spec.json openapi/controller-spec.json

ENV PATH="/app/.venv/bin:$PATH" \
    FASTMCP_TRANSPORT=http \
    FASTMCP_HOST=0.0.0.0 \
    FASTMCP_PORT=8000 \
    OMADA_MCP_SPEC_PATH=/app/openapi/controller-spec.json

USER omada
EXPOSE 8000

# OMADA_BASE_URL, OMADA_CLIENT_ID, OMADA_CLIENT_SECRET are required at
# runtime (docker run -e ...) - no defaults baked into the image.
CMD ["omada-mcp"]
