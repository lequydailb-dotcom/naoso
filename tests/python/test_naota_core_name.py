"""Naota Core's own name and style in one brain ("add a button so people can rename Naota Core, and on
the first chat it asks for its name, keeps a style that suits the user and learns, instead of always Naota Core").

    python tests/run.py naota_core_name

No network, no model.
- identity(): empty by default; set_identity() cleans the name (one line, no long dashes, 40 characters) and saves it
  in <brain>/Naota/core.json, one file per brain.
- The role block: no name and never asked = ask once and call op=asked; asked = no asking again; a name = speak as it.
- The agent editor (POST /agents) renames it for that brain only; GET /agents?system=1 shows the name, keeps the slug.
- The chat tool `naota_core_name` (bundled plugin) writes the same file, owner only.
- The agent routes still refuse to delete or edit Naota Core, and no longer say it cannot be renamed.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

os.environ["NAOTA_STATE_DIR"] = tempfile.mkdtemp(prefix="naota-core-name-")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

fails = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  [{str(extra)[:300]}]" if extra and not cond else ""))
    if not cond:
        fails.append(name)


import naota_core  # noqa: E402

# ---- 1. the identity file ----
A = Path(tempfile.mkdtemp(prefix="core-name-a-"))
B = Path(tempfile.mkdtemp(prefix="core-name-b-"))
check("no name by default", naota_core.identity(A) == {"name": "", "style": "", "asked": False})
check("...so it is still called Naota Core", naota_core.display_name(A) == "Naota Core")
me = naota_core.set_identity(A, name="  Mây " + chr(0x2014) + " bé\n xinh  ")
check("the name is cleaned: one line, no long dash, spaces collapsed", me["name"] == "Mây bé xinh", me)
check("a name counts as asked", me["asked"] is True)
check("saved as the name in the brain's own Naota Core agent file",
      naota_core._read_file(A / "agents" / "naota-core.md")[0].get("name") == "Mây bé xinh")
check("another brain keeps its own (none)", naota_core.identity(B)["name"] == "")
check("40 characters at most", len(naota_core.set_identity(B, name="x" * 99)["name"]) == 40)
naota_core.set_identity(B, name="")
check("an empty name goes back to Naota Core", naota_core.display_name(B) == "Naota Core")
naota_core.set_identity(A, style="thân thiện, ngắn gọn")
check("style is kept apart from the name", naota_core.identity(A)["name"] == "Mây bé xinh"
      and naota_core.identity(A)["style"] == "thân thiện, ngắn gọn")

# ---- 2. what the role block tells the model ----
C = Path(tempfile.mkdtemp(prefix="core-name-c-"))
blk = naota_core.prompt_block(C)
check("no name, never asked: ask once and record it", "NO name of your own yet" in blk and "op=asked" in blk)
naota_core.set_identity(C, asked=True)
blk = naota_core.prompt_block(C)
check("asked already: no asking again", "op=asked" not in blk and "no name of your own yet" in blk)
blk = naota_core.prompt_block(A)
check("named: speaks as that name, with the agreed style",
      "**Mây bé xinh**" in blk and "thân thiện, ngắn gọn" in blk and "op=asked" not in blk)
check("without a brain the block is the plain role block", naota_core.prompt_block() == naota_core.prompt_block(None)
      and "name of your own" not in naota_core.prompt_block().split("# === NAOTA CORE ===")[-1].split("Name and style")[0])
check("the block stays small with a name and a style", len(naota_core.prompt_block(A)) < 3000, len(naota_core.prompt_block(A)))
check("the role body tells it to fit its style to the user and save it with the tool",
      "naota_core_name" in naota_core.definition()["body"] and "style" in naota_core.definition()["body"])

# ---- 3. the server: rename button and the Partners list ----
import config as cfgmod  # noqa: E402
import main  # noqa: E402
import mcp_hub  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

if os.environ["NAOTA_STATE_DIR"] not in str(cfgmod.STATE_DIR):
    print(f"FAIL state dir is not the temp dir: {cfgmod.STATE_DIR}. STOP.")
    sys.exit(1)

client = TestClient(main.app, base_url="http://127.0.0.1:8080")


def localefmt_en(resp):
    """The same refusal in English, whatever language the server picked for this request."""
    return "edited like any" if "sửa như một trợ lý thường" in resp.json().get("error", "") else ""
D = Path(tempfile.mkdtemp(prefix="core-name-d-"))
(D / "agents").mkdir()
r = client.post("/agents", data={"slug": "naota-core", "name": "Sky", "role": "", "prompt": "x", "brain": str(D)})
check("the agent editor renames it", r.status_code == 200 and naota_core.identity(D)["name"] == "Sky", r.text)
ds = client.get("/agents", params={"brain": str(D), "prompt": 0, "system": 1}).json()["agents"]
core = ds[0]
check("the Partners list shows the new name, same slug and system flags",
      core["slug"] == "naota-core" and core["name"] == "Sky" and core["custom_name"] == "Sky"
      and core["system_name"] == "Naota Core" and core["system"] is True, core)
sid = main.get_store().create_session(brain=main._brain_key(str(D)), channel=naota_core.CHANNEL)
check("a Core chat of that brain is told its name", "**Sky**" in main._naota_core_block(sid))
naota_core.set_identity(D, name="")
check("an empty name goes back to Naota Core", naota_core.display_name(D) == "Naota Core"
      and client.get("/agents", params={"brain": str(D), "prompt": 0, "system": 1}).json()["agents"][0]["custom_name"] == "")
r = client.post("/agents/delete", data={"slug": "naota-core", "brain": str(D)})
check("deleting it is still refused", r.status_code == 403)
check("...and the refusal no longer says it cannot be renamed or edited", "renamed" not in r.json().get("error", "")
      and "edited like any" in r.json().get("error", "") + localefmt_en(r), r.text)

# ---- 4. the chat tool ----
check("the tool is the owner's only (a customer bot never renames the owner's assistant)",
      "naota_core_name" in mcp_hub.OWNER_ONLY_TOOLS)
yml = (ROOT / "system/plugins/naota-core-name/plugin.yaml").read_text(encoding="utf-8")
check("the plugin ships enabled at the safe level",
      "slug: naota-core-name" in yml and "enabled: true" in yml and "min_mode: safe" in yml and "naota_core_name" in yml)
spec = importlib.util.spec_from_file_location("naota_core_name_plugin", ROOT / "system/plugins/naota-core-name/plugin.py")
plug = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plug)
reg = {}


class _Reg:
    def register_tool(self, name, desc, fn, **kw):
        reg[name] = fn


plug.register(_Reg())
run = reg["naota_core_name"]


class _Ctx:
    vault_root = str(Path(tempfile.mkdtemp(prefix="core-name-e-")))


ctx = _Ctx()
check("op=get with no name", "chưa đặt" in run({"op": "get"}, ctx))
run({"op": "asked"}, ctx)
check("op=asked records it", naota_core.identity(ctx.vault_root)["asked"] is True)
out = run({"op": "set", "name": "Bé Na", "style": "vui vẻ"}, ctx)
check("op=set saves name and style", naota_core.identity(ctx.vault_root)["name"] == "Bé Na"
      and naota_core.identity(ctx.vault_root)["style"] == "vui vẻ" and "Bé Na" in out, out)
check("op=set with nothing to set is an error", run({"op": "set"}, ctx).startswith("ERROR"))
run({"op": "reset"}, ctx)
check("op=reset goes back to Naota Core", naota_core.identity(ctx.vault_root)["name"] == ""
      and naota_core.identity(ctx.vault_root)["style"] == "")
check("no brain: refused, nothing written", run({"op": "set", "name": "X"}, type("C", (), {"vault_root": ""})()).startswith("ERROR"))

# ---- 5. the card ----
dashes = [chr(0x2014), chr(0x2013)]
for f in (Path(__file__), ROOT / "system/plugins/naota-core-name/plugin.py", ROOT / "system/plugins/naota-core-name/plugin.yaml",
          ROOT / "server/naota_core.py", ROOT / "system/agents/naota-core.md"):
    check(f"no em or en dash in {f.name}", not any(d in f.read_text(encoding="utf-8") for d in dashes))

print()
if fails:
    raise SystemExit(f"FAIL {len(fails)}: " + "; ".join(fails[:6]))
print("ALL PASS")
