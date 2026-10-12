# Nguồn cho 10 repo web — 10/10/2026

> **Bản xuất GitHub:** raw snapshot nói trong hồ sơ này thuộc workspace nghiên cứu gốc. Repo giữ metadata/URL/hash; xem [phạm vi đóng gói](../../../../docs/PACKAGING.md). Verification lịch sử không phải kết quả chạy trên bản clone handbook.


- `github-metadata.json`: 10 repo, star chính xác, commit, nhánh, license metadata và timestamp lấy bằng GitHub REST API; thời gian người dùng Asia/Saigon = UTC + 7.
- `source-manifest.json`: 30 file nguồn chọn lọc, URL theo commit và SHA256; chỉ đọc/lưu nghiên cứu, không chạy code repo mẫu.
- FastAPI template và Cal.diy giữ nguyên commit so với snapshot `../world-web-2026-10-09`; tái sử dụng file đã đọc. Cal.diy có thêm CONTRIBUTING ở snapshot mới.
- Outline đổi HEAD nhưng ARCHITECTURE/package đọc mới không đổi nội dung. Immich server manifest không đổi; Compose thêm `MACHINE_LEARNING_MODEL_REVISION: v2`.
- Refine root README là symlink dạng text `packages/core/README.md`; đã lấy đúng file đích. Có hai lần console không in được emoji tiêu đề trên Windows, nhưng file đã tải/lưu và ghi manifest đầy đủ; kiểm chứng bằng SHA256.
- Hai URL suy đoán ban đầu cho Tabler introduction và Saleor quickstart không mở được qua web tool; đã đi theo link chính thức và dùng URL hợp lệ bên dưới trong tài liệu.

Nguồn hướng dẫn đã mở:

- [Medusa architecture](https://docs.medusajs.com/learn/introduction/architecture), [custom feature tutorial](https://docs.medusajs.com/learn/customization/custom-features).
- [Saleor docs](https://docs.saleor.io/), [Cloud quickstart](https://docs.saleor.io/quickstart/cloud), [self-hosting](https://docs.saleor.io/setup/overview).
- [Next.js Commerce integration](https://vercel.com/kb/guide/deploy-headless-shopify-storefront-with-vercel).
- [React-admin tutorial](https://marmelab.com/react-admin/Tutorial.html).
- [Refine tutorial](https://refine.dev/core/tutorial/essentials/intro/).
- [Tabler docs](https://docs.tabler.io/), [React integration](https://docs.tabler.io/ui/getting-started/frameworks/react).
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/).
- [Immich setup](https://docs.immich.app/developer/setup/), [Outline from source](https://docs.getoutline.com/s/hosting/doc/from-source-BlBxrNzMIP).
- [Next.js Learn](https://nextjs.org/learn/dashboard-app), [Full Stack Open](https://fullstackopen.com/en/), [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development).

Báo cáo và đánh giá ở [sổ kiến thức chính](../../KIEN-THUC-TONG-HOP.md), mục 18–21. Không đánh đồng số star với chất lượng, an toàn hay mức phù hợp cho mọi dự án.
