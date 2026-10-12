# Bản đồ 12 mảng kiến thức

[README](../README.md) · [Lộ trình đọc](START-HERE.md) · [Danh mục đầy đủ](CATALOG.md)

Đây là bản đồ truy xuất, không thay nội dung chi tiết. Các kết luận cần đọc cùng nguồn, thời điểm và trạng thái kiểm chứng trong file gốc.

| Mảng | Đã tìm hiểu | Tài liệu/đoạn cần đọc | Bạn cần tự giải thích được |
|---|---|---|---|
| 01. Nhu cầu và MVP | Actor, ai hưởng lợi/chịu chi phí, scope, lõi và mở rộng, Example Mapping | [Sổ chung mục 2–4/22](../notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md); [đọc sâu mục 2](../notes/nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md) | Tính năng nào mất thì sản phẩm mất giá trị; ví dụ nào xác nhận luật |
| 02. UI và admin | Sidebar, route, permission, dashboard, trạng thái loading/empty/error, design tokens | [Sổ chung mục 6–8](../notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md); [thiết kế mục 10](../notes/design-rener-vn-waterfall.md) | Admin xử lý quyết định gì; một ô số liệu lấy dữ liệu từ đâu |
| 03. Motion và template | GSAP, Motion, các nguồn mẫu/component, accessibility, tinh chỉnh UI | [Sổ chung mục 7/14](../notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md); [creator mục 4–6](../notes/kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md) | Hiệu ứng đang giải thích hành động nào; tinh chỉnh web khác fine-tune model ra sao |
| 04. Kiến trúc web | Frontend/backend, module boundary, ORM/repository, background job, state/cache | [10 repo và kiến trúc mục 18–23](../notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md); [v0.2 mục 16](../notes/design-rener-vn-waterfall.md) | Một request đi qua phần nào; luật thuộc nơi nào và phụ thuộc gì |
| 05. Bài toán dữ liệu trọ | Post/listing/phòng/giao dịch, giá/người/phòng/tháng, giấu giá, nhiều listing, trùng | [Foundation mục 3–6/11–16](../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md); [bảy trục trạng thái](../notes/nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md) | Điều gì quan sát được, điều gì suy ra, điều gì còn chưa biết |
| 06. NLP | Token/span/BIO, regex/CRF/PhoBERT/LLM/Hybrid, evidence và abstention, normalize | [Foundation mục 7–13](../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md); [ghi chú MLM](../notes/08-fine-tuning-mlm-summary.md) | JSON/span đúng có thể sai nghĩa ở đâu; khi nào nên không trả giá |
| 07. Đánh giá và thống kê | Gold, split theo cụm, leakage, exact span/record, coverage, ablation, uncertainty | [Foundation mục 15–19](../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md); [đọc sâu mục 4](../notes/nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md) | Metric đang đo gì; đối chứng nào cho phép kết luận tác dụng grounding |
| 08. Extension và quyền nguồn | Chọn/preview/gửi tin, service worker, message trust, token/storage, retention/withdraw | [Foundation mục 21–22](../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md); [đọc sâu mục 6–7](../notes/nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md) | Đóng popup/worker/browser khác gì; chọn tin có cấp mọi quyền dùng dữ liệu không |
| 09. Vận hành và scale | RPS/concurrency, DB pool, queue, retry/idempotency/fencing, snapshot, cache, SLO/cost | [Scale mục 3/5](../notes/kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md); [đọc sâu mục 5/9](../notes/nghien-cuu-sau-2026-10-11/NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md) | Vì sao thêm CPU/RAM chưa giải mọi bottleneck; một job có thể gọi provider mấy lần |
| 10. AI và GitHub | Repo flow ChoThueGiupViec, harness/role/task, issue/branch/PR/CI, đánh giá outcome | [Harness mục 1–2/4](../notes/kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md); [giao việc](../notes/kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md) | Rule nào có script thực thi; rule nào chỉ là hướng dẫn; ai kiểm người kiểm |
| 11. Solo và nhận khách | Brief/SOW, acceptance, scope change, handover, rollback, 80/20, UX evidence | [Gia công web](../notes/kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md); [solo AI](../notes/kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md) | Khi khách đổi lõi, ảnh hưởng tới dữ liệu/hợp đồng/bằng chứng như thế nào |
| 12. Phản biện và tái lập | Claim/evidence, corrections, 10 gap, nguồn sơ cấp, behavioral cases, log/hash | [Audit](../notes/audit-2026-10-11/BAO-CAO-PHAN-BIEN.md); [26 ca](../notes/nghien-cuu-sau-2026-10-11/BO-CA-PHAN-CHUNG-RENER.md); [21 nguồn](../notes/nghien-cuu-sau-2026-10-11/SO-NGUON-DA-DOC.md) | Bằng chứng nào khiến bỏ một kết luận; chỗ nào chưa đủ để code/khẳng định |

## Các repo đã dùng làm mẫu

KusShoes là mẫu sản phẩm ban đầu; ChoThueGiupViec là mẫu đọc flow và harness. Nhóm 10 repo khảo sát gồm Medusa, Saleor, Vercel Commerce, React Admin, Refine, Tabler, Full Stack FastAPI Template, Cal.diy, Outline và Immich. Tám repo bổ sung gắn với đề tài/extension/gán nhãn nằm trong chuyên đề harness, mục 6.

Danh sách là mẫu có chủ đích ở thời điểm nghiên cứu, không phải xếp hạng chất lượng toàn thế giới. URL, commit và star theo ngày nằm ở [metadata](../notes/kusshoes-to-rener-vn/sources/web-top10-2026-10-10/github-metadata.json), [nguồn kiến trúc](../notes/kusshoes-to-rener-vn/sources/architecture-top10-2026-10-10/source-manifest.json) và [sổ nguồn tập trung](SOURCES.md).

## Kiến thức nền môn học

[TMG301 tổng hợp](../TMG301_TongHopKienThuc.md), [fine-tuning/MLM](../notes/08-fine-tuning-mlm-summary.md) và lab trong `notes/08-assets/` được giữ để tra nền tảng. Script sinh sổ tay ở gốc là công cụ lịch sử; thư mục đầu ra 17 sổ tay trong workspace hiện rỗng, nên repo không tuyên bố có 17 sản phẩm đã xuất thành công. Các đính chính kiến thức nằm trong audit 11/10.
