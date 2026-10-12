# Lộ trình đọc: hiểu hệ thống trước khi viết thêm code

[Về README](../README.md) · [Bản đồ kiến thức](KNOWLEDGE-MAP.md) · [Toàn bộ tài liệu](CATALOG.md)

## Lượt 1 — nắm bối cảnh

Đọc [báo cáo công việc](../BAO-CAO-TONG-HOP-CONG-VIEC.md), [quyết định hiện hành](../notes/HIEN-TRANG-VA-QUYET-DINH.md) và [trạng thái](STATUS.md). Kết quả cần đạt: nói được ai dùng, họ cần gì, dữ liệu vào bằng cách nào và việc nào chưa được chứng minh. Chưa cần đọc toàn bộ kiến trúc hoặc các paper.

## Lượt 2 — đọc đề và hiểu dữ liệu

Đọc [proposal v1.3](../project-realestate-ner/proposal-ReNER-VN-v1.3.pdf), sau đó [nền tảng ReNER](../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md), ưu tiên mục 3–6 và 11–17. Tự trả lời: một post có thể chứa mấy listing? Giá/người và giá/phòng có so cùng nhóm được không? Thiếu giá khác lỗi mô hình thế nào?

Proposal là đầu vào gốc. Các đề xuất mở rộng trong foundation không tự thay kế hoạch gốc hoặc tạo ra dataset đã có.

## Lượt 3 — học từ website khác có chọn lọc

Đọc [sổ kiến thức](../notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md), mục 5–10, 14–21 và 23. Đọc kèm [báo cáo local KusShoes](../KusShoes/notes/kusshoes-local-review.md). Với mỗi repo, ghi lại một luồng: màn hình → API → nghiệp vụ → lưu dữ liệu → phản hồi; nêu phần nào áp dụng được và điều kiện áp dụng.

Đừng chép toàn bộ sidebar, dịch vụ hoặc quy trình của sản phẩm lớn vào demo. Số star và độ đẹp không chứng minh module đó cần cho ReNER.

## Lượt 4 — nối yêu cầu với kiến trúc

Đọc [Waterfall v0.2](../notes/design-rener-vn-waterfall.md), theo thứ tự actor/scope → luật → flow/state → kiến trúc → dữ liệu/API → UI/admin → nghiệm thu. Xem [bài đọc sâu](../notes/nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md) để hiểu những chỗ dễ nhầm.

Bài tập: lấy câu “tìm phòng dưới 3 triệu”, ghi giả định về loại giá/đơn vị/chu kỳ, đưa một ví dụ đạt, một ví dụ không đạt và một ví dụ chưa quyết được. Sau đó vẽ nhánh thất bại hoặc thiếu thông tin; chưa cần thêm màn hình.

## Lượt 5 — giao việc cho AI và kiểm nó

Đọc [sổ tay chia việc](../notes/kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md), [harness ChoThueGiupViec](../notes/kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md) và [quy trình của repo này](WORKFLOW.md). Dùng [task template](../templates/TASK.md) cho một lát cắt nhỏ. Chốt đầu ra và cách kiểm, để AI tự chọn các chi tiết dễ đảo trong phạm vi.

Chọn vài ca liên quan trong [26 phản chứng](../notes/nghien-cuu-sau-2026-10-11/BO-CA-PHAN-CHUNG-RENER.md). Không đổi NOT RUN thành PASS chỉ vì có mô tả hoặc test do AI tự viết.

## Lượt 6 — phản biện và chuẩn bị giao cho người khác

Đọc [audit](../notes/audit-2026-10-11/BAO-CAO-PHAN-BIEN.md), [gia công web](../notes/kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md) và [solo AI/đổi lõi](../notes/kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md). Luyện yêu cầu đổi “giá thuê” thành “tổng chi phí”: dữ liệu nào thiếu, luật nào đổi, cái gì phải kiểm lại và cái gì không thể khôi phục chỉ bằng Git?

## Khi cần tra thay vì đọc tuần tự

Dùng [KNOWLEDGE-MAP](KNOWLEDGE-MAP.md) để chọn chủ đề; [CATALOG](CATALOG.md) để xem các mục của từng file; [SOURCES](SOURCES.md) để tìm lại nguồn; [WORK_LOG](../notes/kusshoes-to-rener-vn/WORK_LOG.md) để biết vì sao tài liệu thay đổi. Mỗi lượt đọc nên để lại một câu hỏi, một ví dụ và một điều kiện khiến mình đổi ý.
