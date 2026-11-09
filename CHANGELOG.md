# Nhật ký cập nhật

***Tiếng Việt** · [English](CHANGELOG.en.md)*

Lịch sử phiên bản VANHANH. Bản mới nhất ở trên cùng. Xem ngay trong app tại mục **Cập nhật** (bấm ô tài khoản dưới đáy thanh bên).

Định dạng: mỗi phiên bản là một khối `## [x.y.z] - ngày`, bên dưới nhóm thay đổi theo `### Thêm mới / Sửa lỗi / Cải thiện / Bảo mật`.

## [1.25.0] - 2026-11-09
### Thêm mới
- **Mỗi hội thoại trong cột lịch sử có một nút ⋯** thay cho bốn icon rời (ghim, chuyển project, đổi tên, xoá). Menu có: Ghim lên đầu, Chuyển vào project, Đổi tên (sửa ngay tại dòng), Chia sẻ link, Xuất ra file .md, Đánh dấu chưa đọc, Lưu trữ và Xoá. Bấm chuột phải, hoặc nhấn giữ trên điện thoại, cũng mở menu này.
- **Lưu trữ hội thoại:** hội thoại lưu trữ rời khỏi danh sách nhưng giữ nguyên nội dung, Vanhanh vẫn nhớ và ô tìm kiếm vẫn tìm thấy. Mục "Đã lưu trữ" ở đáy cột mở danh sách này. Nhắn tiếp vào hội thoại đã lưu trữ thì nó tự trở lại danh sách.
- **Chọn bộ não nào làm mặc định.** Trong bảng chọn bộ não, bấm ngôi sao ở một bộ não để đặt nó làm mặc định. Đổi xong thì bộ não mặc định cũ thành bộ não thường và xoá được (vẫn vào thùng rác 30 ngày).
- **Ô xoá bộ não nói rõ trước** bao nhiêu vòng lặp, nhắc việc sẽ dừng theo, và bot nào đang trả lời từ bộ não đó.
- **Bấm Kết nối GitHub, Vanhanh kiểm tra máy có git chưa, thiếu thì tự cài** rồi mới mở bước đăng nhập. Cài không được thì hiện đúng lệnh để cài tay, nút Thử lại và nút Bỏ qua.
### Sửa lỗi
- **Giờ trong thông báo khớp múi giờ trong Cài đặt.** Trên VPS, cảnh báo bảo mật, thông báo hệ thống, giờ đồng bộ sao lưu và giờ sự kiện webhook từng in giờ máy chủ (UTC), lệch 7 tiếng.
- **Quy trình chạy bằng agent Claude dùng được mọi kết nối của Vanhanh**, không còn báo "thiếu công cụ" khi cần Gmail, Sheet, Zalo hay MCP khác.
- **Trang Chatbot, mục Hội thoại chỉ hiện hội thoại của bộ não đang mở**, kể cả số đếm.
- **Git vừa cài xong được nhận ngay**, không phải khởi động lại Vanhanh.
- **Nút cài app ở chân menu trái không còn tràn ra ngoài** trên máy tính bảng và laptop cảm ứng.
### Cải thiện
- **Đổi mật khẩu có thêm ô "Nhập lại mật khẩu mới"**, hai lần gõ phải khớp mới lưu.
- **Màn mạng nơ-ron và danh sách công cụ MCP không còn làm app khựng vài phút một lần.**
- **Xoá hội thoại hỏi lại ngay trong menu**, kèm gợi ý Lưu trữ nếu chỉ muốn cho gọn.
- **Bỏ nút "Xem thêm":** cuộn tới cuối danh sách là tự tải thêm.
- **Dòng hội thoại gọn hơn:** tin ghim có dấu ghim nhỏ trước tiêu đề.

## [1.24.0] - 2026-11-09
### Cải thiện
- **Trang Tài khoản gọn hơn.** Bỏ thanh tiêu đề trang, hai tab Tài khoản và Bảo mật nằm ngay trên cùng.
- **Token API cho CLI chuyển sang trang Tích hợp** (nhóm Việc, trước là Webhook), tab Token API. Cả hai đều là cửa để chương trình khác gọi vào Vanhanh nên giờ nằm chung một chỗ. Token đã tạo vẫn dùng như cũ.

