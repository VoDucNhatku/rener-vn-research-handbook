# Log chặng UI, motion và bộ skill — 22/10/2026

[Về chặng](README.md). Mỗi mục: đầu vào → việc → kết quả → bằng chứng → còn mở.

## U1 — Đọc KusShoes và handbook

- **Đầu vào:** yêu cầu "dựng UI/UX cho app, động mà đẹp như KusShoes, đọc handbook".
- **Việc:** đọc `DESIGN.md`, hero ghim theo cuộn, `package.json` của KusShoes; đọc mục 5–8, 14 sổ kiến thức và mục 10, 16.4 bản thảo v0.2 của handbook; xem ảnh sidebar, ảnh gợi ý motion, Hình 2 proposal.
- **Kết quả:** [01-KUSSHOES-HOC-DUOC.md](01-KUSSHOES-HOC-DUOC.md).
- **Còn mở:** trang "getdesign.md" người dùng nhắc tới không phân giải được tên miền (DNS), chưa đọc được.

## U2 — Dựng giao diện thử trong repo sản phẩm

- **Việc:** Next.js 15 trong `apps/web`: landing có hero GSAP 4 nhịp, demo extension bằng Motion, Tìm trọ (bộ lọc trên URL, trạng thái rỗng/đang tải), design tokens.
- **Bằng chứng:** `tsc --noEmit` không lỗi; chụp Playwright 1440 × 900 và 390 px; commit `7669290`.
- **Còn mở:** chưa có test tự động, chưa kiểm Safari/Firefox.

## U3 — Nghiên cứu 10 repo UI/UX và 10 repo 3D

- **Việc:** hai lượt nghiên cứu chạy nền; clone và đọc file cụ thể.
- **Kết quả:** [03-REPO-UI-UX-VA-3D.md](03-REPO-UI-UX-VA-3D.md), [manifest](sources/manifest.json).
- **Phát hiện:** hướng "kem + serif + kẻ dòng" của vòng 1 là dấu hiệu slop đã được ghi nhận.

## U4 — Landing trên Claude Design, ba vòng

- **Việc:** vòng 1 hero 3D tĩnh; vòng 2 sửa theo skill (bỏ eyebrow, số trang trí, reveal khắp nơi); vòng 3 câu chuyện ghim 6 nhịp bằng CSS scroll-driven, có 5 bài mẫu bấm thử.
- **Kết quả:** [05-QUYET-DINH-VA-BAI-HOC.md](05-QUYET-DINH-VA-BAI-HOC.md) mục 1–3.
- **Còn mở:** NOT RUN, tác giả chưa tự mở chế độ Play để kiểm hiệu ứng; chờ chủ dự án phản hồi.

## U5 — Review extension `tro`

- **Đầu vào:** zip repo private do chủ dự án tải lên.
- **Bằng chứng:** `npm ci && npm test` → 48 pass, 0 fail.
- **Kết quả:** danh sách 12 điểm thiếu so với đặc tả; rủi ro dữ liệu người thật trong `samples/` và fixture.
- **Còn mở:** chờ chủ extension đồng ý thứ tự sửa.

## U6 — Dữ liệu thật vào giao diện

- **Việc:** file local bị git bỏ qua, che SĐT khi nạp, nhãn gán tay dạng đoạn trích; trang `/tin/[id]`; bộ lọc nguồn bài.
- **Bằng chứng:**
  - `maskPhones` che đủ 6 dạng số giả E5, không che nhầm giá, diện tích hay mã bài;
  - chụp `/tim-tro?nguon=that`, `/tin/x-06`, `/tin/x-07`;
  - commit `56988b7`; `git ls-files data` chỉ có `data/README.md`.
- **Còn mở:** 7 bài đều thiếu giá vì extension chưa mở "Xem thêm".

## U7 — Ghi tri thức vào handbook

- **Yêu cầu:** cấu trúc lại tri thức học từ KusShoes, bộ skill họ dùng, thư viện ReNER dùng; repo sản phẩm chỉ để sản phẩm.
- **Việc:** tạo chặng này, cập nhật index, README, changelog, catalog.
- **Bằng chứng:** `python scripts/validate_docs.py` (kết quả ghi trong PR/commit).
