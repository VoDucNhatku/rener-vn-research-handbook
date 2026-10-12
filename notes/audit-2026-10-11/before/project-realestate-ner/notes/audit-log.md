# AI Audit Log — Decision Moments

### ae_6152930 · 2026-10-09T00:51+07:00 · VERIFY
**Decision:** Tách PDF YOLO do người dùng chỉ định khỏi ảnh Real Estate NER; dùng ReNER-VN v1.3 trong workspace để đối chiếu nội dung.
**Why:** Đọc trực tiếp xác nhận quick guide 13 trang nói YOLO-OBB, còn ReNER v1.3 9 trang khớp aim và ảnh; không thể áp STAL vào NER.
**Delta:** Phát hiện nền sai khi chỉ dựa tên proposal; giảm scope đọc tài liệu thị giác; tổng hợp nền NLP từ nguồn phù hợp và báo mismatch rõ.
**Evidence:** notes/foundation-2026-10-09/01-local-source-review.md

### ae_5d1dc7d · 2026-10-09T00:51+07:00 · DESIGN
**Decision:** Đề xuất grounded IE và tham khảo giá rao có phạm vi; tách trạng thái nguồn, quyết định extractor và vòng đóng góp khỏi gold/training.
**Why:** Giá rao không chứng minh giá sàn/giao dịch; reviewer chỉ ra source ambiguity, denominator và downstream survivor bias; nguồn platform cần gate riêng.
**Delta:** Giữ giá trị sản phẩm và paper nhưng thu hẹp claim; thêm canonical schema, metrics hai mẫu số, full-pipeline tests và release offline; chưa chứng minh hiệu quả thực nghiệm.
**Evidence:** notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md; notes/foundation-2026-10-09/04-adversarial-review.md

