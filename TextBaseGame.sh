#!/bin/bash

# Resolve the project directory from this launcher so it works wherever the
# project folder is located.
APP_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"

cd "$APP_DIR" || {
    echo "Failed to enter directory: $APP_DIR"
    exit 1
}

exec python3 code/game_window.py
