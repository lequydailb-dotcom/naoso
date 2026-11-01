# Naota CLI - hỏi Naota từ terminal

***Tiếng Việt** · [English](en/24-cli.md)*

Cài một gói nhỏ lên máy tính rồi gõ `naota "doanh thu tuần này thế nào"` ngay trong terminal, không cần mở trình duyệt. Câu trả lời vẫn đến từ chính Naota của bạn: cùng brain, cùng bộ nhớ, cùng MCP đã đấu, cùng lịch sử hội thoại.

> **Đọc dòng này trước:** Naota CLI **không chứa Naota bên trong**. Nó là cái ống nói - đầu kia phải có một máy chủ Naota đang chạy, trên chính máy này hoặc trên VPS. Không có máy chủ thì CLI không làm gì được, và nó sẽ nói thẳng như vậy chứ không báo lỗi mạng mơ hồ.

## Tính năng này là gì

- **Kênh thứ ba**, bên cạnh dashboard web và Telegram. Cùng một Naota, chỉ khác chỗ đứng.
- Hỏi một câu rồi thoát (`naota "..."`), hoặc mở phiên hỏi đáp liên tục (`naota chat`).
- Nối được nhiều Naota: một hồ sơ cho máy nhà, một cho VPS, đổi bằng `--profile`.
- Giao việc Kanban, duyệt brain, xem loop, xem trạng thái máy chủ - đều từ terminal.
- **Ghép được vào script**: câu trả lời ra stdout, mọi thứ khác ra stderr. Nên `naota "tóm tắt tuần này" > bao-cao.md` cho ra đúng nội dung, không dính dòng trạng thái.
- Naota biết mình đang nói qua terminal nên trả lời khác: không bảng markdown, không nhúng ảnh, đường dẫn file in tuyệt đối để bạn copy chạy được luôn.

## Cài đặt

Cần Python 3.9 trở lên. Gói chỉ kéo theo **một** thư viện (`httpx`), cài trên máy chưa từng có Naota vẫn được.

```bash
pip install naota-cli
```

Cài từ mã nguồn (khi bạn đã clone repo Naota):

```bash
pip install ./cli
```

Xong thì có lệnh `naota`. Kiểm tra: `naota --help`.

## Bước 1: tạo token trong dashboard

Máy chủ Naota không nhận lệnh từ bên ngoài nếu chưa có token. **Không có token nào sẵn** - chưa tự tay tạo thì cửa này đóng.

1. Mở dashboard Naota, vào **Tài khoản** (nhóm **Hệ thống** ở cuối thanh bên trái) rồi kéo tới mục **Token API (cho CLI)**. Cùng trang với mật khẩu đăng nhập, vì token cũng là một cách đăng nhập.
2. Đặt tên dễ nhớ, ví dụ "laptop của anh" - sau này thu hồi thì biết đang thu hồi cái nào.
3. Chọn phạm vi:
   - **Chỉ chat** - vào được `/chat`, `/version`, `/health`, `/sessions`. Đủ để hỏi đáp và xem lịch sử. Chọn cái này nếu chỉ định hỏi han.
   - **Toàn quyền** - như đang đăng nhập bằng trình duyệt. Cần cho `naota task add`, `naota brain`, `naota loops`.
4. Bấm **Tạo token**. Chuỗi hiện ra **chỉ hiện đúng một lần**: máy chủ băm nó khi lưu, không có đường nào xem lại. Copy ngay.

Mất token thì không xem lại được, chỉ tạo cái mới rồi thu hồi cái cũ. Đó là cố ý.

## Bước 2: nối CLI vào Naota của bạn

```bash
naota login https://naota-cua-ban.com
```

Nó sẽ hỏi token, bạn dán vào. Hoặc đưa thẳng:

```bash
naota login https://naota-cua-ban.com --token nts_xxxxx
```

CLI **thử kết nối thật** trước khi lưu, nên nếu địa chỉ sai hoặc token sai thì bạn biết ngay tại đây chứ không phải lúc hỏi câu đầu tiên.

