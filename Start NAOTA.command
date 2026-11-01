#!/bin/bash
# Double-click in Finder to start NAOTA and open the dashboard.
cd "$(dirname "$0")" || exit 1
bash "bin/naota-start.sh"
echo ""
echo "NAOTA is running at http://127.0.0.1:7777"
echo "This window can be closed - the server keeps running in the background."
