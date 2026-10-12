# Kiểm tra bản giao — 09/10/2026

Phạm vi: kiểm chất lượng **tài liệu và bản đọc trực quan**. Không phải đánh giá NLP, thử crawler/extension, xác nhận quyền nguồn cụ thể hay kiểm tra model đã huấn luyện.

| Chiều kiểm tra | Kết quả | Bằng chứng / giới hạn |
|---|---|---|
| Completeness | PASS cho yêu cầu nghiên cứu/tài liệu | Báo cáo riêng, kiến thức 32 mục, roadmap tương tác, ba nhánh độc lập và phản biện; không triển khai web thật trong phạm vi này |
| Fidelity | PASS có giới hạn | Đọc nguồn 13p YOLO và ReNER v1.3 9p; claims về kế hoạch không chuyển thành kết quả; nguồn có mức đọc; các trang blocked ghi rõ |
| Hallucination guard | PASS trong scope scan | 05-source-audit.md và 04-adversarial-review.md §8; C-2 có trong ledger vật lý; HTML tồn tại; chưa có F1/model gains/venue promises |
| Trình bày | PASS | Xem trực tiếp desktop hero/roadmap/knowledge và mobile 320px; không thấy text bị chồng hoặc cắt bất thường |
| Tương tác | PASS | 6 nút stage, 3 ca minh họa, search/no-result/reset, 32 chương, internal anchors, không pageerror |
| Responsive/contrast | PASS trên kiểm tra đã chạy | 1280px, 375px, 320px; không overflow toàn trang; các cặp text/background kiểm được đạt ≥4,5:1 |
| Print | PASS ở mức DOM/CSS | Print mode hiện đủ 32 chương; chưa xuất/kiểm PDF từng trang |
| Token efficiency | PASS | Nội dung dài nằm trong file; chat cuối chỉ preview và links |

Sửa sau phản biện: source visibility tách khỏi capture/extraction decision; canonical inbox mapping; unit và mẫu số metrics; controlled-value/full-pipeline downstream tests; ontology ablation; property split khác template holdout. Tất cả resolved **ở mức thiết kế**, chưa xác nhận protocol chạy đúng trên dataset.

Bằng chứng render và test lưu trong `_build/qa/`; `verification.json` là kết quả tự động và các ảnh PNG là snapshot đã xem. Các test chỉ xác minh nội dung tĩnh/kỳ vọng và tương tác reader; không có model chạy sau các ca minh họa.

Giới hạn còn lại đã thể hiện trong bản giao: dữ liệu/gold/permission/compute/baseline chưa khóa; chưa biết novelty đủ để công bố; nhóm có 23 ngày đến hạn 01/11 nếu giữ lịch v1.3; roadmap 12 tuần là kế hoạch riêng cho aim rộng hơn.
