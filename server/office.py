"""Office page: what each department's digital staff is doing, read from the brain's own logs.

READ ONLY. Nothing here writes to the brain, calls a model or runs a job. Sources, all under the brain:

    agents/*.md                  staff (name, role, tags; the first tag is the department)
    Vanhanh/loops/*.md             loops (name, enabled, interval_min, quiet_hours, optional group)
    Vanhanh/loop-state.json        per loop: last_run, last_status, fail_streak, auto_paused_reason
    Vanhanh/loop-log/<day>.md      one "## [YYYY-MM-DD HH:MM] <slug> ..." block per run, with
                                 "**Kiểm chứng:** ✓/✗" when the run was verified
    Vanhanh/reminders.json         reminders (label, cron/repeat_min/due_at, status, error)
    Vanhanh/work-log.jsonl         one line per reminder run (ts, ref, title, status)
    Vanhanh/kanban.json            the task board (tasks waiting for the owner)
    Vanhanh/office.json            optional, written by the owner: {"targets": {"<job id>": runs/day}}

Rule for everything that leaves this module: no secret, token, key, chat id, script body or
server path. Free text (run summaries, pause reasons, errors) goes through `scrub()`.

The page shows text through i18n, so this module returns CODES (state, issue kind) and the owner's
own words (job names, tags), never sentences of its own.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, tzinfo
from pathlib import Path

try:
    import fastyaml  # the project's YAML reader (C loader when present); the line parser below covers a bare install
except Exception:  # noqa: BLE001
    fastyaml = None

# Departments every business has. A department with no staff and no job still shows, empty, so the
# owner sees the gap. Ids are stable; the page translates them. Tags that match one of these words
# land in that department; any other tag becomes a department of its own, named as the owner wrote it.
BASE_DEPTS = ["marketing", "sales", "care", "finance", "ops"]
DEPT_WORDS = {
    "marketing": ["marketing", "tiếp thị", "truyền thông", "content", "nội dung", "quảng cáo"],
    "sales": ["sales", "bán hàng", "kinh doanh", "chốt đơn"],
    "care": ["care", "support", "chăm khách", "cskh", "chăm sóc khách hàng", "hỗ trợ"],
    "finance": ["finance", "tài chính", "kế toán", "accounting"],
    "ops": ["ops", "operations", "vận hành", "hệ thống", "system"],
}
# A loop or reminder with no department written on it is placed by the words in its NAME. Order
# matters: "renew the Threads token" is operations, not marketing.
JOB_RULES = [
    ("ops", r"token|gia hạn|renew|sao lưu|backup|cập nhật|update|kết nối|connect|dọn|clean"),
    ("marketing", r"đăng|post|bài|reel|video|content|nội dung|quảng cáo|\bads?\b|fanpage|kênh|channel"),
    ("sales", r"đơn hàng|order|bán|sell|chốt|báo giá|quote"),
    ("care", r"khách|customer|zalo|tin nhắn|message|inbox|chăm|support|bình luận|comment"),
    ("finance", r"doanh thu|revenue|chi phí|cost|tiền|hoá đơn|hóa đơn|invoice|kế toán|thuế|tax"),
]
WAITING = re.compile(r"review|wait|block|approv|duyet|duyệt|owner", re.I)
VERIFY = re.compile(r"\*\*Kiểm chứng:\*\*\s*(✓|✗)\s*([^\n]*)")
RUN_HEAD = re.compile(r"^## \[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\] ([\w-]+)[^\n]*$", re.M)
MAX_TEXT = 600


# ---------- scrubbing ----------
_SECRET_KV = re.compile(r"(token|secret|api[_-]?key|password|passwd|bearer|mật khẩu|khoá|khóa)(\s*[:=]\s*)\S+", re.I)
_PATH = re.compile(r"(?:/opt|/home|/root|/etc|/var|/srv|/usr|/tmp|~/|[A-Za-z]:\\)[^\s'\"`),;]*")
_KEYLIKE = re.compile(r"\b(?:sk|pk|rk|ghp|gho|github_pat|xox[abp]|EAA[A-Za-z]*|AIza)[-_A-Za-z0-9]{12,}")
_LONG = re.compile(r"\b[A-Za-z0-9+/_=-]{32,}\b")
_CHAT_ID = re.compile(r"\b-?100\d{9,}\b|\bchat_id\b\S*", re.I)


def scrub(text, limit: int = MAX_TEXT) -> str:
    """Free text safe to show: secrets, key-like strings, chat ids and server paths are masked."""
    s = str(text or "")
    s = _SECRET_KV.sub(r"\1\2[…]", s)
    s = _PATH.sub("[…]", s)
    s = _KEYLIKE.sub("[…]", s)
    s = _LONG.sub("[…]", s)
    s = _CHAT_ID.sub("[…]", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= limit else s[: limit - 1] + "…"


# ---------- reading ----------
def _read(p: Path):
    try:
        return p.read_text(encoding="utf-8")
    except Exception:  # noqa: BLE001 - missing or unreadable: the caller reports the file as missing
        return None


def _json(p: Path):
    s = _read(p)
    if s is None:
        return None
    try:
        return json.loads(s)
    except Exception:  # noqa: BLE001
        return None


def frontmatter(md: str | None) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", md or "", re.S)
    if not m:
        return {}
    if fastyaml is not None:
        try:
            d = fastyaml.safe_load(m.group(1))
            return d if isinstance(d, dict) else {}
        except Exception:  # noqa: BLE001 - fall through to the line parser
            pass
    out, key = {}, None
    for line in m.group(1).split("\n"):
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and key:
            out.setdefault(key, [])
            if isinstance(out[key], list):
                out[key].append(item.group(1).strip().strip("'\""))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not kv:
            continue
        key, v = kv.group(1), kv.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            out[key] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        elif v == "":
            out[key] = []
        else:
            out[key] = v.strip("'\"")
    return out


def _as_list(v) -> list:
    if v is None or v == "":
        return []
    return [str(x) for x in v] if isinstance(v, list) else [str(v)]


def _truthy(v, default=True) -> bool:
    if v is None or v == "":
        return default
    return str(v).strip().lower() not in ("false", "no", "0", "off")


def dept_of_tag(tag: str) -> str:
    t = (tag or "").strip().lower()
    for d, words in DEPT_WORDS.items():
        if t in words:
            return d
    return tag.strip()


def dept_of_name(name: str) -> str:
    for d, pat in JOB_RULES:
        if re.search(pat, name or "", re.I):
            return d
    return ""


def parse_runs(text: str | None) -> list[dict]:
    """Run blocks of one loop-log day: {"day","hm","slug","verified": True/False/None,"note"}."""
    out = []
    if not text:
        return out
    heads = list(RUN_HEAD.finditer(text))
    for i, h in enumerate(heads):
        body = text[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        v = VERIFY.search(body)
        first = next((ln for ln in body.split("\n") if ln.strip()), "")
        out.append({"day": h.group(1), "hm": h.group(2) + ":" + h.group(3), "slug": h.group(4),
                    "verified": None if not v else v.group(1) == "✓",
                    "verify_note": scrub(v.group(2), 300) if v else "",
                    "note": scrub(first.replace("**", ""), 240)})
    return out


def _day_of(ts: float, tz: tzinfo) -> str:
    return datetime.fromtimestamp(ts, tz).strftime("%Y-%m-%d")


def _ts_of(day: str, hm: str, tz: tzinfo) -> float:
    try:
        return datetime.strptime(day + " " + hm, "%Y-%m-%d %H:%M").replace(tzinfo=tz).timestamp()
    except Exception:  # noqa: BLE001
        return 0.0


def _at(ts: float, tz: tzinfo, today: str) -> str:
    """"HH:MM" for today, "dd/mm HH:MM" otherwise, in the owner's time zone; "" when it never happened."""
    if not ts:
        return ""
    d = datetime.fromtimestamp(ts, tz)
    return d.strftime("%H:%M") if d.strftime("%Y-%m-%d") == today else d.strftime("%d/%m %H:%M")


