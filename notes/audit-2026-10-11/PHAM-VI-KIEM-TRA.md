# Phạm vi kiểm tra từng tài liệu

Ngày 11/10/2026. Tất cả 28 file được kiểm kê/hash và quét claim; bảng nói rõ phần đọc thêm. “Không phát hiện thêm” không có nghĩa chứng nhận không còn lỗi. Proposal gốc được đối chiếu qua text/PDF, không cộng vào số Markdown. Source clone/vendor/build không được audit code toàn diện.

| Tài liệu trước audit | Mức đối chiếu trong lượt này |
|---|---|
| [BAO-CAO-TONG-HOP-CONG-VIEC.md](../../BAO-CAO-TONG-HOP-CONG-VIEC.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [KusShoes/notes/kusshoes-local-review.md](../../KusShoes/notes/kusshoes-local-review.md) | Rà mức tuyên bố kết quả lịch sử/giới hạn; không chạy lại app hay xác nhận server hiện tại. |
| [notes/08-fine-tuning-mlm-summary.md](../08-fine-tuning-mlm-summary.md) | Đọc các phần fine-tuning/MLM/metrics; đối chiếu script và log lịch sử, không chạy lại training; sửa F10. |
| [notes/design-rener-vn-waterfall.md](../design-rener-vn-waterfall.md) | Đối chiếu phần lớn scope, business rules, luồng, API, AT/AR và mục 16; sửa F03; không kiểm bằng app. |
| [notes/INDEX.md](../INDEX.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [notes/kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md](../kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md) | Rà scope, mức nguồn video, khung SOW/change control, giới hạn pháp lý; không legal audit hay xem lại toàn video. |
| [notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md](../kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md) | Quét claims và đối chiếu mục architecture/harness/Waterfall, giới hạn repo; source hash riêng. |
| [notes/kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md](../kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md) | Đối chiếu harness, mức verify, scale và cách gọi phương pháp phát triển; không chạy repo giúp việc. |
| [notes/kusshoes-to-rener-vn/PLAN.md](../kusshoes-to-rener-vn/PLAN.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [notes/kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md](../kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md) | Đối chiếu scope, ví dụ, lát dọc, quyền; sửa F01, bổ sung S0 theo rủi ro. |
| [notes/kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md](../kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md) | Quét toàn file; đối chiếu quyền, state, backend, scope; sửa F01–02. Không mở lại mọi URL nguồn cũ. |
| [notes/kusshoes-to-rener-vn/WORK_LOG.md](../kusshoes-to-rener-vn/WORK_LOG.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [notes/quy-chuan-ai-dev/PROMPT-KIEN-TRUC-GIAO-VIEC-AI.md](../quy-chuan-ai-dev/PROMPT-KIEN-TRUC-GIAO-VIEC-AI.md) | Đọc toàn bộ khuôn; đối chiếu các claim/template/flow; sửa F03–08 và mức quy tắc. |
| [project-realestate-ner/notes/01-research-report.md](../../project-realestate-ner/notes/01-research-report.md) | Đọc trọng điểm taxonomy, baseline/metrics/claim card; sửa F11–12. Chưa tái kiểm mọi chỉ số prior work. |
| [project-realestate-ner/notes/02-proposal-v1.2-change-audit.md](../../project-realestate-ner/notes/02-proposal-v1.2-change-audit.md) | Quét cấu trúc và các đoạn dữ liệu, metric, thay đổi scope; tài liệu lịch sử không được dùng làm baseline mới. |
| [project-realestate-ner/notes/audit-log.md](../../project-realestate-ner/notes/audit-log.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [project-realestate-ner/notes/claims-ledger.md](../../project-realestate-ner/notes/claims-ledger.md) | Đọc toàn bảng; thêm đính chính C-1 và phân biệt C-2 với demo. |
| [project-realestate-ner/notes/foundation-2026-10-09/01-local-source-review.md](../../project-realestate-ner/notes/foundation-2026-10-09/01-local-source-review.md) | Đối chiếu proposal, baseline và nhận định cần sửa; giữ lịch sử. |
| [project-realestate-ner/notes/foundation-2026-10-09/02-research-evidence.md](../../project-realestate-ner/notes/foundation-2026-10-09/02-research-evidence.md) | Đọc trọng điểm evidence/ablation/sampling/metrics; không thẩm định toàn văn mọi paper. |
| [project-realestate-ner/notes/foundation-2026-10-09/03-system-architecture.md](../../project-realestate-ner/notes/foundation-2026-10-09/03-system-architecture.md) | Đọc trọng điểm source gate, architecture, extension, data stores; đối chiếu với v0.2. |
| [project-realestate-ner/notes/foundation-2026-10-09/04-adversarial-review.md](../../project-realestate-ner/notes/foundation-2026-10-09/04-adversarial-review.md) | Đối chiếu các phản biện và mục đã sửa; phân biệt vấn đề đã giải ở design với kiểm chứng chưa làm. |
| [project-realestate-ner/notes/foundation-2026-10-09/05-source-audit.md](../../project-realestate-ner/notes/foundation-2026-10-09/05-source-audit.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [project-realestate-ner/notes/foundation-2026-10-09/BAO-CAO-HIEU-DE-TAI.md](../../project-realestate-ner/notes/foundation-2026-10-09/BAO-CAO-HIEU-DE-TAI.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [project-realestate-ner/notes/foundation-2026-10-09/KIEM-TRA-BAN-GIAO.md](../../project-realestate-ner/notes/foundation-2026-10-09/KIEM-TRA-BAN-GIAO.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md](../../project-realestate-ner/notes/foundation-2026-10-09/KIEN-THUC-NEN-TANG-RENER-VN.md) | Đối chiếu scope, states, split, metric, ablation, lộ trình và các phần liên quan; không thẩm định từng câu. |
| [project-realestate-ner/notes/foundation-2026-10-09/PLAN.md](../../project-realestate-ner/notes/foundation-2026-10-09/PLAN.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [project-realestate-ner/notes/INDEX.md](../../project-realestate-ner/notes/INDEX.md) | Quét cấu trúc/claim, vai trò điều hướng hoặc lịch sử và link; chưa tái thẩm định độc lập mọi nội dung được dẫn lại. |
| [TMG301_TongHopKienThuc.md](../../TMG301_TongHopKienThuc.md) | Đọc toàn văn ghi chú; đối chiếu các phát biểu NLP rủi ro với nguồn; sửa F09. |

539 dòng được công cụ đánh dấu ban đầu chỉ là **ứng viên để đọc**, không phải 539 lỗi. Không chấm phần trăm đúng của tài liệu từ số dòng quét.

Bản trước sửa và SHA256 được lưu để truy nguồn; link bảng trên mở bản hiện tại. Những claim về thử nghiệm, nguồn bị chặn và server còn hoạt động được giữ trạng thái chưa kiểm lại.

Ngoài 28 Markdown: rà các đoạn phạm vi/số liệu của reader [LO-TRINH-TRUC-QUAN.html](../../project-realestate-ner/notes/foundation-2026-10-09/LO-TRINH-TRUC-QUAN.html), 113.405 bytes. Reader có ghi khung 12 tuần là đề xuất, nhánh môn là 4 tuần và số liệu ví dụ; giữ nguyên snapshot, chưa render lại tương tác. Hash/mức kiểm ở [additional-artifacts.json](additional-artifacts.json). Các tài liệu môn học gốc, hình và mọi file nhị phân khác không được hiểu là đã phản biện toàn văn trong lượt này.
