#!/usr/bin/env bash
# Builds .venv-docker for linux/x86_64 regardless of host OS. Run before docker build.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf .venv-docker
UV_PROJECT_ENVIRONMENT=.venv-docker uv sync \
    --locked --no-dev --no-editable \
    --python-platform x86_64-unknown-linux-gnu \
    --python 3.14
echo "Built .venv-docker (linux/x86_64, python 3.14) for docker build"