def _in_quiet(hour: int, quiet) -> bool:
    m = re.match(r"^\s*(\d{1,2})\s*-\s*(\d{1,2})\s*$", str(quiet or ""))
    if not m:
        return False
    a, b = int(m.group(1)), int(m.group(2))
    return (a <= hour < b) if a < b else (hour >= a or hour < b)


# ---------- building the office ----------
def build(brain: Path, now: float, tz: tzinfo, day: str = "", gather=None) -> dict:
    """`gather(day)` -> (teams, tasks, runs) for handoffs(); the server passes it, tests may leave it out."""
    brain = Path(brain)
    nd = brain / "Vanhanh"
    today = _day_of(now, tz)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", day or ""):
        day = today

    files = {}
    reminders_raw = _json(nd / "reminders.json")
    files["reminders"] = reminders_raw is not None
    if isinstance(reminders_raw, dict):
        reminders = reminders_raw.get("reminders") or []
    else:
        reminders = reminders_raw if isinstance(reminders_raw, list) else []
    wl_text = _read(nd / "work-log.jsonl")
    files["work_log"] = wl_text is not None
    work = []
    for line in (wl_text or "").splitlines():
        try:
            x = json.loads(line)
            if isinstance(x, dict) and x.get("ts"):
                work.append(x)
        except Exception:  # noqa: BLE001 - one broken line does not hide the rest
            continue
    loop_state = _json(nd / "loop-state.json")
    files["loop_state"] = loop_state is not None
    loop_state = loop_state if isinstance(loop_state, dict) else {}
    kanban = _json(nd / "kanban.json")
    files["kanban"] = kanban is not None
    cfg = _json(nd / "office.json") or {}
    targets = cfg.get("targets") if isinstance(cfg.get("targets"), dict) else {}

    log_dir = nd / "loop-log"
    log_days = sorted(p.stem for p in log_dir.glob("*.md") if re.match(r"^\d{4}-\d{2}-\d{2}$", p.stem)) \
        if log_dir.is_dir() else []
    runs_by_day = {d: parse_runs(_read(log_dir / f"{d}.md")) for d in set([day] + log_days[-2:]) if d in log_days}
    runs_day = runs_by_day.get(day, [])

    depts: dict[str, dict] = {}

    def dept(did: str) -> dict:
        if did not in depts:
            depts[did] = {"id": did, "base": did in BASE_DEPTS, "staff": [], "jobs": [], "waiting": []}
        return depts[did]

    for d in BASE_DEPTS:
        dept(d)

    # staff
    adir = brain / "agents"
    if not adir.is_dir():
        adir = nd / "agents"
    for p in sorted(adir.glob("*.md")) if adir.is_dir() else []:
        fm = frontmatter(_read(p))
        tags = _as_list(fm.get("tags"))
        did = dept_of_tag(tags[0]) if tags else "system"
        dept(did)["staff"].append({"slug": p.stem, "name": scrub(fm.get("name") or p.stem, 80),
                                   "role": scrub(fm.get("role") or "", 160)})

    jobs = []

    # loops: a file in loops/, or a state left behind by a loop that was removed
    ldir = nd / "loops"
    loop_md = {p.stem: _read(p) for p in ldir.glob("*.md")} if ldir.is_dir() else {}
    for slug in sorted(set(loop_md) | set(loop_state)):
        fm = frontmatter(loop_md.get(slug))
        st = loop_state.get(slug) if isinstance(loop_state.get(slug), dict) else {}
        name = str(fm.get("name") or slug)
        written = fm.get("group") or (_as_list(fm.get("tags")) or [""])[0]
        did = dept_of_tag(written) if written else (dept_of_name(name + " " + slug) or "unsorted")
        mine = [r for r in runs_day if r["slug"] == slug]
        interval = 0
        try:
            interval = int(float(fm.get("interval_min") or 0))
        except Exception:  # noqa: BLE001
            interval = 0
        last = float(st.get("last_run") or 0)
        result = str(st.get("last_status") or st.get("last_summary") or "")
        paused = scrub(st.get("auto_paused_reason") or "", 300)
        streak = int(st.get("fail_streak") or 0)
        if slug not in loop_md:
            state = "removed"
        elif not _truthy(fm.get("enabled")):
            state = "off"
        elif paused:
            state = "paused"
        elif streak > 0 or result.startswith("✗"):
            state = "failed"
        elif not last:
            state = "never"
        elif interval and now - last > interval * 120 + 8 * 3600 \
                and not _in_quiet(datetime.fromtimestamp(now, tz).hour, fm.get("quiet_hours")):
            state = "late"
        else:
            state = "ok"
        jobs.append({"id": slug, "kind": "loop", "name": scrub(name, 120), "dept": did, "dept_guessed": not written,
                     "schedule": {"interval_min": interval, "quiet_hours": str(fm.get("quiet_hours") or "")},
                     "last_run": last, "result": scrub(result), "paused_reason": paused, "fail_streak": streak,
                     "state": state,
                     "day": {"runs": len(mine), "ok": sum(1 for r in mine if r["verified"] is True),
                             "fail": sum(1 for r in mine if r["verified"] is False)}})

    # reminders
    for r in reminders:
        if not isinstance(r, dict) or not r.get("id"):
            continue
        rid = str(r["id"])
        name = str(r.get("label") or (r.get("text") or "")[:60] or rid)
        runs = [x for x in work if x.get("ref") == rid]
        last_run = runs[-1] if runs else None
        mine = [x for x in runs if _day_of(float(x["ts"]), tz) == day]
        repeat = bool(r.get("cron") or float(r.get("repeat_min") or 0))
        status = str(r.get("status") or "")
        err = scrub(r.get("error") or "", 300)
        if status == "cancelled":
            state = "cancelled"
        elif status == "paused":
            state = "off"
        elif status == "done" and not repeat:
            state = "done"
        elif err or (last_run and last_run.get("status") == "fail"):
            state = "failed"
        elif not last_run and not r.get("fired_at"):
            state = "never"
        else:
            state = "ok"
        jobs.append({"id": rid, "kind": "reminder" if repeat else "once", "name": scrub(name, 120),
                     "dept": dept_of_name(name) or "unsorted", "dept_guessed": True,
                     "schedule": {"cron": str(r.get("cron") or ""), "repeat_min": float(r.get("repeat_min") or 0),
                                  "due_at": float(r.get("due_at") or 0) if str(r.get("due_at") or "").replace(".", "", 1).isdigit() else 0},
                     "last_run": float(last_run["ts"]) if last_run else float(r.get("fired_at") or 0),
                     "result": err or ("ok" if last_run and last_run.get("status") == "ok" else ("fail" if last_run else "")),
                     "paused_reason": "", "fail_streak": 0, "state": state,
                     "day": {"runs": len(mine), "ok": sum(1 for x in mine if x.get("status") == "ok"),
                             "fail": sum(1 for x in mine if x.get("status") == "fail")}})

    for j in jobs:
        j["last_at"] = _at(j["last_run"], tz, today)
        t = targets.get(j["id"])
        j["target"] = int(t) if isinstance(t, (int, float)) and t > 0 else None
        dept(j["dept"])["jobs"].append(j["id"])

    # the task board: tasks waiting for the owner
    tasks = kanban.get("tasks") if isinstance(kanban, dict) and isinstance(kanban.get("tasks"), list) else []
    waiting = [t for t in tasks if isinstance(t, dict) and WAITING.search(str(t.get("status") or t.get("column") or ""))]
    for t in waiting:
        tg = _as_list(t.get("tags"))
        did = dept_of_tag(tg[0]) if tg else (dept_of_name(str(t.get("title") or "")) or "unsorted")
        dept(did)["waiting"].append({"id": str(t.get("id") or ""), "title": scrub(t.get("title") or t.get("id") or "", 140)})

    # department light
    by_id = {j["id"]: j for j in jobs}
    live_states = ("ok", "failed", "paused", "late", "never")
    for d in depts.values():
        js = [by_id[i] for i in d["jobs"]]
        live = [j for j in js if j["state"] in live_states]
        if any(j["state"] in ("failed", "paused") for j in js):
            d["light"], d["status"] = "red", "broken"
        elif any(j["state"] == "late" for j in js):
            d["light"], d["status"] = "orange", "late"
        elif not d["staff"] and not live:
            d["light"], d["status"] = "grey", "empty"
        elif not live:
            d["light"], d["status"] = "grey", "idle"
        elif d["waiting"]:
            d["light"], d["status"] = "orange", "waiting"
        else:
            d["light"], d["status"] = "green", "ok"

    issues = []
    for j in jobs:
        if j["state"] == "paused":
            issues.append({"kind": "paused", "level": 0, "job": j["id"]})
        elif j["state"] == "failed":
            issues.append({"kind": "failed", "level": 1, "job": j["id"]})
        elif j["state"] == "late":
            issues.append({"kind": "late", "level": 2, "job": j["id"]})
        if j["target"] and day == today and j["day"]["ok"] < j["target"]:
            issues.append({"kind": "below_target", "level": 3, "job": j["id"]})
    stopped = [j for j in jobs if j["state"] in ("paused", "off")]
    for a in stopped:
        for b in jobs:
            if b is not a and b["state"] == "ok" and a["name"].lower() in b["name"].lower():
                issues.append({"kind": "twin_running", "level": 2, "job": b["id"], "other": a["id"]})
    if waiting:
        issues.append({"kind": "waiting", "level": 1, "count": len(waiting)})
    for d in depts.values():
        if d["status"] == "empty":
            issues.append({"kind": "dept_empty", "level": 4, "dept": d["id"]})
        elif d["status"] == "idle" and d["staff"]:
            issues.append({"kind": "dept_idle", "level": 4, "dept": d["id"], "count": len(d["staff"])})
    issues.sort(key=lambda x: x["level"])

    # activity: reminder runs and loop runs, newest first
    names = {j["id"]: j["name"] for j in jobs}
    feed = [{"ts": float(x["ts"]), "job": str(x.get("ref") or ""), "name": names.get(x.get("ref"), scrub(x.get("title") or "", 120)),
             "result": {"ok": "ok", "fail": "fail"}.get(x.get("status"), "other"), "note": ""} for x in work]
    for d, rs in runs_by_day.items():
        for r in rs:
            feed.append({"ts": _ts_of(r["day"], r["hm"], tz), "job": r["slug"], "name": names.get(r["slug"], r["slug"]),
                         "result": "verified_ok" if r["verified"] is True else ("verified_fail" if r["verified"] is False else "run"),
                         "note": r["note"]})
    feed.sort(key=lambda x: -x["ts"])
    # the replay of the chosen day: every run of that day, oldest first, with its clock time
    day_feed = sorted((dict(f) for f in feed if _day_of(f["ts"], tz) == day), key=lambda x: x["ts"])[:400]
    for f in day_feed:
        f["hm"] = datetime.fromtimestamp(f["ts"], tz).strftime("%H:%M")
    feed = feed[:30]
    for f in feed:
        f["at"] = _at(f["ts"], tz, today)

    days = sorted(set([today] + log_days + [_day_of(float(x["ts"]), tz) for x in work]), reverse=True)[:30]
    order = BASE_DEPTS + sorted(k for k in depts if k not in BASE_DEPTS and k not in ("system", "unsorted")) \
        + [k for k in ("system", "unsorted") if k in depts]
    return {
        "now": now, "day": day, "today": today, "days": days, "files": files,
        "depts": [depts[k] for k in order if k in depts],
        "jobs": jobs, "issues": issues, "feed": feed, "day_feed": day_feed,
        "handoffs": _handoffs_of(brain, now, tz, day, gather),
        "now_at": datetime.fromtimestamp(now, tz).strftime("%H:%M:%S"), "tz": str(getattr(tz, "key", "") or tz),
        "totals": {"runs": sum(j["day"]["runs"] for j in jobs), "fails": sum(j["day"]["fail"] for j in jobs),
                   "broken": sum(1 for j in jobs if j["state"] in ("failed", "paused")),
                   "waiting": len(waiting) if files["kanban"] else None,
                   "empty_depts": sum(1 for d in depts.values() if d["status"] == "empty")},
    }


