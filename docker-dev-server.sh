#!/bin/bash

build_error() {
    echo "Initial build error detected! Stopping."
    exit 1
}

echo "Running initial build..."
conda run --no-capture-output -n jupyter-book jupyter-book clean -a .
conda run --no-capture-output -n jupyter-book jupyter-book build . \
    || build_error

echo "Starting the live reload server..."
conda run --no-capture-output -n jupyter-book ./server.py
