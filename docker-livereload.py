#!/usr/bin/env python3

import livereload


def should_ignore_file(path: str) -> bool:
    # Check for global ignored prefixes.
    global_ignored_prefixes = ["_build/", "."]
    for prefix in global_ignored_prefixes:
        if path.startswith(prefix):
            return True

    # If this is the root folder, ignore these prefixes also.
    root_ignored_prefixes = ["docker", "Docker", "Makefile"]
    if path.find("/") == -1:
        for prefix in root_ignored_prefixes:
            if path.startswith(prefix):
                return True

    return False


server = livereload.Server()
server.watch(
    "**",
    func=livereload.shell(
        "conda run --no-capture-output -n jupyter-book jupyter-book build .",
        cwd=".",
    ),
    ignore=should_ignore_file,
)
server.setHeader("Cache-Control", "no-cache, no-store, must-revalidate")
server.setHeader("Pragma", "no-cache")
server.setHeader("Expires", "0")
server.serve(port=8080, host="0.0.0.0", root="./_build/html")
