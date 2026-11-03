"""Windows mở Vanhanh như một app - bản đối xứng của bộ launcher macOS.

    python tests/run.py windows_launcher

Không chạy được .bat/.ps1 trên CI Linux nên đây là test TĨNH: canh các bất biến mà
vi phạm là hành vi hỏng thật, không canh câu chữ trang trí.

Bất biến quan trọng nhất: "VANHANH.bat" phải THĂM DÒ /health TRƯỚC khi gọi
start-vanhanh.vbs - vì vbs đó LUÔN kill instance cũ trước khi bật. Thiếu bước thăm dò
là double-click lần hai (mở lại cửa sổ) thành restart server, giết sạch việc nền
đang chạy dở. Đó là loại lỗi bấm thấy chạy được ngay nên không ai nghi ngờ.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401
import sys

_fails = []


def check(ten, cond, them=""):
    print(("ok   " if cond else "FAIL ") + ten + (("  [" + str(them) + "]") if them and not cond else ""))
    if not cond:
        _fails.append(ten)


BAT = ROOT / "VANHANH.bat"
AS_BAT = ROOT / "vanhanh-autostart.bat"
AS_PS1 = ROOT / "vanhanh-autostart.ps1"

check("có VANHANH.bat ở gốc repo (đối xứng VANHANH.app bên Mac)", BAT.exists())
check("có vanhanh-autostart.bat + .ps1", AS_BAT.exists() and AS_PS1.exists())

bat = BAT.read_text(encoding="utf-8")
ps1 = AS_PS1.read_text(encoding="utf-8")
as_bat = AS_BAT.read_text(encoding="utf-8")

# ---- VANHANH.bat ----
i_health = bat.find("/health")
i_vbs = bat.find("wscript //nologo start-vanhanh.vbs")   # dòng GỌI thật, không phải comment nhắc tên
check("CANARY: thăm dò /health TRƯỚC khi gọi start-vanhanh.vbs (vbs kill instance cũ - "
      "thiếu bước này là double-click lần hai giết việc nền đang chạy)",
      0 < i_health < i_vbs)
check("tôn trọng VANHANH_PORT, không hardcode một cổng", "VANHANH_PORT" in bat)
check("mở dạng cửa sổ app (--app=), không chỉ mở tab trần", "--app=" in bat)
check("có fallback trình duyệt mặc định khi không có Edge/Chrome", 'start "" %URL%' in bat)
check("máy thiếu curl vẫn mở được (Windows cũ)", "where curl" in bat)
check("chờ server lên có GIỚI HẠN, không xoay vô hạn", "gtr 45" in bat or "gtr 40" in bat)
check("cd /d về thư mục script trước (không tin working directory kế thừa - "
      "cùng bài học với start-vanhanh.vbs)", 'cd /d "%~dp0"' in bat)

# ---- autostart ----
# autostart ghi CHUNG một mục với nút trong dashboard (HKCU Run "Vanhanh"), không còn shortcut trong
# Startup: hai mục cùng bật là lúc đăng nhập hai bản Vanhanh giành nhau cổng 7777.
check("autostart ghi HKCU Run (không cần admin), cùng tên với dashboard",
      "CurrentVersion\\Run" in ps1 and '$Name = "Vanhanh"' in ps1)
check("lệnh trỏ wscript + start-vanhanh.vbs /open (chạy nền rồi mở dashboard)",
      "wscript.exe //nologo" in ps1 and "start-vanhanh.vbs" in ps1 and '`" /open"' in ps1)
check("có đủ ba việc install/uninstall/status", all(k in ps1 for k in ("install", "uninstall", "status")))
check("uninstall xoá mục Run và dọn shortcut kiểu cũ", "Remove-ItemProperty -Path $RunKey -Name $Name" in ps1 and "Remove-Item $Lnk" in ps1)
check("wrapper .bat gọi ps1 với ExecutionPolicy Bypass (máy user mặc định chặn ps1)",
      "ExecutionPolicy Bypass" in as_bat)

# ---- README hai thứ tiếng đều chỉ tới launcher ----
vi = (ROOT / "docs" / "i18n" / "vi" / "README.md").read_text(encoding="utf-8")
en = (ROOT / "README.en.md").read_text(encoding="utf-8")
check("README (vi) nhắc VANHANH.bat", "VANHANH.bat" in vi and "vanhanh-autostart.bat" in vi)
check("README (en) nhắc VANHANH.bat", "VANHANH.bat" in en and "vanhanh-autostart.bat" in en)

# ---- không em dash (luật repo, TTS khựng) ----
for ten, s in (("VANHANH.bat", bat), ("vanhanh-autostart.ps1", ps1), ("vanhanh-autostart.bat", as_bat)):
    check(f"{ten} không dùng em dash", "—" not in s)

print()
if _fails:
    print(f"{len(_fails)} test HỎNG: " + ", ".join(_fails))
    sys.exit(1)
print("Tất cả test windows_launcher đã qua.")
