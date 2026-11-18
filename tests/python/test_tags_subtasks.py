"""My tasks get tags and subtasks.

Expected:
  - a task carries several tags; `project` stays equal to the first one, and an older store (one
    `project`, no `tags`) is read as tags = [project];
  - sending the old `project` field still works (sets one tag), sending `tags` wins over it;
  - deleting a tag takes it off every task, keeping their other tags; moving a task to another brain drops its tags;
  - `order_ids` puts the tags in that order (ones not listed after), through the HTTP route too;
  - subtasks are cleaned (blank ones dropped, names trimmed, at most 100);
  - a repeating task starts each occurrence with its subtasks open again, and unticking it puts them back;
  - the stats count a task under every tag it carries.

Run:
    python tests/python/test_tags_subtasks.py
"""
from _paths import ROOT, SERVER  # noqa: E402,F401  - puts server/ on sys.path (see tests/python/_paths.py)
import json
import tempfile
from pathlib import Path

from fastapi import FastAPI
from fastapi.testclient import TestClient

import my_tasks  # noqa: E402

fails = []
roots = {"brain": Path(tempfile.mkdtemp(prefix="naota-tag-a-")), "other": Path(tempfile.mkdtemp(prefix="naota-tag-b-"))}


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def atomic_write(path, text):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


feat = my_tasks.MyTasks(my_tasks.MyTasksDeps(brain_root=lambda b: str(roots.get(b, roots["brain"])),
                                             atomic_write_text=atomic_write))

# ---- an old store: one project, no tags ----
store = roots["brain"] / "Naota" / "my-tasks.json"
store.parent.mkdir(parents=True, exist_ok=True)
store.write_text(json.dumps({"tasks": [{"id": "m_old", "title": "Old", "project": "p_a", "status": "open"},
                                       {"id": "m_none", "title": "No project", "status": "open"}],
                             "projects": [{"id": "p_a", "name": "A", "color": "#ef4444", "order": 0}], "rev": 3}),
                 encoding="utf-8")
d = feat.load("brain")
check("an old task with a project reads as that one tag", feat._find(d, "m_old")["tags"] == ["p_a"])
check("an old task without a project reads with no tags", feat._find(d, "m_none")["tags"] == [])

# ---- an old store with every kind of field: nothing is lost on the way to tags ----
full_old = {"id": "m_full", "kind": "task", "title": "Full", "notes": "see [[note]]", "date": "2026-10-01", "time": "09:00",
            "end": "10:00", "repeat": {"unit": "week", "n": 1}, "project": "p_a", "status": "open", "done_at": 0,
            "done_dates": {"2026-10-08": {"at": 1, "by": "me"}}, "subs": [{"t": "x", "done": True}], "remind": "auto",
            "location": "HN", "habit": None, "created_at": 1, "updated_at": 2}
appt_old = {"id": "m_appt", "kind": "appt", "title": "Appt", "project": "p_gone", "status": "done", "done_at": 5}
old_store = roots["other"] / "Naota" / "my-tasks.json"
old_store.parent.mkdir(parents=True, exist_ok=True)
old_store.write_text(json.dumps({"tasks": [full_old, appt_old], "projects": [{"id": "p_a", "name": "A", "color": "#ef4444", "order": 0}],
                                 "rev": 7}), encoding="utf-8")
before = old_store.read_bytes()
d = feat.load("other")
check("reading an old store does not rewrite the file", old_store.read_bytes() == before)
got = feat._find(d, "m_full")
check("every old field survives on the way to tags", all(got.get(k) == v for k, v in full_old.items()) and got["tags"] == ["p_a"])
check("a project with no row any more still reads as a tag, nothing dropped", feat._find(d, "m_appt")["tags"] == ["p_gone"])
check("the projects stay as the tag list, same ids", [x["id"] for x in d["projects"]] == ["p_a"] and d["rev"] == 7)
feat.update("other", {"id": "m_full", "title": "Full 2"})
d = feat.load("other")
saved = json.loads(old_store.read_text(encoding="utf-8"))
check("after a save the file keeps project and gains tags", saved["tasks"][0]["project"] == "p_a" and saved["tasks"][0]["tags"] == ["p_a"])
check("after a save the other tasks are intact", saved["tasks"][1]["project"] == "p_gone" and saved["tasks"][1]["done_at"] == 5)
old_store.unlink()

b = feat.project("brain", {"name": "B"})["project"]["id"]
c = feat.project("brain", {"name": "C"})["project"]["id"]

