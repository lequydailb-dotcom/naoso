"""Interface language picker at the foot of the sidebar (1.46.1).

    python tests/run.py rail_lang_picker      (no network)

1.3.0 moved the picker into Settings only and the owner could no longer find where to switch Vietnamese and English.
It is back above the version line. This test keeps it from being dropped again without anyone noticing."""
from _paths import ROOT  # noqa: E402
import re

DASH = ROOT / "dashboard"


def _read(name):
    return (DASH / name).read_text(encoding="utf-8")


def test_picker_sits_in_the_sidebar_above_the_version_line():
    html = _read("index.html")
    rail = html.split('<nav', 1)[1].split('</nav>', 1)[0]
    assert 'id="railLangWrap" hidden' in rail and 'id="railLang"' in rail
    assert rail.index('id="railLangWrap"') < rail.index('id="railVersion"')
    assert 'data-i18n-aria="settings.ui_lang.title"' in rail


def test_picker_stays_hidden_until_filled_and_in_the_icon_only_rail():
    css = _read("console.css")
    assert re.search(r"\.rail-lang\[hidden\][^{]*\{\s*display:\s*none", css)
    assert re.search(r"\.rail\.collapsed \.rail-lang[^{]*\{\s*display:\s*none", css)


def test_picker_uses_the_same_list_and_save_path_as_settings():
    con = _read("console.js")
    block = con.split('document.getElementById("railLangWrap")', 1)[1][:1500]
    assert "uiLangChoices(s)" in block and "langs.length > 1" in block
    assert "NaotaI18n.setLang(sel.value)" in block
    assert 'saveSetting("locale", { ui_lang: uiLangForServer(sel.value, s) })' in block
    assert "wrap.hidden = false" in block


def test_both_pickers_follow_the_language_in_use():
    assert 'for (const id of ["railLang", "vpUiLang"])' in _read("console.js")


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("OK")
