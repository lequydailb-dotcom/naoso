"""The logo stays cached, so a reload on a shaky network never shows a broken logo.

    python tests/run.py brand_logo_cache      (no network)

/brand-logo used to be cached 60 seconds only: every reload after a minute fetched it again, and when the server's
network dropped for a moment the start-up screen and the sidebar showed a broken image. The page now points at
/brand-logo?v=<version>.<logo file time>, a URL that changes whenever the logo does, and that URL is kept 30 days."""
from _paths import ROOT, SERVER  # noqa: E402,F401
import re

MAIN = (SERVER / "main.py").read_text(encoding="utf-8")


def test_page_points_every_logo_at_a_stamped_url():
    root = MAIN.split("async def root()", 1)[1].split("\n@app.", 1)[0]
    assert "_logo_stamp(ver)" in root
    pat = re.search(r"re\.sub\(r'(/brand-logo[^']*)'", root).group(1)
    html = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    out = re.sub(pat, "/brand-logo?v=1.2.3.99", html)
    in_use = len(re.findall(r'/brand-logo(?:\?v=[\w.]+)?"', html))      # every src/href, not the comment
    assert in_use >= 7 and out.count('/brand-logo?v=1.2.3.99"') == in_use
    assert not re.search(r'/brand-logo(\?v=(?!1\.2\.3\.99)[\w.]+)?"', out)


def test_stamped_logo_is_kept_long_and_bare_logo_stays_short():
    fn = MAIN.split("async def brand_logo(", 1)[1].split("\n\n\n", 1)[0]
    assert fn.startswith('v: str = ""')
    assert "2592000 if v else 60" in fn


def test_stamp_changes_with_the_logo_file(tmp_path, monkeypatch):
    import main as M
    f = tmp_path / "logo.png"
    f.write_bytes(b"x")
    import os
    os.utime(f, (1000, 1000))
    monkeypatch.setattr(M, "_current_logo_file", lambda: f)
    a = M._logo_stamp("1.25.5")
    os.utime(f, (2000, 2000))
    b = M._logo_stamp("1.25.5")
    assert a == "1.25.5.1000" and b == "1.25.5.2000"
    monkeypatch.setattr(M, "_current_logo_file", lambda: tmp_path / "missing.png")
    monkeypatch.setattr(M, "_DEFAULT_LOGO", tmp_path / "missing.png")
    assert M._logo_stamp("1.25.5") == "1.25.5"


if __name__ == "__main__":
    import sys
    try:
        import pytest
    except ImportError:
        print("bỏ qua: chưa cài pytest")
        sys.exit(0)
    sys.exit(pytest.main([__file__, "-q"]))
