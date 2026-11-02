"""Mã NAOTA không được chứa dấu vết của dự án cũ: tên người, tài khoản, nhóm, cửa hàng, máy chủ, mã ID.

    python tests/run.py khong_dau_vet_cu     (KHÔNG mạng)

Danh sách cần chặn lưu dạng BĂM (SHA-256, 20 ký tự hex của chữ thường đã chuẩn hoá NFC) để chính file này không
chứa các tên đó. Bài kiểm tách mọi file chữ git theo dõi thành từ, băm từng cụm 1 tới 4 từ liền nhau và so với tập
băm. Lọt một cụm là đỏ, chỉ ra file và số dòng. Thư viện ngoài (vendor, third_party) và nhật ký nội bộ không xét.
"""
from _paths import ROOT  # noqa: E402
import hashlib
import re
import subprocess
import sys
import unicodedata

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

BAM = {
    "03381a1737a505a2fc9b",
    "04253f0b9dac9a41a276",
    "0769626028245e253fa6",
    "077776e2a0960c37e012",
    "12661a43b5e6840390cb",
    "15119f80da0699f1a245",
    "174706d050b90d39b0b6",
    "1813b6157bcbde449eb7",
    "1a7a10450e508ede002c",
    "20c72942a9f65388c22c",
    "2db48a9e4ef7c1a79605",
    "2de03b3eeba125be0ac6",
    "3eef8d665f6fb4a56e23",
    "42b977badf5a646045aa",
    "44e4c2035a785f45f186",
    "457560aad2bf74b7e573",
    "4e3819220b5a57eeb5f9",
    "4e41b17564e57dca9fa8",
    "537f44894d41565c733a",
    "539738a1d0bb64c070cf",
    "567d2034dddbf5b840b0",
    "5fc2f13b9b748f161cfc",
    "63877f30ea1148b1ecc2",
    "63cd6b71b5385b2c539a",
    "6429b07bfe18a1ebfa4a",
    "65ff1fdf3de1bb4bafa6",
    "69e613dbca76aaabfd09",
    "6ca867058a37148bc4b0",
    "7fb81699c06eeae0c837",
    "84891f095f82827366cd",
    "8634336f762198ad8630",
    "8b6aa19a049461de29bd",
    "90f9fcd38b2e58cc85b4",
    "915e8cf7853c8bad73e9",
    "91deba6265026e020f49",
    "9877edde14fa2bac22ea",
    "a1fd3a2f7add048729a4",
    "a3b5cf3e60e634d08c78",
    "a4ad5b0473ff525863f8",
    "ae2cb40c1ad64e2bde9f",
    "b1da18abf80a7a58657a",
    "b7607e4a85c9731708ff",
    "b8f464f9e8e799f0bc8f",
    "bb2f0269f69559e9d394",
    "bce0970211e7693fb562",
    "bebe90cc64bf23f7ca40",
    "c5c27ebf3f48cb504857",
    "cb026ad0a05a238999fd",
    "cc4f96b4ada6e0bcd693",
    "d41516bc594a8a8e15f8",
    "dda820158d142a0b7338",
    "ded7ce21fb7097ca70c7",
    "df175d776cc50e8ad8e0",
    "df4ca362be0dc4fb1961",
    "df74c43832dabaf4a566",
    "e8c591f9e71bdf1c925b",
    "ec628da08ec820d3f3e3",
    "ed0ecf35cba65888c164",
    "f75c6310e0e855cee27c",
    "f84f2e46f6f68409ae6f",
    "fdbfadf3e0c300ea5399",
    "fefab53a10aabc243c55",
    "ffbe790247923d9029b0",
}
BO = ("dashboard/vendor/", "tests/js/vendor/", "third_party/", "dashboard/fonts/")
BO_FILE = {"NHAT-KY.md", "tests/python/test_khong_dau_vet_cu.py"}
NHI_PHAN = re.compile(r"\.(png|jpe?g|webp|gif|ico|mp3|wav|ogg|woff2?|ttf|otf|gz|zip|pdf)$", re.I)
TU = re.compile(r"[\w-]+")


def bam(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:20]


ds = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
lot = []
for rel in ds:
    if rel.startswith(BO) or rel in BO_FILE or NHI_PHAN.search(rel):
        continue
    try:
        t = (ROOT / rel).read_bytes().decode("utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    t = unicodedata.normalize("NFC", t).lower()
    for so, dong in enumerate(t.splitlines(), 1):
        # Từ ghép bằng "-" vừa xét nguyên khối vừa xét từng mảnh (ab-cd -> "ab-cd", "ab", "cd")
        tu = []
        for m in TU.findall(dong):
            tu.extend([m] + [x for x in m.split("-") if x and x != m] if "-" in m else [m])
        for i in range(len(tu)):
            for n in range(1, 5):
                if i + n <= len(tu) and bam(" ".join(tu[i:i + n])) in BAM:
                    lot.append(f"{rel}:{so}")
                    break
if lot:
    print(f"ĐỎ: {len(lot)} chỗ còn dấu vết dự án cũ (tên bị che, xem dòng):")
    for x in sorted(set(lot))[:50]:
        print("  ", x)
    sys.exit(1)
print(f"OK - {len(BAM)} mẫu chặn, không lọt chỗ nào")
