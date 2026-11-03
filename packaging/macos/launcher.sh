#!/bin/bash
# ============================================================
# VANHANH.app (the one inside Vanhanh-macOS.dmg) - what a double-click runs.
#
# First run (no Vanhanh in ~/Vanhanh yet): opens Terminal on bootstrap.sh, which checks the Mac,
# installs what is missing and starts Vanhanh. Terminal on purpose: the first install takes
# minutes and may ask for the Mac password once, so the person must SEE what happens.
# Every run after that: bin/vanhanh-start.sh, which only opens the window when Vanhanh is already
# up and starts it first when it is not. It never restarts a running server.
#
# Unlike the in-repo "VANHANH.app" (which must stay inside the repo folder), this bundle can
# live in /Applications: it finds Vanhanh through VANHANH_HOME, default ~/Vanhanh.
# ============================================================
VANHANH_HOME="${VANHANH_HOME:-$HOME/Vanhanh}"
RES="$(cd "$(dirname "$0")/../Resources" && pwd)"

if [ -d "${VANHANH_HOME}/.git" ] && [ -x "${VANHANH_HOME}/.venv/bin/python" ] && [ -x "${VANHANH_HOME}/bin/vanhanh-start.sh" ]; then
  exec "${VANHANH_HOME}/bin/vanhanh-start.sh"
fi

# macOS asks once whether "VANHANH" may control Terminal. If the person clicks Don't Allow
# (or the prompt never shows), osascript fails and nothing would happen at all: fall back to
# putting the command on the clipboard, opening Terminal, and saying "paste it".
# Not `open -a Terminal bootstrap.sh`: a script copied off the downloaded .dmg carries the
# quarantine flag, and Gatekeeper blocks it when it is opened through LaunchServices.
if ! osascript - "${RES}/bootstrap.sh" "${VANHANH_HOME}" <<'AS' >/dev/null 2>&1
on run argv
  tell application "Terminal"
    activate
    do script "VANHANH_HOME=" & quoted form of (item 2 of argv) & " bash " & quoted form of (item 1 of argv)
  end tell
end run
AS
then
  # %q escapes spaces and quotes in a form both bash and zsh (the Terminal default) accept.
  printf 'VANHANH_HOME=%q bash %q\n' "${VANHANH_HOME}" "${RES}/bootstrap.sh" | pbcopy
  open -a Terminal
  osascript -e 'display alert "VANHANH" message "Terminal is open. Paste (Cmd+V) and press Enter to install VANHANH.\n\nTerminal da mo. Dan (Cmd+V) roi bam Enter de cai VANHANH."' >/dev/null 2>&1 || true
fi
