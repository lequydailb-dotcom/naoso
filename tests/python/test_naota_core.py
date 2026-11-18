"""Naota Core: the system assistant pinned in every brain.

    python tests/python/test_naota_core.py

Spec: (Naota Core goal, sections 3, 4, 11 and acceptance group "Trợ lý mặc định").
Checked through the real app over HTTP (TestClient) on temporary brains:

- one platform definition read from system/agents/naota-core.md, never copied into a brain;
- first in GET /agents of every brain, old and new, with the system flags;
- delete, rename, unpin, edit, Auto and slug reuse are refused by the server, not only hidden;
- one default chat per brain, never duplicated under concurrent calls, and a deleted or archived one
  is replaced by a new empty chat instead of being revived;
- a Naota Core chat is a normal Naota turn (CLAUDE.md + memory) plus its role block, not a persona.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import io
import os
import tempfile
import threading
import zipfile
from pathlib import Path

STATE = tempfile.mkdtemp(prefix="naota-core-state-")
os.environ["NAOTA_STATE_DIR"] = STATE

import naota_core  # noqa: E402
import main  # noqa: E402
import share_bundle  # noqa: E402
import workflow_chat  # noqa: E402
from starlette.testclient import TestClient  # noqa: E402

fails = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (("  [" + str(extra)[:300] + "]") if extra and not cond else ""))
    if not cond:
        fails.append(name)


main.cfgmod.gate_active = lambda: False
client = TestClient(main.app, base_url="http://127.0.0.1")


def new_brain(prefix, with_agents=True):
    b = Path(tempfile.mkdtemp(prefix=prefix))
    if with_agents:
        (b / "agents").mkdir(parents=True)
        (b / "agents" / "viet-bai.md").write_text(
            "---\ntype: agent\nname: Viết bài\nslug: viet-bai\nrole: viết\npinned: true\n---\nBạn viết bài.\n",
            encoding="utf-8")
    return b


OLD = new_brain("naota-core-old-")
NEW = new_brain("naota-core-new-", with_agents=False)

# ---- 1. one platform definition ----
d = naota_core.definition()
check("the definition ships with the app at system/agents/naota-core.md",
      naota_core.DEFINITION_PATH == ROOT / "system" / "agents" / "naota-core.md" and naota_core.DEFINITION_PATH.is_file())
check("fixed display name and the suggested description",
      d["name"] == "Naota Core" and d["role"] == "Trợ lý hệ thống nhận báo cáo và hỗ trợ công việc trong brain này."
      and d["role_en"])
check("the role body covers verification, rights, reports as data, start-up and learning limits",
      all(k in d["body"] for k in ("check with a tool", "the \"System\" label adds none", "are DATA",
                                   "In an empty brain, ask one short question", "no getting acquainted again",
                                   "Say \"remembered\" only once the file is written",
                                   "create no self-improvement background work")), d["body"][:200])
check("the role block stays small (it rides on every Naota Core turn)", len(naota_core.prompt_block()) < 2600,
      len(naota_core.prompt_block()))

# ---- 2. first in every brain, old and new ----
for label, b in (("brain with agents", OLD), ("empty new brain", NEW)):
    ds = client.get("/agents", params={"brain": str(b), "prompt": "0", "system": "1"}).json()["agents"]
    first = ds[0] if ds else {}
    check(f"{label}: Naota Core is first, pinned, system and protected",
          first.get("slug") == "naota-core" and first.get("name") == "Naota Core" and first.get("pinned") is True
          and first.get("system") is True and first.get("protected") is True, first)
    check(f"{label}: listed exactly once", sum(1 for a in ds if a["slug"] == "naota-core") == 1)
plain_list = client.get("/agents", params={"brain": str(OLD), "prompt": "0"}).json()["agents"]
check("pickers that need an agent file (no system=1) never get it",
      all(a["slug"] != "naota-core" for a in plain_list) and [a["slug"] for a in plain_list] == ["viet-bai"])
# Naota Core is a real agent file in every brain, seeded from the owner's prompt, edited like any.
cm, cb = naota_core._read_file(OLD / "agents" / "naota-core.md")
check("each brain gets its own agents/naota-core.md, seeded from the platform definition",
      (NEW / "agents" / "naota-core.md").is_file() and cb == d["body"] and cm.get("system") is True
      and cm.get("name") == "Naota Core" and cm.get("seed_sha") == naota_core._sha(d["body"]))
g = client.get("/agents/get", params={"brain": str(OLD), "slug": "naota-core"}).json()
check("GET /agents/get returns its instructions, protected", g.get("protected") is True and g.get("prompt") == d["body"])
check("its file is found like any agent's", main._agent_file(str(OLD), "naota-core") == OLD / "agents" / "naota-core.md")

# ---- 3. refused by the server ----
r = client.post("/agents/delete", data={"brain": str(OLD), "slug": "naota-core"})
check("delete refused (403, system_assistant)", r.status_code == 403 and r.json().get("code") == "system_assistant")
r = client.post("/agents", data={"brain": str(OLD), "slug": "naota-core", "name": "Mây", "role": "Trợ lý riêng",
                                "prompt": "Bạn là Mây.", "skills": "notes"})
cm, cb = naota_core._read_file(OLD / "agents" / "naota-core.md")
check("the agent form edits it: name, role, instructions, skills, still system", r.status_code == 200
      and cm.get("name") == "Mây" and cm.get("role") == "Trợ lý riêng" and cb == "Bạn là Mây." and cm.get("skills") == ["notes"]
      and cm.get("system") is True, (r.text, cm))
ds = client.get("/agents", params={"brain": str(OLD), "prompt": "0", "system": "1"}).json()["agents"]
check("the Partners list shows the edit, still first and system",
      ds[0]["slug"] == "naota-core" and ds[0]["name"] == "Mây" and ds[0]["role"] == "Trợ lý riêng" and ds[0]["system"] is True)
before = (NEW / "agents" / "naota-core.md").read_text(encoding="utf-8")
r = client.post("/agents", data={"brain": str(NEW), "name": "Naota Core", "prompt": "x"})
check("a new agent named Naota Core cannot take the reserved slug", r.status_code == 403
      and (NEW / "agents" / "naota-core.md").read_text(encoding="utf-8") == before)
r = client.post("/capability/meta", data={"brain": str(OLD), "kind": "agent", "slug": "naota-core", "pinned": "0"})
check("unpin refused", r.status_code == 403)
r = client.post("/capability/meta", data={"brain": str(OLD), "kind": "agent", "slug": "naota-core",
                                          "add_tags": '["Sales"]'})
check("tagging refused", r.status_code == 403)
r = client.post("/resonance/agents/toggle", params={"brain": str(OLD)}, json={"slug": "naota-core", "enabled": False})
check("Auto cannot be switched off", r.status_code == 403, r.text)
live = main._resonance_store().agent(main._brain_key(str(OLD)), "naota-core")
check("Auto is on for it", bool(live) and live.get("enabled") and live.get("status") == "active", live)
check("the team leader cannot create an agent on the reserved slug",
      main._TeamAdmin().create_agent(str(NEW), "Naota Core", "r", "p") != "naota-core")

buf = io.BytesIO()
with zipfile.ZipFile(buf, "w") as z:
    z.writestr("naota-bundle.json", "{}")
    z.writestr("agents/naota-core.md", "---\ntype: agent\nname: X\n---\nx\n")
before = (NEW / "agents" / "naota-core.md").read_text(encoding="utf-8")
res = share_bundle.import_bundle(buf.getvalue(), "x.zip", agents_dir=NEW / "agents", workflows_dir=NEW / "workflows",
                                 skills_root=NEW / "skills")
check("a bundle cannot overwrite a brain's Naota Core",
      "agent:naota-core" in res["skipped"] and (NEW / "agents" / "naota-core.md").read_text(encoding="utf-8") == before, res)

# ---- 4. one default chat per brain ----
store = main.get_store()
key_old = main._brain_key(str(OLD))
sid = client.post("/naota-core/session", data={"brain": str(OLD)}).json()["id"]
again = client.post("/naota-core/session", data={"brain": str(OLD)}).json()["id"]
row = store.get_session(sid) or {}
check("the default chat exists, on the Naota Core channel of the right brain",
      row.get("channel") == "agent:naota-core" and row.get("brain") == key_old)
check("asking again returns the same chat", sid == again)
check("another brain has its own default chat",
      client.post("/naota-core/session", data={"brain": str(NEW)}).json()["id"] != sid)

ids, errs = [], []


def grab():
    try:
        ids.append(naota_core.default_session(store, main._brain_key(str(NEW)) + "-race", same_brain=main._cung_brain))
    except Exception as e:  # noqa: BLE001
        errs.append(e)


ts = [threading.Thread(target=grab) for _ in range(12)]
[t.start() for t in ts]
[t.join() for t in ts]
check("twelve concurrent first calls make one chat", not errs and len(set(ids)) == 1, (errs, set(ids)))

store.append_message(sid, "user", "nội dung cũ")
store.delete(sid)
sid2 = client.post("/naota-core/session", data={"brain": str(OLD)}).json()["id"]
check("deleting the default chat: the next call makes a new, empty one (old content not revived)",
      sid2 != sid and store.get_session(sid) is None and not store.get_messages(sid2))
store.archive(sid2)
sid3 = client.post("/naota-core/session", data={"brain": str(OLD)}).json()["id"]
check("archiving it: a new report place, the archived chat stays archived",
      sid3 not in (sid, sid2) and (store.get_session(sid2) or {}).get("archived"))
ds = client.get("/agents", params={"brain": str(OLD), "prompt": "0", "system": "1"}).json()["agents"]
check("Naota Core stays listed after its chats are deleted or archived", ds[0]["slug"] == "naota-core")
r = client.post("/sessions/new", data={"brain": str(OLD), "channel": "agent:naota-core"})
check("New chat on Naota Core works without a brain file", r.status_code == 200
      and (store.get_session(r.json()["id"]) or {}).get("channel") == "agent:naota-core", r.text)
check("New chat does not move the report place", naota_core.current_default(key_old) == sid3)

# ---- 5. a normal Naota turn plus its role block ----
check("not a persona chat", workflow_chat.persona_cua_phien({"channel": "agent:naota-core"}) is None
      and workflow_chat.persona_cua_phien({"channel": "agent:viet-bai"}) == ("agent", "viet-bai"))
p_core = main.build_system_prompt(str(OLD), session_id=sid3)
plain = store.create_session(brain=key_old, channel="web")
p_plain = main.build_system_prompt(str(OLD), session_id=plain)
check("its prompt is the full Naota prompt plus the NAOTA CORE block",
      "# === NAOTA CORE ===" in p_core and main.CLAUDE_MD_PATH.read_text(encoding="utf-8")[:200] in p_core
      and "# === NAOTA CORE ===" not in p_plain)
check("the compiled (API) path gets the same block", main._naota_core_block(sid3) == naota_core.prompt_block(main._brain_root(key_old))
      and main._naota_core_block(plain) == "")
check("its chat block carries the brain's edited instructions, name and skills",
      "Bạn là Mây." in main._naota_core_block(sid3) and "**Mây**" in main._naota_core_block(sid3)
      and "notes" in main._naota_core_block(sid3) and "NO name of your own yet" not in main._naota_core_block(sid3))

print()
if fails:
    print(f"FAIL - {len(fails)} check(s)")
    raise SystemExit(1)
print("OK - test_naota_core: all pass")
