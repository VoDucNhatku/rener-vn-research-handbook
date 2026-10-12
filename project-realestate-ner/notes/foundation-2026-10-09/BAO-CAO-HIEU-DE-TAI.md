# Báo cáo hiểu đề tài ReNER-VN và hướng phát triển

**Ngày:** 09/10/2026. **Phạm vi:** đọc và phản biện proposal; nghiên cứu nguồn học thuật/chính thức; thiết kế hướng paper + web + extension. Chưa triển khai hệ thống, thu dữ liệu thật hay chạy mô hình mới trong lượt này.

## 1. Điều tôi đã hiểu từ mục tiêu của bạn

Bạn muốn một hệ thống biến tin bất động sản lộn xộn thành thông tin dùng được. Ban đầu nhóm chuẩn bị dữ liệu để website có nền; người dùng sau đó dùng extension phân tích tin đang xem, tự nguyện đóng góp và sửa dữ liệu; hệ thống trả lại thông tin đã trích, các tin tương đồng và góc nhìn về giá. Trong quá trình này, bạn muốn có một paper có đóng góp và thực nghiệm thật.

Ý tưởng có hai vòng nối nhau. Vòng sản phẩm: **tin → trích xuất → kiểm tra → kho listing → tham khảo → người dùng sửa/đóng góp**. Vòng nghiên cứu: **dữ liệu được phép → gold và test khóa → baseline → phương pháp → thực nghiệm → paper**. Hai vòng chia sẻ schema và provenance, nhưng không nên dùng mọi contribution làm gold hoặc dùng dữ liệu test làm mẫu prompt.

## 2. Chỗ lệch giữa tài liệu và đề tài

PDF bạn chỉ định có **13 trang**, là hướng dẫn proposal Group 7 về **YOLO phát hiện vật thể nhỏ có hướng**. Ảnh đính kèm lại là đề tài **Real Estate NER**: sequence labeling/regex và 4 trường Giá–Diện tích–Vị trí–Số phòng; demo tối thiểu 10 bài phức tạp. Hai đề tài khác nhau. Tôi dùng PDF đó để kiểm tra cách diễn đạt proposal, không lấy YOLO hay STAL làm mô hình cho bất động sản.

Trong workspace có **proposal ReNER-VN v1.3, 9 trang**, phù hợp với ảnh và aim. Bản này tập trung thuê để ở, khoảng 100 bài gold, 10 bài complex test; Regex/Gemini/Hybrid; extension; median và P25–P75 từ tin tương đồng; kế hoạch 4 người/4 tuần. Đây đều là kế hoạch đề xuất, chưa chứng minh hệ đã có dữ liệu hay hiệu quả. Xem chi tiết nguồn và page anchors trong `01-local-source-review.md`.

## 3. Nhận xét của giáo sư

Nền tảng có giá trị: dữ liệu thật nhiễu, tiếng Việt có viết tắt, nhiều giá/phí, thiếu giá, nhiều tài sản trong một post; output có cấu trúc và evidence có thể đo được. Nhưng 10 bài và một giao diện dùng API chưa đủ để kết luận phương pháp tổng quát hoặc mới.

Tôi khuyên chọn một RQ chính: **kiểm chứng evidence + phân biệt giá thiếu có giúp tăng độ đúng record và giảm điền giá vô căn cứ, tại cùng mức coverage, so với Regex/LLM riêng lẻ không?** Đó là câu hỏi có đối chứng và có thể thất bại; vì vậy có giá trị nghiên cứu hơn lời hứa “AI định giá nhà”.

Paper cần gold độc lập, hướng dẫn nhãn, grouped/source/time splits phù hợp, baseline supervised khi khả thi, ablations và phân tích lỗi. Độ mới chưa được xác nhận đầy đủ; hướng hiện tại là tích hợp/đánh giá T1 tạm thời, chưa chọn venue. Không có cam kết Q1 hoặc mức cải thiện.

Quan sát “nhà đẹp/bán nhà giấu giá, trọ công khai” nên giữ làm **giả thuyết có ích**. Cần đo tỷ lệ theo nguồn, loại tài sản, ý định giao dịch và thời điểm. Không gọi nó là quy luật toàn thị trường hoặc quy định pháp luật. “Đẹp” cần định nghĩa trước khi đưa vào biến nghiên cứu.

## 4. Nhận xét của kiến trúc sư

Điểm dễ làm sai nhất là schema. Một post có nhiều listing; một listing có nhiều observation theo thời gian; một trường có evidence, giá trị chuẩn và trạng thái. Kho contribution, gold IE, market observations và dataset giá cần tách vai trò. Nếu mô hình dữ liệu đúng, backend/web/extension dùng chung một nền; nếu sai, model mạnh vẫn tạo thống kê sai.

