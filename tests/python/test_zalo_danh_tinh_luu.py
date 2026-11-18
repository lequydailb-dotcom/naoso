"""Nick Zalo nhớ tên và id của CHÍNH nó qua các lần khởi động lại.

    python tests/run.py zalo_danh_tinh_luu      (KHÔNG mạng)

Lỗi đã gặp (03/11/2026): nhãn kết nối là "Naota Cường", tên Zalo của nick là "Tly Hoàng Ngọc Vương". Tên Zalo chỉ học được từ tin
nick tự gửi và chỉ sống trong bộ nhớ, nên sau một lần khởi động lại chủ tag "@Tly Hoàng Ngọc Vương" trong nhóm, bot không nhận
ra mình bị gọi và im.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import json
import os
import sys
import tempfile
from pathlib import Path

os.environ["NAOTA_STATE_DIR"] = tempfile.mkdtemp(prefix="naota-zpself-")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import zalo_personal_channel as zc  # noqa: E402

fails = []


def check(name, cond, them=""):
    print(("ok   " if cond else "FAIL ") + name + (("  [" + str(them) + "]") if them and not cond else ""))
    if not cond:
        fails.append(name)


CID = "zalo-1"
GROUP = "5550001"
TAG = {"text": "@Tly Hoàng Ngọc Vương em có ở đây không", "metadata": {}}

# Nick tự gửi một tin: học tên + id, và ghi xuống đĩa.
zc._hoc_danh_tinh(CID, {"from": "900", "threadId": GROUP, "senderName": "Tly Hoàng Ngọc Vương"})
f = zc._file_danh_tinh()
check("học xong thì ghi file danh tính", f.exists())
luu = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
check("file giữ đúng tên và id", luu.get(CID) == {"uid": "900", "ten": "Tly Hoàng Ngọc Vương"}, luu)
check("tag bằng tên Zalo được nhận ra", zc.nhan_dien_goi(CID, TAG, ("Naota Cường",))[0])

# Giả lập khởi động lại: bộ nhớ trống, chưa nạp.
zc._ID_MINH.clear()
zc._ID_MINH_NAP = False
check("sau khởi động lại vẫn nhận ra tag bằng tên Zalo", zc.nhan_dien_goi(CID, TAG, ("Naota Cường",))[0])
check("và nhận ra tag theo id", zc.nhan_dien_goi(CID, {"text": "alo", "metadata": {"mentions": [{"uid": "900"}]}}, ())[0])
check("id nạp lại vẫn tin được ở lần học sau", (zc._hoc_danh_tinh(CID, {"from": "900", "threadId": GROUP}) or True)
      and zc.danh_tinh(CID).get("uid") == "900")

# Tag người khác thì không phải gọi bot.
check("tag một thành viên khác không tính là gọi bot",
      not zc.nhan_dien_goi(CID, {"text": "@Minh Anh ơi", "metadata": {}}, ("Naota Cường",))[0])

# File hỏng: không sập, học lại từ tin như cũ.
zc._ID_MINH.clear()
zc._ID_MINH_NAP = False
Path(f).write_text("{hong", encoding="utf-8")
check("file hỏng thì coi như chưa biết, không sập", zc.danh_tinh(CID) == {})
zc._hoc_danh_tinh(CID, {"from": "900", "threadId": GROUP, "senderName": "Naota Cường"})
check("học lại và ghi đè file hỏng", json.loads(f.read_text(encoding="utf-8")).get(CID, {}).get("ten") == "Naota Cường")

# Tin chủ đổi tên Zalo: tên mới thay tên cũ trên đĩa.
zc._hoc_danh_tinh(CID, {"from": "900", "threadId": GROUP, "senderName": "Naota Cường 2"})
check("đổi tên Zalo thì file theo tên mới",
      json.loads(f.read_text(encoding="utf-8"))[CID]["ten"] == "Naota Cường 2")

print("\n" + ("TẤT CẢ OK" if not fails else f"{len(fails)} FAIL"))
sys.exit(1 if fails else 0)
