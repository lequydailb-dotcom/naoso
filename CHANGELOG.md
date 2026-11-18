# Nhật ký cập nhật

***Tiếng Việt** · [English](CHANGELOG.en.md)*

Lịch sử phiên bản NAOTA. Bản mới nhất ở trên cùng. Xem ngay trong app tại mục **Cập nhật** (bấm ô tài khoản dưới đáy thanh bên).

Định dạng: mỗi phiên bản là một khối `## [x.y.z] - ngày`, bên dưới nhóm thay đổi theo `### Thêm mới / Sửa lỗi / Cải thiện / Bảo mật`.

## [1.46.3] - 2026-11-18
### Cải thiện
- **Văn phòng 3D có thanh số liệu.** Hàng ô trên đầu khung 3D cho biết số nhân viên AI, lượt đã chạy, tỉ lệ đạt, số việc đang lỗi và số lượt hỏi AI của ngày đang xem. Số đếm từ dữ liệu thật của app, chưa có gì thì hiện dấu gạch. Chạm vào từng ô để đọc ý nghĩa. Trên điện thoại vuốt ngang để xem hết.
- **Cập nhật theo kho NAOSO.** Bản này gộp toàn bộ bản mới của NAOTA (1.46.2) và đổi tên hiển thị thành NAOSO; app sẽ nhận cập nhật từ kho NAOSO của anh Đại.

## [1.46.2] - 2026-11-17
### Sửa lỗi
- **Lệnh chạy nền hiện đúng dấu nháy.** Ở trang Văn phòng và dải việc nền, lệnh có dấu nháy đơn (như `<<'EOF'`) từng hiện thành một dãy dấu ngoặc khó đọc. Giờ lệnh hiện y như lúc gõ.

## [1.46.1] - 2026-11-17
### Sửa lỗi
- **Trang Chatbot mở lại được.** Bản 1.46.0 sót một dòng thừa trong mã trang Chatbot nên tab Bot trắng trơn, không tạo được bot. Đã bỏ dòng đó và thêm bài kiểm để lỗi này không lọt ra bản phát hành nữa.
### Cải thiện
- **Đổi tiếng Việt hay tiếng Anh ngay ở thanh bên trái.** Ô chọn ngôn ngữ giao diện trở lại chỗ cũ, trên dòng số phiên bản, khỏi phải vào Cài đặt. Ô trong Cài đặt vẫn còn, hai ô luôn khớp nhau.

## [1.46.0] - 2026-11-16
### Thêm mới
- **Kết nối API tuỳ chỉnh.** Dịch vụ nào có REST API và API key mà chưa có MCP (POS, CRM, vận chuyển, hoá đơn điện tử...) giờ nối được ở trang Kết nối: dán địa chỉ gốc và key, mọi bộ não gọi được API đó.
- **Key không bao giờ tới tay model.** Key được mã hoá, server tự gắn vào lời gọi và chỉ gửi tới đúng máy chủ đã khai; key có lọt trong kết quả cũng bị che.
- **Mặc định chỉ đọc.** Ở mức Chỉ đọc Naota chỉ gọi GET; muốn tạo, sửa, xoá trên dịch vụ đó thì nâng kết nối lên Toàn quyền.
- **Sửa được webhook sau khi tạo.** Phần Cấu hình của mỗi webhook có nút Sửa: đổi tên, đổi quy trình hoặc việc viết tay, ghi chú và mức quyền ngay trong cửa sổ đó. Link và khoá giữ nguyên, nơi đang gửi sự kiện tới không phải đổi gì.
### Cải thiện
- **Thêm repo GitHub mới ngay ở project, trợ lý và hộp tạo team.** Danh sách chọn repo ở ba chỗ này nay có dòng "+ Thêm repository trên GitHub" như trong hội thoại. Cấp thêm repo trên GitHub xong quay lại là danh sách tự hiện repo mới, không cần tải lại trang.

## [1.45.0] - 2026-11-16
### Sửa lỗi
- **Chat với Naota qua Zalo không còn mặc định trả lời tiếng Việt.** Ai nhắn tiếng gì thì Naota trả lời tiếng đó.
- **Nhắc hẹn tạo qua Telegram nói đúng múi giờ bạn đặt trong Cài đặt**, không còn ghi "giờ Việt Nam" cho mọi người.
- **Mức nghĩ (Effort) giờ có tác dụng với Gemini 4.** Chạy Gemini 4 Hydrogen, Argon hay Carbon bằng API key Gemini thì trước đây chọn mức nghĩ nào cũng như không, model luôn chạy theo mức mặc định của nó. Giờ mức bạn chọn được gửi đi, và mọi đời Gemini sau này cũng tự được nhận.
- **Trang Mức dùng tính đúng tiền Gemini mới.** Gemini 4 trước đây bị tính theo giá Gemini cũ nên hiện rẻ hơn thực tế nhiều lần, còn Gemini 3.5 Flash-Lite lại bị tính theo giá bản Pro. Giờ mỗi model có giá riêng.
### Cải thiện
- **Luật lõi Naota gửi cho model nay viết bằng tiếng Anh, một bản cho mọi ngôn ngữ.** Gồm luật từng kênh chat, chế độ tiết kiệm token, vai Naota Core, đường dẫn agent và skill. Trước đây khoảng một phần tư lời dặn là tiếng Việt và nó kéo câu trả lời về tiếng Việt; nay Naota giữ đúng thứ tiếng bạn viết. Bạn vẫn chat tiếng Việt như cũ, Naota vẫn trả lời tiếng Việt.
- **Lời dặn ngắn hơn về số token**, nên mỗi lượt chat nhẹ hơn một chút.

## [1.44.0] - 2026-11-15
### Sửa lỗi
- **Loop tự đặt nhiệm vụ giờ làm trọn nhiệm vụ trong một vòng, không còn dừng sau bước đầu.** Trước đây lời dặn "thực hiện 1 bước cụ thể" khiến loop nhiều bước (ví dụ đăng bài lên đủ các kênh) chỉ làm bước đầu rồi báo xong. Nay mỗi vòng làm đủ các bước nhiệm vụ ghi, bước nào lỗi thì ghi chú rồi làm tiếp bước sau.

## [1.43.0] - 2026-11-15
### Sửa lỗi
- **Naota không còn trả lời tiếng Việt khi bạn đang chat tiếng Anh.** Lời dặn ngôn ngữ viết lại bằng tiếng Anh, nói rõ ngôn ngữ bạn đã dặn thắng, và phần tiếng Việt xung quanh không phải gợi ý.
- **Việc chạy nền (Kanban, nhắc hẹn, loop) không còn luôn báo bằng tiếng Việt.** Nó theo ngôn ngữ của chính đầu việc.
- **Câu trả lời tiếng Nhật, Hàn, Trung, Thái được đọc bằng giọng bản xứ**, và tin nhắn tiếng Anh kèm file không còn bị hiểu là tiếng Việt.
### Cải thiện
- **Naota trả lời bằng đúng thứ tiếng bạn viết, với mọi ngôn ngữ, giống Claude hay ChatGPT.** Ô ngôn ngữ ở Cài đặt nay chỉ đổi giao diện, chatbot cũng luôn trả lời khách bằng tiếng của khách. Muốn luôn nhận một thứ tiếng thì dặn Naota một lần; ai đã ghim ngôn ngữ trả lời từ trước được chuyển thành một câu trong hồ sơ, không mất.

## [1.42.0] - 2026-11-15
### Thêm mới
- **ChatGPT và Claude đổi được model và effort ngay trong câu lệnh gửi qua Naota Gate.** Bảo ChatGPT "bảo Naota làm việc này bằng Opus, effort cao" là xong: model được ghim cho hội thoại đó như khi bạn chọn trên thanh model (chip hiện đúng, đổi lại lúc nào cũng được), còn effort chỉ áp cho đúng tin đó, không đổi cài đặt chung. Công cụ mới `naota_chat_models` cho AI bên ngoài xem Naota có những model nào.
- **Việc ChatGPT giao xong mà nó đã thôi chờ thì chuông Naota báo về điện thoại**, kèm câu trả lời và câu cần nhắn sang ChatGPT ("xem kết quả Naota"). ChatGPT và Claude chưa cho máy ngoài đánh thức một cuộc chat, nên đây là đường ngắn nhất: nhắn một câu, công cụ mới `naota_chat_updates` trả mọi kết quả chưa đọc, kể cả ở một cuộc chat mới bên ChatGPT.
- **Gắn repository GitHub vào Project.** Mở khung project, tab Tài liệu, bấm Thêm tài liệu rồi chọn Repository GitHub. Mọi cuộc chat trong project tự có repository đó ngay từ tin đầu, mỗi cuộc làm trên một nhánh riêng.
- **Gắn repository vào tài liệu của Cộng sự.** Mỗi cuộc chat riêng với trợ lý đó cũng tự có repository, Naota vẫn tự commit, đẩy lên GitHub và mở PR như thường.
- **Chọn repository ngay lúc tạo Nhóm.** Trong mục tài liệu của hộp Tạo nhóm có nút Gắn repository GitHub, nhóm tạo xong là repository đã sẵn.
### Sửa lỗi
- **Chọn nhiều ảnh một lần trong chat Nhóm trên iPhone giờ đính kèm và gửi được.** Trước đây chọn xong vài ảnh thì không ảnh nào hiện lên ô nhập, chỉ một ảnh mới lọt qua. Thêm tài liệu cho nhóm và nhập file nhóm cũng dùng chung cách chọn file đã sửa.
### Cải thiện
- **ChatGPT chờ Naota lâu hơn trong cùng một lượt trả lời** (tới khoảng 10 phút) thay vì bỏ cuộc sau nửa phút, và biết Naota đã làm bao lâu.

## [1.41.0] - 2026-11-15
### Thêm mới
- **Bật Auto là trợ lý tự nhìn quanh với toàn quyền.** Ở chat riêng, mỗi lần tự thức trợ lý dùng đủ công cụ đã kết nối (email, lịch, bán hàng, tra web...) và được tự làm việc thật trong vai của mình. Việc nào đã làm cũng luôn được báo lại cho bạn.
- **Trợ lý tự hẹn giờ kiểm lại.** Thấy việc có ngày giờ (giải chạy, cuộc hẹn, hạn nộp) thì nó tự đặt mốc, ví dụ sáng hôm trước hay tối hôm trước. Tới giờ nó tự thức, kiểm lại nguồn rồi mới quyết có nhắn hay không.
- **Gợi ý và nhắc nhở, không phải thông báo.** Trợ lý chỉ nhắn khi điều đó mới, đúng lúc và làm được ngay: tối đa hai đoạn ngắn, một lời khuyên cụ thể, kèm link nguồn thật. Lời nhắc vào nhóm Nhắc lịch, gợi ý vào nhóm mới "Gợi ý của trợ lý" (mặc định vẫn tới tay bạn, hạ hay tắt ở trang Thông báo).
- **Bảo cải tiến là làm được, có hoàn tác.** Nói "cải tiến chính em" hay "sửa lại skill này", trợ lý tự sửa vai trò, hướng dẫn, skill, model của nó, trợ lý khác, skill, workflow, vòng lặp, bộ nhớ. Mỗi lần sửa có mã và sao lưu, nói "hoàn tác #12" là về bản cũ.
- **Naota sửa được chính mã nguồn của nó.** Khi GitHub đã kết nối với repo mã nguồn Naota (`vuongtex/naota`), trợ lý tự gắn repo vào chat, sửa trên nhánh riêng; Naota tự kiểm, mở PR và merge khi CI xanh.
- **Tự cập nhật lên bản vừa phát hành.** Bảo "cập nhật đi", Naota chờ lượt chat xong rồi chạy đúng quy trình của nút Cập nhật, bản mới lỗi thì tự lùi.
### Sửa lỗi
- **Bấm vào file team vừa ghi là mở ra đọc được.** Trước đây bấm link file trong chat nhóm không thấy gì xảy ra. Nay file mở ngay trong khung chat của nhóm, bấm X để quay lại cuộc trò chuyện, chữ đang gõ dở vẫn còn.
- **Trang nào chưa có chỗ cho trình sửa thì file mở dạng bảng nổi**, ví dụ link file ở trang Việc, nên không còn chỗ nào bấm mà không thấy gì.
### Cải thiện
- **Bật Auto hỏi lại một lần**, nói rõ là trao toàn quyền. Câu cũ "Auto không phải Toàn quyền" đã thay bằng câu đúng với cách chạy mới.
- **Chỉ bạn ra lệnh mới sửa được.** Lượt tự thức của Auto và bot nói với khách chỉ được đề xuất. Các câu dặn cũ mâu thuẫn trong prompt đã được thay cho khớp.

