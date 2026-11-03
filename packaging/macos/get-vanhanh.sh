#!/bin/bash
# ============================================================
# VANHANH - one-line install for macOS, no "cannot be opened" block
#
#   curl -fsSL https://raw.githubusercontent.com/lequydailb-dotcom/vanhanh/main/packaging/macos/get-vanhanh.sh | bash
#
# Downloads the same Vanhanh-macOS.dmg the website links to, copies VANHANH.app into
# Applications, then runs its first-time install right here in this Terminal window.
# Why no Gatekeeper prompt: macOS only checks files a browser saved (they carry a quarantine
# flag), and the app is not signed with an Apple Developer ID yet. A file curl downloads
# carries no such flag.
# ============================================================
set -euo pipefail

URL="https://github.com/lequydailb-dotcom/vanhanh/releases/download/desktop/Vanhanh-macOS.dmg"
[ "$(uname -s)" = "Darwin" ] || { echo "This installer is for macOS. On Linux run ./install.sh from the repo."; exit 1; }

TMP="$(mktemp -d)"
MNT=""
cleanup() { [ -n "${MNT}" ] && hdiutil detach -quiet "${MNT}" 2>/dev/null; rm -rf "${TMP}"; }
trap cleanup EXIT

echo ""
echo "  VANHANH: dang tai bo cai... (downloading)"
curl -fL --progress-bar -o "${TMP}/Vanhanh-macOS.dmg" "${URL}"
MNT="$(hdiutil attach -nobrowse -readonly "${TMP}/Vanhanh-macOS.dmg" | awk -F'\t' '/\/Volumes\//{print $NF}')"
[ -d "${MNT}/VANHANH.app" ] || { echo "The disk image has no VANHANH.app"; exit 1; }

# /Applications when it is writable (an admin account), else ~/Applications.
DEST="/Applications"
[ -w "${DEST}" ] || { DEST="${HOME}/Applications"; mkdir -p "${DEST}"; }
# Replace only the app bundle; the brain lives in ~/Vanhanh and is never touched here.
rm -rf "${DEST}/VANHANH.app"
cp -R "${MNT}/VANHANH.app" "${DEST}/"
xattr -dr com.apple.quarantine "${DEST}/VANHANH.app" 2>/dev/null || true
echo "  Da chep VANHANH vao ${DEST} (copied to ${DEST})"

APP="${DEST}/VANHANH.app"
if [ -d "${HOME}/Vanhanh/.git" ] && [ -x "${HOME}/Vanhanh/.venv/bin/python" ]; then
  echo "  Vanhanh da cai san, dang mo... (already installed, opening)"
  open "${APP}"
  exit 0
fi
# First install in THIS window. stdin is the curl pipe, so give the installer the keyboard
# back: install.sh asks for the Vanhanh admin account and may ask for the Mac password.
bash "${APP}/Contents/Resources/bootstrap.sh" < /dev/tty
