# Nhật ký cập nhật

***Tiếng Việt** · [English](CHANGELOG.en.md)*

Lịch sử phiên bản VANHANH. Bản mới nhất ở trên cùng. Xem ngay trong app tại mục **Cập nhật** (bấm ô tài khoản dưới đáy thanh bên).

Định dạng: mỗi phiên bản là một khối `## [x.y.z] - ngày`, bên dưới nhóm thay đổi theo `### Thêm mới / Sửa lỗi / Cải thiện / Bảo mật`.

## [1.16.0] - 2026-11-09
### Thêm mới
- **Văn phòng: thấy trợ lý giao việc cho nhau.** Mục mới **Giao việc trong ngày** ghi ai giao việc gì cho ai, lúc mấy giờ, đang làm, xong hay hỏng. Lấy từ trưởng nhóm Team giao cho thành viên, thành viên nhờ nhau, thẻ trên Bảng việc giao cho trợ lý, và các bước nối nhau của Quy trình.
- **Trong 3D**, mỗi lần giao việc là một tờ giấy bay theo vệt đứt nét từ bàn người giao sang bàn người nhận, kèm tên việc; người nhận gõ phím ngay. Việc anh tự giao đi ra từ nhân vật **Bạn** ở mép trước văn phòng. **Phát lại ngày này** cũng phát cả các lần giao việc theo đúng giờ.
- Trợ lý đang làm một bước của Team hay một thẻ việc thì bàn sáng đèn và hiện trong dải **Đang chạy ngay lúc này**. Có việc mới được giao thì trang tải lại ngay.

## [1.15.0] - 2026-11-09
### Thêm mới
- **Văn phòng 3D**: bấm **Xem 3D** trên trang Văn phòng. Mỗi phòng ban một khu, mỗi trợ lý và mỗi việc tự chạy một bàn, đèn trên bàn đúng trạng thái thật.
- **Chạm vào bàn** để xem việc đó: số lượt đạt, lần chạy cuối, lý do dừng và việc nên làm.
- **Đang chạy ngay lúc này**: dải trên cùng trang Văn phòng cho biết việc nào đang chạy ở giây này (vòng lặp, lịch hẹn, việc trên bảng, lệnh chạy nền), chạy từ mấy giờ, đã bao lâu. Hỏi lại hệ thống mỗi 5 giây, đồng hồ đếm từng giây.
- Trong 3D, bàn đang chạy bật **đèn xanh dương**, có nhãn **Đang chạy** và nhân vật gõ phím liên tục; chạy xong là đèn về đúng kết quả và chữ Đạt hoặc Lỗi hiện ngay.
- **Phát lại một ngày**: chọn ngày rồi bấm **Phát lại ngày này**, từng lượt chạy hiện lần lượt theo giờ, chữ Đạt hoặc Lỗi bay lên trên bàn.
- Nhân vật chỉ cử động khi nhật ký có lượt chạy mới. Phần 3D chỉ tải khi bấm nút, máy không vẽ được 3D thì vẫn xem dạng thẻ như cũ.

## [1.14.0] - 2026-11-09
### Thêm mới
- **Trang Văn phòng** (thanh bên, ngay dưới Việc cần làm): mỗi phòng ban một thẻ, đèn xanh là chạy đúng, đỏ nhấp nháy là hỏng hoặc tự tạm dừng, xám là chưa có ai.
- **Mục Cần bạn xử lý**: việc nào tự dừng, lỗi, trễ lịch, chưa đạt chỉ tiêu hay đang chờ duyệt, kèm lý do và việc nên làm.
- **Số liệu thật từ nhật ký**: lượt chạy, lượt hỏng theo giờ của bạn, cập nhật 30 giây một lần; chọn ngày cũ để xem lại.
- **Chỉ tiêu mỗi ngày** đặt trong `Vanhanh/office.json`. Trang chỉ đọc, che token và đường dẫn máy chủ.

## [1.13.1] - 2026-11-08
### Sửa lỗi
- **Tin Zalo đến lúc mạng chập chờn vài giây** nay vào Hộp thư, không chỉ nằm trong lịch sử chat.
- **Một tin Zalo xử lý lỗi** không còn kéo mất các tin đến cùng lượt với nó.
- **Lỗi kết nối Zalo được ghi vào nhật ký** thay vì bị bỏ qua, nên tin bị mất vẫn để lại dấu vết.