def _handoffs_of(brain, now, tz, day, gather):
    if gather is None:
        return []
    try:
        teams, tasks, runs = gather(day)
        return handoffs(brain, now, tz, day, teams, tasks, runs)
    except Exception:  # noqa: BLE001 - a broken store never takes the whole page down
        return []


# ---------- what runs right now ----------
def live(brain: Path, now: float, tz: tzinfo, loop_now: dict | None, rem_now: dict | None,
         tasks: list | None, procs: list | None, team_now: list | None = None) -> dict:
    """Everything running at this second, oldest first, read only and scrubbed like build().

    loop_now = {"slug", "since"} of the loop iteration running, rem_now = {reminder id: started_at},
    tasks = the task-board cards (only "running" ones count), procs = shell work Vanhanh watches.
    Each item: {kind, id, name, since, since_at, secs}; `id` matches the job id in build() for
    loops and reminders, so the page can light the right desk.
    """
    brain = Path(brain)
    nd = brain / "Vanhanh"
    today = _day_of(now, tz)
    items = []

    def add(kind, iid, name, since, extra=None):
        since = float(since or 0)
        x = {"kind": kind, "id": str(iid or ""), "name": scrub(name or iid or "", 120), "since": since,
             "since_at": _at(since, tz, today), "secs": int(max(0.0, now - since)) if since else None}
        x.update(extra or {})
        items.append(x)

    slug = str((loop_now or {}).get("slug") or "")
    if slug:
        fm = frontmatter(_read(nd / "loops" / f"{slug}.md"))
        add("loop", slug, str(fm.get("name") or slug), (loop_now or {}).get("since"))

    if rem_now:
        raw = _json(nd / "reminders.json")
        rems = raw.get("reminders") if isinstance(raw, dict) else raw
        names = {str(r.get("id")): str(r.get("label") or (r.get("text") or "")[:60] or r.get("id"))
                 for r in (rems if isinstance(rems, list) else []) if isinstance(r, dict) and r.get("id")}
        for rid, since in rem_now.items():
            if str(rid) in names:   # only this brain's own reminders
                add("reminder", rid, names[str(rid)], since)

    names = staff_names(brain)
    for t in tasks or []:
        if isinstance(t, dict) and str(t.get("status") or "") == "running":
            to = _card_agent(t)
            add("task", t.get("id"), str(t.get("title") or t.get("id") or ""),
                t.get("updated_at") or t.get("created_at"),
                {"agent": scrub(names.get(to) or to, 60), "agent_slug": to})

    for x in team_now or []:
        s = x.get("step") or {}
        m = next((m for m in x.get("members") or [] if str(m.get("agent_key")) == str(s.get("agent_key"))), {})
        slug = _member_slug(m) if m else str(s.get("agent_key") or "")
        add("team", s.get("step_id"), str(s.get("brief") or ""), s.get("updated_at") or s.get("created_at"),
            {"agent": scrub(names.get(slug) or (m.get("identity") or {}).get("name") or slug, 60), "agent_slug": slug,
             "where": scrub((x.get("team") or {}).get("name") or "", 80)})

    for p in procs or []:
        if isinstance(p, dict):
            add("job", p.get("id"), str(p.get("mo_ta") or ""), p.get("bat_dau"))

    items.sort(key=lambda x: x["since"] or now)
    return {"now": now, "now_at": datetime.fromtimestamp(now, tz).strftime("%H:%M:%S"), "items": items}