## [1.40.0] - 2026-11-15
### Thêm mới
- **Link mở thẳng một trang của dashboard.** Link dạng `#p=tasks` (hay tên trang khác) mở đúng trang đó, kể cả khi tab Naota đang mở sẵn.
- **Huỷ việc nền ngay trong chat.** Bảo Naota huỷ một việc là việc rời hàng đợi, việc đang chạy dừng luôn, lý do được ghi vào nhật ký. Khi trả một việc chưa đạt về làm lại, có thể dặn thêm cách sửa và lần làm lại sẽ theo lời dặn đó.
- **Nối Fanpage có thêm ô "Đọc số liệu bài viết".** Ô tuỳ chọn này xin quyền đọc lượt tiếp cận, lượt lưu của bài. Bảng kiểm tra Messenger báo Trang đã có quyền này chưa.
### Sửa lỗi
- **Việc chạy nền Naota tự bật khi chat bằng API key báo xong đúng lúc.** Trước đây việc kẹt ở trạng thái "đang chạy" tới khi khởi động lại máy chủ.
- **Cuộc chat đã ghim model giữ nguyên model đó.** Khi model ghim tạm hết lượt hoặc mất đăng nhập, lượt chat chạy tạm bằng model chính, rồi tự quay lại model đã ghim khi dùng được lại.
- **Link file kèm số dòng (kiểu `agents/x.md#L66-L75`) mở đúng file.** Câu trả lời không còn bị gắn cảnh báo sai "không tìm thấy file trong brain".
- **Hội thoại Messenger hiện tên khách thay vì một dãy số.** Khi Meta không cho đọc hồ sơ, Naota lấy tên từ cuộc trò chuyện của Trang, và tự thử lại sau 10 phút nếu lần trước không lấy được.
- **Cúp máy khi Naota còn đang làm việc được giao trong cuộc gọi thì việc không bị bỏ.** Naota làm nốt rồi gửi kết quả vào khung chat của cuộc gọi, kèm thông báo.
- **Đường gọi Tự động không tự chuyển sang ChatGPT Live chỉ vì máy có sẵn phiên Codex.** ChatGPT Live chỉ được chọn khi ChatGPT là model chính hoặc đã kết nối ở trang Models.
### Cải thiện
- **Các dòng hệ thống Naota gắn dưới câu trả lời không còn xưng cứng "mình".** Dòng theo dõi việc chạy nền, đính chính lời hẹn, nhắc trí nhớ, link không thấy file viết không đại từ, nên không lệch với cách xưng hô đã chọn.

## [1.39.0] - 2026-11-15
### Thêm mới
- **Ô "Ghi nhớ đăng nhập trên máy này" ở màn đăng nhập.** Để tích như cũ thì máy này giữ đăng nhập 30 ngày. Bỏ tích khi dùng máy của người khác: đóng trình duyệt là thoát, để yên 4 giờ hoặc quá 24 giờ Naota cũng tự đăng xuất.
- Trang Bảo mật đánh dấu thiết bị nào đăng nhập kiểu không ghi nhớ.
- **Bấm vào đoạn trích là cuộn về đúng câu gốc.** Trích một câu trong câu trả lời dài để hỏi tiếp, sau này chạm vào đoạn trích đó trong tin của bạn là khung chat tự cuộn lên đúng câu ấy và tô sáng nó vài giây.
- Câu gốc nằm ở phần tin cũ chưa tải thì Naota tự tải thêm để tìm. Chạy ở cả khung chat chính lẫn trang Nhóm.
### Sửa lỗi
- **Bảng chọn model mở ngay trên nút model.** Trước đây khung soạn tin cao (có file đính kèm, gõ nhiều dòng) thì bảng bị đẩy lên xa nút, và danh sách dài còn bị cắt mất mấy dòng đầu. Giờ bảng chọn model, mức suy nghĩ, hạn mức gói và menu "+" đều mở sát hàng nút, và luôn nằm trọn trong màn hình.
- **Menu "+" ở trang Nhóm cũng vậy**, kể cả bảng chọn thư mục và GitHub mở từ menu đó.
- **Nút "Đẩy lại" và dấu chấm than ở thẻ GitHub không còn kẹt mãi.** Việc đã lỡ lưu một tên nhánh bị trùng trên GitHub (từ trước bản sửa trước) vẫn cứ đẩy vào đúng tên đó, nên lần thử lại nào cũng báo "có commit mà máy này không có". Giờ khi chưa đẩy lên được lần nào, Naota chọn lại tên nhánh còn trống (hoặc theo nhánh đang mở ở máy), đẩy lên và mở PR, dấu chấm than tự tắt.
- **Việc GitHub thứ hai trong một khung chat không còn kẹt ở bước đẩy lên.** Tên PR và tên nhánh giờ lấy từ chính câu yêu cầu, bỏ qua các dòng ngữ cảnh như "[NGỮ CẢNH GIAO DIỆN: ...]", nên mỗi việc có tên riêng. Nếu tên đã có người dùng ở máy hay trên GitHub, Naota tự thêm -2, -3 rồi đẩy lên, không còn dừng với câu "có commit mà máy này không có, Naota không ghi đè".
- **Kết nối Google Workspace làm được việc thật trên Form, Drive và Sheets.** Trước đây thẻ chỉ bật bộ công cụ rút gọn, nên Naota không sửa được câu hỏi Form, không đọc câu trả lời, không xem thư mục Drive, không đổi tên hay chép file, không thêm tab hay ghi nối dòng vào Sheets. Giờ đủ cả, không phải đăng nhập Google lại.
- Kết nối đã tạo từ trước tự lên bộ công cụ đầy đủ sau khi cập nhật.
- **Sửa compose trong hPanel rồi bấm Deploy không còn bị chặn.** Bản 1.37.0 làm file Hostinger dài 33.167 ký tự, quá trần 32.768 của hPanel. File giờ còn chưa tới 30.000 ký tự, phần bảo vệ cập nhật vẫn chạy y như cũ.
- Mở Naota lần đầu trên một trình duyệt mới không còn hiện nhầm dòng đỏ "Phiên đăng nhập đã hết hạn".
- **Lịch nhắc ở mức chỉ đọc xem được Việc của tôi.** Trước đây lịch nhắc kiểm tra tiến độ báo "không kiểm tra được"; giờ nó đọc được danh sách, còn thêm, sửa, xoá, tích vẫn cần quyền ghi.
### Bảo mật
- **Chia sẻ file hay lịch cho người khác cần Toàn quyền.** Cũng vậy với xoá cả một tab, danh sách việc hay nhóm danh bạ, tạo bộ lọc Gmail và xuất bản Apps Script. Ở mức Chỉ đọc, Naota không chép được file Drive hay ghi dòng vào Sheets.

## [1.38.0] - 2026-11-14
### Thêm mới
- **Gửi tin Zalo dạng trả lời có trích dẫn.** Khi bạn bảo Naota trả lời đúng một tin cụ thể, tin gửi đi hiện kèm khung trích tin gốc, giống bấm "Trả lời" trong Zalo. Chỉ trích được tin chữ. Kết nối Zalo tự chuyển sang naota-zalo 1.11.0 ở lần chạy tới.