Cấu hình lưu ở `~/.naota/config.json`, quyền `600` (chỉ chủ máy đọc được). File này chứa token nên đừng đưa vào repo hay backup công khai.

### Nhiều Naota cùng lúc

```bash
naota login http://localhost:7777 --name nha
naota login https://naota.congty.com --name congty --brain brain-cty
naota --profile congty "tuần này bên công ty thế nào"
naota profiles          # xem các hồ sơ đã lưu, dấu * là mặc định
```

### Đặt bằng biến môi trường (cho CI, Docker, server)

Ba biến này đè lên file cấu hình, tiện khi không muốn ghi token xuống đĩa:

| Biến | Nghĩa |
|---|---|
| `NAOTA_URL` | địa chỉ máy chủ Naota |
| `NAOTA_TOKEN` | token API |
| `NAOTA_BRAIN` | brain dùng mặc định |
| `NAOTA_PROFILE` | tên hồ sơ dùng mặc định |

## Dùng hằng ngày

### Hỏi một câu

```bash
naota "doanh thu tuần này thế nào"
naota "tóm tắt các ghi chú tuần rồi"
```

Không cần lệnh con nào cả - gõ thẳng câu hỏi là chạy. Đang ngồi trước terminal thì bạn thấy dòng tiến độ chạy ở bên (Naota đang gọi MCP nào, đọc file nào), rồi câu trả lời hiện ra.

### Phiên hỏi đáp liên tục

```bash
naota chat
```

Gõ câu, Enter, đọc trả lời, gõ tiếp. Cả phiên dùng chung một mã hội thoại nên Naota nhớ mạch: hỏi "còn tháng trước?" là nó hiểu đang nói về cái vừa nãy. `Ctrl+D` hoặc `/thoat` để ra.

Muốn nối lại đúng mạch cũ ở lần chạy sau thì tự đặt mã phiên:

```bash
naota chat --session ban-hang-thang-8
```

### Ghép vào script

Đây là lý do đáng giá nhất của CLI. Câu trả lời ra stdout, tiến độ ra stderr, nên chuyển hướng là ra file sạch:

```bash
naota "viết tóm tắt doanh số tuần này" > bao-cao-tuan.md
naota -q "tình hình hôm nay" | mail -s "Naota" sep@congty.com
```

Cờ `-q` tắt luôn dòng tiến độ. Thất bại thì CLI thoát khác 0 và **không in gì ra stdout**, nên `&&` trong script hành xử đúng.

### Xem trạng thái

```bash
naota status
```

Cho biết phiên bản Naota, có bản mới không, đang chạy bộ não nào, mức tiết kiệm token đang đặt ở đâu, và 24 giờ qua tiết kiệm được bao nhiêu phần trăm.

### Giao việc, duyệt brain, xem loop

Những lệnh này cần token **toàn quyền**.

```bash
naota task add "soạn bài đăng về sản phẩm mới"     # giao một việc Kanban
naota task add "chạy báo cáo tháng" --mode auto     # suggest (mặc định) | auto | full
naota tasks                                          # xem các việc và cột đang đứng

naota brain ls                                       # liệt kê thư mục gốc brain
naota brain ls "05 - Data Cache"
naota brain cat "Memory/MEMORY.md"

naota loops                                          # loop nào đang bật, mức quyền gì
```

Việc giao xong chạy nền trên máy chủ. Kết quả tự về đúng nơi bạn giao việc, xem tiến độ ở trang **Việc** trên dashboard hoặc gõ lại `naota tasks`.

### Bật Naota trên chính máy này

Nếu máy bạn đã cài Naota (clone repo về):

```bash
naota up
```

Nó tìm bản cài (qua biến `NAOTA_HOME`, thư mục hiện tại, hoặc `~/naota`), bật lên rồi lưu sẵn hồ sơ `local` để lần sau `naota "..."` là chạy. Naota đang chạy sẵn rồi thì nó nhận ra và không bật thêm cái thứ hai.

Không tìm thấy bản cài thì nó nói thẳng: **`naota up` không chứa server bên trong**, và chỉ ba cách xử lý (đặt `NAOTA_HOME`, chạy từ trong thư mục Naota, hoặc `naota login` tới một Naota ở nơi khác).

