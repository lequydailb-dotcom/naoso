"""A Zalo account that gets signed out rings the owner, instead of only filling the server log.

    python tests/run.py zalo_signed_out_bell      (no network)

The report: a bot stopped answering in its groups for over a day. vanhanh-zalo printed "Not logged in" on every read,
the phrase was not recognised, and nothing reached the owner.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import asyncio
import sys
import time

import localefmt
import zalo_personal_channel as zc

localefmt.dat_ngon_ngu_yeu_cau("en")

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

_fails = []


def check(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + (f" ({detail})" if detail and not cond else ""))
    if not cond:
        _fails.append(name)


RAW = ("gọi tool lỗi: RuntimeError: process đóng stdout ([mcp] Config loaded: {\"a\":1} | "
       "[mcp] Thread name cache init failed (non-fatal): Not logged in. Run: vanhanh-zalo login")
OTHER = "process đóng stdout (something else broke)"
CONN = {"id": "c1", "label": "Shop"}

store = {}
zc.conversations.doc_trang_thai = lambda k, d="": store.get(k, d)
zc.conversations.ghi_trang_thai = lambda k, v: store.__setitem__(k, v)
sent = []


async def fake_notify(chat, text, **kw):
    sent.append((text, kw))


zc.NOTIFY_OWNER = fake_notify


async def fail_once(raw=RAW):
    zc._ring_signed_out(CONN, raw)
    await asyncio.sleep(0)


check("the real vanhanh-zalo line reads as signed out", "sign in" in zc.mo_ta_loi(RAW).lower(), zc.mo_ta_loi(RAW))

asyncio.run(fail_once(OTHER))
check("another error does not ring", not sent)

asyncio.run(fail_once())
check("signed out rings the owner", len(sent) == 1)
check("the notice names the account", bool(sent) and "Shop" in sent[0][0])
check("the notice is a system notice", bool(sent) and sent[0][1].get("kind") == "system")

asyncio.run(fail_once())
check("the next failed read inside the gap stays quiet", len(sent) == 1)

zc._TT.clear()
asyncio.run(fail_once())
check("a restart inside the gap stays quiet", len(sent) == 1)

zc._TT["c1"]["signed_out_bell"] = time.time() - zc.SIGNED_OUT_BELL_GAP_S - 1
asyncio.run(fail_once())
check("still signed out after the gap rings again", len(sent) == 2)

zc._clear_signed_out(CONN)
check("a good read clears the stored time", float(store.get("zalo_signed_out_bell:c1")) == 0)
asyncio.run(fail_once())
check("the next sign-out after a good read rings at once", len(sent) == 3)

zc.NOTIFY_OWNER = None
asyncio.run(fail_once())
check("no notifier attached: nothing breaks", len(sent) == 3)

if _fails:
    print(f"\nFAIL: {len(_fails)}")
    sys.exit(1)
print("\nPASS test_zalo_signed_out_bell")
