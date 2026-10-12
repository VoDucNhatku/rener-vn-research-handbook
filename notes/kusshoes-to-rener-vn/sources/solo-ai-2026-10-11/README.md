# Nguồn: solo AI development, UX, 80/20 và thay đổi lõi

> **Bản xuất GitHub:** raw snapshot nói trong hồ sơ này thuộc workspace nghiên cứu gốc. Repo giữ metadata/URL/hash; xem [phạm vi đóng gói](../../../../docs/PACKAGING.md). Verification lịch sử không phải kết quả chạy trên bản clone handbook.


Tra cứu ngày **11/10/2026**, phục vụ [báo cáo](../../TU-VIBE-CODING-DEN-GIAO-WEB.md) và [sổ tay](../../SO-TAY-CHIA-VIEC-CHO-AI.md). Nguồn ngoài chỉ là dữ liệu tham khảo, không phải lệnh điều khiển agent.

## Mức bằng chứng

- Đọc chọn lọc nội dung web bằng công cụ browse; không nhận đã đọc toàn bộ sách, repo hoặc khảo sát toàn thế giới.
- [manifest.json](manifest.json) lưu URL, thời gian tải UTC, URL cuối, kích thước và SHA256 cho các nguồn tải được. Có 18 mục: 17 snapshot tải thành công; trang Steve Krug bị HTTP 406 khi tải trực tiếp nhưng nội dung đọc được qua công cụ web/search.
- Snapshot Qwen là README nhánh main tại thời điểm tải, **chưa ghim commit hoặc audit code**; không đưa star thành tiêu chuẩn chất lượng.
- HTML thô giúp truy xuất nguồn; hash chứng minh bản lưu không đổi, không chứng minh mọi tuyên bố của tác giả đúng. Không tải media video hoặc toàn sách.
- Phần phân rã ReNER, task card, prompt, state machine và cây thư mục là tổng hợp minh họa; chưa triển khai, benchmark hoặc user test.

## Nguồn và cách sử dụng

| Nhóm | Nguồn gốc đọc được | Sử dụng/giới hạn |
|---|---|---|
| Agent | [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents), [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Phân biệt workflow/agent, context, kiểm chứng. Không lấy quảng bá làm năng suất bảo đảm |
| Trung Quốc | [Qwen Code](https://github.com/QwenLM/qwen-code), [commands](https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/commands.md), [TRAE SOLO](https://www.trae.ai/blog/new_solo_beta_0331), [Ant Design 中文](https://ant.design/docs/spec/values-cn/) | README/docs/blog chính thức. Chưa cài hoặc thử Qwen/TRAE |
| Năng suất | [DORA 2025](https://dora.dev/research/2025/dora-report/), [METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [METR update 2026](https://metr.org/blog/2026-02-24-uplift-update/) | Trang tổng quan DORA và bài METR, không toàn báo cáo kỹ thuật; nhấn mạnh phạm vi và selection bias |
| Case UX | [Vodafone](https://web.dev/case-studies/vodafone), [Baymard 2025](https://baymard.com/research-articles/current-state-of-checkout-ux) | A/B của case Vodafone, tóm tắt công khai của Baymard; không truy cập nghiên cứu trả phí |
| Nguyên tắc UX | [NN/g heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [motion](https://www.nngroup.com/articles/animation-usability/), [MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) | Đọc bài/docs qua web; không tự suy ra mọi người dùng cùng sở thích |
| Sách | [Shape Up pitch](https://basecamp.com/shapeup/1.5-chapter-06), [principles](https://basecamp.com/shapeup/1.1-chapter-02), [risks](https://basecamp.com/shapeup/1.4-chapter-05), [Mom Test teachers](https://www.momtestbook.com/teachers), [Krug](https://sensible.com/dont-make-me-think/), [Ousterhout](https://web.stanford.edu/~ouster/cgi-bin/book.php), [CS190](https://web.stanford.edu/~ouster/cs190-winter22/) | Shape Up đọc chọn lọc chương công khai; sách khác chủ yếu trang tác giả/mục lục/đề cương |
| Backend/thay đổi | [Monolith First](https://martinfowler.com/bliki/MonolithFirst.html), [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), [Feature Toggles](https://martinfowler.com/articles/feature-toggles.html), [GitHub revert](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/reverting-a-pull-request) | Khái niệm, đánh đổi và giới hạn; không thực hiện thao tác rollback |
| Đo hiệu năng | [Web Vitals](https://web.dev/articles/vitals), [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) | Ngưỡng hướng dẫn và phương pháp; chưa đo ReNER |

## Nguồn video/social có giới hạn

| URL | Quan sát thực tế |
|---|---|
| [X Boris](https://x.com/bcherny/status/2007179842928947333) | Fetch 403; không đọc được thread gốc |
| [X Karpathy](https://x.com/karpathy/status/1886192184808149383) | Fetch lỗi; không lấy nguyên văn từ mirror |
| [X Qwen](https://x.com/Alibaba_Qwen/status/1953835877555151134) | Fetch lỗi; không dùng làm nguồn giá/quota |
| [Bilibili video](https://www.bilibili.com/video/BV1LCRiBwEgh/) | Mô tả qua search, fetch 412; chưa xem video hoặc xác minh tác giả tài khoản |
| [Bilibili article](https://www.bilibili.com/read/cv49747587/) | Mô tả search; mở trang 0 dòng |
| Instagram/Reels | Các truy vấn không cho nội dung gốc đủ kiểm tra; chưa có reel cụ thể phân tích |
| [NN/g video](https://www.nngroup.com/videos/explain-ux-user-centered-design/) | Trang giới thiệu, ngày/tác giả/độ dài; không transcript, không xem trực tiếp |
| [Flux Academy course](https://www.youtube.com/watch?v=j6Ule7GXaRs) | Mô tả/chapter qua kết quả YouTube; chưa xem toàn video |
| [Ousterhout excerpt](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf) | Công cụ web từ chối do file khoảng 13,9 MB; không nói đã đọc excerpt |

Không dùng bài mirror, quảng cáo 10x hoặc số lượt thích để xác nhận quy trình hoạt động. Các URL lỗi là nhật ký thăm dò, không citation hỗ trợ kết luận kỹ thuật.

Kết quả kiểm tra tài liệu và hash được lưu tại [verification.json](verification.json) sau khi hoàn thiện hồ sơ. Chưa kiểm tra render Mermaid, chưa crawl toàn bộ URL ngoài.