## [1.23.0] - 2026-11-09
### Thêm mới
- **Trình sửa file tự lưu như Google Docs.** Ngừng gõ khoảng một giây là file được lưu, nút Lưu báo "Đang lưu…" rồi "Đã lưu". Đóng file, chuyển file, tải lại hay lỡ vuốt lùi trang cũng không mất chữ đã gõ.
- **Mất mạng giữa chừng vẫn giữ chữ.** Phần chưa lưu được giữ trong trình duyệt và tự khôi phục ở lần mở file sau.
- **Nút mic đọc chữ trong trình sửa file .md và .txt.** Bấm, nói, chữ hiện đúng chỗ con trỏ và được viết lại cho đúng ngữ cảnh, giống mic ở khung chat.
- **Xuất và tải lên cả bộ não bằng một file .zip:** mỗi dòng trong hộp chọn bộ não có nút Xuất. File mang theo ghi chú, ảnh, agent, skill, workflow và bộ nhớ, không mang theo token, khoá, chat thô hay lịch sử git. Nút "Tải lên bộ não (.zip)" luôn tạo một bộ não mới, không đè bộ não đang có. Plugin, vòng lặp và nhắc việc đi kèm file đều được tắt sẵn, bật lại ở trang tương ứng nếu cần. Không có trần dung lượng cố định: máy chủ còn đủ chỗ trống là nhận, tới một triệu file. Nén và giải nén chạy nền có hiện tiến độ, file tải lên được gửi từng phần 32MB, nên bộ não lớn vẫn đi qua được Cloudflare Tunnel.
- **Đổi tên và xoá ngay trên từng dòng của hộp chọn bộ não**, cuối hộp có ba nút Tạo bộ não, Tải lên bộ não và Mở thư mục ngoài. Bốn nút rời cạnh hộp chọn trên thanh trên cùng đã gộp vào hộp này.
### Sửa lỗi
- **Khối chữ (như khối TEXT của email nháp) tự xuống dòng** thay vì kéo dài sang phải. Lúc đang sửa, vuốt ngang bàn di chuột không còn làm trình duyệt lùi trang.
### Cải thiện
- **Màn hình khởi động:** mở Vanhanh là thấy logo cùng dòng "Đang khởi động Vanhanh…" cho tới khi trang đầu tiên đã có đủ dữ liệu. Vanhanh vừa cập nhật hay khởi động lại thì màn này báo thêm lần mở đầu có thể lâu hơn một chút.
- **Mọi màn đang chờ tải dùng chung một hiệu ứng** như trang Cộng sự: vòng xoay nhỏ kèm chữ "Đang tải", trang lớn thì vòng xoay ở giữa. Trang đang nạp không còn hiện nhầm câu "đang phát triển".
- **Số node và liên kết trên thanh trên cùng chỉ hiện ở màn mạng nơ-ron**, các trang khác gọn hơn.
- **Hộp chọn bộ não ghi số node và số liên kết của từng bộ não**, đúng như đồ thị đếm. Số chỉ được đếm khi mở hộp, nên không làm chậm lúc tải trang.
- **Trang Cộng sự và Team hiện dòng "Đang tải…"** ở chỗ danh sách và cuộc trò chuyện chưa về, thay vì để trống như bị treo.
- **Mở một team là thấy ngay tab Thông tin** ở khung bên phải trên màn rộng. Đóng khung đó thì lần sau Vanhanh nhớ và để đóng.
- **Nút tìm kiếm, cài đặt và nút đóng của Team gọn đẹp hơn:** nút vuông, không viền, cùng kiểu với các tab bên cạnh.
- **Danh sách team tải nhanh hơn khoảng 2,5 lần**, và tốc độ mở team không đổi dù team có hàng chục nghìn tin nhắn.