## [1.13.0] - 2026-11-08
### Thêm mới
- **Gói ChatGPT nghe được giọng anh**, không tốn thêm tiền ngoài gói. Tai nghe tự theo mô hình đang dùng, không cần cài.
- **Zalo OA kết nối bằng đăng nhập OAuth v4** của Zalo, không phải dán refresh token.
- **Chấp nhận hoặc trả lại một việc** không qua bước tự kiểm, ngay trong chat.
### Cải thiện
- **Review chéo GitHub do anh bật**, mặc định tắt, chạy bằng mô hình của chính chat đó hoặc mô hình chọn trên từng thẻ.
- **Việc không qua bước tự kiểm** được trả về cho người làm sửa, không hỏi anh một câu hỏi rỗng.
- **Đọc chính tả vẫn chạy** khi chuyển tab hoặc chuyển app.
### Sửa lỗi
- **Sau khi cập nhật, trang vẫn ở bộ não của anh**, Nhóm không còn biến mất.
- **Ô chat trang Cộng sự** không còn bị khoá sau khi cập nhật.

## [1.12.0] - 2026-11-08
### Thêm mới
- **Chat của kênh quản trị** hiện trong lịch sử của Vanhanh Core và của agent được nối, kể cả bot Zalo của anh.
- **Thẻ agent hiện tag** ngay dòng dưới tên, cạnh avatar.
### Cải thiện
- **Mở chat và mở trang tức thì** từ bản trình duyệt đã thấy trước đó, rồi cập nhật lại khi máy chủ trả lời.
- **Mở app, đổi trang, đổi chat** chỉ cần một lượt hỏi máy chủ cho mọi thứ cần đọc.
- **Lượt chat, việc Kanban và trang đọc nặng** không còn làm chậm các cú bấm khác.
- **Đọc to** chọn giọng tiếng Anh hay tiếng Việt theo ngôn ngữ của câu trả lời.
### Sửa lỗi
- **App trên iPhone (iOS 26, 27)** không còn dải mờ ở đầu màn hình. Icon đã thêm từ trước phải gỡ ra thêm lại mới hết.
- **Chatbot của khách im lặng** khi gói Claude chạm trần chi tiêu tháng, không gửi câu lỗi tiếng Anh cho khách.

## [1.11.0] - 2026-11-08
### Thêm mới
- **Đặt tên từng tài khoản** ngay lần đăng nhập đầu và đổi tên được sau đó, để hai tài khoản không bao giờ trông giống nhau.
- **Tải ảnh riêng làm avatar** và dùng ảnh đó làm icon trên tab trình duyệt, mở nhiều VANHANH cạnh nhau vẫn phân biệt được.
- **Gửi chat qua API không cần chờ** (`POST /chat/jobs`): gửi việc rồi quay lại lấy kết quả sau.
### Cải thiện
- **Danh sách nhà cung cấp trên trang Models** mở ngay tại chỗ, không bật bảng riêng.
- **Vai trò của trợ lý** nằm trong nút (i) cạnh tên, không còn dòng chữ xám bị cắt giữa chừng.
- **Trang Nhóm** gập phần giải thích và mô tả nhóm vào nút (i).
- **Cuộc gọi với cộng sự** giữ đủ hướng dẫn dài và luật đã ghim.
- **Bỏ trần thời gian** của Grok, Claude Code, ChatGPT, việc nền và Nhóm: việc dài chạy tới cùng, vẫn có nút Dừng.
- **Trang và chuyển chat không còn khựng** khi việc nền đang ghi dữ liệu.
### Sửa lỗi
- **Tin Zalo riêng bị sót** được lấy bù từ lịch sử, chỉ khi lịch sử thật sự có tin mới.
- **Tin thoại Zalo** lại nghe được qua Groq và OpenAI.
- **Antigravity** không còn dừng ở phút thứ 15.
- **Chat chuyển sang tài khoản Claude thứ hai** không còn chết với lỗi "ProcessError exit code 1".
- **PR đã gộp** không còn để biểu tượng "đang chờ kiểm" trong chat.

