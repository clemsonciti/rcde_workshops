#!/bin/bash
 
 rm -Rf _build
source activate jupyter-book
jupyter-book build .

# https://jupyterbook.org/en/stable/publish/gh-pages.html

if [[ $1 == "pages" ]]
then
  ghp-import -n -p -f _build/html
fi
