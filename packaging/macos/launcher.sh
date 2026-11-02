#!/bin/bash
# ============================================================
# NAOTA.app (the one inside Naota-macOS.dmg) - what a double-click runs.
#
# First run (no Naota in ~/Naota yet): opens Terminal on bootstrap.sh, which checks the Mac,
# installs what is missing and starts Naota. Terminal on purpose: the first install takes
# minutes and may ask for the Mac password once, so the person must SEE what happens.
# Every run after that: bin/naota-start.sh, which only opens the window when Naota is already
# up and starts it first when it is not. It never restarts a running server.
#
# Unlike the in-repo "NAOTA.app" (which must stay inside the repo folder), this bundle can
# live in /Applications: it finds Naota through NAOTA_HOME, default ~/Naota.
# ============================================================
NAOTA_HOME="${NAOTA_HOME:-$HOME/Naota}"
RES="$(cd "$(dirname "$0")/../Resources" && pwd)"

if [ -d "${NAOTA_HOME}/.git" ] && [ -x "${NAOTA_HOME}/.venv/bin/python" ] && [ -x "${NAOTA_HOME}/bin/naota-start.sh" ]; then
  exec "${NAOTA_HOME}/bin/naota-start.sh"
fi

# macOS asks once whether "NAOTA" may control Terminal. If the person clicks Don't Allow
# (or the prompt never shows), osascript fails and nothing would happen at all: fall back to
# putting the command on the clipboard, opening Terminal, and saying "paste it".
# Not `open -a Terminal bootstrap.sh`: a script copied off the downloaded .dmg carries the
# quarantine flag, and Gatekeeper blocks it when it is opened through LaunchServices.
if ! osascript - "${RES}/bootstrap.sh" "${NAOTA_HOME}" <<'AS' >/dev/null 2>&1
on run argv
  tell application "Terminal"
    activate
    do script "NAOTA_HOME=" & quoted form of (item 2 of argv) & " bash " & quoted form of (item 1 of argv)
  end tell
end run
AS
then
  # %q escapes spaces and quotes in a form both bash and zsh (the Terminal default) accept.
  printf 'NAOTA_HOME=%q bash %q\n' "${NAOTA_HOME}" "${RES}/bootstrap.sh" | pbcopy
  open -a Terminal
  osascript -e 'display alert "NAOTA" message "Terminal is open. Paste (Cmd+V) and press Enter to install NAOTA.\n\nTerminal da mo. Dan (Cmd+V) roi bam Enter de cai NAOTA."' >/dev/null 2>&1 || true
fi
