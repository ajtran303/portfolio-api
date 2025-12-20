#!/usr/bin/env bash
# start.sh - Start script for Render deployment

# Exit immediately if a command exits with a non-zero status
set -e

# Optional: print each command before executing
set -x

# Run the FastAPI app with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port $PORT
