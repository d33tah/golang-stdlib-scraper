#!/bin/bash
set -euo pipefail
mkdir -p cache
wget -O cache/std https://pkg.go.dev/std
python3 parse-tree.py cache/std | xargs -I{} -n1 bash -c 'wget -nv https://pkg.go.dev/{}@go1.18.1 -O cache/$( echo {} | tr / _ ) '
python3 parse-tree.py cache/std | xargs -I{} -n1 bash -c 'python3 render.py cache/$( echo {} | tr / _ ) || true ' > concatenated.html
