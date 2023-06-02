#!/bin/bash

build_error() {
    echo "Build error detected!"
    kill_background_server 2>/dev/null || true
    echo "Stopped the server."
    exit 1
}

run_build() {
    conda run --no-capture-output -n jupyter-book jupyter-book build . \
        || build_error
    echo "Build complete!"
    echo "You can access this at http://localhost:8080."
}

echo "Running initial build..."
conda run --no-capture-output -n jupyter-book jupyter-book clean -a .
run_build

echo "Starting server..."
python3 -m http.server -d _build/html -b "0.0.0.0" 8080 &
SERVER_PID="$!"

kill_background_server() {
    echo "Exit signal detected; killing server..."
    kill -9 "$SERVER_PID"
    echo "Done. Goodbye!"
    exit
}

# Set a trap to kill all background processes when this exits.
trap kill_background_server SIGINT SIGTERM EXIT

echo "Watching for changes..."
inotifywait -m --event modify --format '%w' --exclude "^_build/.*$" . | \
    while read -r; do
        echo "Changes detected, rebuilding!"
        run_build
    done
