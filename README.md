<div align="center">

<img src="dashboard/logo.svg" width="88" alt="Logo NAOSO">

# NAOSO

### Não Ta: bộ não AI của riêng bạn

Trợ lý AI chạy trên máy bạn hoặc VPS riêng, đổi được bộ não (Claude, ChatGPT, Grok, Gemini...) mà không mất công cụ nào, có giọng nói, và có Second Brain thông minh dần lên mỗi ngày.

Làm bởi **[Đại Lê](https://lequydai.com)** · [vanhanh.lequydai.com](https://vanhanh.lequydai.com)

[Hướng dẫn đầy đủ](docs/i18n/vi/README.md) · [Cài nhanh](QUICKSTART.md) · [Lên VPS](DEPLOY.md) · [Tài liệu](docs/README.md) · [English](README.en.md)

</div>

---

## VANHANH là gì?

VANHANH không phải chatbot. Nó là một **AI làm việc thay bạn**: đọc, ghi file, gọi các kết nối (bán hàng, quảng cáo, lịch, email, Zalo...), chạy kỹ năng, giao việc chạy nền và tự đặt lịch. Mọi thứ gói trong một bảng điều khiển nói chuyện được bằng giọng.

- **Bộ não do bạn chọn, đổi lúc nào cũng được.** Dùng gói Claude, ChatGPT, Grok, Antigravity bạn đang có, hoặc chỉ cần một API key. Năng lực nằm ở VANHANH, không nằm ở model.
- **Second Brain của chính bạn.** Ký ức, wiki, kỹ năng lưu thành file chữ trên máy bạn, có lịch sử, mang đi đâu cũng được.
- **Báo cáo bằng số thật.** Đấu kết nối nào thì VANHANH báo cáo kinh doanh và cuộc sống từ nguồn đó, không bịa số.

## Hai cách dùng

| Cách | Hợp với ai |
|---|---|
| **Cài trên máy** Windows, macOS, Linux | Muốn dữ liệu nằm ở máy mình |
| **Đưa lên VPS riêng** | Muốn chạy 24/7, gọi từ điện thoại |

## Cài trên máy bằng một lệnh

Cần có Git (Windows: `winget install -e --id Git.Git`). Mở PowerShell hoặc Terminal, dán đúng một dòng:

| Máy | Lệnh |
|---|---|
| **Windows** | `git clone https://github.com/lequydailb-dotcom/naoso.git vanhanh; cd vanhanh; powershell -ExecutionPolicy Bypass -File install.ps1` |
| **Linux / macOS** | `git clone https://github.com/lequydailb-dotcom/naoso.git vanhanh && cd vanhanh && chmod +x install.sh && ./install.sh` |

Lệnh cài Python, thư viện, các bộ não CLI, rồi mở VANHANH ở `http://localhost:7777`. Có bản mới thì bấm nút **Cập nhật** trong app. Phải tải bằng `git clone` như trên: tải file ZIP vẫn chạy được nhưng **không cập nhật được**. Trên Windows, lần sau chỉ cần bấm đúp **`VANHANH.bat`**. Các bước chi tiết ở [QUICKSTART.md](QUICKSTART.md), lên VPS xem [DEPLOY.md](DEPLOY.md).

## Bản quyền

Bản quyền © 2026 Đại Lê ([lequydai.com](https://lequydai.com)). Bảo lưu mọi quyền. Thành viên cộng đồng VANHANH được tải về, cài đặt và dùng miễn phí. Xem [LICENSE](LICENSE).
