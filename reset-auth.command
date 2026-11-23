#!/bin/bash
# Double-click in Finder to forget the NAOSO login password, then set a new one in the app.
# Same logic as reset-auth.bat on Windows: tools/reset_auth.py.
cd "$(dirname "$0")" || exit 1
PY=".venv/bin/python"
[ -x "$PY" ] || PY="$(command -v python3)"
if [ -z "$PY" ]; then
  echo "Khong thay Python - hay cai NAOSO xong truoc. / Python not found - finish installing NAOSO first."
  exit 1
fi
"$PY" tools/reset_auth.py
echo ""
echo "Co the dong cua so nay. / You can close this window."