## [1.37.0] - 2026-11-13
### Thêm mới
- **Model Claude mới tự hiện trong trình chọn model.** Naota đọc thêm danh mục model mà Claude Code tải về từ Anthropic, nên model vừa ra (bản CLI đang cài chưa ghi sẵn tên) cũng hiện ngay, không phải chờ bản Naota mới ghi thêm tên.
- **Chọn được cả thư mục làm tài liệu.** Ô tìm ở phần Thêm file của dự án, cộng sự, cuộc trò chuyện và nhóm (lúc tạo nhóm lẫn tab Thông tin) giờ hiện cả thư mục khớp tên, có icon thư mục riêng. Bấm Thêm là gắn cả thư mục, không phải chọn từng file.
- **Naota biết trong thư mục có gì.** Thư mục chưa ghim thì Naota thấy đường dẫn và tự mở file bên trong khi cần. Ghim thì danh sách file trong thư mục được nạp sẵn vào mỗi lượt. Thư mục thêm vào nhóm được ghim sẵn.
- **An toàn hơn cho thư mục.** Hàng thư mục không có nút xoá khỏi bộ não, chỉ có gỡ khỏi danh sách. Bấm vào tên thư mục là mở nó ở trang Tệp tin.
- **Project tự học ngữ cảnh.** Trong lúc làm việc ở một project, Naota tự ghi lại điều bền và riêng của project (sự thật, quyết định đã chốt, thuật ngữ) và dùng lại ở mọi cuộc sau trong project. Xem, sửa, xoá ở tab mới "Đã học". Ô Hướng dẫn vẫn là của bạn: Naota chỉ sửa khi bạn bảo thẳng.
- **Thả tài liệu vào chat là đủ.** File hay link dùng lâu dài được Naota tự gắn vào project kèm một dòng nói nó chứa gì, nên nó mở đúng tài liệu mà không cần ghim cả file.
- **Cộng sự và nhóm cũng có mô tả tài liệu.** Chat riêng với một cộng sự, nó tự gắn và mô tả tài liệu của mình; tài liệu nhóm có dòng mô tả cho mọi thành viên đọc.
### Sửa lỗi
- **Gắn repo riêng tư vào chat không còn hỏng khi nhánh chính có file mới.** Trước đây repo riêng tư chỉ gắn được lần đầu; hễ nhánh chính có thêm hoặc đổi file là chat mới báo `could not fetch ... from promisor remote`.
- **Đổi nhánh gốc của chat cũng chạy với repo riêng tư.** Cùng lỗi đó làm nút Đổi nhánh và việc tạo lại nhánh sau khi merge thất bại; cả hai đã được sửa.
- **PR của repo riêng tư bị xung đột giờ được Naota tự gộp lại.** Trước đây vòng sửa xung đột dừng ngay ở bước tải nhánh chính, vì phần chạy lệnh của AI không có quyền vào GitHub. Giờ Naota tự tải nhánh chính về trước, AI chỉ còn việc gộp và giải quyết xung đột.
- **Mất mạng lúc đó thì Naota chờ rồi thử lại.** Vòng sửa không còn bị tiêu mất vào một lần gộp chắc chắn hỏng; thẻ repo ghi rõ lý do đang chờ.
- **Bộ kiểm tra tự động xanh trở lại.** Hai bản cập nhật GitHub vừa rồi vào cùng lúc làm một bài kiểm tra báo đỏ sai; bài đó đã được viết lại. Cách Naota chạy không đổi gì.
- **Vòng sửa xung đột chạy được trên máy chưa khai tên và email cho git.** Trên máy chủ mới hoặc trong Docker, lệnh gộp nhánh của AI dừng ngay với lỗi `empty ident name`. Giờ mỗi repo gắn vào chat có sẵn danh tính, là tài khoản GitHub bạn đã kết nối.
- **Commit do AI tự tạo trong repo đó giờ đứng tên giống commit của Naota.** Nếu bạn đã tự khai tên và email riêng cho repo thì Naota giữ nguyên.
- **Dùng lâu không còn ì dần.** Mỗi lần mở trang Trò chuyện, trình duyệt giữ lại cả trang cũ trong bộ nhớ, đổi trang càng nhiều máy càng nặng. Giờ trang cũ được dọn sạch.
- **Màn Đồ thị hết khựng.** Đồ thị nhớ chỗ các chấm đã nằm nên lần mở sau hiện ngay, không tính lại từ đầu (bộ não 2.600 ghi chú: quãng đứng hình dài nhất từ hơn 1 giây xuống khoảng 0,2 giây). Chấm vừa rê qua cũng không còn sáng mãi và vẽ liên tục sau khi chuột đã rời đi.
- **Bộ cài Windows không còn bị thay file mới vô cớ.** File `Naota-Setup.exe` chưa ký số nên trình duyệt và trình diệt virus chỉ nhận ra nó qua mã băm. Trước đây cứ sửa script cài (kể cả script của Linux) là file bị thay, và mỗi lần thay thì Edge lại báo "isn't commonly downloaded" từ đầu. Giờ file chỉ đổi khi chính bộ cài thay đổi.
- **Hướng dẫn cài nhanh có thêm cách gỡ khi bị chặn.** Thêm bước bấm **Keep anyway** khi Edge hoặc Chrome không chịu lưu file, và một dòng lệnh cài không cần file exe cho máy bị trình diệt virus hoặc Smart App Control chặn.
- **Dùng Team nhiều không còn làm rớt kết nối tới máy chủ.** Team càng chạy nhiều lượt thì mỗi lần mở team Naota càng lâu mới cộng xong mức dùng của nó: team vài nghìn lượt mất cả phút, trang chờ quá 30 giây thì báo mất kết nối rồi gọi lại, và cả máy chủ đứng theo. Giờ việc này nhanh hơn khoảng 100 lần và không bao giờ chạy chồng lên nhau.
- **Mỗi lần gọi model không còn làm máy chủ khựng.** Sổ mức dùng từng giữ một dòng cho mỗi lần Team gọi model suốt 30 ngày và bị ghi lại toàn bộ sau mỗi lần gọi, nên file phình tới hàng chục MB, chat thường cũng chậm theo. Naota tự dọn file này lúc khởi động, số liệu mức dùng giữ nguyên.
- **Đang xem trang Nhiệm vụ không còn bị khựng định kỳ.** Cứ 30 giây (5 giây khi có việc đang chạy) trang lại vẽ lại toàn bộ danh sách dù không có gì mới, làm màn hình đứng một nhịp và mất chỗ đang rê chuột. Giờ không có gì đổi thì không vẽ lại.
- **Naota không còn đứng hình khi đĩa của máy chủ trả lời chậm.** Trên VPS, mỗi lần đĩa chậm vài giây là mọi trang, bot và kết nối cùng đứng theo, có lúc máy chủ bị coi là sập. Nặng nhất ngay sau khi cập nhật. Giờ các việc chạy liên tục (kiểm tra đăng nhập, hub MCP, bot, link chia sẻ) không còn phải chờ đĩa.
- **Cập nhật bản Docker xong, các nguồn MCP không phải tải và cài lại từ đầu.** Phần đã cài được giữ trên ổ dữ liệu, nên máy chủ không bị dồn việc lúc vừa khởi động lại. Riêng lần cập nhật lên bản này vẫn cài lại một lần cuối.
- **Lúc khởi động, Naota mở các nguồn MCP theo từng nhóm nhỏ** thay vì tất cả cùng lúc, để máy chủ nhỏ không bị quá tải.
- **Nhóm không còn hiện hồ sơ của một người.** Trước đây ô ghi chú của một nhóm Zalo hiện hồ sơ của người nhắn đầu tiên trong nhóm, như thể cả nhóm là một khách. Giờ nhóm có ghi chú riêng của nhóm, sửa ở đó không đụng tới hồ sơ của ai.
- **Bình luận Facebook, Instagram, Threads không được ghi hồ sơ.** Người bình luận không nhắn tin cho shop, nên A.I. không ghi hồ sơ từ các luồng bình luận nữa, và bot trả lời công khai cũng không mang theo hồ sơ học từ chat riêng.
- **Thẻ OpenAI Compatible và Claude Compatible không còn báo "Chưa lấy được danh sách model" oan.** Naota đọc được danh sách model của nhiều kiểu cổng hơn, và Base URL gõ thiếu `/v1` thì tự tìm đúng địa chỉ. Máy nâng cấp từ bản cũ cũng tự hiện lại model.
- **Tên model bạn tự gõ luôn nằm trong bảng chọn**, kể cả khi cổng có danh sách riêng hoặc tạm thời không trả danh sách.
- **Khi thật sự không có danh sách, bảng chọn nói rõ vì sao** (sai địa chỉ, key bị từ chối, cổng không báo model) và có lối bấm sang trang Models để sửa. Sửa xong mở lại là thấy ngay, không phải chờ vài phút.
- **Key vừa kết nối không còn tự biến mất** nếu đúng lúc đó Naota đang tải danh sách model của một thẻ khác.
- **Bấm dừng ghi âm phản hồi ngay.** Thanh ghi chuyển sang "Đang viết lại câu cho đúng" ngay khi bấm, và đoạn ghi âm được gửi đi nghe lại luôn chứ không chờ trình duyệt đóng mic xong.
- **Bước viết lại câu nhanh hơn nhiều.** Lớp sửa từ trước đó có lúc tốn vài giây, nay chỉ vài phần trăm giây. Model nhanh không còn "nghĩ" hết lượt rồi trả câu rỗng, máy chạy gói đăng ký thì model chính nghĩ ở mức thấp nhất cho việc này.
- **Đọc dài không còn mất chữ.** Câu dài hơn khoảng 2.000 ký tự trước đây bị cắt cụt sau bước viết lại, nay giữ đủ từng chữ.
- **Bớt đổi nhầm chữ thường thành tên riêng.** "đã viết" không còn thành "Naota", "cần và" không còn thành "Canva".
- **Lấy câu gợi ý rồi xóa bớt thì gợi ý không còn mất.** Trước đây nhấn Tab lấy cả câu (hoặc lấy hết từng chữ) rồi xóa vài chữ là phần gợi ý biến mất luôn. Giờ xóa đến đâu, phần còn lại hiện xám lại đến đó. Xóa hết ô chat thì câu gợi ý hiện lại nguyên vẹn. Gợi ý chỉ mất khi bạn gửi tin.
- **Máy tính cũng có dấu > sau câu gợi ý.** Trước đây dấu này chỉ hiện trên điện thoại. Giờ trên máy tính bấm chuột vào dấu **>** ngay sau chữ cuối là lấy cả câu.
- **Naota không còn biến mất (lỗi 404) sau khi cập nhật.** Trên VPS ổ đĩa chậm, Watchtower hết giờ đúng lúc đang xoá container cũ, bỏ dở mà không dựng bản mới, nên Naota mất hẳn khỏi Docker cho tới khi Redeploy.
- Thêm container canh gác `naota-guard`: thấy Naota biến mất hay bị dừng giữa chừng quá 2 phút là tự dựng lại (lên đúng bản mới) hoặc bật lại. Naota bạn tự bấm dừng thì nó để yên.
- Mỗi lần cập nhật bằng nút bấm có 30 phút thay vì 10. Cần Redeploy một lần để nhận file compose mới.
### Cải thiện
- **Mở Naota nhanh hơn rõ rệt.** Màn "Đang khởi động Naota…" trước đây luôn đứng đủ 4 giây trên máy có hơn một trang cuộc chat, dù dữ liệu đã về sau khoảng 1 giây. Giờ dữ liệu về là app hiện ngay. Đồ thị bộ não cũng không còn được dựng ngầm khi bạn mở thẳng vào Trò chuyện hay Cộng sự.
- **Để yên thì Naota gần như không tốn máy.** Vành của linh vật, nền sao và đồ thị không còn bắt trình duyệt làm việc 60 lần mỗi giây khi không có gì thay đổi, nên cuộn và gõ mượt hơn, máy đỡ nóng.
- **Trang Nhiệm vụ mở mượt hơn hẳn.** Trước đây mỗi lần mở, trang vẽ lại toàn bộ danh sách hai lần và dựng cả bản máy tính lẫn bản điện thoại. Giờ chỉ vẽ một lần, đúng bản đang hiện. Với 170 việc trên máy chậm: quãng đứng hình từ 0,45 giây xuống khoảng 0,1 giây, trên điện thoại gần như không còn.
- **Trang Cộng sự mở nhanh hơn.** Danh sách trợ lý trước đây bị vẽ lại năm lần mỗi lần mở trang, nay chỉ một lần, nên rê chuột và cuộn không còn bị giật lúc trang vừa hiện.
- **Gõ tìm việc không còn trễ chữ.** Danh sách lọc theo sau khi bạn ngừng gõ một nhịp ngắn, thay vì vẽ lại sau từng chữ.
- **Câu gợi ý không còn biến mất khi bạn gõ chữ đầu tiên.** Gõ theo câu gợi ý thì phần còn lại vẫn hiện màu xám ngay sau chữ bạn gõ, kể cả khi gõ không dấu hay đang gõ dở một chữ. Nhấn **Tab** để lấy hết phần còn lại, nhấn **mũi tên phải** để lấy từng chữ. Trên điện thoại không còn nút Tab ở hàng nút: có một dấu **>** nhỏ ngay sau chữ cuối của câu gợi ý, chạm vào là lấy câu đó.
- **Gõ khác đi thì Naota đoán nốt câu.** Dừng gõ một nhịp, Naota viết tiếp phần còn lại của câu bạn đang gõ theo ý mới của bạn, giống gợi ý chữ trên iPhone. Máy có key API (Groq, OpenAI...) thì gần như tức thì. Chỉ dùng gói thuê bao thì chậm vài giây và tối đa 5 lần mỗi lượt, để không ăn vào hạn mức.
- **Câu gợi ý dài hiện đủ.** Ô chat tự cao lên để thấy cả câu, trên điện thoại không còn bị cắt giữa dòng. Áp dụng cho chat chính và trang Nhóm.
- **Duyệt nhiều nhóm chờ cho bot bằng một lần bấm.** Trong bảng Tình trạng của bot, mỗi nhóm hay người đang chờ là một ô tích, có **Chọn tất cả** và một thanh nút **Cho phép** / **Bỏ qua** chung. Trước đây chín nhóm chờ là chín lần mở bảng rồi bấm.
- **Bảng không tự đóng sau mỗi lần bấm.** Duyệt xong một loạt, bảng ở lại với những dòng còn chờ. Nút ghi sẵn số dòng đang tích, ví dụ "Cho phép (9)".
- **Dễ đọc hơn trên điện thoại.** Tên nhóm chữ to, cả dòng bấm được, thanh nút luôn nằm trong tầm ngón tay dù danh sách dài.
- **Bỏ nút chữ "Tab" ở hàng nút dưới ô chat.** Dấu **>** đã làm việc đó, nên hàng nút chỉ còn các nút vốn có (thêm file, model, mức suy nghĩ, mic, gửi). Phím Tab trên bàn phím vẫn lấy câu gợi ý như cũ.
- **File, thư mục và link gộp một tab "Tài liệu".** Phân biệt bằng biểu tượng, nút Thêm tài liệu có cả dán link, khung gọn hơn một tab.
### Bảo mật
- **Hook và cấu hình git trong repo không còn đọc được token GitHub.** Trước đây một hook nằm trong bản clone (ví dụ do `npm install` kiểu husky cài, hoặc do model tạo) chạy đúng lúc Naota tải về hay đẩy code và thấy được token. Giờ các lệnh git có mang token của Naota bỏ qua mọi hook của repo.
- **Token chỉ đi tới đúng repo trên GitHub.** Nếu cấu hình git của bản clone bị sửa để lái kết nối sang nơi khác (đổi `origin`, `insteadOf`, proxy), Naota dừng lại và nói rõ dòng nào cần gỡ, thay vì gửi token đi.
- **Thay đổi cần biết:** hook `pre-push` của repo không còn chạy khi Naota đẩy code (bộ kiểm tra của Naota và CI vẫn chạy như cũ). Repo dùng Git LFS: file LFS mới tạo trong chat chưa được tải lên theo lần đẩy.

