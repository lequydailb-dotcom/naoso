#!/bin/bash
# Double-click in Finder to stop VANHANH.
cd "$(dirname "$0")" || exit 1
bash "bin/vanhanh-stop.sh"
echo ""
echo "You can close this window."