## [1.22.0] - 2026-11-09
### Cải thiện
- **Mở app nhanh hơn rõ rệt.** Khoảng 110 file giao diện lúc khởi động giờ đi chung một gói. Trên đường mạng có độ trễ 150ms, danh sách Cộng sự hiện sau khoảng 2 giây thay vì gần 5 giây.
- **Khởi động lại hay cập nhật xong không còn bị khựng ở lần mở đầu.** Bản nén gọn được lưu lại trên đĩa, chỉ file nào vừa đổi mới phải nén lại.
- **Trang Cộng sự không còn đứng chờ cả loạt.** Các lệnh đọc danh sách, trạng thái Cộng hưởng và việc nền chạy ở luồng phụ, không chặn các lệnh khác.
### Sửa lỗi
- **ChatGPT (Codex) không còn mất công cụ khi chat nghỉ vài phút rồi nhắn tiếp.** Lịch, Zalo, Drive dùng được ngay ở lượt sau.
- **Trên Windows, việc nền Codex mức "Được ghi" ghi được file trở lại.**
- **Ký ức không còn bị hỏng hay mất thông tin sau lượt chat.** Ký ức có dấu hai chấm trong mô tả giữ nguyên loại, mô tả và thẻ. Ký ức đã hỏng từ trước tự lành khi sửa trong app.
- **Ollama Local chạy được việc nhóm và việc nền.** Hết báo "engine chưa sẵn sàng" khi Ollama ở máy nhà không đặt khoá.
- **Chạy sau Caddy (VPS Hostinger) thì nút Đăng nhập Facebook không còn bị khoá.**
- **Thẻ CapCut đăng nhập được.**
- **GitHub trong chat dùng đúng Lệnh kiểm tra đã lưu** và hiểu repo đặt app trong thư mục con.
- **Mở hội thoại ở trang Cộng sự hết báo nhầm "mở quá lâu".** Lúc trang đang tự kết nối lại thì không báo lỗi nữa. Mở Vanhanh Core bị treo thì báo lỗi kèm nút Thử lại, và bấm Thử lại là tải lại thật.
- **Việc nền chạy bằng ChatGPT (Codex) bị chặn ghi file giờ báo đúng là lỗi môi trường**, kèm cách sửa, thay vì nằm ở "chờ bạn trả lời".
- **Ký ức do việc nền ghi không còn bị gắn nhầm nguồn** là cuộc chat đang mở cùng lúc.

## [1.21.0] - 2026-11-09
### Thêm mới
- **Bot Zalo cá nhân hiện "đang soạn tin..." trong nhóm.** Chỉ bật sau khi bot đã quyết định trả lời (được gọi tên, hoặc bộ phán xử chọn lên tiếng) và giữ tới lúc gửi xong, nên nhóm không còn im 20-30 giây rồi mới thấy bot nói. Tin bot đọc rồi im thì không hiện gì.
- **Ô bật tắt "Hiện đang soạn tin... trong nhóm khi bot sắp trả lời"** trong phần cài đặt từng bot ở trang Chatbot, mặc định bật.
### Sửa lỗi
- **Nút Nhập tin cũ của Zalo nhập được thật.** Trước đây cuộc chat nào đã có dù chỉ một tin trong Hộp thư đều bị bỏ qua, nên tài khoản đã bật Ghi hội thoại bấm nhập gần như không được gì. Giờ cuộc chat đã có tin nhận thêm các tin cũ hơn tin đầu tiên của nó, xếp lên trên đúng thứ tự thời gian.
- Tin cũ vừa nhập không nhảy xuống cuối khung chat đang mở, không làm bot hiểu nhầm là tin mới, và nhóm vẫn chỉ giữ các tin gần nhất như cũ.
- **"Đang soạn tin" ở chat riêng không còn tắt cả tiếng.** Trước đây chỉ một cuộc chat bị Zalo từ chối, hoặc MCP khởi động lại, là dấu này tắt ở mọi cuộc chat của nick suốt một giờ. Giờ chỉ tắt cho đúng lượt đó, và dấu được giữ tới khi tin đã gửi đi.
### Cải thiện
- **Mở màn mạng nơ-ron không còn làm cả app đứng.** Bộ theo dõi file của đồ thị được dựng trên luồng riêng, nên bộ não nhiều thư mục không còn khiến mọi thao tác khác chờ tới 2 giây.
- **Mọi kết nối ra ngoài dùng chung một bộ chứng chỉ bảo mật**, nạp một lần lúc khởi động. Trước đây mỗi lần gọi ra ngoài (Telegram, Zalo, model...) đều nạp lại cả bộ, có lần làm app đứng gần 2 giây.
- **Đọc lịch sử Zalo cá nhân chạy nền.** Phần dò lại tin bị sót trong file lịch sử không còn chặn các thao tác khác.
## [1.20.1] - 2026-11-09
### Cải thiện
- Dọn tài liệu bên thứ ba.

