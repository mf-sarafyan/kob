#!/usr/bin/env bash
set -euo pipefail

if [ ! -f ".venv/bin/activate" ]; then
  echo "Virtual env not found. Run scripts/setup.sh first." >&2
  exit 1
fi

source .venv/bin/activate
streamlit run src/app.py


