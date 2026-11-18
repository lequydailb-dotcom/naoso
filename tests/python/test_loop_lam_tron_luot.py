"""Regression: loop tự đặt nhiệm vụ (goal 'custom') phải làm TRỌN nhiệm vụ mỗi vòng.

Bối cảnh lỗi thật (12/11/2026): lời dặn cũ "Thực hiện 1 bước cụ thể cho nhiệm vụ trên" khiến
loop đăng bài theo lịch chỉ làm bước đầu (mở chia sẻ file) rồi báo xong, không đăng kênh nào.
Test này chốt lời dặn mới: đủ mọi bước, bước lỗi thì ghi chú rồi làm tiếp.

Chạy tay / CI:

    python tests/run.py loop_lam_tron_luot

KHÔNG cần Claude CLI/SDK/mạng - chỉ test logic thuần _norm_loop + _build_prompt.
"""
from _paths import ROOT, SERVER  # noqa: E402,F401  - nạp server/ vào sys.path (xem tests/python/_paths.py)
import asyncio
import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("NAOTA_STATE_DIR", tempfile.mkdtemp(prefix="naota-trontest-"))

import self_improve  # noqa: E402

_fails = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        _fails.append(name)


_BRAIN_ROOT = tempfile.mkdtemp(prefix="naota-tronbrain-")


def _atomic_write(path, text):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


deps = self_improve.LoopDeps(
    build_system_prompt=lambda brain: "SYS",
    brain_root=lambda brain: _BRAIN_ROOT,
    aux_model=lambda: None,
    atomic_write_text=_atomic_write,
    project_root=Path("."),
    state_dir=Path(os.environ["NAOTA_STATE_DIR"]),
    safe_tools=["Read", "Write", "Edit", "Glob", "Grep"],
    readonly_tools=["Read", "Glob", "Grep", "LS"],
)
feat = self_improve.LoopFeature(deps)

_BODY = "Bước 1: mở chia sẻ file. Bước 2: đăng Facebook. Bước 3: đăng Instagram. Bước 4: đăng Threads."

for mode in ("full", "auto"):
    loop = feat._norm_loop({"name": "Đăng theo lịch", "goal": "custom", "mode": mode}, _BODY, "dang")
    prompt, skip = asyncio.run(feat._build_prompt(loop))
    check(f"{mode}: không bị bỏ qua", skip == "")
    check(f"{mode}: prompt chứa thân nhiệm vụ", _BODY in prompt)
    check(f"{mode}: KHÔNG còn lời dặn 'Thực hiện 1 bước cụ thể'", "1 bước cụ thể" not in prompt)
    check(f"{mode}: dặn làm TRỌN mọi bước", "TRỌN" in prompt and "MỌI bước" in prompt)
    check(f"{mode}: bước lỗi thì làm tiếp bước sau", "làm tiếp bước sau" in prompt)

# Chế độ chỉ đọc giữ nguyên: chỉ đề xuất, không ghi
loop_s = feat._norm_loop({"name": "Đăng theo lịch", "goal": "custom", "mode": "suggest"}, _BODY, "dang")
prompt_s, _ = asyncio.run(feat._build_prompt(loop_s))
check("suggest: vẫn là CHẾ ĐỘ ĐỀ XUẤT", "CHẾ ĐỘ ĐỀ XUẤT" in prompt_s)


if _fails:
    print(f"\nFAIL - test_loop_lam_tron_luot: {len(_fails)} lỗi: {_fails}")
    sys.exit(1)
print("\nOK - test_loop_lam_tron_luot: tất cả pass")