## [1.36.0] - 2026-11-13
### Thêm mới
- **Agent chọn ChatGPT giờ chạy đúng bằng ChatGPT trong workflow nền giới hạn công cụ.** Trước đây các bước đó luôn chạy bằng Claude Code dù bạn chọn ChatGPT. Bước chỉ được gọi đúng danh sách công cụ của nó, giữ mức quyền của việc, không có lệnh máy, web hay tác tử con.
- Máy chưa cài Codex thì bước đó vẫn chạy bằng Claude Code như trước, không báo lỗi.
- **Tạo team kèm tài liệu ngay từ đầu.** Hộp Tạo team có thêm mục "Thêm tài liệu cho team (file, link)": tìm file có sẵn trong brain theo tên, tải file từ máy, hoặc dán link. Cộng sự trong team đọc được các tài liệu này từ tin đầu tiên.
- **Không phải tải lại file đã có trong brain.** Tab Thông tin của mỗi team có ô tìm file trong brain, bấm Thêm là xong. File vẫn nằm nguyên chỗ cũ, không tạo bản sao.
- **Một team chạy được nhiều việc cùng lúc.** Trước đây mỗi team chỉ chạy một việc tại một thời điểm, nên việc của cộng sự này phải chờ việc của cộng sự kia xong. Giờ tối đa 3 việc chạy song song khi chúng thuộc các cộng sự khác nhau.
- **Việc của cùng một cộng sự vẫn chạy lần lượt** theo đúng thứ tự trong hàng chờ. Các việc do người điều phối lên kế hoạch cũng vậy.
- **Muốn việc sau chờ kết quả việc trước thì nói rõ trong yêu cầu.** Việc có câu như "sau khi ... xong", "lần lượt" hay "theo thứ tự" sẽ chờ mọi việc đứng trước nó xong rồi mới chạy, và không việc nào phía sau chen lên trước.
- **Team mới chạy việc tới khi xong.** Team tạo từ bản này không còn trần số lần trả lời và số bước của mỗi việc, nên việc không dừng giữa chừng để chờ bấm "Cho thêm lượt". Đổi lại một việc khó có thể tốn nhiều token hơn. Trần số lần trả lời mỗi ngày của team vẫn giữ nguyên, và việc vẫn tự dừng khi ra hai kết quả giống hệt nhau.
- Team đã có từ trước giữ nguyên giới hạn cũ. Muốn đổi thì vào Nâng cao, mục Giới hạn của team, tích "Không giới hạn" hoặc nhập lại con số.
### Sửa lỗi
- **Tạo ảnh ChatGPT không báo "không có tài khoản" khi mọi tài khoản đang nghỉ vì hết lượt chat.** Naota vẫn thử tài khoản đang bật đầu tiên, như trước khi có xoay tài khoản. Tài khoản đã tắt thì vẫn không được dùng.
- **Mở một Team đã chat nhiều giờ không còn làm cả app chậm lại.** Trước đây, mỗi lần mở Team trên màn hình rộng là tab Thông tin tự mở, và máy chủ đọc lại toàn bộ tin nhắn của nhóm để dò file và link. Nhóm càng dài càng chậm, và trong lúc đó tải tin nhắn, chuyển nhóm, gửi tin đều phải chờ. Giờ máy chủ nhớ kết quả, lần sau chỉ đọc tin mới. Đo với nhóm 3.000 tin: từ 1,5 giây mỗi lần mở còn 0,003 giây.
- Mục Tài liệu của một cuộc trò chuyện dài cũng nhanh theo, vì dùng chung cách đọc này.
- **Mở phiên chat mới với Claude Code không còn ghi lại toàn bộ cache khi bật tiết kiệm token.** Trước đây một dòng giờ đổi theo từng phút, cùng phần ký ức chọn theo câu hỏi, nằm trong phần prompt được cache, nên mỗi phiên mới phải ghi lại khoảng 25 nghìn token. Nay phần đó đi kèm tin nhắn đầu của phiên, còn prompt giữ nguyên giữa các phiên.
- **Quy ước ghi ở trang Hồ sơ giờ tới được model cả khi bật tiết kiệm token.** Trước đây ở các mức tiết kiệm (kể cả mức mặc định) hồ sơ bị bỏ cùng với mục lục ký ức, nên cách xưng hô hay cách trình bày bạn đặt một lần cho mọi brain chỉ có tác dụng khi tắt tiết kiệm.
- **Kiểm tra Messenger phát hiện được webhook không truy cập được.** Trước đây mọi dòng đều báo ổn trong khi đường HTTPS đã chết, nên bot không trả lời mà không rõ vì sao.
- **Link nhanh đổi địa chỉ thì Sửa tự động trỏ lại đúng địa chỉ đang chạy**, giữ nguyên đường dẫn nhận tin, và chỉ lưu sau khi Meta xác minh thành công.
- **Vòng hạn mức hết đỏ ngay khi gói dùng lại được.** Trước đây bạn đặt lại gói trên trang nhà cung cấp rồi mà vòng vẫn đỏ 100% và việc Naota tự làm vẫn nghỉ, cho tới giờ làm mới cũ.
- **Đọc được giờ mở lại có ghi cả năm.** Câu báo kiểu "try again at Nov 13th, 2026 3:32 PM" trước đây bị coi là không rõ lúc nào mở lại, nay hiện đúng giờ.
- **Việc nền bị từ chối vì hết lượt cũng làm vòng hạn mức đỏ.** Trước đây chỉ lượt chat mới ghi nhận, nên việc nền dùng cạn gói mà vòng vẫn xanh.
- **Lỗi "SDK engine: ProcessError... Check stderr output for details" giờ nói rõ lý do.** Khi Claude Code thoát trước khi trả lời, khung chat hiện đúng câu nó in ra thay vì một dòng không biết làm gì tiếp.
- **Ba ca hay gặp có luôn cách xử lý:** Naota chạy bằng tài khoản root, cấu hình nguồn dữ liệu (MCP) hỏng, và Claude Code trên máy quá cũ.
- **Việc nền chạy dự phòng bằng đúng model bạn chọn trên thẻ.** Trước đây lựa chọn đó bị bỏ qua: khi model việc nền hết lượt và việc rơi sang Claude Code, nó chạy model mặc định của CLI, thường là model tốn hạn mức nhất. Thẻ chưa chọn model thì vẫn chạy như cũ.
- **ChatGPT (hay Claude, Grok) mất đăng nhập thì Naota tự chuyển sang model khác đã kết nối.** Trước đây chỉ khi hết lượt mới chuyển, còn mất đăng nhập thì lượt nào cũng báo lỗi cho tới khi bạn đăng nhập lại.
- **Áp dụng cho cả bot trả lời khách và trợ lý có model riêng.** Bot hay trợ lý đặt model ChatGPT sẽ trả lời bằng model chính trong lúc ChatGPT chưa đăng nhập lại, khách không còn gặp lượt hỏng.
- **Có báo rõ để bạn biết.** Khung chat hiện dòng "Đang dùng ... vì ChatGPT mất đăng nhập", ô chọn model gắn nhãn "Mất đăng nhập", và chuông có một thông báo nhắc đăng nhập lại ở trang Models. Đăng nhập xong là dùng lại model cũ ngay.
- **Quy ước ở trang Hồ sơ giờ có tác dụng cả với câu trả lời đi đường tắt.** Trước đây còn sót: lời chào, lời cảm ơn (ở mọi mức) và câu hỏi đơn giản ở mức Siêu tiết kiệm vẫn được trả lời mà không có hồ sơ, nên Naota có thể xưng hô sai ngay ở câu chào đầu tiên.
- Câu trả lời tổng hợp từ dữ liệu vừa đọc (trên bộ não dùng API key) cũng theo hồ sơ.
- Hồ sơ trống thì không có gì thay đổi. Hồ sơ dài nhất (4.000 ký tự) làm một lượt đi đường tắt nặng thêm khoảng 1.400 token.
- **Mục Bộ phán xử luôn có trong menu "..." của thẻ bot.** Trước đây nó chỉ hiện khi bot ở chế độ Tự đánh giá, nên nhiều người tìm không thấy.
- **Bot chưa bật Tự đánh giá thì bảng nói rõ bộ phán xử đang nghỉ**, kèm nút Sửa để bật, thay vì một danh sách trống.
### Cải thiện
- **Màn "Đang khởi động Naota…" nhường chỗ cho app nhanh hơn.** Dữ liệu trang đầu về xong là màn này tắt gần như ngay.
- **Máy tải dữ liệu chậm không còn bị che tới 12 giây.** Trang đầu đã mở mà danh sách còn tải thì sau 4 giây app hiện ra, phần nào chưa xong tự hiện dòng "Đang tải" của nó như mọi trang khác.
- **Tìm file theo tên dễ trúng hơn.** Gõ nhiều từ như "bảng giá" sẽ ra cả `bang-gia-dich-vu.md`: tên file chỉ cần chứa đủ các từ, không cần đúng dấu gạch hay thứ tự. Áp dụng cho mọi ô tìm file theo tên, gồm ngăn Tài liệu của cuộc trò chuyện.
- **Dải việc đầu khung chat hiện đủ các việc đang chạy**, không chỉ một việc.
- Cần quay về kiểu từng việc một thì đặt biến môi trường `NAOTA_TEAM_JOBS=1`.
- **Tab cài đặt của Team gọn hơn.** Phần hiện sẵn chỉ còn những gì bạn cần quyết cho một team: thành viên, mục tiêu, người điều phối tự quyết đến đâu, hành động ra ngoài có cần duyệt không, tên và trạng thái team.
- **Nghiệm thu và mức dùng chuyển vào mục Nâng cao**, cùng chỗ với các con số giới hạn và quyền chi tiết. Không có gì bị bỏ đi, mở Nâng cao là thấy đủ như trước.
- **Mục tiêu của team được đưa lên ngay dưới danh sách thành viên.**
### Bảo mật
- **Công cụ Facebook và Meta Ads không còn đưa token cho AI.** Link "trang sau" và thông báo lỗi của Facebook có kèm token truy cập; nay Naota gỡ token trước khi trả kết quả cho model. Dữ liệu bài viết, bình luận và con trỏ phân trang giữ nguyên.