MVP nên là backend chia module rõ, PostgreSQL, worker job, frontend web và extension chủ động. Giữ model/prompt/rule/schema/snapshot versions. Retry phải idempotent; review có lịch sử; contribution đi qua gate trước analytics hoặc training. Không cần bắt đầu bằng nhiều microservice.

Extension đọc được tab là quyền kỹ thuật; nó không thay quyền thu thập từ website. Meta đã giải thích tự động thu dữ liệu khi chưa có sự cho phép trước vi phạm terms. Thiết kế cần source-policy gate, preview payload văn bản tối thiểu, giảm PII và xác nhận. Đường dự phòng là web paste từ nội dung có quyền dùng, nguồn đối tác và fixture do nhóm sở hữu. [Meta chính thức](https://about.fb.com/news/2021/04/how-we-combat-scraping/), [Chrome activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab).

## 5. Nhận xét của người làm web

Người dùng cần hiểu một tin, không cần nhìn một dashboard kỹ thuật trước. Luồng có ích là **chọn/dán tin → nhìn thông tin đã trích và evidence → sửa nếu cần → xem comparables đủ điều kiện → chọn đóng góp riêng**. Tin giấu giá vẫn cho giá trị: hệ thống xác nhận “bài không công khai giá” và cho xem các tin công khai tương đồng, không điền giá dự đoán vào ô giá của bài.

Màn nghiên cứu riêng cho nhóm có benchmark, error cases, dataset version và export. Màn review xử lý multi-listing, giá mơ hồ và trùng tài sản. Làm tốt các tác vụ này trước tính năng phụ sẽ giúp cả paper lẫn demo.

## 6. “Giá sàn” nên được thay bằng khái niệm nào?

Với dữ liệu bài đăng, tên phù hợp là **khoảng giá rao tham khảo từ nhóm tin có giá công khai đã quan sát**. Trung vị/P25–P75/N/freshness/filter/coverage là thông tin hữu ích. Chưa có giao dịch xác minh thì không khẳng định giá thị trường thực, giá công bằng hay mức thấp nhất chủ nhà chấp nhận.

Giấu giá tạo rủi ro thiên lệch: nhóm công khai giá có thể khác nhóm giấu giá. Người dùng extension còn tạo thiên lệch vùng và hành vi đóng góp. N≥10 không tự loại thiên lệch; IQR không phải khoảng tin cậy. Nếu sau này muốn model giá, cần dataset và evaluation riêng theo đúng nhãn mục tiêu.

## 7. Hướng đi tôi đề xuất

| Ưu tiên | Việc làm | Lý do |
|---|---|---|
| 1 | Nguồn được phép, scope thuê, schema, pilot, guideline | Xác định bài toán có thể chạy và dữ liệu đáng tin |
| 2 | Gold, split khóa, baseline và bộ chấm | Nền cho paper và phép so sánh công bằng |
| 3 | Grounded hybrid và web paste/review/comparables | Một vertical slice dùng được |
| 4 | Extension cho nguồn được phép + contribution có gate | Thuận tiện và tăng dữ liệu có kiểm soát |
| 5 | Ablation, holdout, downstream error, manuscript | Claims dựa trên run thật |
| 6 | Fine-tune/active learning/price prediction nếu đủ điều kiện | Mở rộng sau khi đã có bằng chứng và nhãn |

Giữ hạn 01/11/2026 như v1.3 thì ưu tiên phần còn lại của kế hoạch pilot 05/10–01/11; từ 09/10 đến hạn có 23 ngày. Mục tiêu paper rộng hơn dùng khung 12 tuần theo gate, không hứa đủ mọi tính năng trong lịch môn học. Critical path là nguồn → gold → split → baseline → evaluation; web fixture có thể làm song song.

## 8. Những file đã tạo để dùng tiếp

- **KIEN-THUC-NEN-TANG-RENER-VN.md:** tài liệu tổng hợp độc lập, gồm nền NLP, missingness, schema, đánh giá, paper, kiến trúc, UX, roadmap, glossary và nguồn.
- **LO-TRINH-TRUC-QUAN.html:** đọc offline, chọn giai đoạn lộ trình, xem các ca dữ liệu và đọc toàn bộ tài liệu nền tảng.
- **01-local-source-review.md:** đọc proposal có page anchors và phản biện chi tiết.
- **02-research-evidence.md:** nghiên cứu học thuật, nguồn/giới hạn đọc và thiết kế thực nghiệm.
- **03-system-architecture.md:** thiết kế dữ liệu, extension, API và gate nguồn.
- **04-adversarial-review.md:** phản biện độc lập và các sửa đổi sau phản biện.

Mức chắc chắn cao với sự lệch PDF/ảnh và nội dung proposal đã đọc; trung bình với thiết kế có thể áp dụng sau pilot; chưa có bằng chứng về độ chính xác, hiệu quả price model hay khả năng công bố. Các điều chưa chạy được đã được đánh dấu trong tài liệu nền tảng.
