#!/usr/bin/env python3

import livereload


def should_ignore_file(path: str) -> bool:
    ignored_prefixes = ["_build/"]
    for prefix in ignored_prefixes:
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
server.serve(port=8080, host="0.0.0.0", root="./_build/html")