## [1.20.0] - 2026-11-09
### Thêm mới
- **Khung trò chuyện hiện kế hoạch của bộ não như một danh sách việc.** Khi Claude Code, ChatGPT (Codex) hay Grok Build tự lập kế hoạch cho một việc nhiều bước, thẻ "Kế hoạch 2/5" hiện ngay trên câu trả lời: việc xong có dấu tích và gạch ngang, việc đang làm in đậm, việc còn lại để trống. Dòng trạng thái dưới khung chat ghi đang ở bước nào. Thẻ được giữ lại khi tải lại trang, và không tốn thêm token.
- **Bảy bộ não chạy bằng API key cũng có thẻ Kế hoạch.** OpenRouter, OpenAI, Anthropic API, Gemini, Groq, DeepSeek và Ollama có công cụ `vanhanh_plan`: gặp việc từ 3 bước trở lên, model lập danh sách và đánh dấu từng mục khi xong. Tốn thêm khoảng 200 token mỗi lượt; muốn tắt thì vào menu **+** ở ô nhập, mục **Kế hoạch việc dài (bộ não API)**. Chỉ khung chat của chủ có công cụ này, bot trả lời khách và việc nền thì không.
- **Tab Công việc ở trang Cộng sự hiện việc cộng sự đang làm trong chat**: thẻ "Đang làm trong chat" kèm số bước và kế hoạch, xong lượt là thẻ tự tắt.
- **Tab Công việc hiện các lần chạy Quy trình mà cộng sự có tham gia.** Đang chạy thì ghi bước nào và của ai, chờ duyệt thì nằm ở Cần bạn, hỏng thì đánh dấu hỏng, bấm Mở là tới đúng quy trình. Bộ lọc nguồn có thêm "Quy trình".
- **Mỗi hội thoại ở cột trái có nhãn thư mục nhỏ ghi tên project.** Đang lọc đúng một project thì nhãn tự ẩn cho đỡ lặp.
- **Nhãn bộ não ghi tên dễ hiểu:** "Claude", "Codex", "Grok", "OpenRouter"... thay cho mã nội bộ như "cli".
### Cải thiện
- **Câu trả lời trải rộng hết khung chat**, không chừa khoảng trống lớn bên phải. Ở trang Cộng sự trên iPad câu trả lời rộng từ khoảng 780px lên hơn 1.000px; màn rất rộng thì dừng ở khoảng 120 chữ mỗi dòng cho đỡ mỏi mắt. Trang Trò chuyện và trang Team đổi theo cùng kiểu.
### Sửa lỗi
- **Chấm trạng thái trên thẻ cộng sự khớp với tab Công việc.** Việc đã bấm Xong hay đã xoá không còn làm chấm xanh hay chấm đỏ sáng lên.
- **Lần chạy Quy trình bị cắt giữa chừng** (máy chủ tắt khi đang chạy) không còn nằm mãi ở Đang làm.
- **Cài lại trợ lý từ Kho nay hiện lại ở trang Cộng sự.** Trước đây đổi tên hay sửa trợ lý của gói, gỡ rồi cài lại thì bị bỏ qua. Nay bản của bạn giữ nguyên, bản của gói được cài thêm dưới tên mới và màn hình nói rõ tên đó.
- **Xoá trợ lý, quy trình, kỹ năng của gói trong app thì Kho thôi báo "Đã cài"**, thẻ hiện lại nút Cài. Gỡ gói thì dọn sạch cả kỹ năng đang tắt và bản Claude Code đọc.

