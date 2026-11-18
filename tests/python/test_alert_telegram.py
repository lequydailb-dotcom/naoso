"""A failure that needs the owner reaches their own Telegram.

    python tests/python/test_alert_telegram.py

- an incident that needs the owner is urgent, so Naota Core's default ("urgent only") lets it ring;
- an incident from a job made in a web chat goes to that chat AND to the owner's Telegram, once;
- an incident whose chat is the owner's Telegram is not sent twice; a calm notice ("ran it again") is not copied;
- a Team notice (blocked, failed, waits for you) reaches the owner's Telegram, not the bell only;
- no owner Telegram, or the group turned off: nothing is sent;
- the Office page says whether alerts reach Telegram, without any secret.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import asyncio
import os
import tempfile

STATE = tempfile.mkdtemp(prefix="naota-alert-tg-")
os.environ["NAOTA_STATE_DIR"] = STATE

import main  # noqa: E402
import notify_policy  # noqa: E402

fails = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (("  [" + str(extra)[:300] + "]") if extra and not cond else ""))
    if not cond:
        fails.append(name)


LOOP = asyncio.new_event_loop()
asyncio.set_event_loop(LOOP)


def run(coro):
    return LOOP.run_until_complete(coro)


main.cfgmod.gate_active = lambda: False


def set_tg(ids, owner=None, enabled=True, token="123:abc"):
    cfg = main.cfgmod.read_settings()
    t = cfg.setdefault("telegram", {})
    t.update({"enabled": enabled, "token": token, "chat_id": ids})
    if owner is not None:
        t["owner_chat_id"] = owner
    else:
        t.pop("owner_chat_id", None)
    main.cfgmod.write_settings(cfg)


sent = []


async def fake_channel(owner_chat, text, **kw):
    sent.append((str(owner_chat), text))
    return True, ""


main._gui_qua_kenh = fake_channel
web = main.get_store().create_session(brain=main._brain_key("brain"), channel="web")
web_chat = f"{main.WEB_CHAT_PREFIX}{web}"


def tg_sent():
    return [t for c, t in sent if not c.startswith(main.WEB_CHAT_PREFIX)]


# ---- 1. incidents ----
set_tg("111")
check("default mode is urgent only (what a fresh install rings)", notify_policy.DEFAULT_MODE == "urgent")

sent.clear()
run(main._incident_post("brain", "⚠ Sự cố cần bạn: 'Đăng bài'. Lỗi: timeout", chat=web_chat))
check("web-chat incident: the owner's Telegram gets one copy", tg_sent().count("⚠ Sự cố cần bạn: 'Đăng bài'. Lỗi: timeout") == 1,
      sent)

sent.clear()
run(main._incident_post("brain", "⚠ Sự cố cần bạn: 'Báo cáo'. Lỗi: 401", chat=""))
check("no-chat incident rings the owner's Telegram at the default mode", len(tg_sent()) == 1, sent)

sent.clear()
run(main._incident_post("brain", "⚠ Sự cố cần bạn: 'Chốt đơn'. Lỗi: x", chat="111"))
check("incident made from the owner's Telegram is not sent twice", len(tg_sent()) == 1, sent)

sent.clear()
run(main._incident_post("brain", "Sự cố: 'Đăng bài' vừa hỏng, em đã cho chạy lại một lần.", chat=web_chat))
check("a calm 'ran it again' notice is not copied to Telegram", tg_sent() == [], sent)

# ---- 2. teams ----
sent.clear()
run(main._team_notify("team-session", "Việc nhóm \"Viết bài\" bị chặn: Trợ lý gặp lỗi khi làm"))
check("a blocked team job reaches the owner's Telegram", len(tg_sent()) == 1, sent)

# ---- 3. nobody to send to, or the owner turned the group off ----
set_tg("111,222")
sent.clear()
run(main._team_notify("team-session", "Việc nhóm \"Viết bài\" bị chặn: x"))
check("several ids and no owner link: nothing sent", tg_sent() == [], sent)

set_tg("111")
notify_policy.set_mode("team", "off")
sent.clear()
run(main._team_notify("team-session", "Việc nhóm \"Viết bài\" bị chặn: y"))
check("team group turned off: nothing sent", tg_sent() == [], sent)
notify_policy.set_mode("team", "urgent")

# ---- 4. the Office page line ----
set_tg("111")
check("office: Telegram ready", main._office_alert() == {"tg": "ok"}, main._office_alert())
set_tg("111", enabled=False)
check("office: Telegram off", main._office_alert() == {"tg": "off"})
set_tg("111,222")
check("office: no owner picked", main._office_alert() == {"tg": "no_owner"})
check("office: no secret in the answer", "123:abc" not in str(main._office_alert()))

print()
if fails:
    print(f"FAIL - {len(fails)} check(s)")
    raise SystemExit(1)
print("OK - test_alert_telegram: all pass")
