#!/bin/bash

build_error() {
    echo "Build error detected! Stopping."
    exit 1
}

conda run --no-capture-output -n jupyter-book jupyter-book build . \
    || build_error

