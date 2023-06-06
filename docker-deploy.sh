#!/bin/bash

if [ ! -f /.dockerenv ]; then
    echo "Docker environment not detected!"
    echo "This script should only be run from inside the Docker container."
    exit 1
fi

if [ -z "$DKR_GIT_NAME" ]; then
    echo "Must provide a value for DKR_GIT_NAME."
    exit 1
fi

if [ -z "$DKR_GIT_EMAIL" ]; then
    echo "Must provide a value for DKR_GIT_EMAIL."
    exit 1
fi

if [ ! -d /app/_build/html ]; then
    echo "Build output directory is missing! Abort."
    exit 1
fi

# These run inside the container and set global values within the container.
# Since ghp-import makes commits, we need this to be set.
git config --global user.name "$DKR_GIT_NAME"
git config --global user.email "$DKR_GIT_EMAIL"

# Run ghp-import, which will make the commits.
# Unlike the other build script, we do not push here.
# Pushing must be handled by makefile.
conda run --no-capture-output -n jupyter-book ghp-import  -n /app/_build/html
