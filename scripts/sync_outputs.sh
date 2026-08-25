#!/usr/bin/env bash
# Copy notebook artefacts into the docs tree.
#
# MkDocs only serves files that live under docs/, and the notebook writes to
# output/. Rather than duplicate paths in the notebook, sync after each run:
#
#     ./scripts/sync_outputs.sh
#
# The copies are committed so the site can be built (or gh-deploy'd) from a
# clean checkout without first running the notebook.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

if ! compgen -G "output/*" > /dev/null; then
  echo "output/ is empty - run main.ipynb first (Kernel > Restart Kernel and Run All Cells)" >&2
  exit 1
fi

mkdir -p docs/assets docs/notebook
cp output/*.png output/*.csv docs/assets/
cp main.ipynb docs/notebook/main.ipynb

echo "synced $(ls output | wc -l | tr -d ' ') artefacts + main.ipynb into docs/"

# The Scenario lab reads its own JSON, derived from the same artefacts. --verify
# round-trips the recovered revenue/cost inputs back through the notebook's
# forward model, so a bad sync fails here rather than silently shipping a
# calculator that disagrees with the published tables.
python3 scripts/build_scenario_data.py --verify