## [1.35.0] - 2026-11-13
### Thêm mới
- **Ô chat tự nhảy số thứ tự.** Dòng trên là `1. ...` thì xuống dòng sẽ có sẵn `2. `, giống trong Claude. Xuống dòng là Enter trên điện thoại, Shift+Enter trên máy tính (Enter trên máy tính vẫn là gửi). Có ở chat chính, Nhóm, Hội thoại và ô chạy thử chatbot.
- Xuống dòng lần nữa ở mục còn trống thì số tự mất để kết thúc danh sách. Chèn một dòng vào giữa thì các số bên dưới tự tăng theo.
- **Ghim thư mục lên đầu cây Vault.** Bấm nút ba chấm của thư mục rồi chọn "Ghim lên đầu". Thư mục nằm sâu bên trong cũng ghim được, không phải mở từng tầng để tới nó nữa.
- **Thư mục luôn mở sẵn.** Cũng trong menu đó, chọn "Luôn mở sẵn" thì mỗi lần mở Naota thư mục ấy đã xổ ra, ví dụ thư mục wiki.
- **Lưu theo từng brain, trên máy chủ.** Điện thoại và máy tính thấy cùng một cây, bản chạy trên VPS cũng dùng được. Đổi tên thư mục trong Naota thì ghim vẫn đi theo.
- **Bot Zalo chính thức nhận được file.** Khi Zalo chuyển file cho bot, Naota tải về và đọc luôn PDF, Word, Excel và file chữ, gửi kèm câu hỏi là trả lời theo file.
- **Không còn im lặng.** Zalo chưa có loại tin file riêng cho bot, nên khi Zalo không kèm nội dung thì bot nói thẳng là chưa nhận được và nhờ gửi ảnh chụp hoặc dán chữ. Trước đây bot im.
- **Chatbot trả lời được trên WeChat.** Ở Chatbot, Thêm kênh có thêm **WeChat**: bot chuyên trách trả lời người theo dõi WeChat Official Account của bạn, mọi cuộc chat vào chung Hộp thư và bạn tiếp quản được như các kênh khác.
- **Cài đặt gọn.** Form hiện sẵn địa chỉ webhook và Token để dán sang WeChat; bên Naota chỉ cần dán AppID và AppSecret. Bấm Kiểm tra là biết ngay IP nào cần thêm vào whitelist.
- **Cần biết:** WeChat chỉ cho tài khoản đã xác minh (hoặc tài khoản thử nghiệm) trả lời qua API, chỉ trong 48 giờ sau tin cuối của khách, gửi được chữ và ảnh. Hướng dẫn từng bước ở tài liệu 36.
- **Hồ sơ khách hàng.** Sau khi một cuộc chat riêng im khoảng 15 phút, model chạy nền tự ghi lại những gì cần nhớ về khách: tên, cách xưng hô, liên hệ, đang quan tâm gì, đã chốt gì, việc còn dang dở. Lần sau bot đọc hồ sơ này cùng 30 tin gần nhất nên không phải hỏi lại, kể cả khi khách quay lại sau vài tháng.
- **Ô ghi chú về khách thành mục Hồ sơ khách hàng** trong khung Thông tin của trang Hội thoại, dài tới 4.000 ký tự. Bạn vẫn sửa, ghi thêm hay xoá trắng được, phần bạn viết được giữ lại ở lần cập nhật sau.
### Sửa lỗi
- **Naota Store hiện gói "Trọn bộ".** Gói gồm nhiều loại trong một, như Quản lý khách hàng (CRM), trước đây không nằm ở tab nào nên không tìm và không cài được từ trang Store. Giờ có tab "Trọn bộ" ở cuối hàng tab.
- **Bộ cài Windows hết đứng im.** Trước đây lỗi nằm chờ bấm Enter trong cửa sổ đen bị che, hoặc một trình cài phụ (winget, npm, Grok, Antigravity) không chịu kết thúc là cả bộ cài treo. Giờ mỗi bước có giới hạn thời gian, quá giờ thì bỏ qua và đi tiếp.
- **Tải Git, Python, Node nhanh hơn nhiều** trên máy không có winget.
- **Đọc tiếng Anh vào mic không còn bị tự dịch sang tiếng Việt.** Sau khi bấm dừng, Naota nhờ mô hình viết lại câu cho đúng chính tả, và mô hình đôi khi trả về bản dịch tiếng Việt thay vì câu tiếng Anh đã nói (hay gặp ở câu dài, lần đọc thứ hai). Giờ câu nói bằng tiếng nào thì giữ đúng tiếng đó. Nếu mô hình vẫn dịch, Naota bỏ bản dịch và giữ nguyên lời đã nghe. Áp dụng cho mic ở chat chính, Nhóm, Hội thoại và trình sửa ghi chú.
- **Bot không còn quên khách sau mỗi lần cập nhật.** Trước đây lịch sử chat riêng của bot chỉ nằm trong bộ nhớ tạm, nên Naota khởi động lại là bot gặp khách cũ như người lạ. Giờ bot đọc lại cuộc chat từ Hộp thư, gồm cả câu bạn tự trả lời tay.
- **Đăng nhập được MCP có thông tin OAuth đặt ở máy chủ khác (impact.com).** Trước đây thẻ kết nối báo máy chủ không khai OAuth chuẩn MCP. Nay Naota đọc thông tin đó khi nó nằm trên https công khai, do chính địa chỉ MCP đã khai trả về, và đúng là của địa chỉ đó.
- **Tắt riêng bản tổng hợp Việc của tôi lúc 07:30 khi đã có Morning Brief.** Đặt `agenda_enabled: false` trong `Naota/my-tasks.json` của brain cần tắt. Không thay đổi task, nhắc deadline, lịch hẹn hay thông báo thói quen của brain đó. Mặc định các brain khác vẫn có bản tổng hợp như cũ.
- **Tag bot Zalo trong nhóm không còn bị nhầm là tag người khác sau khi Naota khởi động lại.** Lưu Zalo ID đã xác minh từ tin do chính tài khoản gửi, dùng lại khi khởi động lại và từ chối ID không khớp.
- **Tạo ảnh ChatGPT không mắc kẹt ở tài khoản hết lượt.** Khi tài khoản đang dùng báo lỗi hạn mức, Naota thử tài khoản ChatGPT đã đăng nhập tiếp theo theo thứ tự trong Models. Lỗi khác không tự gửi lại yêu cầu tạo ảnh và tài khoản bị tắt không được sử dụng.
### Cải thiện
- **Mỗi dòng trong cây Vault chỉ còn một nút ba chấm.** Tạo file, tạo thư mục, ghim, tải về, đổi tên, xoá đều nằm trong menu bấm ra, nên tên file không còn bị các nút che mất, nhất là trên điện thoại.
- **Cài trên Windows không còn cửa sổ đen riêng.** Tiến trình cài hiện ngay trong cửa sổ Setup: dòng "Bước 2/5", thanh chạy liên tục và một khung ghi từng việc đang làm.
- **Lỗi hiện ngay trong Setup.** Bước nào hỏng thì Setup nói rõ thiếu gì kèm đường dẫn nhật ký, trang cuối không còn báo "đã cài xong" khi chưa xong.
- **Bot xem lại 30 tin gần nhất của chat riêng thay vì 20.** Áp cho mọi kênh bot (Zalo Bot, Zalo cá nhân, Telegram, Messenger...). Cuộc chat có tin rất dài thì bot bớt từ tin cũ nhất. Nhóm vẫn xem 30 tin trước tin đang hỏi như cũ.
- **Chỉ chat riêng mà bot đã trả lời mới có hồ sơ.** Nhóm và các cuộc chat của bạn bè, người nhà trên nick Zalo cá nhân thì không. Mỗi 5 phút Naota làm tối đa 5 hồ sơ nên không tốn hạn mức dồn dập.
### Bảo mật
- **Bot của chủ không tải gì của người lạ.** Ảnh, tin thoại và file chỉ được tải về khi chat đã được bấm Cho phép.
- **Tin WeChat giả bị chặn từ cửa.** Naota kiểm chữ ký từng tin, từ chối yêu cầu cũ quá 15 phút, và tài khoản bật Chế độ an toàn thì chỉ nhận tin đã mã hoá.
- **Kết nối Chỉ đọc không còn xin phạm vi dạng `mcp:write`.** Khi đăng nhập theo kiểu Naota tự dò và máy chủ có sẵn phạm vi đọc (vd `mcp:read`), kết nối đặt Chỉ đọc bỏ các phạm vi có tên kết thúc bằng `write`. Kiểm tra tên tool của hub vẫn là lớp chặn chính. Nâng mức quyền sau đó thì phải đăng nhập lại.

## [1.33.0] - 2026-11-11
### Cải thiện
- **Khung chat trên điện thoại gọn hơn.** Vòng hạn mức, tên model và mức suy nghĩ gộp thành một viên duy nhất (ví dụ "Opus 5.5 Medium"), tên model không còn bị cắt thành "Op...".
- **Bấm vào viên đó là mở một bảng từ dưới lên**, có đủ ba thứ: hạn mức gói (mỗi khung một dòng), thanh mức suy nghĩ kèm Fast mode, và danh sách model có ô tìm. Chọn model xong bảng tự đóng; bấm X, bấm vùng mờ hoặc kéo xuống cũng đóng.
- Bản máy tính giữ nguyên ba nút và ba bảng nhỏ như trước.
- **Điện thoại: nút chọn model về khung nhập, đứng ngay cạnh nút mức suy nghĩ** y như bản máy tính. Bấm vào thì bảng chọn model mở ngay phía trên khung nhập, vừa khít bề ngang màn hình.
- **Thanh trên cùng gọn hơn:** chỉ còn nút menu, chuông thông báo và nút + hội thoại mới.

## [1.32.0] - 2026-11-11
### Thêm mới
- **Nút "Đúng trợ lý cũ, xác nhận tất cả" theo gói** trên trang Cộng sự. Khi Naota vẫn phải hỏi về nhiều trợ lý của cùng một gói, bấm một lần là xong, không phải mở từng thẻ.
- **Bấm tên file Naota tạo ngoài brain để mở ngay.** Ví dụ một bài giảng nằm trong ~/Documents. Trước đây khung chat chỉ hiện tên file như chữ thường. Giờ đường dẫn đầy đủ thành link, bấm vào là file mở bằng ứng dụng mặc định trên máy, như khi nhấp đúp trong Finder.
- Link chỉ hiện khi bạn dùng Naota ngay trên máy đang chạy nó. Trên VPS, qua tên miền hoặc trong Docker, đường dẫn vẫn là chữ như cũ để bạn sao chép. Link chỉ mở file trong thư mục người dùng. Chương trình và script không được chạy, Naota chỉ mở thư mục chứa chúng.
### Sửa lỗi
- **Cài lại gói Store không còn bắt xác nhận Auto từng trợ lý.** Gỡ rồi cài lại một gói, Naota tự nhận các trợ lý của gói là trợ lý cũ: công tắc Auto, mục tiêu và cuộc trò chuyện giữ nguyên. File bạn tự tạo trùng tên một trợ lý cũ thì vẫn được hỏi như trước.
- **Trợ lý chưa bật Auto và không có mục tiêu đang mở không còn báo "Cần xác nhận"** khi file của nó mất rồi có lại.
### Cải thiện
- **Màn chào mừng: nhập mật khẩu hai lần.** Hai ô không giống nhau thì Naota báo ngay và đưa bạn tới đúng ô cần sửa, chưa tạo tài khoản. Gõ nhầm một ký tự không còn làm mất quyền vào máy mới cài.
- **Có nút con mắt để xem mật khẩu.** Bấm là hiện cả hai ô cùng lúc để so cho dễ, bấm lần nữa là ẩn lại.

## [1.31.0] - 2026-11-11
### Thêm mới
- **Hộp thư báo khi câu bot trả lời chưa tới khách trên Zalo cá nhân.** Trước đây câu bot soạn xong là hiện trong Hộp thư như đã gửi, dù Zalo từ chối hay gửi hết giờ. Giờ tin gửi được thì không hiện gì thêm. Tin chưa gửi được, tin chưa rõ kết quả hoặc tin bị bỏ vì khách nhắn thêm sẽ có một dòng nhỏ ngay dưới, kèm lý do. Tin kẹt ở trạng thái đang gửi quá 5 phút tự chuyển thành chưa rõ kết quả.
- **Kết quả tool lớn không còn bị cắt mất phần giữa.** Naota cất bản đầy đủ, đưa cho model phần gọn kèm mã tham chiếu, và model đọc lại đúng phần nó cần. Báo cáo hết thiếu đơn, lại tốn ít token hơn trên mọi bộ não.
- **Tính bằng code, không nhẩm.** Tool `naota_query` tự lật hết các trang rồi cộng, đếm, xếp hạng bằng SQL chỉ đọc. Model lớn hay nhỏ đều ra cùng một con số.
- **Trinh sát bằng model nền.** Việc đọc nhiều nguồn có thể giao cho model việc nền (`naota_scout`), chỉ kết luận quay về khung chat. Trinh sát chỉ đọc, không gửi hay tạo gì.
- **Việc định kỳ nhớ cách lấy số.** Sau hai lần chạy giống nhau ở hai ngày khác nhau, Naota tự lấy sẵn dữ liệu cho lần sau. Chưa chắc về ngày tháng thì chạy như cũ.
### Sửa lỗi
- **Trình kết nối không khởi động được không còn bị báo nhầm là "hết phiên đăng nhập".** Naota nhận lỗi đăng nhập bằng cách tìm số 401 trong câu lỗi, nên khi đường dẫn cài đặt tình cờ có chứa 401, lỗi "không tìm thấy file" hiện thành lời mời bấm Kết nối lại. Giờ 401 (và 502, 503, 504) chỉ được tính khi đứng riêng như một mã lỗi.
- **Gỡ gói ở Store nay nói rõ đồ của gói nằm ở brain nào.** Cộng sự và skill của một gói chỉ được đặt vào brain đang mở lúc cài. Trước đây đứng ở brain khác bấm gỡ là mất đồ ở brain kia mà màn xác nhận không nói đó là brain nào.
- Thẻ gói cũng ghi rõ khi đồ của gói nằm ở một brain khác với brain đang mở, thay vì chỉ ghi "Đã cài".
### Cải thiện
- **Tìm tool gọn hơn**, và mục Đề xuất ở trang Mức dùng cho biết kết quả tool đã giữ được bao nhiêu ngoài hội thoại.