# ---------- who handed what to whom ----------
OWNER = "owner"
_STEP_STATUS = {"queued": "waiting", "held": "waiting", "waiting": "waiting", "waiting_owner": "waiting",
                "running": "running", "done": "done", "continued": "done", "failed": "failed", "cancelled": "cancelled"}
_TASK_STATUS = {"running": "running", "done": "done", "cancelled": "cancelled", "archived": "done", "blocked": "failed"}


def staff_names(brain: Path) -> dict:
    """{slug: name} of the brain's assistants, from agents/*.md (old Vanhanh/agents/ as a fallback)."""
    brain = Path(brain)
    adir = brain / "agents"
    if not adir.is_dir():
        adir = brain / "Vanhanh" / "agents"
    out = {}
    for p in sorted(adir.glob("*.md")) if adir.is_dir() else []:
        out[p.stem] = str(frontmatter(_read(p)).get("name") or p.stem)
    return out


def _member_slug(m: dict) -> str:
    ident = m.get("identity") or {}
    return str(ident.get("slug") or m.get("slug_at_join") or m.get("agent_key") or "")


def _card_agent(task: dict) -> str:
    """Slug of the assistant a board card was given to: the "Giao việc" key first, then the router's pick."""
    k = str(task.get("idempotency_key") or "")
    if k.startswith("agent:"):
        parts = k[len("agent:"):].split(":")
        if len(parts) >= 2 and parts[1]:
            return parts[1]
    ag = (task.get("metadata") or {}).get("agent")
    return str((ag.get("slug") if isinstance(ag, dict) else ag) or "")


