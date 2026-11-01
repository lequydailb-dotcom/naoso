#!/bin/bash
# Double-click in Finder to stop NAOTA.
cd "$(dirname "$0")" || exit 1
bash "bin/naota-stop.sh"
echo ""
echo "You can close this window."
