# Trạng thái và cách đọc bằng chứng

[README](../README.md) · [Roadmap](../ROADMAP.md) · [Log nghiên cứu](../notes/kusshoes-to-rener-vn/WORK_LOG.md)

Ngày chốt bản xuất: 12/10/2026. Đóng gói GitHub không biến kết luận nghiên cứu thành kết quả thực nghiệm.

| Nhãn | Ý nghĩa | Ví dụ trong repo |
|---|---|---|
| CONFIRMED | Người dùng đã xác nhận | Ưu tiên người tìm trọ; extension chọn từng tin; demo trước |
| RESEARCHED | Đã đọc nguồn/quan sát code trong phạm vi ghi rõ | Khảo sát 10 repo; đọc sâu 21 nguồn chọn lọc |
| DRAFT | Đề xuất chưa chốt hoặc chưa triển khai | Kiến trúc v0.2, ontology, protocol RQ2 |
| HISTORICAL RUN | Có bằng chứng chạy trong môi trường/thời điểm cũ | KusShoes local và lab ghi trong báo cáo tương ứng |
| VERIFIED DOCUMENTS | Đã kiểm file/link/hash theo phạm vi script | Kiểm bản xuất GitHub; không là benchmark hoặc app test |
| NOT RUN / OPEN | Chưa chạy hoặc chưa đủ bằng chứng | 26 ca ReNER, nguồn thật, chất lượng mô hình, kiểm tải |
| SUPERSEDED | Nội dung cũ giữ để truy lịch sử | Bản `before/`, nhận định được audit đính chính |

## Những giới hạn cần giữ nguyên

Chưa có web ReNER hoàn chỉnh, gold/evaluator mới đã chạy, xác minh toàn bộ nguồn Facebook hoặc load test cho 5.000 người. Một số nội dung YouTube chỉ được đọc description/transcript; X/Bilibili/Reels có phần không truy cập được. Xem log từng chặng, không suy ra đã xem hết video hoặc đọc trọn sách.

Foundation chứa hướng mở rộng paper/12 tuần; proposal v1.3 chứa kế hoạch đồ án bốn tuần. So sánh ba pipeline không tự cô lập hiệu ứng của từng thành phần. Kết quả chính xác trên mẫu tổng hợp không chứng minh đúng trên thị trường.

## Khi hai tài liệu không khớp

Xác định khác thời điểm, scope hay nghĩa dữ liệu; xem [quyết định hiện hành](../notes/HIEN-TRANG-VA-QUYET-DINH.md) và chỉ dẫn mới của chủ dự án. Đọc [audit](../notes/audit-2026-10-11/BAO-CAO-PHAN-BIEN.md) trước khi dùng tài liệu lịch sử. Ghi thay đổi tại nơi sở hữu luật, thêm log và liên kết từ các bản tóm tắt; không sửa âm thầm proposal gốc.

Các JSON verification cũ lưu bằng chứng cho workspace gốc. Sau khi redaction/đổi link cho GitHub, hash của bản xuất có thể khác. Manifest xuất bản ghi cả hai; lệnh kiểm portable là `python scripts/validate_docs.py`.
