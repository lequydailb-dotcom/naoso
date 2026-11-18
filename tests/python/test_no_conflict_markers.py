"""No leftover merge-conflict markers in shipped code (1.46.1).

    python tests/run.py no_conflict_markers      (no network)

1.46.0 shipped a lone `=======` line in dashboard/chatbots.js. The browser refused the whole file, so the Chatbot
page broke for every install. This scans every shipped source file for a line that is only a conflict marker."""
from _paths import ROOT  # noqa: E402
import re

MARKER = re.compile(r"^(<{7}|={7}|>{7})( .*)?$", re.M)
DIRS = ("dashboard", "server", "system")
EXTS = {".js", ".mjs", ".py", ".html", ".css", ".json", ".yml", ".yaml"}


def test_no_conflict_markers_in_shipped_files():
    bad = []
    for d in DIRS:
        for p in (ROOT / d).rglob("*"):
            if p.suffix not in EXTS or not p.is_file() or "node_modules" in p.parts:
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
            for m in MARKER.finditer(text):
                bad.append("%s:%d" % (p.relative_to(ROOT), text.count("\n", 0, m.start()) + 1))
    assert not bad, "conflict markers left in: " + ", ".join(bad)


if __name__ == "__main__":
    test_no_conflict_markers_in_shipped_files()
    print("OK")