## [1.10.0] - 2026-11-08
### Thêm mới
- **Gợi ý tin nhắn kế tiếp** hiện mờ trong ô chat trống, bấm Tab là điền vào.
- **Chấm đỏ chưa đọc** trên mọi danh sách lịch sử chat, tắt khi anh mở chat đó.
- **Chọn giọng ChatGPT Live riêng** cho từng cộng sự.
- **Tắt việc hẹn giờ trên một máy**, để hai máy chạy cùng bộ não không làm trùng việc.
### Cải thiện
- **Cuộc gọi với cộng sự** tự giới thiệu đúng tên cộng sự đó, không xưng là trợ lý chính.
- **Agent trong quy trình** chưa chọn mô hình riêng thì chạy bằng mô hình chính, không tự rơi về Claude.
- **Trang Chatbot** mở nhanh hơn khi hòm thư có nhiều hội thoại.
### Sửa lỗi
- **Chat không còn kẹt "Mất kết nối tới máy chủ"** chỉ vì một tin lỗi hoặc phiên đăng nhập đã hết hạn.

## [1.9.0] - 2026-11-07
### Thêm mới
- **Trang Link chia sẻ làm lại:** đổi được địa chỉ sau `/s/`, đếm lượt xem từng link, tìm, lọc, sắp xếp và phân trang.
- **Mã QR** cho mọi link chia sẻ.
- **Cloudflare là kết nối dựng sẵn**, nằm cạnh GitHub, vào bằng token hoặc đăng nhập web.
- **Mỗi ngày một việc ưu tiên** gắn sao.
- **Âm thanh khi tick việc**, có nút bật tắt cạnh nút sáng tối.
- **Thói quen lỡ hẹn** có thêm nút Bỏ qua và Xoá.
- **Mọi thứ trong Của tôi đều lên thông báo**, không chỉ một phần như trước.
### Cải thiện
- **Đọc chính tả viết lại câu:** chữ hiện ngay trong ô chat, nói xong mô hình viết lại đúng ngữ cảnh rồi mới gửi. Lỗi thì giữ nguyên câu đã nghe.
- **Mic nghe đúng tên AI** như Groq, Claude, Gemini, không còn đẩy từ của anh ra xa.
- **Đẩy mã GitHub lỗi tự thử lại**, và chạy tiếp ngay khi GitHub được nối lại.
- **Gộp mã GitHub vẫn chạy** khi đóng bảng hoặc đóng tab.
- **Danh sách repo GitHub** theo kiểu trang Việc cần làm.
- **Ô mô hình trong chat** hiện đúng mô hình đang trả lời khi phải chuyển sang thẻ dự phòng.
### Sửa lỗi
- **Không mất tin nhắn** khi vừa gửi đã chuyển app trên điện thoại: tin được giữ tới khi máy chủ nhận.
- **ChatGPT Live hết lượt** tự chuyển sang tài khoản hoặc đường gọi khác, không kẹt trên gói đã hết.
- **Android** không còn mất chữ hay lặp chữ khi đọc chính tả.
- **Đẩy GitHub từ chat** không còn kẹt vì việc kiểm của hệ điều hành khác.
- **Biểu tượng GitHub trong chat** không còn đứng màu cam sau khi đã gộp xong.
- **Review chéo GitHub** không còn chọn gói không chạy được việc đó.
- **iPhone:** menu không còn đè ô chọn ngôn ngữ, app thêm vào màn hình chính bấm lại đúng chỗ.
- **Nút + trang Việc cần làm** trên điện thoại không còn che dòng cuối.
- **Không còn bong bóng trả lời rỗng** khi quay lại một chat đang chạy.

## [1.8.1] - 2026-11-07
### Sửa lỗi
- **Nick Zalo rớt đăng nhập thì chuông báo ngay:** trước đây bot im mà chủ không hay biết, vì lỗi chỉ nằm trong nhật ký máy chủ. Nay chuông và Telegram báo rõ nick nào cần đăng nhập lại, và thẻ bot nói đúng lý do.

