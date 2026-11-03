<div align="center">

# 🧠 VANHANH

**AI agentic đổi được bộ não + Second Brain - chạy trên model nào bạn muốn (Claude Code, ChatGPT/Codex, Antigravity CLI, OpenRouter, OpenAI, Gemini, Anthropic API, Groq, Ollama), có giọng nói, đồ thị tri thức, và tự thông minh dần lên.**

<!-- flags:start -->
<p align="center">
<b>🌐 Có 12 thứ tiếng</b><br><br>
<a href="../../../README.en.md"><img src="../../assets/flags/gb.svg" width="30" alt="English" title="English"></a>
<img src="../../assets/flags/vn.svg" width="30" alt="Tiếng Việt" title="Tiếng Việt">
<a href="../zh/README.md"><img src="../../assets/flags/cn.svg" width="30" alt="简体中文" title="简体中文"></a>
<a href="../es/README.md"><img src="../../assets/flags/es.svg" width="30" alt="Español" title="Español"></a>
<a href="../ja/README.md"><img src="../../assets/flags/jp.svg" width="30" alt="日本語" title="日本語"></a>
<a href="../hi/README.md"><img src="../../assets/flags/in.svg" width="30" alt="हिन्दी" title="हिन्दी"></a>
<a href="../pt-BR/README.md"><img src="../../assets/flags/br.svg" width="30" alt="Português" title="Português"></a>
<a href="../ko/README.md"><img src="../../assets/flags/kr.svg" width="30" alt="한국어" title="한국어"></a>
<a href="../ru/README.md"><img src="../../assets/flags/ru.svg" width="30" alt="Русский" title="Русский"></a>
<a href="../de/README.md"><img src="../../assets/flags/de.svg" width="30" alt="Deutsch" title="Deutsch"></a>
<a href="../fr/README.md"><img src="../../assets/flags/fr.svg" width="30" alt="Français" title="Français"></a>
<a href="../id/README.md"><img src="../../assets/flags/id.svg" width="30" alt="Bahasa Indonesia" title="Bahasa Indonesia"></a>
</p>
<!-- flags:end -->