## Quản lý token

Vào **Tài khoản > Token API** trong dashboard. Danh sách hiện tên, 12 ký tự đầu, phạm vi, và **lần dùng cuối** - nếu thấy một token bạn không nhớ đang được dùng đều đặn thì đó là dấu hiệu cần thu hồi ngay.

Bấm **Thu hồi** là token chết lập tức, máy nào đang dùng nó mất kết nối ngay và không hoàn tác được.

Vài điều đáng biết về cách Naota giữ token:

- **Trên đĩa chỉ có bản băm** (SHA-256). Ai đọc được file cấu hình của máy chủ cũng không lấy được token.
- **Không dùng token để tạo token.** Muốn tạo token mới phải đang đăng nhập bằng trình duyệt. Nếu một token lỡ rò ra, kẻ cầm nó không tự cấp thêm được cái khác - thu hồi là dứt.
- **Nhưng thu hồi thì token tự thu hồi được chính mình.** Mất laptop mà không mở nổi trình duyệt thì vẫn hạ được credential.
- **Sai token quá 10 lần trong 5 phút thì IP đó bị chặn 15 phút**, và mỗi lần sai đều ghi vào `auth_audit.jsonl` (chỉ ghi 12 ký tự đầu, vì file log hay bị gửi kèm báo lỗi). Một cuộc dò token trở thành thứ nhìn thấy được thay vì chạy im lặng hàng tháng.

## Khi có trục trặc

**"Chưa nối tới Naota nào"** - chạy `naota login <địa-chỉ>` trước.

**Báo 401 hoặc "token không hợp lệ"** - token sai, hoặc đã bị thu hồi. Tạo cái mới ở Tài khoản > Token API rồi `naota login` lại.

**Báo 403 khi gõ `naota task add` hay `naota brain ls`** - token của bạn là loại **chỉ chat**. Tạo một token **toàn quyền** cho những lệnh này.

**Bị chặn tạm thời** - sai token quá nhiều lần liên tiếp. Chờ 15 phút, hoặc khởi động lại máy chủ Naota.

**Không kết nối được** - kiểm tra máy chủ Naota còn chạy không (`naota status`, hoặc mở dashboard trong trình duyệt). Nếu Naota nằm trên VPS, kiểm tra cổng và tên miền.

**Chữ tiếng Việt hiện sai trên Windows** - chạy `chcp 65001` trong terminal trước, hoặc dùng Windows Terminal thay cho cmd.exe cũ.

Xem thêm [17 - Khắc phục sự cố & FAQ](17-khac-phuc-su-co.md).

## Vì sao CLI không tự chạy được một mình

Câu hỏi hợp lý: sao không làm hẳn một agent chạy độc lập trong terminal, khỏi cần server?

Vì gần như mọi thứ làm nên Naota đều đòi một tiến trình **sống dài**: loop chạy theo chu kỳ, nhắc hẹn chờ tới giờ, MCP Hub giữ kết nối tới POS và quảng cáo, kho capability giữ registry, runtime tiết kiệm token học dần qua từng lượt. Một CLI gõ xong là thoát không phải chỗ cho những thứ đó.

Làm bản thứ hai nghĩa là chép lại toàn bộ rồi để hai bản trôi lệch nhau - và bản nào ít người dùng hơn thì lỗi cứ nằm im ở đó. Nên CLI đi qua **đúng cái lõi** mà dashboard và Telegram đang dùng. Đổi lại: tính năng mới vào Naota là CLI thấy ngay, không phải sửa hai chỗ.


## Liên quan

- [02 - Trò chuyện & giọng nói](02-tro-chuyen-va-giong-noi.md) - kênh web.
- [11 - Kênh Telegram](11-telegram.md) - kênh điện thoại.
- [14 - Bảo mật & tài khoản](14-bao-mat-tai-khoan.md) - mật khẩu, đăng nhập, mã hoá khoá bí mật.
- [21 - Việc (Kanban)](21-viec-kanban.md) - việc `naota task add` giao vào chạy ở đâu.