## [1.8.0] - 2026-11-05
### Bảo mật
- **Đóng nhiều đường rò từ đợt rà soát:** chatbot và việc nền dưới mức Toàn quyền không còn ghi được vào chỗ chứa mã chạy, việc hẹn giờ không vượt mức quyền của người tạo, file HTML mở từ bộ não chạy trong hộp cách ly, trang lạ trên máy không gửi lệnh vào VANHANH được.
### Thêm mới
- **Trang Models mới:** nút Ngắt kết nối trên mọi thẻ, OpenAI Compatible và Claude Compatible thêm được nhiều key và tự chuyển key khi hết lượt, Antigravity trên VPS thêm được tài khoản (phần này chưa thử với `agy` thật).
- **Vanhanh Core sửa như một trợ lý**, đổi được tên riêng theo từng bộ não. **Một bot phục vụ tới 100 Trang Facebook.** Avatar có menu tự sắp xếp, gọi thoại từ chat trợ lý thì nói đúng vai trợ lý đó.
### Cải thiện
- **Việc nền bằng API key chạy tới cùng**, tới 500 vòng công cụ, mức Toàn quyền có terminal thật. **Chat sửa được mọi việc và lịch hẹn** trong Việc cần làm.
- **Nhanh và gọn hơn:** chuyển chat, Việc cần làm, Nhóm và Trợ lý tức thì, mic chép lời có ở hộp trả lời khách, Enter là gửi, trên Android không còn lặp từ.

## [1.7.0] - 2026-11-05
### Thêm mới
- **Việc của tôi có Nhịp hôm nay**: chuỗi Ngày sạch, gắn sao tối đa 3 việc ưu tiên, Bỏ qua lần này cho việc lặp, icon Dời và Xoá ngay trên dòng (xoá nhầm thì bấm Hoàn tác), và lời khen khi xong việc.
- **Lượt trả lời dài xong thì báo điện thoại**: từ 3 phút trở lên chuông sẽ rung, máy đang mở thì thôi. Lệnh chạy ngầm xong tự báo về đúng khung chat rồi làm tiếp phần đã hẹn.
### Cải thiện
- **Việc hẹn giờ tạo trong chat Cộng sự** báo về đúng chat đó và chạy đúng vai trợ lý đó, sự cố cũng báo về nơi giao việc. Việc đã tạo trước đây vẫn chạy như cũ. Lịch chạy bằng Codex giờ giao được việc cho Nhóm.
- **Hộp thư mở hội thoại tức thì**, chỉ tải phần tin mới. **Tên gói Claude hiển thị đúng** theo nhà cung cấp (ví dụ Ultra).

## [1.6.1] - 2026-11-04
### Thêm mới
- **Nút Sửa Agent ngay trong form Chatbot**: sửa Agent của bot tại chỗ, phần đang nhập trong form vẫn còn nguyên.
### Sửa lỗi
- **Luật dạy Trợ lý trong chat giờ tới được bot**: bot ở mọi mức quyền đều làm theo, không cần chép lại vào file Agent.
- **Bot đọc được danh thiếp Zalo**: khách gửi danh thiếp thì bot và Hộp thư thấy tên và số điện thoại.
- **Bot mức Chỉ đọc, Đọc tài liệu, Được ghi biết giờ hiện tại**: khách hỏi hôm nay hay giờ làm việc, bot không còn phải đoán.

## [1.6.0] - 2026-11-04
### Thêm mới
- **Threads vào thẻ Kết nối Meta**: bình luận dưới bài Threads về Hộp thư, bot trả lời công khai được. Mỗi tài khoản chọn tắt, chỉ hiện Hộp thư, hoặc bot trả lời. Threads chỉ cho ẩn bình luận chứ không cho xoá, VANHANH nói rõ và hỏi lại trước khi làm.
- **Nhóm làm được nhiều hơn**: gắn repo GitHub (sửa trên nhánh riêng, mở PR, CI đỏ tự giao sửa tối đa 3 vòng), gọi `/skill` trong chat Nhóm, và thành viên tự mở việc khi được giao từ khung chat, mặc định tối đa 5 việc mỗi ngày.
- **Việc của tôi có Tags và việc con**: Dự án cũ tự thành tag, không mất gì. Ghi chú gắn được link, `[[note]]` và file.
- **Kênh API nội bộ (thử nghiệm)**: một máy chủ của bạn hỏi Chatbot qua HTTP. Khoá hiện một lần, bot chỉ đọc, mặc định chỉ chính máy chạy VANHANH gọi được.