def handoffs(brain: Path, now: float, tz: tzinfo, day: str, teams: list | None, tasks: list | None,
             runs: list | None) -> list:
    """Every handoff of one day, oldest first: {kind, from, to, from_name, to_name, title, where, ts, hm, status}.

    teams = [{"team": row, "members": [...], "steps": [steps of that day], "titles": {task_id: title}}],
    tasks = task-board cards, runs = workflow runs (newest first). `from`/`to` are assistant slugs, so the page
    finds their desks, or "owner" for the person who runs the brain. Read only, scrubbed.
    """
    names = staff_names(brain)
    by_name = {v.strip().lower(): k for k, v in names.items()}
    t0 = _ts_of(day, "00:00", tz)
    t1 = t0 + 86400
    out = []

    def add(kind, frm, to, title, where, ts, status, fname="", tname=""):
        ts = float(ts or 0)
        if not (t0 <= ts < t1) or not to or frm == to:
            return
        out.append({"kind": kind, "from": frm, "to": to,
                    "from_name": scrub(names.get(frm) or fname or frm, 60) if frm != OWNER else "",
                    "to_name": scrub(names.get(to) or tname or to, 60) if to != OWNER else "",
                    "title": scrub(title, 160), "where": scrub(where, 80), "ts": ts,
                    "hm": datetime.fromtimestamp(ts, tz).strftime("%H:%M"), "status": status})

    for t in teams or []:
        team = t.get("team") or {}
        mem = {str(m.get("agent_key")): m for m in t.get("members") or []}
        slug = {k: _member_slug(m) for k, m in mem.items()}
        nm = {k: str((m.get("identity") or {}).get("name") or "") for k, m in mem.items()}
        leader = str(team.get("leader_key") or "")
        steps = t.get("steps") or []
        by_id = {s.get("step_id"): s for s in steps}
        planned = {s.get("task_id") for s in steps if s.get("kind") == "plan"}
        for s in steps:
            kind = s.get("kind")
            key = str(s.get("agent_key") or "")
            if kind == "work":
                src = leader if (s.get("task_id") in planned and leader) else ""
            elif kind == "help":
                src = str((by_id.get(s.get("parent_step")) or {}).get("agent_key") or "")
            else:
                continue
            frm = slug.get(src, src) if src else OWNER
            title = (t.get("titles") or {}).get(s.get("task_id")) or s.get("brief") or ""
            add("team", frm, slug.get(key, key), title, team.get("name") or "", s.get("created_at"),
                _STEP_STATUS.get(str(s.get("status") or ""), "waiting"), nm.get(src, ""), nm.get(key, ""))

    for task in tasks or []:
        if not isinstance(task, dict):
            continue
        to = _card_agent(task)
        if not to:
            continue
        cb = str(task.get("created_by") or "")
        frm = cb.rsplit(":", 1)[-1] if cb.startswith("agent:") else OWNER
        if frm != OWNER and frm not in names:
            frm = OWNER
        add("board", frm, to, task.get("title") or "", "", task.get("created_at"),
            _TASK_STATUS.get(str(task.get("status") or ""), "waiting"))

    for r in runs or []:
        if not isinstance(r, dict):
            continue
        steps = r.get("steps") or []
        start = float(r.get("started_at") or 0)
        last = len(steps) - 1
        prev = OWNER
        for i, s in enumerate(steps):
            nm_ = str(s.get("agent") or "")
            to = by_name.get(nm_.strip().lower(), nm_)
            if s.get("error"):
                status = "failed"
            elif i == last and r.get("status") == "running":
                status = "running"
            elif i == last and r.get("status") == "waiting":
                status = "waiting"
            else:
                status = "done"
            add("workflow", prev, to, r.get("name") or r.get("slug") or "", r.get("name") or "",
                start + i * 0.001, status, "", nm_)
            prev = to
    out.sort(key=lambda x: x["ts"])
    return out[-300:]



