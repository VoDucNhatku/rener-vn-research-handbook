# UI, motion và bộ skill — học từ KusShoes và dựng giao diện ReNER (22/10/2026)

[Về index](../INDEX.md) · [Bối cảnh và quyết định](../HIEN-TRANG-VA-QUYET-DINH.md) · [Log chặng này](WORK_LOG.md)

Chặng này trả lời bốn câu hỏi của chủ dự án:

1. Học được gì từ KusShoes để làm giao diện, đặc biệt là phần chuyển động?
2. KusShoes dùng bộ skill nào cho AI agent, nguồn ở đâu?
3. Các thư viện và repo UI/UX, 3D nào đáng học, mỗi cái cho bài học gì?
4. ReNER đã dùng thư viện nào, vì sao, và bài học rút ra khi làm thật?

**Ranh giới hai repo:** repo sản phẩm [`rener-vn`](https://github.com/VoDucNhatku/rener-vn) chỉ chứa đặc tả, code, README chạy được. Mọi phân tích, so sánh nguồn, lý do chọn và log làm việc nằm ở repo này.

## Đọc theo thứ tự

| # | Tài liệu | Trả lời |
|---|---|---|
| 1 | [Học từ KusShoes](01-KUSSHOES-HOC-DUOC.md) | Design system, hero ghim theo cuộn, cách code-split GSAP, cách tổ chức `.spec/` |
| 2 | [Bộ skill KusShoes dùng](02-BO-SKILL-KUSSHOES.md) | 52 skill trong `.agents/skills/`, nhóm theo nguồn và việc, cái nào đã xác minh nguồn |
| 3 | [10 repo UI/UX và 10 repo 3D/scroll](03-REPO-UI-UX-VA-3D.md) | Mỗi repo dạy gì, quy tắc cụ thể, giới hạn |
| 4 | [Thư viện ReNER đã dùng](04-THU-VIEN-RENER-DA-DUNG.md) | Phiên bản, vai trò, lựa chọn đã loại |
| 5 | [Quyết định thiết kế và bài học](05-QUYET-DINH-VA-BAI-HOC.md) | Ba vòng thiết kế landing, sai lầm "AI slop", review extension, dữ liệu thật |
| — | [Nguồn đã đọc](sources/manifest.json) | URL, commit đã clone, ngày đọc |

## Nhãn mức chắc chắn

Dùng đúng năm nhãn của [quyết định hiện hành](../HIEN-TRANG-VA-QUYET-DINH.md#4-năm-nhãn-dùng-cho-kết-luận-sau-này): **Người dùng xác nhận**, **Đề xuất**, **Đã quan sát**, **Đã thực nghiệm**, **Chưa biết**.

## Trạng thái

- Giao diện thử đã có trên nhánh `feat/web-ui-prototype` của repo sản phẩm (commit `7669290`, `56988b7`). Dữ liệu là bài ví dụ tự tạo, cộng 7 bài thật đặt ở thư mục bị git bỏ qua.
- Bản landing có câu chuyện ghim 6 nhịp đang ở Claude Design (artifact riêng tư của chủ dự án), **chưa** chuyển vào code.
- Chưa có user test, chưa đo hiệu năng, chưa kiểm trên Safari/Firefox. Hiệu ứng cuộn của landing trên Claude Design chưa được tác giả tự mở xem: **NOT RUN**.
