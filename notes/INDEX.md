# Tài liệu trong TMG301

**GitHub riêng tư:** [rener-vn-research-handbook](https://github.com/VoDucNhatku/rener-vn-research-handbook) — README, lộ trình đọc, bản đồ kiến thức, nguồn và quy trình issue/PR. Xem [log xuất bản](github-publication-2026-10-12/WORK_LOG.md).

**Đọc sâu bổ sung 12/10/2026:** [Thay đổi tư duy sau 21 nguồn](nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md), [26 ca phản chứng chưa chạy](nghien-cuu-sau-2026-10-11/BO-CA-PHAN-CHUNG-RENER.md), [sổ nguồn và mức đọc](nghien-cuu-sau-2026-10-11/SO-NGUON-DA-DOC.md). Làm rõ yêu cầu, nghĩa dữ liệu, đánh giá NLP, retry/extension và kiểm outcome của AI; giữ mục tiêu demo và trạng thái nghiên cứu.

**Bắt đầu ở đây:** [Bối cảnh và quyết định hiện hành](HIEN-TRANG-VA-QUYET-DINH.md). [Phản biện toàn hồ sơ 11/10](audit-2026-10-11/BAO-CAO-PHAN-BIEN.md): 13 nhóm lỗi/lệch nghĩa đã hiệu chỉnh, 10 khoảng trống cần kiểm chứng; có bản trước sửa và phạm vi kiểm từng file.

| Chủ đề | Kế hoạch | Kiến thức tổng hợp | Log |
|---|---|---|---|
| Học KusShoes để xây ReNER-VN | [PLAN](kusshoes-to-rener-vn/PLAN.md) | [Sổ kiến thức](kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md) | [WORK_LOG](kusshoes-to-rener-vn/WORK_LOG.md) |

Nghiên cứu nền tảng ReNER-VN trước đó: [index riêng](../project-realestate-ner/notes/INDEX.md). Khảo sát/chạy KusShoes local: [báo cáo](../KusShoes/notes/kusshoes-local-review.md).

Cập nhật 10/10/2026: sổ kiến thức mục 18–21 có **10 repo đa lĩnh vực, tutorial chi tiết và cách đọc kiến trúc/GitHub**. Nguồn kiểm tra mới: [metadata 10 repo](kusshoes-to-rener-vn/sources/web-top10-2026-10-10/github-metadata.json).

Thiết kế sản phẩm mới nhất: [ReNER-VN — yêu cầu và kiến trúc Waterfall](design-rener-vn-waterfall.md). Có P0/P1/P2, extension chọn từng tin, logic nguồn–trích xuất–duyệt–so sánh, admin/dashboard, ERD/API và nghiệm thu. Trạng thái: bản thảo đã tự kiểm tra, chờ người dùng xem; chưa code. Tóm tắt quyết định ở mục 22 sổ kiến thức, log D1–D4.

Đối chiếu code 10 repo bổ sung: sổ kiến thức mục 23 và [snapshot nguồn](kusshoes-to-rener-vn/sources/architecture-top10-2026-10-10/README.md). Thiết kế **v0.2 mục 16** ghi kiến trúc thống nhất, ownership/dependency, cây repo, frontend state, transaction/cache và AR01–AR08; log E1–E3. Bản thảo vẫn chưa duyệt và chưa triển khai.


Ưu tiên hiện hành sau xác nhận của người dùng: **nghiên cứu/bản thảo để học, mục tiêu demo; chưa thiết kế thêm hoặc code**. Xem [chuyên đề harness, scale, AI tạo web và tám repo sát đề tài](kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md), sổ kiến thức v0.6 mục 24 và log F1–F5. Giữ v0.2 ở trạng thái bản thảo; mũi tên dependency được đính chính ngày 11/10, không đổi stack; 5.000 người chỉ là ví dụ.


[Báo cáo tổng hợp công việc đến 12/10/2026](../BAO-CAO-TONG-HOP-CONG-VIEC.md): bản ngắn gồm yêu cầu của người dùng, kết quả đã làm, bằng chứng, giới hạn và tài liệu bàn giao.


Bổ sung 11/10/2026: [Gia công web và AI workflow](kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md) — brief/SOW/nghiệm thu/bàn giao; năm video/creator; nguồn template/component; tinh chỉnh sản phẩm so với fine-tune model. Sổ kiến thức v0.7 mục 25, log H0–H4.


Bổ sung 11/10/2026: [Từ vibe coding đến giao web](kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md) và [Sổ tay chia việc cho AI](kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md) — nghiên cứu quốc tế/Trung Quốc, UX/80-20, backend gọn, quản lý một người và đổi lõi/khôi phục. Ưu tiên mới: học bài bản bằng proposal/ReNER để chuyển tư duy sang dự án khác và tiến tới nhận khách. Sổ kiến thức v0.8 mục 26; log I0–I5.