## [1.30.0] - 2026-11-11
### Thêm mới
- **Công cụ hay dùng được ghim sẵn theo từng brain.** Khi brain đấu nhiều nguồn, công cụ phải "tìm rồi mới gọi", tốn thêm một vòng mỗi lần dùng. Giờ Naota tự đếm công cụ nào mỗi brain gọi nhiều nhất và ghim sẵn vài cái (mặc định tối đa 4, Naota Core tự nới tới 8 khi cần): công cụ đã ghim được gọi thẳng. Việc nền như loop được lợi nhiều nhất vì trước đây lần nào cũng phải tìm lại. Không phải cài gì, có thông báo ở chuông khi ghim.
- **Xem và tắt bằng lời.** Hỏi Naota "đang ghim công cụ nào" để xem danh sách kèm số lượt gọi thẳng và số lượt còn phải tìm. Nói "đừng ghim công cụ nữa" để tắt.
- **Model việc nền có chế độ Tự động, và là mặc định.** Trước đây việc nền chạy bằng model mặc định của nhà cung cấp, trên gói thuê bao thường là model mạnh và tốn nhất. Giờ Naota dùng nhà cung cấp của MAIN và chọn sẵn hai model từ danh sách của chính nhà đó: model nhẹ cho việc Naota tự làm (tự học, gợi ý câu tiếp theo, chấm điểm), model bậc giữa cho việc bạn giao chạy nền (nhắc hẹn, loop, Kanban). Trang Models ghi rõ hai model đang dùng. Naota chỉ chọn lại khi danh sách model của nhà đó thay đổi, và báo ở chuông mỗi lần chọn.
- **Mỗi việc nền tự tìm model vừa đủ cho nó.** Hai model trên chỉ là điểm xuất phát. Từng nhắc hẹn, từng loop, từng loại việc Kanban và tự học có một bậc riêng: hỏng vì model yếu thì lần chạy sau leo một bậc, chạy tốt nhiều lần liền thì thử xuống một bậc, không được thì quay lại. Lỗi do hết hạn mức, mất đăng nhập hay đứt kết nối không làm đổi model. Mỗi lần đổi có thông báo ở chuông kèm lý do.
- **Chỉnh việc nền bằng lời, không có ô cài đặt.** Nói "tiết kiệm token giúp anh", "việc gửi báo cáo phải thật chắc", "báo cáo sáng nay sai rồi" hay "việc nền đang chạy model gì": Naota ghi ý định của bạn cho mọi việc hoặc riêng một việc, điều chỉnh theo, và hoàn lại được một lần đổi model khi bạn bảo.
- **Model bạn tự chọn thì Naota không bao giờ đổi.** Bấm Đổi model ở khối Model việc nền và chọn một model: nó giữ nguyên. Muốn về Tự động thì chọn dòng "Tự động (khuyên dùng)" ở đầu danh sách. Máy đã cài: model nền còn nguyên cấu hình mặc định thì chuyển sang Tự động, bạn từng chọn model khác thì giữ nguyên.
- **Việc Naota tự làm tự nghỉ khi gói sắp hết hạn mức.** Cửa sổ 5 giờ của gói đã dùng từ 80% thì tự học và gợi ý câu tiếp theo chờ tới lúc hạn mức mở lại, phần còn lại để dành cho chat của bạn.
- **Naota Core giữ một vòng cải tiến chung.** Phần nào của Naota muốn tự điều chỉnh thì đăng ký một "núm chỉnh" với Naota Core. Vòng dời núm theo cùng một cách: mỗi lần một bước, trong khoảng cho phép, nhiều nhất một lần mỗi ngày, có ghi lý do, có thông báo ở chuông và hoàn lại được bằng lời. Vòng này chỉ là mã, không gọi model và không chạm vào lượt chat.
- **Tự học tự chỉnh ngưỡng mở mẻ.** Khi phần lớn các mẻ học gần đây không rút ra được gì (thường gặp khi bạn hay hỏi nhanh một hai câu), Naota Core tự nâng số lượt cần có trước khi mở một mẻ; các mẻ có ích trở lại thì tự hạ xuống. Lượt chưa đủ ngưỡng vẫn nằm chờ và được học cùng các lượt sau.
- **Dặn Naota nên học thế nào, bằng lời.** Nói "đừng ghi doanh thu từng ngày thành ghi nhớ" hay "chỉ ghi nhớ quyết định đã chốt": Naota Core giữ thành một bài học và mọi mẻ tự học đọc nó trước. Xem và thu hồi như bài học của mọi trợ lý.
### Cải thiện
- **Danh sách ghim tự theo thói quen.** Công cụ lâu không dùng tự rời danh sách, công cụ mới dùng nhiều tự vào. Danh sách của một brain đổi nhiều nhất một lần mỗi ngày và có giới hạn kích thước, nên prompt không phình và phần lưu đệm của nhà cung cấp ít bị làm mới.
- **Điều bạn dặn Naota Core được giữ nguyên.** Một giá trị bạn đặt bằng lời cho bất kỳ núm tự chỉnh nào thì Naota Core không tự đổi lại trong 30 ngày, kể cả sau khi khởi động lại.
- **Tự học mặc định chỉ học ký ức và wiki.** Học skill mở thêm một lượt phản biện mỗi mẻ và kéo theo cả phần chấm điểm skill chạy ngầm, là chỗ tốn hạn mức nhất khi bạn không gõ gì. Máy đã cài cũng được tắt một lần; cần thì bật lại công tắc Kỹ năng ở trang Tự học.
- **Tự học chạy 15 phút sau sự kiện cuối cùng, một lần cho cả cuộc trò chuyện.** Trước đây cứ 3 lượt chat là một mẻ học, nên một cuộc 12 lượt mở 4 mẻ đọc lại gần như cùng một đoạn. Giờ Naota chờ brain yên 15 phút (bạn hỏi thêm, việc nền chạy xong hay khách đang nhắn với chatbot đều tính lại từ đầu) rồi học một mẻ, mỗi tin nhắn chỉ đọc một lần. Cả ngày không có sự kiện nào thì không học và không tốn gì. Câu "ghi nhớ giúp" vẫn được học sau 30 giây, và brain bận liên tục (chatbot có khách suốt ngày) thì vẫn học sau tối đa 2 giờ.
- **Bỏ trần ngày của tự học.** Trần 40 mẻ và 15 triệu token mỗi ngày không hợp cho cả người dùng nhiều lẫn người dùng ít, và chạm trần thì Naota vẫn chạy mẻ học rồi chỉ không ghi file. Nhịp mới đã giữ số mẻ theo đúng số cuộc trò chuyện.
- **Gợi ý câu tiếp theo và các lượt chỉ cần chữ nhẹ đi nhiều.** Những lượt này (gợi ý câu tiếp theo sau mỗi lượt chat, bộ phán xử, phân loại sự cố, câu nhắc thói quen) không dùng công cụ nào nhưng vẫn gửi kèm cả bộ luật và mô tả công cụ của Claude Code. Phép đo sẵn có trong mã cho cùng một câu: 27.665 token khi gửi kèm, 183 token khi không. Giờ chúng không gửi kèm nữa.
- **Ghi nhớ học sai được tính vào kết quả.** Một ghi nhớ Naota tự học mà bạn bảo xoá được tính là một lần học sai, nên mẻ học sau tự dùng model mạnh hơn một bậc. Ghi nhớ do bạn tự viết bị xoá thì không ảnh hưởng gì.
- **Một chỗ để xem và hoàn lại.** Hỏi Naota "việc nền và tự học đang chỉnh gì": một câu trả lời gồm model của từng việc nền, các núm đang tự chỉnh, các thay đổi gần đây và bài học về cách học.

## [1.29.0] - 2026-11-11
### Cải thiện
- **Zalo cá nhân: có tin là Naota đọc ngay, không còn quét 20 giây một lần.** Trước đây Naota hỏi Zalo đều đặn cả ngày kể cả khi không có tin nào, và tin trong nhóm phải chờ tới 20 giây bot mới thấy. Giờ tin tới lúc nào Naota đọc lúc đó; ngày không có tin thì không đọc lần nào.
- Không có tin thì Naota không chạy nhịp nào cho Zalo. Tiến trình Zalo bị tắt thì Naota dựng lại ngay và đọc bù. Máy chưa lên bản Zalo mới vẫn chạy theo nhịp cũ, không mất tin.

