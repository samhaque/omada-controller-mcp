#!/usr/bin/env bash
# Regenerate the Omada SDK client from openapi/controller-spec.json.
# Re-fetch the spec first if the controller firmware changed:
#   curl -sk "https://your-controller.local:8043/v3/api-docs/00%20All" -o openapi/controller-spec.json
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf src/omada_client /tmp/omada_client_gen
uvx openapi-python-client generate \
    --path openapi/controller-spec.json \
    --output-path /tmp/omada_client_gen \
    --meta none
rm -rf /tmp/omada_client_gen/.ruff_cache
mv /tmp/omada_client_gen src/omada_client
echo "Regenerated src/omada_client"
