"""What the owner teaches an assistant in chat reaches its bot, the clock reaches lower-level bots, and Zalo contact cards
become text the bot can read.

    python tests/run.py bot_owner_rules      (no network)
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import json
import os
import sys
import tempfile

os.environ["NAOTA_STATE_DIR"] = tempfile.mkdtemp(prefix="naota-bot-rules-")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import chatbot_runtime  # noqa: E402
import zalo_personal_channel as zp  # noqa: E402

fails = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (("  [" + str(extra)[:300] + "]") if extra and not cond else ""))
    if not cond:
        fails.append(name)


# ---- Owner rules in the bot prompt
MEMORY = """# Agent notes

## Bài học (tự học)
- SECRET-LESSON khách A nợ tiền

## Luật chủ dặn
- Nhóm Zoom thì gửi link đăng ký
- Tin nhắn Zalo không dùng markdown

## Lịch sử (tự học)
- SECRET-HISTORY phiên riêng với chủ
"""
seen = []


def memory_reader(brain, slug):
    seen.append((brain, slug))
    return MEMORY


def wire(reader):
    chatbot_runtime.wire(answer=None, brain_root=lambda b: tempfile.gettempdir(),
                         read_agent=lambda b, s: ({"name": "CSKH"}, "Nội dung file Agent."),
                         read_agent_memory=reader)


BOT = {"name": "Bot", "agent": {"brain": "CSKH Zalo", "slug": "cskh"}, "muc_quyen": "read_docs"}
wire(memory_reader)
p = chatbot_runtime.build_bot_prompt(BOT)
check("reads the memory of the bot's own agent and brain", seen == [("CSKH Zalo", "cskh")], seen)
check("the owner's rules are in the prompt", "- Nhóm Zoom thì gửi link đăng ký" in p and "- Tin nhắn Zalo không dùng markdown" in p, p)
check("rules come after the Agent file, so they win", p.find("Nội dung file Agent.") < p.find("Nhóm Zoom"), p)
check("lessons and history stay private", "SECRET" not in p, p)

for label, reader in (("empty memory", lambda b, s: ""), ("no rules section", lambda b, s: "## Bài học (tự học)\n- x\n"),
                      ("memory read fails", lambda b, s: 1 / 0), ("reader not wired", None)):
    wire(reader)
    p = chatbot_runtime.build_bot_prompt(BOT)
    check(f"{label}: prompt still builds, without a rules block", "Nội dung file Agent." in p and "LUẬT CHỦ" not in p, p)

# ---- Clock line for lower-level bots
src = (ROOT / "server" / "main.py").read_text(encoding="utf-8")
check("Reads documents and Can write bots get the clock",
      "text, sess=sess, sysprompt=_bot_co_dong_ho(_sys_bot, bot), prov=prov" in src)
check("Read only bots get the clock", "_bot_tra_loi(text, sess=sess, sysprompt=_bot_co_dong_ho(_sys_bot, bot)," in src)
check("rules are wired from the agent memory", "read_agent_memory=_agent_memory," in src)

# ---- Zalo contact cards
CONN = {"id": "c1", "label": "Zalo"}
TEN = {"t1": {"name": "Khách", "type": 0}}


def ev(**kw):
    return zp.chuan_hoa_tin(CONN, dict({"threadId": "t1", "from": "u1", "id": "m1", "ts": 1793800000000}, **kw), TEN)


card = json.dumps({"title": "Nguyễn Văn A", "description": json.dumps({"phone": "0901 234 567", "gUid": "x"}),
                   "action": "recommened.user", "href": "https://zalo.me/x"})
e = ev(type="chat.recommended", text=card)
check("a card in `text` becomes a text message", e["message_type"] == "text", e["message_type"])
check("the name and the phone are readable", "Nguyễn Văn A" in e["text"] and "0901234567" in e["text"], e["text"])
check("the raw JSON is gone", "{" not in e["text"], e["text"])

e = ev(type="chat.recommended", content={"title": "B", "phone": "+84901234567"})
check("a card as an object in `content`", "+84901234567" in e["text"] and e["message_type"] == "text", e)
e = ev(type="chat.recommended", text=json.dumps({"title": "C", "params": json.dumps({"phone": "0912345678"})}))
check("phone nested in `params`", "0912345678" in e["text"], e["text"])
e = ev(type="chat.recommended", text=json.dumps({"title": "D", "action": "recommened.user", "description": ""}))
check("a card with a hidden number still shows the name", e["message_type"] == "text" and "D" in e["text"], e)

e = ev(type="chat.recommended", text=json.dumps({"title": "Bài viết", "action": "recommened.link", "href": "https://a.vn"}))
check("a shared link is not a card", e["message_type"] == "other", e["message_type"])
e = ev(type="chat.recommended", text="https://hoc.example/courses/1")
check("a plain link stays as it was", e["message_type"] == "other" and e["text"] == "https://hoc.example/courses/1", e)
e = ev(type="text", text=json.dumps({"phone": "0901234567"}))
check("a text message that only looks like a card is untouched", '"phone"' in e["text"], e["text"])

e1 = ev(type="chat.recommended", text=card)
e2 = ev(type="text", text="Anh gọi số này giúp em", id="m2")
g = zp.gop_tin([e1, e2])
check("the merged turn keeps the card", "0901234567" in g["text"] and "Anh gọi" in g["text"], g.get("text"))

print()
if fails:
    print(f"{len(fails)} FAIL")
    sys.exit(1)
print("ALL OK")
