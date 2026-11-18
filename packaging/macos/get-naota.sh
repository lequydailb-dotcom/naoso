#!/bin/bash
# ============================================================
# NAOTA - one-line install for macOS, no "cannot be opened" block
#
#   curl -fsSL https://raw.githubusercontent.com/vuongtex/naota/main/packaging/macos/get-naota.sh | bash
#
# Downloads the same Naota-macOS.dmg the website links to, copies NAOTA.app into
# Applications, then runs its first-time install right here in this Terminal window.
# Why no Gatekeeper prompt: macOS only checks files a browser saved (they carry a quarantine
# flag), and the app is not signed with an Apple Developer ID yet. A file curl downloads
# carries no such flag.
# ============================================================
set -euo pipefail

URL="https://github.com/vuongtex/naota/releases/download/desktop/Naota-macOS.dmg"
[ "$(uname -s)" = "Darwin" ] || { echo "This installer is for macOS. On Linux run ./install.sh from the repo."; exit 1; }

TMP="$(mktemp -d)"
MNT=""
cleanup() { [ -n "${MNT}" ] && hdiutil detach -quiet "${MNT}" 2>/dev/null; rm -rf "${TMP}"; }
trap cleanup EXIT

echo ""
echo "  NAOTA: dang tai bo cai... (downloading)"
curl -fL --progress-bar -o "${TMP}/Naota-macOS.dmg" "${URL}"
MNT="$(hdiutil attach -nobrowse -readonly "${TMP}/Naota-macOS.dmg" | awk -F'\t' '/\/Volumes\//{print $NF}')"
[ -d "${MNT}/NAOTA.app" ] || { echo "The disk image has no NAOTA.app"; exit 1; }

# /Applications when it is writable (an admin account), else ~/Applications.
DEST="/Applications"
[ -w "${DEST}" ] || { DEST="${HOME}/Applications"; mkdir -p "${DEST}"; }
# Replace only the app bundle; the brain lives in ~/Naota and is never touched here.
rm -rf "${DEST}/NAOTA.app"
cp -R "${MNT}/NAOTA.app" "${DEST}/"
xattr -dr com.apple.quarantine "${DEST}/NAOTA.app" 2>/dev/null || true
echo "  Da chep NAOTA vao ${DEST} (copied to ${DEST})"

APP="${DEST}/NAOTA.app"
if [ -d "${HOME}/Naota/.git" ] && [ -x "${HOME}/Naota/.venv/bin/python" ]; then
  echo "  Naota da cai san, dang mo... (already installed, opening)"
  open "${APP}"
  exit 0
fi
# First install in THIS window. stdin is the curl pipe, so give the installer the keyboard
# back: install.sh asks for the Naota admin account and may ask for the Mac password.
bash "${APP}/Contents/Resources/bootstrap.sh" < /dev/tty
