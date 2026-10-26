#!/bin/sh
# Rebuild every release file in dist/ and site/ from work/: sh build/all.sh
set -e
cd "$(dirname "$0")/.."
python3 -I build/build_tree.py .
python3 -I build/apply_ecommerce.py .
python3 -I build/export.py .
