# Snapshot nguồn web quốc tế — 09/10/2026

> **Bản xuất GitHub:** raw snapshot nói trong hồ sơ này thuộc workspace nghiên cứu gốc. Repo giữ metadata/URL/hash; xem [phạm vi đóng gói](../../../../docs/PACKAGING.md). Verification lịch sử không phải kết quả chạy trên bản clone handbook.


Chỉ lưu nguồn đọc để nghiên cứu, không phải dự án đã cài dependency hoặc chạy local.

- `github-metadata.json`: kết quả chọn lọc từ GitHub REST API, gồm tên thực tế, star/fork, nhánh, commit và thời điểm lấy.
- `source-manifest.json`: URL file theo commit, đường dẫn bản sao local, SHA256 và thời điểm tải; lỗi truy cập được giữ để đối chiếu.
- Các thư mục `owner--repo`: file manifest/architecture/config/license chọn lọc từ repo công khai, không phải bản clone đầy đủ.
- Truy vấn `DavidHDev/react-bits/LICENSE` trả 404; đã tìm và lấy đúng `LICENSE.md`. Không coi lỗi đường dẫn này là thiếu license của dự án.

Giải thích, bảng so sánh và quyết định đề xuất nằm trong [sổ kiến thức chính](../../KIEN-THUC-TONG-HOP.md), mục 14–17.

Nguồn website đã đọc:

- [GSAP](https://gsap.com/), [React](https://gsap.com/resources/React/), [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/), [accessibility](https://gsap.com/resources/a11y/).
- [Motion React](https://motion.dev/docs/react), [motion component](https://motion.dev/docs/react-motion-component), [accessibility](https://motion.dev/docs/react-accessibility), [examples](https://examples.motion.dev/react).
- [Immich architecture](https://docs.immich.app/developer/architecture/), [scaling](https://docs.immich.app/guides/scaling-immich/), [PR checklist](https://docs.immich.app/developer/pr-checklist/).

Số star chỉ phản ánh snapshot; không phải bảng xếp hạng toàn cầu, đánh giá bảo mật hoặc độ phù hợp đã được kiểm thử.