### Cải thiện
- **Kéo thả sắp xếp** Project, chat đã ghim và tag, mọi máy thấy cùng thứ tự. Thẻ Vanhanh Core nói rõ đang chạy model nào và chọn được ngay trên thẻ. Điện thoại có nút **Cài lên điện thoại** trong menu.
- **Claude Code chờ việc chạy nền xong** rồi trả lời tiếp, tối đa 30 phút. Câu trả lời cho tin nhắn thêm giữa chừng hiện ngay dưới tin đó. Antigravity hết báo nhầm là không đọc được file ngữ cảnh.

## [1.5.0] - 2026-11-04
### Thêm mới
- **Nhắn riêng cho người bình luận** ngay trong hội thoại bình luận: chọn Trả lời công khai hoặc Nhắn riêng phía trên ô soạn. Meta cho một lần mỗi bình luận, trong vòng 7 ngày.
- **Instagram vào chung Hộp thư**: tick "Nối cả Instagram của Trang" khi kết nối, tin nhắn và bình luận Instagram về cùng chỗ, cùng bot với Trang.
- **Menu "..." của mỗi hội thoại** có thêm Xem trang cá nhân, Chặn, Xoá hội thoại. VANHANH luôn hỏi lại trước khi Xoá, vì xoá bình luận hay hội thoại Zalo cá nhân là xoá thật trên đó.

### Cải thiện
- Thẻ Facebook Messenger đổi thành **Kết nối Meta**, có icon từng ứng dụng, thêm nút **Gỡ kết nối** từng Fanpage. Hội thoại cũ vẫn giữ. Bình luận và Instagram có icon riêng để dễ phân biệt trong Hộp thư.

## [1.4.0] - 2026-11-03
### Thêm mới
- **Chọn múi giờ** ở **Cài đặt** (khối Ngôn ngữ và múi giờ) và ở bước cuối bộ cài lần đầu. "Hôm nay, hôm qua", nhắc hẹn và số liệu báo cáo tính theo múi giờ đó, kể cả khi máy chủ chạy giờ UTC. Mặc định là giờ Việt Nam.

### Sửa lỗi
- **Hết đơ máy lúc VANHANH đang trả lời**, và hết cảnh "Đang kết nối lại" lặp đi lặp lại trên máy hay mạng chậm.
- **Máy chủ nhỏ (VPS 1-2 nhân) không còn đứng hình** vì vài việc chậm chạy chặn cả app. Bộ nghe tin thoại chừa lại một nhân cho máy chủ.
- **Báo hết hạn mức 5 giờ của gói Claude ghi giờ mở lại theo múi giờ của bạn**, không còn theo giờ UTC.
- Windows: kết nối chạy bằng `npx` không còn hỏng khi đường dẫn có dấu cách, và link dạng `/C:/...` trong câu trả lời bấm mở được.

### Cải thiện
- **Mở chat mới bằng Claude Code đỡ tốn hạn mức**: phần lời dặn hệ thống giữ y nguyên giữa các chat để đọc lại từ bộ nhớ đệm.
- Bảng từ 4 cột trở lên trong Trò chuyện được rộng hơn trên máy tính, chữ thường vẫn giữ khổ dễ đọc.

## [1.3.6] - 2026-11-03
### Sửa lỗi
- **Trên điện thoại, bấm nút Cập nhật ở đáy menu thì menu tự đóng**, trang Cập nhật hiện ra ngay. Trước đây trang đã chuyển nhưng menu vẫn che.
- **Bấm Nâng cao trên điện thoại không còn làm menu đóng mất**, nên chọn được các mục bên trong.

## [1.3.4] - 2026-11-03
### Sửa lỗi
- **Bot Zalo trong nhóm nhận ra khi được tag bằng tên Zalo của nick**, kể cả ngay sau khi máy chủ khởi động lại. Trước đây VANHANH quên tên đó mỗi lần khởi động lại, nên tag nick bằng tên khác với tên kết nối thì bot im.