## [1.28.0] - 2026-11-11
### Thêm mới
- **Lịch nhắc chạy việc nay gửi kèm ảnh nó vừa tạo.** Báo cáo định kỳ dạng ảnh (quảng cáo, doanh số theo mẫu cố định) trước đây chỉ tới Zalo Bot và Telegram phần chữ, còn ảnh nằm lại trong brain. Giờ ảnh có trong câu trả lời và được tạo trong đúng lượt chạy đó sẽ đi cùng, tối đa 4 ảnh mỗi lượt.
- Zalo Bot chỉ nhận ảnh, nên PDF hay bảng tính vẫn như cũ. Ảnh gửi lỗi không làm hỏng lượt nhắc: phần chữ vẫn tới.
### Sửa lỗi
- **Trợ lý tạo lại đúng tên cũ đã xác nhận được Auto.** Thẻ báo "Auto: Cần xác nhận" nhưng bấm vào thì cột phải không có hai nút "Đúng trợ lý cũ" và "Đây là trợ lý mới", nên không cách nào bật lại Auto. Nay hai nút hiện ra ngay dưới phần cài đặt của trợ lý.
- **Trang Models không còn làm app ì dần.** Mỗi lần mở trang để lại một lớp theo dõi thao tác kéo thả không bao giờ gỡ. Nay chỉ còn một lớp dùng chung.
- **Chatbot dùng gói ChatGPT nay tự chuyển tài khoản khi hết lượt.** Trước đây bot riêng luôn gọi bằng tài khoản 1, bỏ qua thứ tự tài khoản ở trang Models, nên tài khoản 1 hết lượt là bot báo lỗi 429 dù tài khoản khác còn dùng được.
- Bot chỉ đổi tài khoản khi chưa nói chữ nào và chưa gọi công cụ nào, nên khách không nhận tin trùng.
- **Claude trả lời lại trên máy Windows cài bằng npm.** Sau khi cập nhật, mọi lượt chat Claude báo "Refusing to execute batch script ...claude.CMD". Naota giờ tự tìm `claude.exe` thật nằm cạnh file đó (hoặc bản cài native, hoặc bản đi kèm SDK) nên không cần cài lại gì. Codex không dính lỗi này.
- **Codex chạy đúng mức suy luận đã chọn ngay sau khi Naota khởi động lại.** Trước đây, cho tới khi có người mở trang Models, bot và việc nền chạy bằng Codex rơi về mức mặc định của Codex (thường là cao) dù đã chọn thấp hay trung bình, nên chậm và tốn lượt hơn.
- **Việc nền chạy bằng Codex không còn bị bỏ cả lượt vì cổng công cụ lên chậm.** Trước đây cổng trả lời chậm hơn 20 giây là lượt nhắc hẹn hay lịch định kỳ đó hỏng luôn, phải chờ tới lần chạy kế tiếp. Giờ Naota chờ cổng tới 45 giây và tự thử lại một lần sau 30 giây. Lỗi này xảy ra trước khi gọi model nên thử lại không tốn lượt và không lặp hành động nào.
- Hiện lại mục Sửa cấu hình cho MCP tự thêm đã đăng nhập OAuth. Khi sửa URL, biểu mẫu giữ đăng nhập và chặn chuyển thông tin OAuth sang máy chủ khác.
- **Claude Fable 5.2 đã có trong ô chọn model.** Trước đây danh sách model Claude chỉ lấy từ bản Claude Code đang cài, nên máy nào Claude Code chưa lên bản mới thì không thấy model mới dù đã cập nhật Naota. Nay danh sách gộp cả model mà bản Naota biết, bản mới nhất đứng trên.
- **Thêm Claude Haiku 5.5 vào danh sách dự phòng và sửa giá quy đổi** của Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5 trên trang Mức dùng.
- Công cụ được tìm qua Hub có thêm cách nhận tham số bằng chuỗi JSON, tránh mất các trường dữ liệu trên một số cổng tương thích. Tham số sai định dạng bị từ chối trước khi gọi công cụ; quyền truy cập vẫn giữ nguyên.
- **Bot nhóm tự gỡ các nhãn "bỏ lỡ" sai đã học trước đây.** Bản 1.28.0 chặn nhãn sai mới, còn nhãn cũ vẫn nằm trong kho và tiếp tục đẩy bot nói nhiều. Lần mở kho đầu tiên sau khi cập nhật, Naota gỡ nhãn "bỏ lỡ" gắn trên lượt thả cảm xúc, trả lại ngưỡng cho các nhóm bị kéo lệch, và thôi coi nhãn tự suy ra từ tin của chủ là lời chủ dạy.
- Lời chủ dạy thật (bấm 👍/👎, bảo bot im, dạy trong chat) giữ nguyên.
- **Bot nhóm không còn tự học sai rằng phải trả lời lượt thả cảm xúc.** Chủ thả tim vào tin của khách, hay một người thả hai cảm xúc liền nhau, từng bị tính là bot "bỏ lỡ" tin trước đó, khiến bot nói nhiều dần lên ở đúng những nhóm nó im là đúng.
- Chữ "up" trong câu thường như "up ảnh giúp em" và "hỏi lại" trong một câu dặn dài không còn bị hiểu là khách hỏi lại vì không ai trả lời.
- Nhãn bot tự suy ra từ tin của chủ không còn được tính nặng như lời chủ dạy trực tiếp.
- **Nhóm (Team) không còn kẹt ở tài khoản đã hết lượt.** Thẻ Claude Code, ChatGPT hay Grok Build có nhiều tài khoản thì lượt của cộng sự trong nhóm giờ chạy trên tài khoản còn hạn mức, giống chat và việc nền. Trước đây nhóm luôn chạy tài khoản 1, nên tài khoản 1 hết lượt tuần là cả nhóm báo "You've hit your weekly limit" dù tài khoản kia vẫn còn.
- **Hết lượt giữa lượt nhóm thì tự chạy lại bằng tài khoản kế.** Tài khoản báo hết lượt trước khi gọi công cụ nào: Naota cho nó nghỉ và chạy lại ngay, tin trả lời ghi rõ đang dùng tài khoản nào. Bước đã gọi công cụ thì không chạy lại, để không gửi hay đăng hai lần.
- **Câu báo hết lượt không còn bị đăng thành câu trả lời của cộng sự.** Claude Code đôi khi in câu đó như một câu trả lời thường, nhóm giờ nhận ra và xử lý như lỗi hết lượt.
- **Workflow cũng xoay tài khoản.** Bước workflow chạy bằng Claude Code hay ChatGPT bắt đầu trên tài khoản còn lượt; tài khoản hết lượt khi bước chưa làm gì thì bước đó tự chạy lại bằng tài khoản kế và lần chạy đi tiếp. Trước đây cả lần chạy dừng với câu "gói hết lượt" dù tài khoản kia vẫn còn.
- **Thẻ ở trang Models ghi đúng tài khoản đang dùng.** Dòng đầu thẻ hiện tên, email và gói của tài khoản đang chạy. Trước đây nó luôn ghi tài khoản 1, nên thẻ đang chạy tài khoản Max vẫn đề "Pro".
- **Bước quy trình nay chạy đúng mức suy luận của trợ lý.** Trước đây mức suy luận đặt cho một trợ lý chỉ có tác dụng khi chat và trong nhóm; bước quy trình, kể cả việc Kanban giao theo quy trình, luôn chạy ở mức mặc định của model. Trợ lý chưa đặt mức thì bước vẫn chạy như cũ.
### Cải thiện
- **Câu trả lời dài chảy ra không còn khựng.** Trong lúc chữ đang về, Naota chỉ vẽ lại đoạn đang viết dở, các đoạn đã xong giữ nguyên. Đo với một câu trả lời 20.000 ký tự trên điện thoại yếu: thời gian vẽ từ 5,4 giây xuống 1 giây, hết hẳn các lần đứng hình.
- **Màn chính lúc rảnh nhẹ máy hơn.** Nền sao sau quả cầu vẽ thưa lại khi không ai nói và Naota không nghĩ, nhìn vẫn như cũ. Điện thoại đỡ nóng và đỡ hao pin khi để mở.

## [1.27.0] - 2026-11-11
### Thêm mới
- **Claude Agent SDK tự cập nhật.** Cùng công tắc "Tự cập nhật Claude Code mỗi ngày" ở trang Models nay giữ luôn gói Claude Agent SDK ở bản mới nhất trong dòng của nó. Naota chỉ lấy bản đã ra ít nhất ba ngày, chạy thử trước khi giữ, lỗi thì tự lùi về bản cũ. Bản mới dùng từ lần khởi động lại kế tiếp. Bản Docker vẫn nhận theo ảnh Naota mới.
### Sửa lỗi
- **Kết nối Google Ads không còn đòi developer token.** Ô này giờ là tuỳ chọn và hướng dẫn đi theo đường Google Cloud: bật Google Ads API, bấm xin mức Explorer ngay trong project, rồi tạo OAuth client. Người mới không còn kẹt ở bước xin một token mà Google không còn yêu cầu.
- **Ảnh trong chat không còn tự thành ô trống sau 30 ngày.** Trước đây phiên đăng nhập hết hạn đúng 30 ngày sau lần đăng nhập dù ngày nào cũng dùng, chat vẫn chạy nhưng ảnh và danh sách tải không được mà không báo gì. Giờ còn dùng là phiên tự gia hạn.
- **Phiên hết hạn giữa chừng thì hiện ngay màn đăng nhập** thay vì để trang hỏng lặng lẽ.
### Cải thiện
- **Chat nhẹ đĩa hơn, và một kết nối hỏng không còn kéo chậm mọi lượt.** Mỗi lượt chat bớt hàng chục lần ép ghi đĩa (đỡ rõ trên VPS). Nguồn dữ liệu đứng hình hai lần liền thì Naota trả lời ngay bằng danh sách công cụ đang có và dò lại ở nền.
### Bảo mật
- **Tool sửa nhãn của Google Ads không còn chạy được ở mức Chỉ đọc.** Bản MCP mới của Google có thêm tool tạo, sửa, xoá nhãn và tải video lên YouTube; hai tool nhãn từng bị xếp nhầm vào nhóm đọc. Giờ chúng chỉ chạy ở mức Toàn quyền, tạo asset ở mức Ghi nháp, và thẻ kết nối nói rõ mỗi mức sửa được gì.
- **Siết khung chat, trung tâm công cụ và việc chạy nền.** Chữ trong tin nhắn không còn chen được mã vào trang điều khiển. Trung tâm công cụ chỉ trả lời chính máy đang chạy Naota. Việc chạy ở mức Ghi nháp chỉ ghi được file thường trong bộ não.
- **Chatbot trả lời khách dưới mức Toàn quyền không còn giao được việc cho AI chạy sau.** Nó vẫn tạo được lời nhắc chỉ nhắc bằng chữ. Cần bot tự giao việc thì nâng bot lên Toàn quyền.
- **Bộ não nhập từ tệp về luôn ở trạng thái nghỉ.** Vòng lặp, plugin và nhắc việc đều tắt dù tệp viết kiểu nào; cấu hình chạy lệnh của các engine không được nhập theo. Thư viện đọc PDF lên bản đã vá.

## [1.25.6] - 2026-11-10
### Sửa lỗi
- **Ô Chi phí AI ở trang Văn phòng chỉ còn tính tiền thật.** Trước đây ô này cộng cả giá quy đổi của các lượt chạy bằng gói tháng (Claude Code, Grok), nên dùng gói Pro hay Max vẫn hiện vài chục đô dù không bị trừ thêm đồng nào. Giờ ô chỉ cộng tiền trả theo khoá API, lượt chạy bằng gói tháng vẫn được đếm nhưng tính 0 đô.

## [1.25.5] - 2026-11-10
### Sửa lỗi
- **Logo không còn vỡ khi mạng máy chủ chập chờn.** Trình duyệt trước chỉ giữ logo 1 phút, nên tải lại trang đúng lúc mạng rớt là màn khởi động và thanh bên hiện ảnh hỏng. Giờ logo được giữ lâu, đổi logo thì tự lấy ảnh mới.

## [1.25.4] - 2026-11-10
### Sửa lỗi
- **Mở hay tải lại trang nhanh trở lại, chừng 1 đến 2 giây.** Màn "Đang khởi động Naota..." từng đứng đủ 12 giây mỗi lần vì chờ dòng "Đang tải thêm..." ở cuối danh sách hội thoại, dòng này không bao giờ mất. Giờ màn khởi động bỏ qua dòng đó.

## [1.25.3] - 2026-11-10
### Sửa lỗi
- **Không còn chỗ nào hiện mã kiểu `page.chat.label` hay `app.pin_meta` thay cho chữ.** Chú thích khi rê chuột vào menu trái, nút trong cây file, dòng dưới file đang ghim ở ô chat từng kẹt ở mã vì được vẽ trước khi bộ chữ tải xong. Giờ bộ chữ tải xong là các chỗ đó tự đổi thành chữ.

## [1.25.2] - 2026-11-10
### Cải thiện
- **Số node và liên kết chuyển vào góc trên bên trái bản đồ bộ não**, rời thanh đầu trang cho gọn. Nút con mắt ẩn nó cùng nhãn thư mục.
- **Ô chọn bộ não ghi số node và liên kết trên một dòng**, không còn bị gãy làm hai.

## [1.25.1] - 2026-11-10
### Cải thiện
- Dọn dữ liệu mẫu trong bộ kiểm thử và từ điển phát âm.

