# ReNER-VN — bối cảnh và quyết định hiện hành

Cập nhật **12/10/2026**, sau lượt phản biện và đọc sâu bổ sung. Đây là trang tra cứu phạm vi và trạng thái, **không phải bản phê duyệt thiết kế hoặc bằng chứng app đã chạy**.

## 1. Điều người dùng đã xác nhận

| Nội dung | Quyết định hiện hành |
|---|---|
| Bài thực hành | Theo proposal ReNER-VN và website đang nghiên cứu, làm bài bản để chuyển tư duy sang dự án khác |
| Người dùng ưu tiên | Người tìm trọ: tìm/lọc tin, hiểu và so sánh giá thuê |
| Tiếp nhận dữ liệu | Extension để người dùng chọn và gửi từng tin; chưa xác nhận quyền thu thập trên nguồn thật |
| Mục tiêu trước mắt | Demo môn học. Đến 12/10: nghiên cứu, học và bản thảo, chưa code. Từ 22/10: người dùng yêu cầu dựng giao diện trước (dữ liệu demo, chưa có backend) |
| Quy mô 5.000 người | Ví dụ để học về tải, không phải chỉ tiêu phải đáp ứng |
| Cách học | Ưu tiên hiểu luồng giữa các phần, chuyển ý tưởng ngắn thành yêu cầu và việc nhỏ |
| Quyền tự chủ AI | Tự xử lý chi tiết dễ đảo trong phạm vi; làm rõ quyết định nghiệp vụ/dữ liệu có ảnh hưởng, tránh hỏi vụn vặt |
| Mục tiêu dài hạn | Có khả năng nhận dự án web cho khách; không biến mọi yêu cầu doanh nghiệp thành P0 của demo |
| Cách ghi nhận | Chia việc tuần tự, có log sau từng phần, kiến thức nằm trong TMG301 |
| Ranh giới repo (22/10) | `rener-vn` chỉ chứa sản phẩm (đặc tả, code, README chạy được); tư duy, nghiên cứu, so sánh nguồn và log nằm ở handbook này |
| Giao diện (22/10) | Đã có giao diện thử trên nhánh `feat/web-ui-prototype`; phong cách riêng, chỉ mượn ý tưởng chuyển động của KusShoes; muốn có 3D và nhiều nhịp như hero KusShoes. Xem [chặng UI](ui-motion-2026-10-22/README.md) |

## 2. Ba phạm vi phải đọc riêng

1. **Proposal v1.3:** mục tiêu và kế hoạch đồ án gốc, gồm phần thực nghiệm NLP. Giữ file gốc; phát hiện cần sửa được ghi ở báo cáo audit, chưa tự viết lại proposal đã nộp/đã thống nhất.
2. **Bản thảo web v0.2:** thiết kế đề xuất cho pilot có tài khoản. Catalog là **công bố nội bộ cho người có quyền**; không mặc định công khai dữ liệu thật ra Internet. Chưa duyệt stack/schema/API/ngưỡng và chưa triển khai theo bản thảo. Lượt audit chỉ sửa mũi tên sai trong sơ đồ, không chốt thiết kế mới.
3. **Nghiên cứu mở rộng và nhận khách:** paper, fine-tune, định giá, active learning, tải lớn, hợp đồng/deploy là kiến thức để đánh giá khi có nhu cầu. Không tự nhập thành phạm vi bắt buộc hiện tại.

Tài liệu foundation đề xuất 12 tuần/300–500 gold; proposal có kế hoạch 4 tuần/~100 gold. Đây là **hai kế hoạch khác nhau**, không phải bằng chứng đã có dataset hoặc người dùng đồng ý tăng phạm vi. Tương tự, học làm việc một mình không xác nhận nhóm đồ án bốn người đã đổi thành một người.

## 3. Đọc file nào cho câu hỏi nào?

