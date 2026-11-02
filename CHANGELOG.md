# Nhật ký cập nhật

***Tiếng Việt** · [English](CHANGELOG.en.md)*

Lịch sử phiên bản NAOTA. Bản mới nhất ở trên cùng. Xem ngay trong app tại mục **Cập nhật** (thanh bên, nhóm Hệ thống).

Định dạng: mỗi phiên bản là một khối `## [x.y.z] - ngày`, bên dưới nhóm thay đổi theo `### Thêm mới / Sửa lỗi / Cải thiện / Bảo mật`.

## [1.1.0] - 2026-11-02
### Thêm mới
- **Bộ cài cho máy tính.** Tải Naota-Setup.exe (Windows) hoặc Naota-macOS.dmg (Mac), mở như mọi ứng dụng, không phải gõ lệnh.
- **Fanpage nối một lần, dùng cho ba việc:** bấm Đăng nhập Facebook là bot trả lời tin nhắn Messenger, trả lời bình luận dưới bài, và Naota đăng bài lên Trang ngay hoặc theo lịch. Có hướng dẫn từng bước.
- **Nghe tin nhắn thoại không cần Groq:** dùng khoá OpenAI, Gemini, hoặc bộ nghe chạy ngay trên máy. Chatbot Zalo cá nhân nghe được tin thoại và xem được video khách gửi.
- **AI bên ngoài giao việc cho Naota:** tìm, đọc và gửi lời nhắn vào một cuộc trò chuyện của Naota như chính bạn gõ, bạn xem được trực tiếp và bấm Dừng khi cần.
### Cải thiện
- **Chữ hiện ra dần khi trả lời** với mọi bộ não: Claude Code, Grok Build, Antigravity và các bộ não dùng khoá API.
- **Trang Webhook làm lại:** tóm tắt gọn một dòng, mỗi webhook mở trong một cửa sổ riêng, tìm quy trình theo tên.
- **Chọn bộ não** bằng danh sách riêng của Naota, giống nhau trên mọi máy và tự sắp được thứ tự. File .html mở ra xem trang ngay, mã ở tab bên cạnh. Dán đoạn dài thì xem trước rồi chọn dán hay đính kèm.
- **Đội ngũ tự thử lại** bước gặp lỗi tạm thời, và mỗi phần của kế hoạch ghi rõ phải chờ phần nào xong trước.
### Sửa lỗi
- Đăng nhập Claude trên máy có trình duyệt tự hoàn tất, không còn chờ mã. Kéo thả file vào khung chat chính chạy lại, ghi nhớ bớt lấy nhầm nhật ký cũ, tên file có dấu giữ đúng khi tải về.
## [1.0.5] - 2026-11-02
### Sửa lỗi
- **Nút Cập nhật trên VPS không còn đứng chờ mãi.** Máy chủ chạy NAOTA bằng tài khoản thường mà chưa cho phép tự cập nhật thì trang báo lỗi ngay, kèm lệnh cập nhật tay và cách bật nút Cập nhật, thay vì chờ 10 phút rồi bảo tải lại trang.

## [1.0.4] - 2026-11-02
### Cải thiện
- **Bộ icon mới** cho cả thanh bên lẫn bên trong app, nét gọn và dễ nhận hơn.
- Mục **Linh vật** đổi tên thành **Avatar**.
- **Cập nhật** ra hẳn thanh bên, ngay dưới **Tài khoản**. Có bản mới thì mục này hiện chấm **Mới**.
- Chữ "brain" sót lại trong giao diện, trang Plugin và trang Tự học đã đổi sang tiếng Việt: **bộ não** là kho ghi chú, **model AI** là Claude, ChatGPT...

## [1.0.3] - 2026-11-02
### Cải thiện
- **Trang Tài khoản và Cài đặt** ghi khối **Tên NAOTA** thay cho chữ Workspace. Trang **Models AI** ghi nhãn **Chính** trên thẻ bộ não chính.

## [1.0.2] - 2026-11-02
### Cải thiện
- **Chợ ứng dụng gọi một tên.** Nút và lời nhắc ở trang Cộng sự, Nguồn dữ liệu, Plugin đều ghi **Chợ ứng dụng**, khớp thanh bên.
- **Bớt chữ tiếng Anh khó hiểu:** trang Học ghi Ghi nhớ, Cộng sự, Quy trình, Bảng việc, **Dọn dẹp định kỳ**; trang Models AI ghi **bộ não chính**; trang Tài khoản ghi **Tên NAOTA của bạn**.

## [1.0.1] - 2026-11-02
### Cải thiện
- **Thanh bên gọn hơn.** Mọi mục hiện một lượt, không phải mở từng nhóm. Mục ít dùng gom vào nhóm **Nâng cao**, nhóm **Hệ thống** ghim ở đáy.
- **Tên menu dễ hiểu hơn:** Sơ đồ, Tài liệu, Ghi nhớ, Đội ngũ, Bảng việc, Nguồn dữ liệu, Chợ ứng dụng, Kênh của tôi, Models AI. Ra lệnh bằng giọng nói nhận cả tên mới.
- **Màn chào mừng nói dễ hiểu hơn.** Chọn bộ não bằng gói bạn đang dùng, vào xong bấm **Đăng nhập Claude** ở **Models AI**, không phải gõ lệnh.
- **Trang chủ toàn tiếng Việt:** Bộ não, Cộng sự, Kỹ năng, Quy trình, số ghi chú.
## [1.0.0] - 2026-10-31
### Thêm mới
- **NAOTA ra đời.** Bộ não AI của riêng bạn, do Hoàng Ngọc Vương phát triển cho cộng đồng NAOTA.