## [1.25.0] - 2026-11-09
### Thêm mới
- **Mỗi hội thoại trong cột lịch sử có một nút ⋯** thay cho bốn icon rời (ghim, chuyển project, đổi tên, xoá). Menu có: Ghim lên đầu, Chuyển vào project, Đổi tên (sửa ngay tại dòng), Chia sẻ link, Xuất ra file .md, Đánh dấu chưa đọc, Lưu trữ và Xoá. Bấm chuột phải, hoặc nhấn giữ trên điện thoại, cũng mở menu này.
- **Lưu trữ hội thoại:** hội thoại lưu trữ rời khỏi danh sách nhưng giữ nguyên nội dung, Naota vẫn nhớ và ô tìm kiếm vẫn tìm thấy. Mục "Đã lưu trữ" ở đáy cột mở danh sách này. Nhắn tiếp vào hội thoại đã lưu trữ thì nó tự trở lại danh sách.
- **Chọn bộ não nào làm mặc định.** Trong bảng chọn bộ não, bấm ngôi sao ở một bộ não để đặt nó làm mặc định. Đổi xong thì bộ não mặc định cũ thành bộ não thường và xoá được (vẫn vào thùng rác 30 ngày).
- **Ô xoá bộ não nói rõ trước** bao nhiêu vòng lặp, nhắc việc sẽ dừng theo, và bot nào đang trả lời từ bộ não đó.
- **Bấm Kết nối GitHub, Naota kiểm tra máy có git chưa, thiếu thì tự cài** rồi mới mở bước đăng nhập. Cài không được thì hiện đúng lệnh để cài tay, nút Thử lại và nút Bỏ qua.
### Sửa lỗi
- **Giờ trong thông báo khớp múi giờ trong Cài đặt.** Trên VPS, cảnh báo bảo mật, thông báo hệ thống, giờ đồng bộ sao lưu và giờ sự kiện webhook từng in giờ máy chủ (UTC), lệch 7 tiếng.
- **Quy trình chạy bằng agent Claude dùng được mọi kết nối của Naota**, không còn báo "thiếu công cụ" khi cần Gmail, Sheet, Zalo hay MCP khác.
- **Trang Chatbot, mục Hội thoại chỉ hiện hội thoại của bộ não đang mở**, kể cả số đếm.
- **Git vừa cài xong được nhận ngay**, không phải khởi động lại Naota.
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
- **Token API cho CLI chuyển sang trang Tích hợp** (nhóm Việc, trước là Webhook), tab Token API. Cả hai đều là cửa để chương trình khác gọi vào Naota nên giờ nằm chung một chỗ. Token đã tạo vẫn dùng như cũ.

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
- **Màn hình khởi động:** mở Naota là thấy logo cùng dòng "Đang khởi động Naota…" cho tới khi trang đầu tiên đã có đủ dữ liệu. Naota vừa cập nhật hay khởi động lại thì màn này báo thêm lần mở đầu có thể lâu hơn một chút.
- **Mọi màn đang chờ tải dùng chung một hiệu ứng** như trang Cộng sự: vòng xoay nhỏ kèm chữ "Đang tải", trang lớn thì vòng xoay ở giữa. Trang đang nạp không còn hiện nhầm câu "đang phát triển".
- **Số node và liên kết trên thanh trên cùng chỉ hiện ở màn mạng nơ-ron**, các trang khác gọn hơn.
- **Hộp chọn bộ não ghi số node và số liên kết của từng bộ não**, đúng như đồ thị đếm. Số chỉ được đếm khi mở hộp, nên không làm chậm lúc tải trang.
- **Trang Cộng sự và Team hiện dòng "Đang tải…"** ở chỗ danh sách và cuộc trò chuyện chưa về, thay vì để trống như bị treo.
- **Mở một team là thấy ngay tab Thông tin** ở khung bên phải trên màn rộng. Đóng khung đó thì lần sau Naota nhớ và để đóng.
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
- **Mở hội thoại ở trang Cộng sự hết báo nhầm "mở quá lâu".** Lúc trang đang tự kết nối lại thì không báo lỗi nữa. Mở Naota Core bị treo thì báo lỗi kèm nút Thử lại, và bấm Thử lại là tải lại thật.
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
- **Bảy bộ não chạy bằng API key cũng có thẻ Kế hoạch.** OpenRouter, OpenAI, Anthropic API, Gemini, Groq, DeepSeek và Ollama có công cụ `naota_plan`: gặp việc từ 3 bước trở lên, model lập danh sách và đánh dấu từng mục khi xong. Tốn thêm khoảng 200 token mỗi lượt; muốn tắt thì vào menu **+** ở ô nhập, mục **Kế hoạch việc dài (bộ não API)**. Chỉ khung chat của chủ có công cụ này, bot trả lời khách và việc nền thì không.
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
- **File cài đặt bị sửa từ ngoài NAOTA** thì mọi thiết bị bị đăng xuất và có cảnh báo đỏ. Lần đầu chạy bản này chỉ ghi nhận tài khoản hiện tại, không đăng xuất ai.
- **Trợ lý AI không còn đụng được file bí mật** (cài đặt, khoá mã hoá, phiên đăng nhập), ở mọi mức quyền.
- **Gỡ 2FA khi bị khoá:** thêm biến `NAOTA_RESET_2FA=1` rồi Redeploy. Mỗi giá trị chỉ dùng được một lần.
- **Hostinger: cổng 7777 tự đóng ra ngoài khi đã có tên miền HTTPS**, chỉ còn đường vào có mã hoá.
- **Lỡ lộ link quản trị thì Google không đưa lên kết quả tìm kiếm.** Mọi trang của NAOTA giờ mang lệnh `noindex`, kể cả màn hình đăng nhập và link chia sẻ.
- **Bot AI không đọc được NAOTA.** GPTBot, ClaudeBot, PerplexityBot, công cụ SEO và máy quét như Shodan, Censys nhận lỗi 403. NAOTA cũng có `/robots.txt` cấm chúng.
- Trình duyệt thật, khung xem trước link khi dán vào Zalo hay Telegram, webhook Meta, Threads, Zalo OA, link chia sẻ `/s/` và Naota Gate vẫn chạy như cũ. Cần tắt lớp chặn thì đặt `NAOTA_BLOCK_BOTS=0`.
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
- **Chỉ tiêu mỗi ngày** đặt trong `Naota/office.json`. Trang chỉ đọc, che token và đường dẫn máy chủ.

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
- **Chat của kênh quản trị** hiện trong lịch sử của Naota Core và của agent được nối, kể cả bot Zalo của anh.
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
- **Tải ảnh riêng làm avatar** và dùng ảnh đó làm icon trên tab trình duyệt, mở nhiều NAOTA cạnh nhau vẫn phân biệt được.
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
- **Đóng nhiều đường rò từ đợt rà soát:** chatbot và việc nền dưới mức Toàn quyền không còn ghi được vào chỗ chứa mã chạy, việc hẹn giờ không vượt mức quyền của người tạo, file HTML mở từ bộ não chạy trong hộp cách ly, trang lạ trên máy không gửi lệnh vào NAOTA được.
### Thêm mới
- **Trang Models mới:** nút Ngắt kết nối trên mọi thẻ, OpenAI Compatible và Claude Compatible thêm được nhiều key và tự chuyển key khi hết lượt, Antigravity trên VPS thêm được tài khoản (phần này chưa thử với `agy` thật).
- **Naota Core sửa như một trợ lý**, đổi được tên riêng theo từng bộ não. **Một bot phục vụ tới 100 Trang Facebook.** Avatar có menu tự sắp xếp, gọi thoại từ chat trợ lý thì nói đúng vai trợ lý đó.
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
- **Threads vào thẻ Kết nối Meta**: bình luận dưới bài Threads về Hộp thư, bot trả lời công khai được. Mỗi tài khoản chọn tắt, chỉ hiện Hộp thư, hoặc bot trả lời. Threads chỉ cho ẩn bình luận chứ không cho xoá, NAOTA nói rõ và hỏi lại trước khi làm.
- **Nhóm làm được nhiều hơn**: gắn repo GitHub (sửa trên nhánh riêng, mở PR, CI đỏ tự giao sửa tối đa 3 vòng), gọi `/skill` trong chat Nhóm, và thành viên tự mở việc khi được giao từ khung chat, mặc định tối đa 5 việc mỗi ngày.
- **Việc của tôi có Tags và việc con**: Dự án cũ tự thành tag, không mất gì. Ghi chú gắn được link, `[[note]]` và file.
- **Kênh API nội bộ (thử nghiệm)**: một máy chủ của bạn hỏi Chatbot qua HTTP. Khoá hiện một lần, bot chỉ đọc, mặc định chỉ chính máy chạy NAOTA gọi được.

### Cải thiện
- **Kéo thả sắp xếp** Project, chat đã ghim và tag, mọi máy thấy cùng thứ tự. Thẻ Naota Core nói rõ đang chạy model nào và chọn được ngay trên thẻ. Điện thoại có nút **Cài lên điện thoại** trong menu.
- **Claude Code chờ việc chạy nền xong** rồi trả lời tiếp, tối đa 30 phút. Câu trả lời cho tin nhắn thêm giữa chừng hiện ngay dưới tin đó. Antigravity hết báo nhầm là không đọc được file ngữ cảnh.

## [1.5.0] - 2026-11-04
### Thêm mới
- **Nhắn riêng cho người bình luận** ngay trong hội thoại bình luận: chọn Trả lời công khai hoặc Nhắn riêng phía trên ô soạn. Meta cho một lần mỗi bình luận, trong vòng 7 ngày.
- **Instagram vào chung Hộp thư**: tick "Nối cả Instagram của Trang" khi kết nối, tin nhắn và bình luận Instagram về cùng chỗ, cùng bot với Trang.
- **Menu "..." của mỗi hội thoại** có thêm Xem trang cá nhân, Chặn, Xoá hội thoại. NAOTA luôn hỏi lại trước khi Xoá, vì xoá bình luận hay hội thoại Zalo cá nhân là xoá thật trên đó.

### Cải thiện
- Thẻ Facebook Messenger đổi thành **Kết nối Meta**, có icon từng ứng dụng, thêm nút **Gỡ kết nối** từng Fanpage. Hội thoại cũ vẫn giữ. Bình luận và Instagram có icon riêng để dễ phân biệt trong Hộp thư.

## [1.4.0] - 2026-11-03
### Thêm mới
- **Chọn múi giờ** ở **Cài đặt** (khối Ngôn ngữ và múi giờ) và ở bước cuối bộ cài lần đầu. "Hôm nay, hôm qua", nhắc hẹn và số liệu báo cáo tính theo múi giờ đó, kể cả khi máy chủ chạy giờ UTC. Mặc định là giờ Việt Nam.

### Sửa lỗi
- **Hết đơ máy lúc NAOTA đang trả lời**, và hết cảnh "Đang kết nối lại" lặp đi lặp lại trên máy hay mạng chậm.
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
- **Bot Zalo trong nhóm nhận ra khi được tag bằng tên Zalo của nick**, kể cả ngay sau khi máy chủ khởi động lại. Trước đây NAOTA quên tên đó mỗi lần khởi động lại, nên tag nick bằng tên khác với tên kết nối thì bot im.

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
- **Nâng cao nằm dưới Tài khoản**, bấm là xổ Terminal, Plugin, Webhook, Phiên đăng nhập, Link chia sẻ và Cộng đồng NAOTA. Ngôn ngữ chọn trong Cài đặt. Các trang và thanh trên giữ nguyên như 1.2.1.

## [1.2.1] - 2026-11-03
### Cải thiện
- **Chợ ứng dụng có Naota Gate**: ChatGPT, Claude nối vào Naota qua một gói, đọc và nhắn vào hội thoại, ghi sổ tay. Máy đã cài gói **Naota trong ChatGPT** thấy Gate như một bản cập nhật, không phải nối lại.
- **14 gói của Chợ ứng dụng đổi sang mã tiếng Anh**, ví dụ Quản lý khách hàng là `naota.crm`. Gói đã cài hiện **Có bản mới** và cập nhật tại chỗ, giữ nguyên dữ liệu.

## [1.2.0] - 2026-11-03
### Thêm mới
- **ChatGPT, Claude ghi sổ tay vào Naota.** Khi bạn bàn việc với một AI bên ngoài đã nối vào Naota, AI đó ghi lại bạn đã nói gì, đã chốt gì và vì sao. Naota giữ được ngữ cảnh và nhớ quyết định của bạn, không tốn lượt chạy nào.
### Cải thiện
- Trang **Ghi nhớ** ghi rõ là **NAOTA**: đồng bộ NAOTA với GitHub, NAOTA tự học từ trò chuyện, NAOTA đã tự học gì.

## [1.1.1] - 2026-11-03
### Sửa lỗi
- **Menu trên điện thoại không còn đè chữ.** Các mục cuối (Nguồn dữ liệu, Chợ ứng dụng, Hệ thống...) từng tràn lên ô ngôn ngữ, ô chọn bộ não và số phiên bản. Giờ mọi thứ xếp liền nhau, vuốt xuống là thấy.

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