| Câu hỏi | Tài liệu dùng chính | Cách dùng |
|---|---|---|
| Hiện tại người dùng muốn gì? | File này + chỉ dẫn mới trực tiếp của người dùng | Cập nhật khi có thay đổi; không lấy tài liệu cũ phủ quyết chỉ dẫn mới |
| Đề tài gốc đòi gì? | [Proposal v1.3](../project-realestate-ner/proposal-ReNER-VN-v1.3.pdf) | Đối chiếu yêu cầu môn học, RQ và nghiệm thu nghiên cứu |
| Luồng web, quyền, admin ra sao? | [Bản thảo v0.2](design-rener-vn-waterfall.md) | Tham khảo có trạng thái draft; xác nhận trước triển khai phụ thuộc quyết định chưa chốt |
| Bài toán NLP/đánh giá có gì khó? | [Nền tảng ReNER](../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md) | Có phân biệt nguồn, suy luận và thiết kế; phần mở rộng không tự thay proposal |
| Những chỗ vừa bị phản biện? | [Báo cáo audit](audit-2026-10-11/BAO-CAO-PHAN-BIEN.md) | Xem lỗi đã sửa, giới hạn và khoảng trống còn mở |
| Đọc thêm đem lại hiểu biết gì? | [Nghiên cứu sâu](nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md), [ca phản chứng](nghien-cuu-sau-2026-10-11/BO-CA-PHAN-CHUNG-RENER.md) | 21 nguồn đọc chọn lọc, nghĩa dữ liệu/protocol trên giấy và 26 ca NOT RUN; không chốt schema mới |
| Biến ý tưởng ngắn thành task thế nào? | [Sổ tay chia việc](kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md) | Bắt đầu bằng ví dụ đúng/sai, rồi đi theo một hành trình |
| Cần khuôn prompt đầy đủ? | [Prompt v1.2](quy-chuan-ai-dev/PROMPT-KIEN-TRUC-GIAO-VIEC-AI.md) | Chọn phần có ích; ví dụ/command chưa phải file hay kết quả có thật |
| Công việc đã làm thật? | [Báo cáo ngắn](../BAO-CAO-TONG-HOP-CONG-VIEC.md), [log](kusshoes-to-rener-vn/WORK_LOG.md) | Mốc lịch sử có ngày; kết quả chạy cũ không chứng minh server đang chạy hôm nay |
| Học gì từ repo/motion/harness? | [Sổ kiến thức](kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md) | Repo nhiều star là mẫu để đọc; không phải bảo đảm kiến trúc tối ưu/an toàn |

Khi tài liệu mâu thuẫn: xác định khác **thời điểm**, **phạm vi** hay **ý nghĩa**; xem nguồn gốc và quyết định mới nhất của người dùng; ghi sửa ở đúng nơi sở hữu quyết định. Không giải quyết chỉ bằng “file mới nhất luôn thắng”, hoặc sửa âm thầm cả hệ thống theo một ví dụ trong tutorial.

## 4. Năm nhãn dùng cho kết luận sau này

- **Người dùng xác nhận:** trỏ phát biểu đã chốt, không nâng suy đoán thành yêu cầu.
- **Đề xuất:** lý do, điều kiện áp dụng và câu hỏi chưa chốt.
- **Đã quan sát:** file/commit/log/nguồn cụ thể, cùng ngày và phạm vi kiểm.
- **Đã thực nghiệm:** command, cấu hình, dữ liệu, kết quả và giới hạn. Chỉ dùng khi thật sự chạy.
- **Chưa biết:** ghi phép thử hoặc bằng chứng cần có để quyết định; không điền con số cho đủ dashboard.

Quy tắc này dùng khi viết kiến thức, không bắt mọi câu chat mang nhãn.

## 5. Cách dùng với một yêu cầu ngắn

Ví dụ người dùng nói: “Cho tao biết phòng này đắt hay rẻ”. AI cần chuyển thành:

1. **Ý nghĩa cần làm rõ:** so với tin nào, giá thuê cơ bản hay tổng chi phí, có đủ dữ liệu/đơn vị không? Trước hết dùng phạm vi đã xác nhận; chỉ hỏi phần ảnh hưởng kết quả chưa biết.
2. **Ví dụ để thử:** giá/phòng so với giá/người; “từ 3 triệu”; tin thiếu diện tích; tin đích bị đăng lại trong tập so sánh. Ghi đáp án mong đợi trước khi code.
3. **Hành trình:** người xem chọn tin → API kiểm quyền/điều kiện → lấy nhóm tin hợp lệ, bỏ cụm của tin đích → tính thống kê hoặc trả thiếu dữ liệu → UI giải thích được tập so sánh.
4. **Task đầu tiên:** kiểm định nghĩa và vài ca biên bằng dữ liệu tổng hợp. Đầu ra là ví dụ nghiệm thu được chủ dự án hiểu; chưa cần dựng thêm dashboard.
5. **Tiêu chí xong:** người xem biết kết luận dựa trên tập nào và giới hạn gì. Có một con số hoặc biểu đồ đẹp chưa đủ.

Đây là ví dụ học cách đặc tả. Chưa quyết định sản phẩm phải gọi tin là “đắt/rẻ”, chưa tạo dự đoán giá thị trường và chưa chạy user test.