## [1.3.3] - 2026-11-03
### Sửa lỗi
- **Trang Chatbot ghi đúng tên bộ não đang chọn**, không còn hiện chữ "brain" hay đường dẫn thư mục. Phần giải thích mức **Được ghi** và **Toàn quyền** của bot cũng ghi "bộ não".

## [1.3.2] - 2026-11-03
### Cải thiện
- **Tiêu đề trang khớp tên trên thanh bên**: Bản đồ bộ não, Việc cần làm, Trợ lý, Kết nối dữ liệu, Kênh của tôi, Chọn Models.
- **Trên điện thoại, ô chọn bộ não nằm đầu menu**, mở menu ra là thấy ngay đang ở bộ não nào.

## [1.3.1] - 2026-11-03
### Cải thiện
- Chỉ đổi số phiên bản. Hai thay đổi định đưa vào bản này nằm ở bản 1.3.2.

## [1.3.0] - 2026-11-03
### Cải thiện
- **Thanh bên mới một cột**: các mục chia khúc có tên nhỏ (Đội ngũ, Kiến thức, Kết nối, Hệ thống).
- **Tên mục dễ hiểu hơn trên thanh bên**: Bản đồ bộ não, Trò chuyện, Việc cần làm, Trợ lý, Kết nối dữ liệu, Chọn Models.
- **Số phiên bản và nút Cập nhật luôn hiện dưới đáy thanh bên**, có bản mới thì nút chuyển vàng.
- **Nâng cao nằm dưới Tài khoản**, bấm là xổ Terminal, Plugin, Webhook, Phiên đăng nhập, Link chia sẻ và Cộng đồng VANHANH. Ngôn ngữ chọn trong Cài đặt. Các trang và thanh trên giữ nguyên như 1.2.1.

## [1.2.1] - 2026-11-03
### Cải thiện
- **Chợ ứng dụng có Vanhanh Gate**: ChatGPT, Claude nối vào Vanhanh qua một gói, đọc và nhắn vào hội thoại, ghi sổ tay. Máy đã cài gói **Vanhanh trong ChatGPT** thấy Gate như một bản cập nhật, không phải nối lại.
- **14 gói của Chợ ứng dụng đổi sang mã tiếng Anh**, ví dụ Quản lý khách hàng là `vanhanh.crm`. Gói đã cài hiện **Có bản mới** và cập nhật tại chỗ, giữ nguyên dữ liệu.

## [1.2.0] - 2026-11-03
### Thêm mới
- **ChatGPT, Claude ghi sổ tay vào Vanhanh.** Khi bạn bàn việc với một AI bên ngoài đã nối vào Vanhanh, AI đó ghi lại bạn đã nói gì, đã chốt gì và vì sao. Vanhanh giữ được ngữ cảnh và nhớ quyết định của bạn, không tốn lượt chạy nào.
### Cải thiện
- Trang **Ghi nhớ** ghi rõ là **VANHANH**: đồng bộ VANHANH với GitHub, VANHANH tự học từ trò chuyện, VANHANH đã tự học gì.

## [1.1.1] - 2026-11-03
### Sửa lỗi
- **Menu trên điện thoại không còn đè chữ.** Các mục cuối (Nguồn dữ liệu, Chợ ứng dụng, Hệ thống...) từng tràn lên ô ngôn ngữ, ô chọn bộ não và số phiên bản. Giờ mọi thứ xếp liền nhau, vuốt xuống là thấy.

