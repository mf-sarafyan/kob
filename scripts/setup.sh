#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.10+ not found." >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

if ! command -v ollama >/dev/null 2>&1; then
  echo "Ollama not found. Install from https://ollama.com" >&2
  exit 1
fi

ollama pull llama3.1:8b-instruct
ollama pull nomic-embed-text

echo "Setup complete."