# ---------- teams talking and meeting right now ----------
TALK_ROLES = ("leader_reply", "member_reply", "member_volunteer", "plan", "synthesize", "work", "help")


def talk_view(brain: Path, talk: list | None) -> dict:
    """Who is talking in a team right now and which teams sit in the meeting room.

    talk = [{"team": row, "members": [...], "turn": {agent_key, role, engine_at}}] from active team turns.
    Returns {"talk": [{slug, name, role, team, since}], "meetings": [{team, leader, members: [slugs]}]}: a team
    meets while its leader plans the job (role "plan") or sums it up ("synthesize"); every active member sits in.
    """
    names = staff_names(brain)
    talking, meetings = [], {}
    for x in talk or []:
        team = x.get("team") or {}
        turn = x.get("turn") or {}
        mem = {str(m.get("agent_key")): m for m in x.get("members") or []}
        key = str(turn.get("agent_key") or "")
        slug = _member_slug(mem[key]) if key in mem else key
        role = str(turn.get("role") or "")
        if role not in TALK_ROLES or not slug:
            continue
        talking.append({"slug": slug, "name": scrub(names.get(slug) or ((mem.get(key) or {}).get("identity") or {}).get("name") or slug, 60),
                        "role": role, "team": scrub(team.get("name") or "", 80), "since": float(turn.get("engine_at") or 0)})
        if role in ("plan", "synthesize"):
            tid = str(team.get("team_id") or "")
            members = [_member_slug(m) for m in x.get("members") or [] if (m.get("status") or "active") == "active"]
            meetings[tid] = {"team": scrub(team.get("name") or "", 80), "leader": slug,
                             "members": [s for s in members if s]}
    return {"talk": talking, "meetings": list(meetings.values())}