## [1.1.0] - 2026-11-02
### Thêm mới
- **Bộ cài cho máy tính.** Tải Vanhanh-Setup.exe (Windows) hoặc Vanhanh-macOS.dmg (Mac), mở như mọi ứng dụng, không phải gõ lệnh.
- **Fanpage nối một lần, dùng cho ba việc:** bấm Đăng nhập Facebook là bot trả lời tin nhắn Messenger, trả lời bình luận dưới bài, và Vanhanh đăng bài lên Trang ngay hoặc theo lịch. Có hướng dẫn từng bước.
- **Nghe tin nhắn thoại không cần Groq:** dùng khoá OpenAI, Gemini, hoặc bộ nghe chạy ngay trên máy. Chatbot Zalo cá nhân nghe được tin thoại và xem được video khách gửi.
- **AI bên ngoài giao việc cho Vanhanh:** tìm, đọc và gửi lời nhắn vào một cuộc trò chuyện của Vanhanh như chính bạn gõ, bạn xem được trực tiếp và bấm Dừng khi cần.
### Cải thiện
- **Chữ hiện ra dần khi trả lời** với mọi bộ não: Claude Code, Grok Build, Antigravity và các bộ não dùng khoá API.
- **Trang Webhook làm lại:** tóm tắt gọn một dòng, mỗi webhook mở trong một cửa sổ riêng, tìm quy trình theo tên.
- **Chọn bộ não** bằng danh sách riêng của Vanhanh, giống nhau trên mọi máy và tự sắp được thứ tự. File .html mở ra xem trang ngay, mã ở tab bên cạnh. Dán đoạn dài thì xem trước rồi chọn dán hay đính kèm.
- **Đội ngũ tự thử lại** bước gặp lỗi tạm thời, và mỗi phần của kế hoạch ghi rõ phải chờ phần nào xong trước.
### Sửa lỗi
- Đăng nhập Claude trên máy có trình duyệt tự hoàn tất, không còn chờ mã. Kéo thả file vào khung chat chính chạy lại, ghi nhớ bớt lấy nhầm nhật ký cũ, tên file có dấu giữ đúng khi tải về.
## [1.0.5] - 2026-11-02
### Sửa lỗi
- **Nút Cập nhật trên VPS không còn đứng chờ mãi.** Máy chủ chạy VANHANH bằng tài khoản thường mà chưa cho phép tự cập nhật thì trang báo lỗi ngay, kèm lệnh cập nhật tay và cách bật nút Cập nhật, thay vì chờ 10 phút rồi bảo tải lại trang.

## [1.0.4] - 2026-11-02
### Cải thiện
- **Bộ icon mới** cho cả thanh bên lẫn bên trong app, nét gọn và dễ nhận hơn.
- Mục **Linh vật** đổi tên thành **Avatar**.
- **Cập nhật** ra hẳn thanh bên, ngay dưới **Tài khoản**. Có bản mới thì mục này hiện chấm **Mới**.
- Chữ "brain" sót lại trong giao diện, trang Plugin và trang Tự học đã đổi sang tiếng Việt: **bộ não** là kho ghi chú, **model AI** là Claude, ChatGPT...

## [1.0.3] - 2026-11-02
### Cải thiện
- **Trang Tài khoản và Cài đặt** ghi khối **Tên VANHANH** thay cho chữ Workspace. Trang **Models AI** ghi nhãn **Chính** trên thẻ bộ não chính.

## [1.0.2] - 2026-11-02
### Cải thiện
- **Chợ ứng dụng gọi một tên.** Nút và lời nhắc ở trang Cộng sự, Nguồn dữ liệu, Plugin đều ghi **Chợ ứng dụng**, khớp thanh bên.
- **Bớt chữ tiếng Anh khó hiểu:** trang Học ghi Ghi nhớ, Cộng sự, Quy trình, Bảng việc, **Dọn dẹp định kỳ**; trang Models AI ghi **bộ não chính**; trang Tài khoản ghi **Tên VANHANH của bạn**.

## [1.0.1] - 2026-11-02
### Cải thiện
- **Thanh bên gọn hơn.** Mọi mục hiện một lượt, không phải mở từng nhóm. Mục ít dùng gom vào nhóm **Nâng cao**, nhóm **Hệ thống** ghim ở đáy.
- **Tên menu dễ hiểu hơn:** Sơ đồ, Tài liệu, Ghi nhớ, Đội ngũ, Bảng việc, Nguồn dữ liệu, Chợ ứng dụng, Kênh của tôi, Models AI. Ra lệnh bằng giọng nói nhận cả tên mới.
- **Màn chào mừng nói dễ hiểu hơn.** Chọn bộ não bằng gói bạn đang dùng, vào xong bấm **Đăng nhập Claude** ở **Models AI**, không phải gõ lệnh.
- **Trang chủ toàn tiếng Việt:** Bộ não, Cộng sự, Kỹ năng, Quy trình, số ghi chú.
## [1.0.0] - 2026-10-31
### Thêm mới
- **VANHANH ra đời.** Bộ não AI của riêng bạn, do Đại Lê phát triển cho cộng đồng VANHANH.