[🇬🇧 English](../../../README.en.md) · 🇻🇳 **Tiếng Việt** · [🇨🇳 简体中文](../zh/README.md) · [🇪🇸 Español](../es/README.md) · [🇯🇵 日本語](../ja/README.md) · [🇮🇳 हिन्दी](../hi/README.md) · [🇧🇷 Português](../pt-BR/README.md) · [🇰🇷 한국어](../ko/README.md) · [🇷🇺 Русский](../ru/README.md) · [🇩🇪 Deutsch](../de/README.md) · [🇫🇷 Français](../fr/README.md) · [🇮🇩 Bahasa Indonesia](../id/README.md) · [🌍 Giúp dịch](CONTRIBUTING.md#dịch-thuật)

</div>

> 🌍 Đây là bản hướng dẫn đầy đủ bằng tiếng Việt. Trang đầu ngắn gọn ở [README.md](../../../README.md), bản tiếng Anh đầy đủ ở [README.en.md](../../../README.en.md). Tài liệu hướng dẫn chi tiết bằng tiếng Việt vẫn ở [docs/](../../README.md).

---

## Cài nhanh bằng chính AI của bạn

Đưa link repo này cho **Claude Code** hoặc **Codex** đang chạy trên máy bạn và nói "cài VANHANH giúp tôi". Nó chỉ cần chạy **một lệnh duy nhất**:

| Máy | Một lệnh cài hết |
|---|---|
| **Windows** | `powershell -ExecutionPolicy Bypass -File install.ps1` |
| **Linux / macOS** | `chmod +x install.sh && ./install.sh` |

Lệnh đó cài trọn gói: Python + thư viện, **bốn bộ não CLI chạy bằng gói thuê bao bạn đang có** (`claude`, `codex`, `agy`, `grok`), `.env`, rồi bật server ở `http://localhost:7777`. Sau đó đăng nhập từng bộ não **ngay trong trang Models** của dashboard, không phải gõ lệnh nữa.

> ⚠️ Cài thêm một CLI **sau khi** Vanhanh đã chạy thì **khởi động lại Vanhanh**. Tiến trình đang chạy giữ PATH của lúc nó bật, nên CLI vừa cài nó chưa thấy.

<p align="center">
<img src="../../../docs/assets/diagrams/install-terminal.svg" width="100%" alt="Terminal động: lệnh cài một dòng dựng Python, bốn bộ não CLI chạy bằng gói thuê bao và file .env, rồi báo Vanhanh đang chạy ở http://localhost:7777">
</p>

---

## Vanhanh là gì?

VANHANH **không phải** một chatbot. Nó là một **AI agentic tự host** chạy trên máy/VPS của bạn: đọc/ghi file, gọi công cụ (MCP), chạy skill, giao việc chạy nền, tự đặt lịch - rồi gói tất cả vào một **dashboard đẹp, điều khiển bằng giọng nói**, kèm một **Second Brain** (bộ nhớ + wiki) tích luỹ tri thức theo thời gian.

**Bộ não thì bạn chọn, và đổi lúc nào cũng được.** 14 đường dùng được ngay: **Claude Code**, **ChatGPT/Codex**, **Grok Build** và **Antigravity CLI** (dùng chính gói subscription bạn đang trả, không cần mua API riêng), **OpenRouter · OpenAI API · Google Gemini · Anthropic API · Groq · DeepSeek · Ollama Cloud** (chỉ cần API key), cộng thêm **Ollama chạy ngay trên máy bạn** và **mọi endpoint tương thích OpenAI hoặc Anthropic**.

<p align="center">
<img src="../../../docs/assets/diagrams/swappable-brain.svg" width="100%" alt="Hình động: lõi Vanhanh ở giữa, bộ đồ nghề (MCP Hub, Skills, Second Brain, Tasks, Schedules, Plugins) bao quanh, 12 bộ não lần lượt lắp vào mà mọi công cụ vẫn sáng nguyên">
</p>

> **Lưu ý khi cho gói subscription chạy việc nền.** Anthropic chỉ tính gói Claude Pro/Max cho việc dùng **cá nhân, thông thường** của Claude Code. Chạy nền liên tục (loop, nhắc hẹn, việc Kanban, chatbot), chạy trên VPS, hoặc nhiều người dùng chung một tài khoản đều nằm ngoài phạm vi đó nên có nguy cơ **bị khoá tài khoản**, dù tới nay Vanhanh chưa ghi nhận trường hợp nào. Nếu bạn gặp, hãy báo cho nhà phát triển qua [Issues](https://github.com/lequydailb-dotcom/vanhanh/issues/new/choose). Vanhanh không tự đọc token đăng nhập của bạn - nó chạy qua đúng binary `claude`, nhưng như vậy vẫn không làm việc chạy nền 24/7 trở thành hợp lệ. Muốn yên tâm: ở trang **Models**, đặt Claude Code chạy bằng **API key**, hoặc trỏ **model việc nền** sang một provider khác. Xem `server/claude_auth.py`.

> Triết lý: **năng lực nằm ở Vanhanh, không nằm ở model.** Mọi bộ não đều được cấp cùng bộ đồ nghề qua trung tâm kết nối (MCP Hub) chung - MCP đã đấu, tool đọc/ghi brain, skill, việc Kanban, agent/workflow/loop/nhắc hẹn. Khác biệt duy nhất: hai engine CLI chạy thêm được **lệnh máy**. Đổi từ Claude sang Gemini không làm Vanhanh mất chức năng nào ngoài chuyện đó.

<p align="center">
<img src="../../../docs/assets/diagrams/chat-to-action.svg" width="100%" alt="Hình động: một câu chat đi vào Vanhanh, Vanhanh chọn công cụ nhỏ nhất đủ làm xong việc, từ trả lời thẳng, xếp việc, tới tạo agent, workflow, nhắc hẹn hay loop">
</p>

Bạn đấu các **kết nối** của riêng mình vào (bán hàng/POS, quảng cáo, lịch, email, Zalo, ghi chú…) → Vanhanh tự phát hiện và **báo cáo kinh doanh + cuộc sống** bằng số liệu thật, nói chuyện như người.

### Cái bẫy không ai nói trước: bị khoá vào một nhà cung cấp AI

Thử dùng một app AI mỗi ngày trong một năm, rồi nhìn lại xem bên trong nó đã chất những gì:

- **Hàng trăm cuộc trò chuyện**, chứa những quyết định và bối cảnh bạn đã mất công cùng nó nghĩ ra.
- **Trí nhớ** về bạn: bạn là ai, làm việc kiểu gì, kinh doanh bán gì.
- **Hướng dẫn riêng, trợ lý, dự án**: bí quyết bạn đã ngồi chỉnh hàng giờ.
- **Tự động hoá và agent** chỉ chạy được trên đúng nền tảng đó.

Tất cả nằm trên máy chủ của nhà cung cấp, theo định dạng của họ. Rồi một model tốt hơn ra đời ở chỗ khác. Bạn dùng thử được, nhưng không mang công việc theo được: app mới không biết gì về bạn, hướng dẫn cũ không sang được, lịch sử thì ở lại. Nếu có nút xuất dữ liệu, thứ nhận về thường chỉ là một đống log chat, không phải trí nhớ mà công cụ khác dùng được.

Thế là bạn ở lại. Không phải vì model cũ còn tốt nhất, mà vì rời đi nghĩa là làm lại từ con số không. Và khi nhà cung cấp tăng giá, siết giới hạn, khai tử model hay khoá tài khoản, bạn không có đường lui.

### Vanhanh đảo ngược chuyện đó: model đi thuê, bộ não là của bạn

Trong Vanhanh, model chỉ là một bộ phận thay được. Mọi thứ bạn tích luỹ đều nằm trong tay bạn, dưới dạng file mở ra đọc được:

| Thứ bạn tích luỹ | Nằm ở đâu | Định dạng |
|---|---|---|
| **Lịch sử trò chuyện** | `conversations.db` trên máy hoặc VPS của bạn, chung một chỗ dù bộ não nào trả lời | SQLite, tìm kiếm toàn văn |
| **Trí nhớ về bạn** | `memory/` trong brain: `MEMORY.md` và mỗi điều nhớ một file | Markdown |
| **Tri thức** | thư mục Wiki và Sources của brain | Markdown, mở được bằng Obsidian |
| **Skill** | `skills/<tên>/SKILL.md` | Markdown |
| **Agent và workflow** | `agents/*.md`, `workflows/*.md` | Markdown có front matter |
| **Loop và nhắc hẹn** | `Vanhanh/loops/*.md`, `Vanhanh/reminders.json` | Markdown, JSON |

Nhờ vậy:

- **Có model mới? Đổi ở trang Models rồi làm tiếp.** Model mới đọc cùng trí nhớ, chạy cùng skill, agent, workflow, gọi cùng các kết nối qua MCP Hub. Không phải chuyển dữ liệu, không phải dựng lại gì cả.
- **Dùng nhiều bộ não cùng lúc.** Model mạnh để trò chuyện, model rẻ chạy việc nền, model Ollama chạy ngay trên máy cho ghi chú riêng tư, tất cả cùng làm việc trên một brain.
- **Không cần Vanhanh vẫn đọc được.** Brain là một thư mục markdown, mở bằng Obsidian hay trình soạn thảo nào cũng được. Lỡ mai Vanhanh không còn, tri thức của bạn vẫn nằm đó, bằng chữ thường.
- **Có lịch sử phiên bản, mang đi đâu cũng được.** Mỗi lần Vanhanh tự học là một commit git, hoàn tác bằng một chạm, và cả brain đồng bộ được lên repo GitHub riêng tư của bạn, dùng chung giữa laptop và VPS.
- **Dữ liệu nằm trên máy của bạn.** Không có máy chủ Vanhanh nào đứng giữa. Mỗi yêu cầu chỉ đi tới đúng nhà cung cấp model bạn chọn, còn dùng model Ollama trên máy thì không rời khỏi máy bạn.

### Vanhanh so với chatbot thường

| | Chatbot thường | **VANHANH** |
|---|---|---|
| Bộ não | Khoá cứng 1 model, API gọi rời từng câu | **Đổi được**: 14 nhà cung cấp, cái nào cũng đủ tool, MCP, skill, session - kể cả model chạy ngay trên máy bạn qua Ollama |
| Trí nhớ | Quên sau mỗi phiên | **Second Brain sống** - nhớ bạn, dày lên qua từng hội thoại |
| Dữ liệu | Bịa hoặc không có | **Số liệu thật** từ kết nối bạn đấu vào (POS, Ads, Lịch, Zalo…) |
| Tự cải thiện | Không | **Vòng lặp tự chạy nền** + hàng đợi việc do AI tự vận hành |
| Giao diện | Khung chat | Dashboard + đồ thị tri thức + **giọng nói rảnh tay** + Telegram |
| Công việc của bạn | Nằm trên máy chủ nhà cung cấp, theo định dạng của họ | **File thường trên máy bạn**: lịch sử, trí nhớ, skill, agent, workflow mang sang được mọi model mới |
| Triển khai | Khoá vào 1 nhà cung cấp | **Tự host**: [Hostinger](https://www.hostinger.com) 1-click / Docker / VPS bất kỳ |

> 💡 **Triết lý:** Vanhanh *biên dịch một lần* tri thức từ ghi chú thô → Wiki, rồi *duy trì* nó sống cùng mỗi nguồn mới. Tri thức **tích luỹ**, không tái phát hiện mỗi lần.

---

## ✨ Tính năng nổi bật

<p align="center">
<img src="../../../docs/assets/diagrams/second-brain-grows.svg" width="100%" alt="Đồ thị tri thức động: ghi chú và liên kết lần lượt mọc ra, Second Brain lớn dần từ vài ghi chú lên hơn một nghìn">
</p>

- 🎙️ **Trò chuyện bằng giọng nói rảnh tay** - nói, Vanhanh nghe và trả lời bằng giọng. Chọn được nhà cung cấp giọng đọc: Edge TTS (miễn phí, mặc định), OpenAI hoặc ElevenLabs.
- 🌌 **Đồ thị tri thức** - bộ não của bạn hiện ra thành mạng note nối nhau qua `[[wikilink]]`, bằng canvas nhẹ và chạy được ngoại tuyến.
- 💬 **Phiên hội thoại** - lưu / mở lại / **tìm kiếm toàn văn** mọi cuộc trò chuyện cũ; phiên dài được nén tóm tắt thay vì cắt cụt trí nhớ.
- 🗂️ **Quản lý tệp tin** - duyệt, **sửa file `.md`/`.txt` trực tiếp** trong trình duyệt, tìm file theo tên hoặc theo nội dung, tải lên/về.
- 🧩 **Skills** - gom nhóm, tìm kiếm, **bật/tắt từng skill**, thêm/sửa/xoá, nhập/xuất gói; Vanhanh tự xếp skill mới vào đúng nhóm.
- 🧰 **Plugins** - thả một thư mục Python vào là có thêm **tool/hook native** cho MỌI engine, không phải sửa lõi.
- 🤖 **Agents & Workflows** - tạo trợ lý chuyên biệt (có bộ nhớ riêng) + chuỗi tự động nhiều bước, có bước kiểm chứng.
- ♻️ **Việc định kỳ & nhắc hẹn** - nhiều vòng lặp chạy nền song song, mỗi vòng làm đúng một việc bạn mô tả rồi tự kiểm chứng; kèm nhắc hẹn theo giờ cố định hoặc cron.
- 🗃️ **Việc (Kanban)** - giao một "goal" bằng lời, AI tự đặc tả, chọn worker, chạy nền và chỉ gọi bạn khi có ngoại lệ.
- 🧠 **Tự học** - sau mỗi hội thoại Vanhanh tự rút ký ức, đúc tri thức Wiki và kỹ năng; mỗi lần học là một commit git nên **hoàn tác được một chạm**.
- 🔌 **Kho kết nối đa tài khoản** - Pancake POS, Zalo, Meta/Google/TikTok Ads, Google Workspace, Slack, Webcake, Substack… nhiều tài khoản cùng một dịch vụ, mỗi tài khoản một mức quyền riêng, Vanhanh **chặn cứng** thao tác vượt quyền.
- 📱 **Telegram & Zalo** - hỏi Vanhanh qua Telegram; đọc, tìm lịch sử và gửi tin Zalo bằng MCP của `vanhanh-zalo`, bản CLI Zalo riêng của Vanhanh.
- 💬 **Slack & WhatsApp** - chat với Vanhanh và đặt bot khách hàng trên Slack (không cần tên miền) và WhatsApp (API chính thức của Meta). Hướng dẫn: [docs/29](../../../docs/29-slack-whatsapp.md).
- 🎨 **Tạo ảnh** bằng chính gói ChatGPT đã đăng nhập, không cần API key riêng.
- 📊 **Mức dùng** - Vanhanh tự đo token vào/ra và chi phí theo ngày, theo nhà cung cấp, tách rõ phần bạn gõ tay với phần Vanhanh tự chạy nền.
- ⇅ **Sao lưu brain lên GitHub** - đồng bộ 2 chiều mọi brain lên một repo riêng tư, dùng chung giữa máy nhà và VPS.
- 🔄 **Đa engine, đổi không mất chức năng** - Claude Code, ChatGPT (Codex), OpenRouter, OpenAI API, Google Gemini, Anthropic API, Groq. Đổi trong **Models** một cú bấm; bộ não nào cũng gọi được MCP Vanhanh, tool file brain và skill.
- 🔐 **An toàn khi lên VPS** - tự bắt buộc đăng nhập khi chạy public, chống chiếm tài khoản, rate-limit, chặn CSRF, mã hoá khoá bí mật trong cấu hình.


<p align="center">
<img src="../../../docs/assets/diagrams/background-work.svg" width="100%" alt="Bảng Kanban động trong đêm: việc tự đi từ Queued sang Running, Review rồi Done, sáng ra báo cáo bay về Telegram">
</p>

---

## 🚀 Cài đặt

> ⚠️ **Quan trọng về bảo mật:** Vanhanh chạy bộ não AI với **toàn quyền** trên máy. Khi chạy public (Docker/VPS/Hostinger), Vanhanh **tự bắt buộc đăng nhập** - mở app ra là màn tạo tài khoản / đăng nhập, không ai điều khiển được khi chưa có mật khẩu.

> 💻 **Cài trên máy tính Windows hoặc Mac của bạn?** Tải bộ cài về rồi mở như mọi ứng dụng: [Vanhanh-Setup.exe](https://github.com/lequydailb-dotcom/vanhanh/releases/download/desktop/Vanhanh-Setup.exe) (Windows 10/11) hoặc [Vanhanh-macOS.dmg](https://github.com/lequydailb-dotcom/vanhanh/releases/download/desktop/Vanhanh-macOS.dmg) (macOS 11+). Bộ cài tự kiểm tra máy thiếu gì (Git, Python, Node, các bộ não AI), tự cài, rồi để lại biểu tượng VANHANH để bấm. Các bước: [QUICKSTART.md](../../../QUICKSTART.md).

### Cách 1 - Hostinger Docker Manager (tên miền + HTTPS) ⚡

> 🛒 **Chưa có VPS?** [Đăng ký VPS Hostinger tại đây](https://www.hostinger.com). VPS có sẵn Docker Manager nên cài Vanhanh đúng một cú bấm. Thuê xong quay lại làm các bước dưới.

VPS Hostinger → **Docker Manager → Compose → URL** → dán **file Hostinger** rồi **Deploy**:
```
https://raw.githubusercontent.com/lequydailb-dotcom/vanhanh/main/docker-compose.hostinger.yml
```
Ô **Environment** của mẫu mới chỉ còn 3 trường cần thiết: `DOMAIN_NAME`,
`VANHANH_ADMIN_USER`, `VANHANH_ADMIN_PASSWORD`, cộng một trường tuỳ chọn
`VANHANH_AUTO_UPDATE` (đặt `true` là Vanhanh tự cập nhật mỗi ngày, bỏ trống thì cập
nhật bằng nút trong app). Các biến kỹ thuật về cổng, state, brain và thư mục chạy
đã được ẩn vì Docker image tự đặt đúng.

Đặt `DOMAIN_NAME` để Traefik của Hostinger cấp HTTPS:
- **Link miễn phí** (không cần mua tên miền): `DOMAIN_NAME=vanhanh.<hostname-vps>.hstgr.cloud`
  (hostname xem ở hPanel → VPS, vd `vanhanh.srv1234567.hstgr.cloud`).
- **Tên miền riêng:** `DOMAIN_NAME=tenmien.com` + trỏ DNS A về IP VPS.

Deploy → đợi 1-3 phút Traefik cấp SSL → mở `https://<DOMAIN_NAME>`. (Chi tiết + xử lý sự cố: [DEPLOY.md](../../../DEPLOY.md).)

> Chỉ muốn chạy nhanh bằng `http://<ip>:7777` (chưa cần tên miền): dùng `docker-compose.yml` (Cách 2).

**3 việc làm 1 lần:**
1. **Để image GHCR ở chế độ Public:** GitHub → repo → **Packages** → `vanhanh` → *Package settings* → Visibility = **Public**.
2. **Tạo tài khoản admin** (chọn 1):
   - *Khuyến nghị:* điền sẵn `VANHANH_ADMIN_USER` + `VANHANH_ADMIN_PASSWORD` đang có trong ô Environment → mở app **đăng nhập luôn**.
   - *Hoặc:* bỏ trống rồi mở app **ngay sau khi deploy** và tự đặt tên đăng nhập + mật khẩu (tối thiểu 8 ký tự). Lưu ý: khi chưa có admin, ai mở link trước sẽ tạo được tài khoản, nên đừng để trống lâu.
   - Vào được rồi thì **bật 2FA** (xem [Bảo mật & tài khoản](../../../docs/14-bao-mat-tai-khoan.md)).
3. **Đăng nhập bộ não:** App terminal → `claude auth login --claudeai` → mở link, dán code. (Dùng gói ChatGPT thì đăng nhập ở trang **Models** sau khi mở app.)

### Cách 2 - Docker trên VPS bất kỳ (pull image, không cần clone)

> 🛒 **Cần thuê VPS?** [VPS Hostinger](https://www.hostinger.com) chạy được cả cách này.

```bash
# Cần Docker (chưa có?  curl -fsSL https://get.docker.com | sh)
mkdir vanhanh && cd vanhanh
curl -fsSLO https://raw.githubusercontent.com/lequydailb-dotcom/vanhanh/main/docker-compose.yml

docker compose run --rm vanhanh claude auth login --claudeai   # đăng nhập Claude 1 lần
docker compose up -d                                          # pull image + chạy
```
Mở `http://<ip-vps>:7777` → màn tạo tài khoản admin: đặt tên đăng nhập + mật khẩu (tối thiểu 8 ký tự), làm ngay sau khi chạy vì ai mở link trước sẽ tạo được admin (hoặc đặt sẵn `VANHANH_ADMIN_USER` + `VANHANH_ADMIN_PASSWORD` trong env). Vào được rồi thì bật 2FA.

### Cách 3 - Cài trực tiếp lên Linux/macOS (không Docker)

```bash
git clone https://github.com/lequydailb-dotcom/vanhanh.git vanhanh && cd vanhanh
chmod +x install.sh && ./install.sh
```
Script tự cài Python + Node + hai engine CLI (Claude Code, Codex), tạo venv, đăng ký dịch vụ systemd tự chạy khi boot, in ra địa chỉ. Báo Claude chưa đăng nhập thì chạy 1 lần: `claude auth login --claudeai`.

> 🍎 **macOS - mở như một app:** sau khi cài xong, double-click `VANHANH.app` (hoặc `Start VANHANH.command`) để chạy server + mở dashboard; `./install.sh` cho Vanhanh tự chạy khi đăng nhập máy và tự mở dashboard (tắt: `./bin/vanhanh-autostart.sh uninstall`). Chi tiết: [bin/README.md](../../../bin/README.md).

### Cách 4 - Windows (máy cá nhân)

**Một lệnh, cài hết:**

```powershell
git clone https://github.com/lequydailb-dotcom/vanhanh.git vanhanh; cd vanhanh
powershell -ExecutionPolicy Bypass -File install.ps1
```

`install.ps1` làm trọn một lượt: Python + venv + thư viện, rồi **cả bốn bộ não CLI chạy bằng gói thuê bao** (`claude`, `codex`, `agy`, `grok`), tạo `.env`, giải phóng port 7777 và bật server. Cuối cùng nó in một bảng cho biết bộ não nào đã sẵn sàng. Đăng nhập từng bộ não ngay trong **trang Models** của dashboard, không cần gõ lệnh.

Không có `winget` để tự cài Python/Node thì cài tay trước: Python 3.12 (tick "Add python.exe to PATH") và Node.js LTS, rồi chạy lại.

```
Chạy hiện cửa sổ (xem log trực tiếp):  setup.bat
Chạy ngầm từ lần sau:                  start-vanhanh.vbs   (log ở server\vanhanh.log)
Dừng:                                  stop-vanhanh.bat
Mở dashboard:                          http://localhost:7777
```

> ⚠️ **Cài thêm một CLI sau khi Vanhanh đang chạy thì phải khởi động lại Vanhanh** (`stop-vanhanh.bat` rồi `start-vanhanh.vbs`). Tiến trình đang chạy giữ PATH của lúc nó bật, nên CLI vừa cài nó không thấy - trang Models sẽ vẫn báo "CLI chưa cài" cho một CLI đã nằm sẵn trên ổ đĩa.

> 🪟 **Windows - mở như một app:** sau khi `setup.bat` chạy xong lần đầu, từ đó về sau chỉ cần double-click **`VANHANH.bat`** - server tự chạy nền (không cửa sổ đen) rồi dashboard tự mở thành **cửa sổ riêng** không thanh địa chỉ, có ô riêng trên taskbar. Bộ cài cho Vanhanh tự chạy khi đăng nhập máy và tự mở dashboard (tắt: `vanhanh-autostart.bat uninstall` hoặc nút trong Cài đặt).

### Nhiều bản Vanhanh trên cùng một VPS (mỗi bản một link riêng)

Chạy được bao nhiêu bản cũng được - brain, cài đặt và tài khoản của mỗi bản tách bạch hoàn toàn.
Chỉ cần ba giá trị khác nhau giữa các bản: `VANHANH_NAME`, `VANHANH_HOST_PORT`, `DOMAIN_NAME`.

- **Hostinger:** deploy `docker-compose.hostinger.yml` thành stack thứ hai, điền ba ô đó.
- **VPS tự quản:** chạy proxy dùng chung `docker-compose.proxy.yml` **một lần cho cả máy**, rồi
  mỗi bản một thư mục riêng dùng kèm `docker-compose.multi.yml`. Proxy tự phát hiện bản mới,
  tự xin SSL - thêm bản không phải sửa gì ở proxy.
- **Native:** `VANHANH_NAME=vanhanh-shop VANHANH_PORT=7778 ./install.sh`.

Bỏ trống các biến = y hệt cách cài cũ. Từng bước một: **[DEPLOY.md](../../../DEPLOY.md)**.

📄 Chi tiết hơn (named tunnel URL cố định, build từ source…) xem **[DEPLOY.md](../../../DEPLOY.md)**.

---

## 🎬 Thiết lập lần đầu

Mở Vanhanh → bộ cài đặt sẽ dẫn bạn qua:

1. **Tài khoản admin** - đặt mật khẩu (bắt buộc khi chạy public, để chặn người lạ).
2. **Chọn bộ não** - đi bằng gói subscription thì đăng nhập 1 lần, không cần API key: Claude Code lưu token trong `~/.claude` (Docker: volume riêng → không mất khi update), ChatGPT/Codex đăng nhập ngay trong trang **Models**. Đi bằng API key thì chỉ dán key OpenRouter / OpenAI / Gemini / Anthropic là xong. Ở thẻ Claude Code còn một ô **"Chạy bằng"**: giữ gói đang đăng nhập, hoặc chuyển sang API key Anthropic - hai lựa chọn giữ nguyên năng lực, chỉ khác ai trả tiền và ai chịu rủi ro (xem cảnh báo ở trên).
3. **Chọn model** - mặc định chọn sẵn Claude Code, nhưng đổi sang nhà cung cấp nào trong **Models** cũng được và **không mất chức năng nào** (trừ chạy lệnh máy, vốn chỉ có ở hai engine CLI).
4. **Đấu kết nối** (tuỳ chọn) - vào **Kết nối**, chọn dịch vụ trong Kho rồi dán key hoặc quét QR. Vanhanh sẽ báo cáo số liệu thật từ đó.

---

## 📖 Hướng dẫn sử dụng

> 📚 **Tài liệu chi tiết:** xem thư mục **[docs/](../../../docs/README.md)** - hướng dẫn từng chức năng (mở ở đâu, bấm gì, dùng thế nào). Bảng dưới là bản đồ nhanh; cột **Chi tiết** dẫn tới trang hướng dẫn tương ứng.

Thanh điều hướng bên trái gom **22 trang** thành **6 nhóm**, hiện hết một lượt; riêng nhóm **Nâng cao** (Terminal, Plugins, Webhook, Cookies, Link chia sẻ) gập lại, bấm tên nhóm để mở:

| Nhóm | Mục | Làm gì | Chi tiết |
|---|---|---|---|
| **Bộ não** | **Đồ thị** | Màn chính khi mở app: đồ thị tri thức, trò chuyện (gõ hoặc nói), cây thư mục brain bên trái. | [Trò chuyện & giọng nói](../../../docs/02-tro-chuyen-va-giong-noi.md) · [Đồ thị tri thức](../../../docs/03-do-thi-tri-thuc.md) |
| | **Trò chuyện** | Khung chat rộng toàn màn hình kèm cột lịch sử hội thoại. | [Phiên hội thoại](../../../docs/04-phien-hoi-thoai.md) |
| | **Tệp tin** | Duyệt brain, **sửa `.md`/`.txt` trực tiếp**, tìm file theo tên/nội dung, tải lên/về. | [Quản lý tệp tin](../../../docs/05-quan-ly-tep-tin.md) |
| | **Tự học** | Vanhanh tự rút ký ức, đúc Wiki, kỹ năng sau mỗi hội thoại; hoàn tác được. | [Tự học](../../../docs/22-tu-hoc.md) |
| **Năng lực** | **Agents** | Tạo trợ lý chuyên biệt (vai trò + skill + bộ nhớ riêng). | [Agents & Workflows](../../../docs/07-agents-va-workflows.md) |
| | **Skills** | Gom nhóm + tìm kiếm + **bật/tắt** + thêm/sửa/xoá + nhập/xuất skill. | [Skills](../../../docs/06-skills.md) |
| | **Workflows** | Tạo/chạy chuỗi tự động (agent → agent), có bước kiểm chứng. | [Agents & Workflows](../../../docs/07-agents-va-workflows.md) |
| | **Plugins** | Thêm tool/hook native cho mọi engine bằng một thư mục Python. | [Plugins](../../../docs/20-plugins.md) |
| | **Chatbot** | Đem Agent ra trả lời khách qua bot Telegram/Zalo/Slack/WhatsApp/Lark riêng, brain riêng. | [Chatbot](../../../docs/25-chatbot.md) |
| | **Hội thoại** | Hộp thư gom mọi cuộc chat khách nhắn cho bot và Zalo cá nhân; đọc lại, tiếp quản khi cần người thật. | [Hội thoại khách](../../../docs/28-hoi-thoai-khach.md) |
| | **Terminal** | **Dòng lệnh thật** của máy chạy Vanhanh, mở ngay trong trình duyệt - khỏi mở SSH. | [Terminal](../../../docs/27-tab-code-terminal.md) |
| **Việc** | **Việc** | Hàng đợi task nền do AI tự đặc tả và tự chạy; bạn chỉ xử lý ngoại lệ. | [Việc (Kanban)](../../../docs/21-viec-kanban.md) |
| | **Việc định kỳ** | Nhiều vòng lặp chạy nền + nhắc hẹn theo giờ hoặc cron. | [Việc định kỳ & Nhắc hẹn](../../../docs/08-viec-dinh-ky.md) |
| **Kết nối** | **Kết nối** | Kho dịch vụ ngoài, đa tài khoản cùng một dịch vụ, phân quyền 3 mức. | [Kết nối & số liệu](../../../docs/09-mcp-va-so-lieu.md) |
| | **Kênh** | Bật bot Telegram, Zalo, Slack, WhatsApp (hỏi Vanhanh qua điện thoại). | [Kênh Telegram](../../../docs/11-telegram.md) · [Kênh Zalo](../../../docs/12-zalo.md) · [Slack và WhatsApp](../../../docs/29-slack-whatsapp.md) |
| | *(terminal)* | `pip install vanhanh-cli` rồi gõ `vanhanh "..."` - kênh thứ ba, cùng một Vanhanh. | [Vanhanh CLI](../../../docs/24-cli-terminal.md) |
| | **Models** | Main model + các provider + mức suy nghĩ + model việc nền. | [Models & engine](../../../docs/10-models-va-engine.md) |
| **Hệ thống** | **Mức dùng** | Token và chi phí theo ngày, theo nhà cung cấp, theo nguồn phát sinh. | [Mức dùng](../../../docs/23-muc-dung-token.md) |
| | **Cài đặt** | Trạng thái hệ thống, giao diện & brain, giọng nói, thương hiệu, tên miền. | [Bắt đầu & thiết lập](../../../docs/01-bat-dau-thiet-lap.md) |
| | **Linh vật** | Hình dáng, bảng màu và bật tắt con pet nép ở mép màn hình. | [Bắt đầu & thiết lập](../../../docs/01-bat-dau-thiet-lap.md) |
| | **Cập nhật** | Phiên bản hiện tại, cập nhật/Redeploy, tiến trình và nhật ký tính năng mới. | [Khắc phục sự cố](../../../docs/17-khac-phuc-su-co.md) |
| | **Tài khoản** | Workspace, đăng nhập/đăng xuất, đổi/tắt mật khẩu, token API cho CLI. | [Bảo mật & tài khoản](../../../docs/14-bao-mat-tai-khoan.md) · [Vanhanh CLI](../../../docs/24-cli-terminal.md) |

**Mục lục đầy đủ (27 trang):** [docs/README.md](../../../docs/README.md) - gồm thêm [Second Brain: bộ nhớ / Wiki / INGEST](../../../docs/13-second-brain-bo-nho-wiki.md), [Sao lưu brain lên GitHub](../../../docs/18-sao-luu-github.md), [Task & Dataview trong note](../../../docs/19-task-va-dataview.md), [Thương hiệu & tên miền riêng](../../../docs/15-thuong-hieu-ten-mien.md), [Cấu hình .env](../../../docs/16-cau-hinh-env.md).

### Vài luồng hay dùng

- **Hỏi số liệu:** *"Doanh thu hôm nay thế nào? So với hôm qua?"* → Vanhanh gọi đúng kết nối, trả số thật + đề xuất.
- **Tiêu hoá tri thức (INGEST):** thả file/ghi chú vào → Vanhanh tóm tắt, rút insight, viết vào Wiki, gợi ý task.
- **Giao việc nền:** vào **Việc** → **+ Giao goal** → mô tả bằng lời (vd *"tổng hợp bán hàng tuần này, tìm hàng bán chậm, soạn 3 caption đẩy hàng"*) → AI tự đặc tả và chạy, báo kết quả về Telegram.
- **Việc định kỳ:** vào **Việc định kỳ** → **+ Thêm việc** → chọn *Việc lặp* (mỗi N phút) hoặc *Nhắc hẹn* (8h30 mỗi ngày).
- **Giọng nói:** bấm mic (hoặc bật rảnh tay) → nói → Vanhanh trả lời bằng giọng.

---

## ⚙️ Cấu hình (`.env`)

Mọi dòng để trống vẫn chạy được. Sao chép `env.example` → `.env` rồi thêm biến bạn cần.

File mẫu cố ý **chỉ có dòng `TÊN=giá trị`, không một dòng chú thích nào**: các nền tảng deploy (Docker Manager của Hostinger chẳng hạn) tự quét file cấu hình trong repo rồi cắt mọi dòng có dấu `=` thành một biến, nên một dòng chú thích thành một biến tên `#` và cả bảng Environment đỏ lên. **Danh sách đầy đủ kèm giải thích từng biến: [docs/16-cau-hinh-env.md](../../../docs/16-cau-hinh-env.md).**

| Biến | Ý nghĩa | Mặc định |
|---|---|---|
| `VANHANH_HOST` | Địa chỉ nghe. `127.0.0.1`=chỉ máy này; `0.0.0.0`=public | `127.0.0.1` |
| `VANHANH_PORT` | Cổng | `7777` |
| `VANHANH_REQUIRE_LOGIN` | `1`/`0` ép bật/tắt bắt buộc đăng nhập (mặc định: bật khi bind public) | *(auto)* |
| `VANHANH_ADMIN_USER` / `VANHANH_ADMIN_PASSWORD` | Tạo sẵn admin lúc deploy (khuyến nghị khi chạy public) | - |
| `VANHANH_ALLOWED_HOSTS` | Thêm hostname vào danh sách cho phép (chống CSRF / DNS-rebinding) | localhost + tên miền đã đặt |
| `VANHANH_SECURE_COOKIE` | Ép cookie `Secure`. Chỉ bật khi chắc chắn HTTPS đầu-cuối | *(auto theo tên miền)* |
| `VANHANH_STATE_DIR` | Nơi ghi state (settings, sessions, khoá mã hoá, cấu hình việc định kỳ) | `server/` (Docker: `/data/state`) |
| `BRAINS_DIR` | Thư mục CHA chứa mọi brain | `brains/` (Docker: `/brains`) |
| `OBSIDIAN_VAULT_PATH` | Vault Second Brain ngoài (nếu bạn đã có vault sẵn) | `vault/` (Docker: `/data/vault`) |
| `CLAUDE_CWD` | Thư mục dự phòng của bộ não Claude (chat chạy trong thư mục brain) | repo root |
| `VANHANH_ENABLE_USER_PLUGINS` | `false` để tắt plugin do bạn cài (chúng chạy code Python thật trong server) | *(bật)* |
| `WATCHTOWER_TOKEN` | Token cho nút "Cập nhật ngay" trên bản Docker | `vanhanh-update` |
| `TTS_VOICE` / `TTS_RATE` | Giọng đọc + tốc độ (Edge TTS) | `en-US-EmmaMultilingualNeural` / `+5%` |

Danh sách đầy đủ mọi biến: [docs/16 - Cấu hình .env](../../../docs/16-cau-hinh-env.md).

---

## 🔐 Bảo mật

- Khi chạy public, **bắt buộc đăng nhập** trước khi dùng bất kỳ chức năng nào (bộ não chạy full quyền trên máy).
- Màn chạy lần đầu chỉ hỏi tên đăng nhập + mật khẩu. Trên server public, **ai mở link trước khi có admin sẽ tạo được admin** → đặt sẵn admin qua env (`VANHANH_ADMIN_USER` + `VANHANH_ADMIN_PASSWORD`) hoặc tạo tài khoản ngay sau khi deploy, rồi **bật 2FA** (TOTP).
- **Rate-limit** đăng nhập (khoá tạm sau nhiều lần sai), mật khẩu ≥ 8 ký tự, cookie `secure` khi HTTPS, session hết hạn 30 ngày.
- **Chặn CSRF và DNS-rebinding**: mọi request ghi có Origin lạ đều bị từ chối.
- **Khoá bí mật được mã hoá** trong `settings.json` (API key, token OAuth, token bot Telegram, token backup) bằng khoá riêng của máy ở `VANHANH_STATE_DIR/.secret_key`.
- **Plugin do bạn cài được tải mặc định, nhưng từng plugin vẫn tắt cho tới khi bạn bật nó trong app**; đặt `VANHANH_ENABLE_USER_PLUGINS=false` nếu muốn tắt hết.
- Truy cập từ xa nên qua **HTTPS** (Hostinger `*.hstgr.cloud` hoặc Cloudflare Tunnel) - đừng phơi cổng thô.

---

## 🔄 Cập nhật

```bash
# Trên máy bạn (sau khi sửa code): đẩy lên GitHub
git add -A && git commit -m "..." && git push     # → CI tự build image mới lên GHCR

# Trên VPS: kéo bản mới
cd vanhanh && ./update.sh          # tự pull image + restart (dữ liệu trong volume KHÔNG mất)
```

Trong app: mở **Cập nhật** (nhóm Hệ thống) → **⬆ Cập nhật ngay** nếu môi trường hỗ trợ, có thanh tiến trình và nút lùi bản khi bản mới hỏng.

## 🌐 Truy cập từ xa (VPS không phải Hostinger)

```bash
docker compose --profile tunnel up -d
docker compose logs tunnel | grep trycloudflare   # → URL https://xxx.trycloudflare.com
```

---

## 🏗️ Kiến trúc

```
Trình duyệt (voice + đồ thị) ─┐                        ┌→ Claude Agent SDK   (gói Claude)
Telegram ─────────────────────┤→ FastAPI (server/) ────┼→ Codex CLI          (gói ChatGPT)
Zalo Agent MCP ──────────────┤          │             └→ OpenRouter / OpenAI / Gemini / Anthropic API
                              │          ├→ MCP Hub  (kho Kết nối dùng chung cho MỌI engine)
                              └──────────┴→ Second Brain (vault markdown: Memory + Wiki + Sources)
```
- **Backend:** Python FastAPI trong `server/`.
  - Bộ não & engine: `claude_sdk_engine.py` (engine Claude, qua Claude Agent SDK), `claude_cli.py` (factory + auth cho Claude/Codex), `engine.py` (năm engine API kèm vòng gọi tool MCP), `aux_engine.py` (chọn engine cho việc nền + chuỗi dự phòng khi engine chết).
  - Công cụ: `mcp_hub.py`, `mcp_store.py`, `mcp_client.py`, `mcp_catalog.py`, `plugins_host.py`, `oauth_mcp.py`.
  - Việc nền: `self_improve.py` (việc định kỳ), `reminders.py` (nhắc hẹn), `tasks.py` + `task_store.py` (Kanban), `learn.py` (tự học).
  - Dữ liệu: `sessions.py`, `compaction.py`, `git_brain.py`, `media_gc.py`, `usage_index.py` + `usage_store.py`.
  - Kênh: `telegram_bot.py`, `channel_context.py`; Zalo đi qua MCP Hub.
  - Nền tảng: `main.py`, `routes/` (domain, graph), `config.py`, `web_security.py`, `secrets_store.py`.
- **Frontend:** HTML/CSS/JS thuần (`dashboard/`) - không framework, nhẹ cho VPS.
- **Second Brain:** vault markdown trong `brains/<tên brain>/` - bộ nhớ sống + Wiki tích luỹ.

---

## 🩺 Khắc phục sự cố

| Hiện tượng | Cách xử lý |
|---|---|
| Sửa code mà không thấy đổi | Đã đổi `.py`? **Khởi động lại server** (Windows: `stop-vanhanh.bat` → `start-vanhanh.vbs`). Đổi giao diện? **Ctrl+Shift+R**. |
| Port 7777 bị giữ, bản mới không lên | Kill tiến trình cũ TRƯỚC (`stop-vanhanh.bat`, hoặc `taskkill /F /PID <pid>`), rồi start lại. |
| Hostinger không pull được image | Để package GHCR = **Public**; đợi GitHub Action build xong (tab Actions). |
| Bộ não báo chưa đăng nhập | Vào **Models**, thẻ nhà cung cấp tương ứng, bấm đăng nhập. Hoặc chạy 1 lần `claude auth login --claudeai` (Docker: trong App terminal). |
| Ảnh cũ trong hội thoại hiện ô xám | Đúng thiết kế: `attachments/` là vùng cache, hết hạn 30 ngày hoặc 300MB. Xem [Khắc phục sự cố](../../../docs/17-khac-phuc-su-co.md). |

---

## 📂 Cấu trúc thư mục

```
vanhanh/
├── server/              # Backend FastAPI (engine, kết nối, việc nền, kênh, bộ nhớ…)
│   └── routes/          # Route tách riêng (tên miền, đồ thị)
├── dashboard/           # Frontend (voice, đồ thị, console, studio, usage)
│   └── i18n/            # Từ điển chữ trên giao diện, mỗi ngôn ngữ 1 file JSON
├── brains/              # MỌI second brain (brain mặc định: brains/Brain Default)
├── system/              # Đi kèm app: plugin bundled, skill hệ thống, kho kết nối mẫu
├── tests/               # Bộ test Python
├── docs/                # Hướng dẫn sử dụng chi tiết (27 trang + mục lục; bản tiếng Anh ở docs/en/)
├── Dockerfile           # Image: python + Node + Claude CLI
├── docker-compose.yml   # Production (pull image GHCR) - VPS thường, vào bằng http://<ip>:7777
├── docker-compose.hostinger.yml  # Cho Hostinger: tên miền + HTTPS qua Traefik (đặt DOMAIN_NAME)
├── docker-compose.https.yml      # Auto-HTTPS bằng Caddy cho VPS thường (kèm file trên)
├── install.sh           # Cài native Linux/macOS
├── update.sh            # Cập nhật trên VPS
├── env.example          # Mẫu biến môi trường
├── VERSION · CHANGELOG.md
├── QUICKSTART.md        # Bắt đầu nhanh (QUICKSTART.en.md: bản tiếng Anh)
├── DEPLOY.md            # Hướng dẫn deploy chi tiết
└── CLAUDE.md            # "System prompt" + quy ước cho AI agent
```

---

## 🤝 Đóng góp

Báo lỗi, góp ý, bản dịch và Pull Request đều được chào đón, viết tiếng Việt hay tiếng Anh đều được.
Đọc [hướng dẫn đóng góp](CONTRIBUTING.md) trước (cách dựng môi trường, chạy test, quy ước code).
Người đóng góp quốc tế có [ARCHITECTURE.md](../../../ARCHITECTURE.md) và
[Quy tắc ứng xử](../../../CODE_OF_CONDUCT.md); lỗi bảo mật báo riêng theo [SECURITY.md](../../../SECURITY.md).

---

## 🙏 Cảm hứng & ghi nhận

- **Bộ não:** [Claude Code](https://claude.com/claude-code) và [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) (Anthropic), [Codex CLI](https://developers.openai.com/codex/cli) (OpenAI), cùng API của [OpenRouter](https://openrouter.ai), OpenAI, [Google Gemini](https://ai.google.dev), Anthropic và [Groq](https://groq.com).
- **Chuẩn công cụ:** [Model Context Protocol](https://modelcontextprotocol.io) - toàn bộ kho Kết nối của Vanhanh chạy trên chuẩn này.
- Pattern Second Brain + Bullet Journal số hoá.

---

## 📄 Giấy phép

Bản quyền © 2026 Đại Lê ([lequydai.com](https://lequydai.com)). Bảo lưu mọi quyền. Thành viên cộng đồng VANHANH được tải về, cài đặt và dùng miễn phí. Xem [LICENSE](../../../LICENSE).


<div align="center">

Made with ☕ by **[Đại Lê](https://lequydai.com)** · Repo: `github.com/lequydailb-dotcom/vanhanh`

</div>