## [1.19.0] - 2026-11-09
### Bảo mật
- **Cần làm sau khi cập nhật:** mở Agent của từng chatbot, ghim các file bảng giá, chính sách, hướng dẫn mà bot cần đọc, rồi bấm **Thử** để chắc bot vẫn trả lời đúng. Bot chưa ghim file nào chỉ trả lời theo vai trò của Agent.
- **Chatbot chỉ đọc tài liệu ghim ở mục Tài liệu của Agent nó dùng**, cộng thư mục `rieng-theo-nhom/` và Google Docs gắn từ Agent. Trước đây bot coi mọi ghi chú trong bộ não là tài liệu, nên có thể trích ghi chú riêng của chủ cho khách.
- **Tab Bảo mật mới trong trang Tài khoản.** Xem 2FA, thiết bị đang đăng nhập (IP, trình duyệt, lần hoạt động cuối) và lịch sử đăng nhập đúng, sai, mọi lần đổi tài khoản. Đăng xuất từng thiết bị hoặc mọi thiết bị khác mà không cần đổi mật khẩu.
- **Báo ngay khi tài khoản có biến.** Đổi tên, đổi mật khẩu, bật tắt 2FA, đăng nhập từ mạng lạ: chuông và Telegram của chủ báo liền.
- **File cài đặt bị sửa từ ngoài VANHANH** thì mọi thiết bị bị đăng xuất và có cảnh báo đỏ. Lần đầu chạy bản này chỉ ghi nhận tài khoản hiện tại, không đăng xuất ai.
- **Trợ lý AI không còn đụng được file bí mật** (cài đặt, khoá mã hoá, phiên đăng nhập), ở mọi mức quyền.
- **Gỡ 2FA khi bị khoá:** thêm biến `VANHANH_RESET_2FA=1` rồi Redeploy. Mỗi giá trị chỉ dùng được một lần.
- **Hostinger: cổng 7777 tự đóng ra ngoài khi đã có tên miền HTTPS**, chỉ còn đường vào có mã hoá.
- **Lỡ lộ link quản trị thì Google không đưa lên kết quả tìm kiếm.** Mọi trang của VANHANH giờ mang lệnh `noindex`, kể cả màn hình đăng nhập và link chia sẻ.
- **Bot AI không đọc được VANHANH.** GPTBot, ClaudeBot, PerplexityBot, công cụ SEO và máy quét như Shodan, Censys nhận lỗi 403. VANHANH cũng có `/robots.txt` cấm chúng.
- Trình duyệt thật, khung xem trước link khi dán vào Zalo hay Telegram, webhook Meta, Threads, Zalo OA, link chia sẻ `/s/` và Vanhanh Gate vẫn chạy như cũ. Cần tắt lớp chặn thì đặt `VANHANH_BLOCK_BOTS=0`.
- **Các file bảo mật tài khoản không còn lọt vào git hay image Docker** khi chạy `git add -A` hay `docker build` trên máy.
### Sửa lỗi
- **Chatbot tra tài liệu, lượt học tự động và nhắc việc không còn làm cả app đứng vài giây.** Các việc này giờ chạy ở luồng phụ và không còn quét cả bộ não.
- **Trang Cộng sự không còn chờ khoá dữ liệu Cộng hưởng**, và danh mục kết nối không còn kiểm tra lại ổ đĩa ở mọi lần gọi.

## [1.18.0] - 2026-11-09
### Sửa lỗi
- **Tin việc hỏng cần bạn xử lý nay là tin khẩn.** Trước đây nó ở mức "đáng chú ý", mà bộ lọc thông báo mặc định chỉ cho tin khẩn đi Telegram, nên trên máy mới việc hỏng không bao giờ tới điện thoại. Muốn bớt thì vẫn tắt được nhóm Sự cố trong Thông báo.
- **Việc hỏng nay luôn báo về Telegram của chủ.** Việc giao từ khung chat trên web mà hỏng cần bạn xử lý, trước chỉ báo vào đúng khung chat đó; nay gửi thêm một tin vào Telegram của bạn để bạn biết khi không mở máy.
- **Việc nhóm (Team) bị chặn, hỏng hay chờ bạn duyệt** trước chỉ nằm trong chuông; nay cũng gửi về Telegram của bạn.
### Cải thiện
- **Văn phòng 3D hết chữ đè nhau.** Tên mỗi bàn nằm gọn trên đúng bàn đó, không rộng quá bàn, tên dài thì xuống hai dòng. Hai nhãn chạm nhau trên màn hình thì giữ nhãn quan trọng hơn (tên phòng, việc đang chạy, việc hỏng), nhãn kia tạm ẩn và hiện lại khi phóng to.
- Mục **Cần bạn xử lý** trên trang Văn phòng ghi rõ tin việc hỏng có đang tới Telegram không. Chưa nối Telegram thì nói thẳng là tin chỉ nằm trong chuông, kèm nút mở Cài đặt.

## [1.17.0] - 2026-11-09
### Thêm mới
- **Phòng họp trong Văn phòng 3D**: khi trưởng nhóm Team đang chia việc hay tổng hợp, cả nhóm đứng dậy đi vào phòng họp ngồi quanh bàn, xong thì tự về bàn mình.
- **Bong bóng trao đổi** trên đầu trợ lý đang nói trong Team: đang chia việc, đang trả lời nhóm, đang làm việc nhóm, đang giúp.
- **Dòng tin chạy** dưới cảnh 3D: ai vừa giao gì cho ai, việc nào vừa chạy đạt hay hỏng, mới nhất trước.
- **Chi phí AI trong ngày** thêm vào hàng số đầu trang, kèm số lượt gọi AI. Tính cho cả máy chủ; engine chạy bằng gói thuê bao tính 0.
- **Biển mỗi phòng ban** ghi thêm số trợ lý, số lượt chạy và số lượt hỏng trong ngày. Mỗi phòng có **tường kính** ba mặt, mặt trước để mở cho dễ nhìn.

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
