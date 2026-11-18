"""The Office page's AI cost tile shows money actually billed, not a plan's API-equivalent price.

    python tests/run.py office_ai_cost      (no network)

usage.json keeps Claude Code's own total_cost_usd (and Grok's) as `cost` even on a Pro/Max plan, so the tile once
read "$48, 81 calls" for a day that charged nothing. billed_day() counts only per-token API providers, plus Claude
Code when it is signed in with an API key; plan turns still count as calls, at $0."""
from _paths import ROOT, SERVER  # noqa: E402,F401
import json
import tempfile
from pathlib import Path

import usage_store

DAY = "2026-11-10"
BUCKET = {"cli|opus": {"in": 1, "out": 1, "turns": 60, "cost": 44.5},
          "grok|grok-4": {"in": 1, "out": 1, "turns": 5, "cost": 0.3},
          "anthropic-api|claude-haiku-4-5": {"in": 1, "out": 1, "turns": 14, "cost": 0.27},
          "deepseek|deepseek-chat": {"in": 1, "out": 1, "turns": 2, "cost": 0.03}}


def _with_usage(fn):
    old = usage_store._PATH
    with tempfile.TemporaryDirectory() as td:
        usage_store._PATH = Path(td) / "usage.json"
        usage_store._PATH.write_text(json.dumps({"days": {DAY: BUCKET}, "total": {}}), encoding="utf-8")
        try:
            return fn()
        finally:
            usage_store._PATH = old


def test_plan_turns_cost_nothing_but_still_count():
    r = _with_usage(lambda: usage_store.billed_day(DAY))
    assert r == {"cost": 0.3, "turns": 81, "plan_turns": 65}


def test_claude_code_on_an_api_key_is_real_money():
    r = _with_usage(lambda: usage_store.billed_day(DAY, claude_on_api_key=True))
    assert r["cost"] == 44.8 and r["plan_turns"] == 5 and r["turns"] == 81


def test_empty_day_is_zero():
    assert _with_usage(lambda: usage_store.billed_day("2026-01-01")) == {"cost": 0.0, "turns": 0, "plan_turns": 0}


def test_office_uses_billed_day_and_the_tile_says_plan():
    main = (SERVER / "main.py").read_text(encoding="utf-8")
    build = main.split("def _office_build(", 1)[1].split("\n\n\n", 1)[0]
    assert "usage_store.billed_day(" in build and "claude_auth.API_KEY" in build
    assert "usage_store.daily(" not in build
    js = (ROOT / "dashboard" / "office.js").read_text(encoding="utf-8")
    assert '"office.k_ai_plan"' in js
    for lang in ("vi", "en"):
        d = json.loads((ROOT / "dashboard" / "i18n" / (lang + ".json")).read_text(encoding="utf-8"))
        assert "{n}" in d["office.k_ai_plan"]
        assert "0" in d["office.k_ai_note"]