# ---- several tags ----
t = feat.create("brain", {"title": "Write post", "tags": ["p_a", b, "p_a", "", b]})["task"]
check("tags keep their order, without duplicates or blanks", t["tags"] == ["p_a", b])
check("project mirrors the first tag", t["project"] == "p_a")
u = feat.update("brain", {"id": t["id"], "tags": [c, b]})["task"]
check("tags replaced, project follows", u["tags"] == [c, b] and u["project"] == c)
u = feat.update("brain", {"id": t["id"], "project": "p_a"})["task"]
check("the old project field sets a single tag", u["tags"] == ["p_a"] and u["project"] == "p_a")
u = feat.update("brain", {"id": t["id"], "tags": [b], "project": "p_a"})["task"]
check("tags win over project when both come", u["tags"] == [b])
u = feat.update("brain", {"id": t["id"], "tags": []})["task"]
check("clearing the tags clears project", u["tags"] == [] and u["project"] == "")
check("at most 20 tags on a task", len(my_tasks.clean_tags(["t%d" % i for i in range(40)])) == 20)

# ---- delete a tag ----
feat.update("brain", {"id": t["id"], "tags": [b, c]})
r = feat.project_delete("brain", b)
d = feat.load("brain")
check("deleting a tag lists the tasks that had it", t["id"] in r["tasks"])
check("deleting a tag keeps the task's other tags", feat._find(d, t["id"])["tags"] == [c] and feat._find(d, t["id"])["project"] == c)

# ---- reorder ----
e = feat.project("brain", {"name": "E"})["project"]["id"]
r = feat.project("brain", {"order_ids": [e, c]})
names = [x["id"] for x in sorted(feat.load("brain")["projects"], key=lambda x: x["order"])]
check("order_ids puts the listed tags first, in that order", names[:2] == [e, c] and "p_a" in names[2:])
check("order_ids gives each tag its place", [x["order"] for x in sorted(feat.load("brain")["projects"], key=lambda x: x["order"])] == list(range(len(names))))

# ---- move drops tags ----
m = feat.move("brain", "other", t["id"], copy=True)
check("a task copied to another brain has no tags", m["ok"] and m["task"]["tags"] == [] and m["task"]["project"] == "")

# ---- subtasks ----
u = feat.update("brain", {"id": t["id"], "subs": [{"t": "  Draft  ", "done": False}, {"t": "  "}, {"t": "Photos", "done": 1}, "bad"]})["task"]
check("subtasks cleaned: trimmed, blank and broken ones dropped", u["subs"] == [{"t": "Draft", "done": False}, {"t": "Photos", "done": True}])
u = feat.update("brain", {"id": t["id"], "subs": [{"t": "s%d" % i} for i in range(150)]})["task"]
check("at most 100 subtasks", len(u["subs"]) == 100)

rep = feat.create("brain", {"title": "Weekly review", "date": "2026-11-01", "repeat": {"unit": "week", "n": 1},
                            "subs": [{"t": "Inbox", "done": True}, {"t": "Calendar", "done": False}]})["task"]
r = feat.check("brain", rep["id"], "2026-11-04")
check("ticking an occurrence opens its subtasks again for the next one", [x["done"] for x in r["task"]["subs"]] == [False, False])
check("the ticked subtasks are kept on that day", r["task"]["done_dates"]["2026-11-04"]["subs"][0]["done"] is True)
r = feat.check("brain", rep["id"], "2026-11-04", done=False)
check("unticking the occurrence puts its subtasks back", [x["done"] for x in r["task"]["subs"]] == [True, False])
one = feat.create("brain", {"title": "One-off", "subs": [{"t": "a", "done": True}]})["task"]
r = feat.check("brain", one["id"])
check("a one-off task keeps its ticked subtasks when done", r["task"]["subs"][0]["done"] is True)

# ---- HTTP ----
app = FastAPI()
app.include_router(feat.router)
cl = TestClient(app)
res = cl.post("/my-tasks/project", json={"brain": "brain", "order_ids": [c, e]}).json()
check("the route reorders tags", res["ok"] and [x["id"] for x in res["projects"]][:2] == [c, e])
res = cl.post("/my-tasks", json={"brain": "brain", "title": "Via HTTP", "tags": [c, e]}).json()
check("the route creates a task with tags", res["ok"] and res["task"]["tags"] == [c, e])
check("GET returns tags on every task", all(isinstance(x.get("tags"), list) for x in cl.get("/my-tasks?brain=brain").json()["tasks"]))

# ---- stats: a task counts under each of its tags ----
try:
    import task_stats
    src = Path(task_stats.__file__).read_text(encoding="utf-8")
    check("the stats read tags through my_tasks.task_tags", "my_tasks_mod.task_tags(x)" in src)
except Exception as ex:  # noqa: BLE001
    check("task_stats imports: %s" % ex, False)

print("\n%d failed" % len(fails) if fails else "\nall ok")
raise SystemExit(1 if fails else 0)
