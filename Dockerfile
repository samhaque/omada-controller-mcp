# syntax=docker/dockerfile:1
# No installs here, run scripts/build_venv_for_docker.sh first.
FROM --platform=linux/amd64 python:3.14.7-slim

RUN groupadd --system omada && useradd --system --gid omada --home /app omada
RUN rm -rf /usr/local/lib/python3.14/site-packages/pip*
WORKDIR /app

COPY --chown=omada:omada .venv-docker/lib/python3.14/site-packages /app/site-packages
COPY --chown=omada:omada openapi/controller-spec.json openapi/controller-spec.json

ENV PYTHONPATH=/app/site-packages \
    FASTMCP_TRANSPORT=http \
    FASTMCP_HOST=0.0.0.0 \
    FASTMCP_PORT=8000 \
    OMADA_MCP_SPEC_PATH=/app/openapi/controller-spec.json

USER omada
EXPOSE 8000

# OMADA_BASE_URL, OMADA_CLIENT_ID, OMADA_CLIENT_SECRET set at runtime.
CMD ["python", "-m", "omada_mcp"]
