"""Messenger: heart before answering, like on comments, gifts sent privately to commenters.

    python tests/run.py messenger_react_gift

No network: Graph is faked. Guarded:

  1. A Messenger message the bot answers gets a heart (sender_action "react" on its mid) before the answer.
  2. A silent turn ([IM_LANG], a personal message left for the owner) gets no heart and no answer.
  3. A comment the bot answers is liked first.
  4. The gift part ([QUA_RIENG]...[/QUA_RIENG]) of a comment answer goes as a Private Reply to that comment,
     never publicly; the public reply tags the commenter and says the gift is in their inbox.
  5. A link left outside the markers in a comment answer still goes private.
  6. When the private reply fails, no link is posted publicly.
  7. Account meta react="off" turns the heart/like off.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import asyncio
import os
import sys
import tempfile

os.environ["VANHANH_STATE_DIR"] = tempfile.mkdtemp(prefix="vanhanh-messenger-react-")

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import messenger_bot  # noqa: E402
import bot_reaction  # noqa: E402

_fails = []


def check(name, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"  [{detail}]"))
    if not ok:
        _fails.append(name)


def run(coro):
    return asyncio.run(coro)


PAGE = "1234567890123"
SECRET = "c" * 32
TOKEN = "EAA" + "t" * 60
GIFT = "https://drive.google.com/file/d/abc/view"


def ev(mid, text):
    return {"sender": {"id": "555"}, "recipient": {"id": PAGE}, "timestamp": 1,
            "message": {"mid": mid, "text": text}}


def com(text="AI", cid="555_101"):
    return {"comment_id": cid, "root_id": "555_100", "post_id": f"{PAGE}_555", "from_id": "777",
            "from_name": "Chị Lan", "message": text, "photo": "", "video": "", "permalink": ""}


def _bot(answer, fail=()):
    calls = []
    bot = messenger_bot.MessengerBot({"page_id": PAGE, "access_token": TOKEN, "app_secret": SECRET}, "",
                                     answer, giau_trang_thai=True)

    async def fake_post(client, path, payload):
        calls.append((path, payload))
        for f in fail:
            if f(path, payload):
                return {"ok": False, "code": 100, "error": "nope"}
        if (payload.get("recipient") or {}).get("comment_id"):
            return {"ok": True, "recipient_id": "psid-777", "message_id": "m.9"}
        return {"ok": True, "id": "x"}

    async def fake_name(client, psid):
        return "Khách"

    async def fake_post_text(client, post_id):
        return "Tặng quà AI"
    bot._post_json = fake_post
    bot._name_of = fake_name
    bot._post_text = fake_post_text
    return bot, calls


async def _drain(bot):
    for task in list(bot._current.values()):
        await task
    await asyncio.sleep(0)
    if bot._client:
        await bot._client.aclose()


async def _msg_turn(reply):
    async def answer(text, meta, progress):
        return reply
    bot, calls = _bot(answer)
    await bot._on_event(ev("mid.1", "Cho mình hỏi khoá học"))
    await _drain(bot)
    return calls


async def _comment_turn(reply, fail=(), text="AI"):
    async def answer(t, meta, progress):
        return reply
    bot, calls = _bot(answer, fail)
    orig = messenger_bot.comment_mode
    messenger_bot.comment_mode = lambda aid: "reply"
    try:
        await bot._on_comment(com(text))
        await _drain(bot)
    finally:
        messenger_bot.comment_mode = orig
    return calls


# 1. heart before the answer
calls = run(_msg_turn({"text": "Dạ khoá học bên em có 3 gói ạ."}))
kinds = [("react" if c[1].get("sender_action") == "react" else
          "text" if (c[1].get("message") or {}).get("text") else c[1].get("sender_action")) for c in calls]
react = [c for c in calls if c[1].get("sender_action") == "react"]
check("messenger: a heart goes on the customer's message", len(react) == 1
      and react[0][1]["payload"] == {"message_id": "mid.1", "reaction": "❤️"}
      and react[0][1]["recipient"] == {"id": "555"}, calls)
check("messenger: the heart comes before the answer", "react" in kinds and "text" in kinds
      and kinds.index("react") < kinds.index("text"), kinds)

# 1b. the Agent's own reaction wins
calls = run(_msg_turn({"text": "Haha đúng rồi ạ", "reaction": "haha"}))
react = [c for c in calls if c[1].get("sender_action") == "react"]
check("messenger: the Agent's chosen reaction is used", react and react[0][1]["payload"]["reaction"] == "\U0001f606",
      react)

# 2. silent turn: nothing
calls = run(_msg_turn({"text": "", "im_lang": True}))
check("messenger: silent turn gets no heart and no answer",
      not any(c[1].get("sender_action") == "react" or c[1].get("message") for c in calls), calls)

# 3-4. comment: like + private gift + tagged public line
calls = run(_comment_turn({"text": f"Quà đã gửi bạn nhé!\n[QUA_RIENG]Quà của bạn: {GIFT}\nNhóm Zalo: "
                                   "https://zalo.me/g/abc[/QUA_RIENG]"}))
paths = [c[0] for c in calls]
priv = [c for c in calls if (c[1].get("recipient") or {}).get("comment_id")]
pub = [c for c in calls if c[0].endswith("/comments")]
check("comment: liked first", paths and paths[0] == "555_101/likes", paths)
check("comment: the gift goes as a private reply to that comment",
      len(priv) == 1 and priv[0][0] == f"{PAGE}/messages" and priv[0][1]["recipient"] == {"comment_id": "555_101"}
      and GIFT in priv[0][1]["message"]["text"], priv)
check("comment: the public reply tags the commenter and carries no link",
      len(pub) == 1 and pub[0][1]["message"].startswith("@[777] ") and "http" not in pub[0][1]["message"]
      and "zalo.me" not in pub[0][1]["message"], pub)
check("comment: private before public", paths.index(f"{PAGE}/messages") < paths.index("555_100/comments"), paths)

# 4b. only the gift, no public words -> a default public line
calls = run(_comment_turn({"text": f"[QUA_RIENG]{GIFT}[/QUA_RIENG]"}))
pub = [c for c in calls if c[0].endswith("/comments")]
check("comment: gift only -> public line says it is in the inbox",
      len(pub) == 1 and "tin nhắn riêng" in pub[0][1]["message"] and "http" not in pub[0][1]["message"], pub)

# 4c. tagging refused -> plain name
calls = run(_comment_turn({"text": f"Đã gửi quà nhé [QUA_RIENG]{GIFT}[/QUA_RIENG]"},
                          fail=(lambda p, d: p.endswith("/comments") and "@[" in d.get("message", ""),)))
pub = [c for c in calls if c[0].endswith("/comments")]
check("comment: when tagging is refused the name is written instead",
      len(pub) == 2 and pub[-1][1]["message"].startswith("Chị Lan ơi") and "http" not in pub[-1][1]["message"], pub)

# 5. link outside the markers still goes private
calls = run(_comment_turn({"text": f"Quà đây bạn: {GIFT}"}))
priv = [c for c in calls if (c[1].get("recipient") or {}).get("comment_id")]
pub = [c for c in calls if c[0].endswith("/comments")]
check("comment: a bare link is moved to the private reply",
      priv and GIFT in priv[0][1]["message"]["text"] and pub and "http" not in pub[0][1]["message"], (priv, pub))

# 6. private reply fails -> no link in public
calls = run(_comment_turn({"text": f"Quà đây [QUA_RIENG]{GIFT}[/QUA_RIENG]"},
                          fail=(lambda p, d: bool((d.get("recipient") or {}).get("comment_id")),)))
pub = [c for c in calls if c[0].endswith("/comments")]
check("comment: private reply failed -> public reply has no link",
      pub and all("http" not in c[1]["message"] for c in pub), pub)

# 6a. comment already privately replied by another tool -> gift goes to the person's conversation
async def _already():
    async def answer(t, meta, progress):
        return {"text": f"Quà đây [QUA_RIENG]{GIFT}[/QUA_RIENG]"}
    calls = []
    bot = messenger_bot.MessengerBot({"page_id": PAGE, "access_token": TOKEN, "app_secret": SECRET}, "",
                                     answer, giau_trang_thai=True)

    async def fake_post(client, path, payload):
        calls.append((path, payload))
        if (payload.get("recipient") or {}).get("comment_id"):
            return {"ok": False, "code": 10900, "error": "Activity already replied to"}
        return {"ok": True, "id": "x"}

    async def fake_psid(client, cid):
        return "psid-777"

    async def fake_post_text(client, post_id):
        return ""
    bot._post_json, bot._psid_of_comment, bot._post_text = fake_post, fake_psid, fake_post_text
    orig = messenger_bot.comment_mode
    messenger_bot.comment_mode = lambda aid: "reply"
    try:
        await bot._on_comment(com())
        await _drain(bot)
    finally:
        messenger_bot.comment_mode = orig
    return calls

calls = run(_already())
direct = [c for c in calls if (c[1].get("recipient") or {}).get("id") == "psid-777"]
pub = [c for c in calls if c[0].endswith("/comments")]
check("comment already replied privately: gift goes to the person's conversation",
      direct and GIFT in direct[0][1]["message"]["text"], calls)
check("comment already replied privately: public reply is tagged, no link",
      pub and pub[0][1]["message"].startswith("@[777] ") and "http" not in pub[0][1]["message"], pub)

# 6b. a comment answer without a gift is not tagged and not private
calls = run(_comment_turn({"text": "Dạ bên em có lớp tối thứ 3 ạ."}))
check("comment: plain answer stays plain", not any((c[1].get("recipient") or {}).get("comment_id") for c in calls)
      and [c[1]["message"] for c in calls if c[0].endswith("/comments")] == ["Dạ bên em có lớp tối thứ 3 ạ."], calls)

# 7. react off
orig = messenger_bot.react_on
messenger_bot.react_on = lambda aid: False
try:
    calls = run(_msg_turn({"text": "Dạ."}))
finally:
    messenger_bot.react_on = orig
check("react=off: no heart", not any(c[1].get("sender_action") == "react" for c in calls), calls)

# helpers
pub, priv = messenger_bot.split_private("A [QUA_RIENG]x[/QUA_RIENG] B [qua_rieng]y")
check("split_private: both parts, markers gone", pub == "A  B".replace("  ", " ") or pub == "A  B", (pub, priv))
check("split_private: private parts joined", priv == "x\n\ny", priv)
check("unwrap_private drops markers in a private chat",
      messenger_bot.unwrap_private("Quà [QUA_RIENG]link[/QUA_RIENG]") == "Quà link", messenger_bot.unwrap_private(
          "Quà [QUA_RIENG]link[/QUA_RIENG]"))
check("messenger is a reaction channel", "messenger" in bot_reaction.CHANNELS)
check("the comment note teaches the gift markers", messenger_bot.QUA_RIENG in messenger_bot.comment_note("x"))

print()
if _fails:
    print(f"{len(_fails)} FAILED")
    sys.exit(1)
print("all ok")
