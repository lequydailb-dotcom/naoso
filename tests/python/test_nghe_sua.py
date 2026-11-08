"""Sửa chữ nghe nhầm theo ngữ cảnh (nghe_sua.sua) và gợi ý hotwords cho Whisper.

    python tests/run.py nghe_sua

Vì sao file này tồn tại: người dùng nói lẫn Việt - Anh, máy nghe chép sai tên trợ lý
rồi bộ não trả lời bám nghĩa đen. Lớp này sửa theo ÂM và NGỮ CẢNH trước khi câu đi vào bộ não.
VANHANH 1.0.0: mẫu nghe nhầm đổi theo tên mới ("Vận Hành", "Vân Hạnh", "Vạn Hạnh", "Van hanh"). Ranh giới quan
trọng: không đổi tên người thứ ba ("nhắn cho Vân Hạnh"), không đổi tên riêng hai chữ ("Vận Hành
Beckham"), không đụng câu tiếng Việt thường có âm gần ("nào ta", "lao ta"), không sửa gì thì trả
y nguyên.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401

import nghe_sua  # noqa: E402

_fails = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        _fails.append(name)


TV = ["Vanhanh"]
S = lambda s, tv=TV: nghe_sua.sua(s, tv)   # noqa: E731

# ---- 1. Khoá âm: cách viết khác của "Vanhanh" phải về cùng một khoá ----
for w in ("Vanhanh", "VANHANH", "vanhanh", "Vận Hành"):
    check(f"khoá âm của {w!r} trùng Vanhanh", nghe_sua.khoa_am(w) == nghe_sua.khoa_am("Vanhanh"))
check("Java KHÔNG trùng khoá Vanhanh", nghe_sua.khoa_am("Java") != nghe_sua.khoa_am("Vanhanh"))

# ---- 2. Gọi tên: sửa ở mọi vị trí khi trùng âm hoàn toàn ----
check("đầu câu không gọi tên: 'Vận Hành' là chữ thật, giữ nguyên", S("Vận Hành mở trang việc giúp anh") == "Vận Hành mở trang việc giúp anh")
check("giữa câu: 'vận hành' là chữ thật, giữ nguyên", S("hệ thống vận hành ổn định") == "hệ thống vận hành ổn định")
check("hey Vận Hành", S("hey Vận Hành, doanh thu hôm nay bao nhiêu") == "hey Vanhanh, doanh thu hôm nay bao nhiêu")
check("cuối câu: cảm ơn Vận Hành", S("cảm ơn Vận Hành") == "cảm ơn Vanhanh")
check("sửa nhiều chỗ trong một câu",
      S("Vận Hành ơi, Vận Hành nghe rõ không") == "Vanhanh ơi, Vanhanh nghe rõ không")
check("giữ nguyên xuống dòng và dấu câu quanh chỗ sửa",
      S("Ok Vận Hành.\nMở trang cài đặt!") == "Ok Vanhanh.\nMở trang cài đặt!")

# ---- 3. Trùng vừa phải: CHỈ sửa ở vị trí gọi tên ----
check("Vân Hạnh ơi (gọi tên) -> Vanhanh", S("Vân Hạnh ơi, mấy giờ rồi") == "Vanhanh ơi, mấy giờ rồi")
check("bị tách hai tiếng: Van hanh, đầu câu -> Vanhanh", S("Van hanh, đọc tin mới") == "Vanhanh, đọc tin mới")
check("cảm ơn Vạn Hạnh -> Vanhanh", S("cảm ơn Vạn Hạnh") == "cảm ơn Vanhanh")
check("Vân Hạnh đầu câu mà không gọi tên thì giữ nguyên",
      S("Vân Hạnh mở trang việc giúp anh") == "Vân Hạnh mở trang việc giúp anh")

# ---- 4. Không sửa bừa ----
GIU = [
    "nhắn cho Vận Hành là tôi đến muộn",           # người thứ ba
    "gặp Vân Hạnh lúc 3 giờ",
    "Vận Hành Beckham đá bóng hay",                 # tên riêng hai chữ
    "hôm nay nào ta cùng xem số liệu",           # "nào ta" là tiếng Việt thường
    "Nào ta đi thôi",
    "lao ta về quê",
    "học Java với anh Nam",                      # Java không phải Vanhanh
    "đọc file README.md và mở https://github.com/x",
    "doanh thu tháng này bao nhiêu",
    "",
]
for s in GIU:
    check(f"giữ nguyên: {s[:40]!r}", S(s) == s)
check("không có gì sửa thì trả CÙNG đối tượng", S("xin chào") == "xin chào")
check("đã đúng Vanhanh thì không đổi gì", S("Vanhanh ơi mở lịch") == "Vanhanh ơi mở lịch")
check("chạy hai lần ra cùng kết quả (idempotent)",
      S(S("Vận Hành ơi Van hanh nghe không")) == S("Vận Hành ơi Van hanh nghe không"))
check("bộ từ vựng rỗng: trả y nguyên", nghe_sua.sua("Vận Hành ơi", []) == "Vận Hành ơi")

# ---- 5. Từ vựng người dùng khai: nhiều từ, cụm hai tiếng ----
TV2 = ["Vanhanh", "OpenRouter", "Pancake"]
check("Open Router (tách) -> OpenRouter",
      S("đổi bộ não sang open router đi", TV2) == "đổi bộ não sang OpenRouter đi")
check("Pan cake -> Pancake", S("xem đơn trên pan cake", TV2) == "xem đơn trên Pancake")
check("Bánh kếp không thành Pancake", S("ăn bánh kếp", TV2) == "ăn bánh kếp")

# ---- 6. Rút bộ từ vựng từ settings + gợi ý cho Whisper ----
cfg = {"voice": {"hotwords": "OpenRouter, Pancake\n vanhanh ; Zalo,, Pancake"}}
tv = nghe_sua.vocabulary(cfg)
check("Vanhanh luôn đứng đầu, không nhân đôi dù người dùng gõ 'vanhanh'", tv[0] == "Vanhanh" and tv.count("Vanhanh") == 1
      and not any(t.lower() == "vanhanh" for t in tv[1:]))
check("tách bằng phẩy, chấm phẩy, xuống dòng; bỏ trùng", tv == ["Vanhanh", "OpenRouter", "Pancake", "Zalo"])
check("không có cài đặt vẫn có Vanhanh", nghe_sua.vocabulary({}) == ["Vanhanh"])
check("gợi ý Whisper là danh sách ngăn phẩy, khép dấu chấm",
      nghe_sua.goi_y_whisper(tv, ky_thuat=()) == "Vanhanh, OpenRouter, Pancake, Zalo.")
check("gợi ý rỗng khi không có từ", nghe_sua.goi_y_whisper([], ky_thuat=()) == "")

# ---- 7. Mồi thêm từ tiếng Anh hay nói xen ("GitHub Actions" thành "huyết áp Action") ----
gy = nghe_sua.goi_y_whisper(tv)
check("mặc định mồi kèm từ tiếng Anh thông dụng", "GitHub Actions" in gy and "deploy" in gy)
check("từ người dùng khai đứng CUỐI (Whisper chỉ giữ phần cuối prompt)",
      gy.endswith("Vanhanh, OpenRouter, Pancake, Zalo."))
gy2 = nghe_sua.goi_y_whisper(["Vanhanh", "github"])
check("không nhân đôi từ người dùng đã khai (không phân biệt hoa thường)",
      [x.strip(" .").lower() for x in gy2.split(",")].count("github") == 1 and gy2.endswith("Vanhanh, github."))
dai = ["Tu%02d dai dai dai dai" % i for i in range(20)]      # ~460 ký tự, chừa chỗ cho vài từ mồi
gy3 = nghe_sua.goi_y_whisper(dai)
check("quá trần thì bỏ bớt từ mồi chung, giữ nguyên từ người dùng",
      gy3.endswith(", ".join(dai) + ".") and len(gy3) <= nghe_sua.MAX_GOI_Y
      and gy3.startswith("GitHub") and "email" not in gy3)
check("vừa trần thì nằm trong MAX_GOI_Y", len(nghe_sua.goi_y_whisper(tv)) <= nghe_sua.MAX_GOI_Y)
check("từ mồi chung KHÔNG đi vào lớp sửa mờ", "GitHub" not in nghe_sua.vocabulary(cfg))

if _fails:
    print("\nFAIL:", len(_fails), _fails)
    raise SystemExit(1)
print("\nOK - nghe_sua")
