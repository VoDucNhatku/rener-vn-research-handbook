# Nguồn đối chiếu lượt phản biện

Kiểm tra 11/10/2026. Nguồn web dưới được mở/tra đoạn liên quan bằng công cụ web, **không tuyên bố đọc toàn văn mọi tài liệu**. Không tải lại toàn bộ corpus nguồn cũ; hash cũ kiểm riêng. URL upstream có thể đổi sau ngày kiểm.

| Nguồn chính | Đoạn dùng / mục đích | Giới hạn |
|---|---|---|
| [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) | §3 giải mã tự hồi quy, §4 Table 1: full self-attention bậc hai | Nói về kiến trúc gốc; không áp độ phức tạp này cho mọi biến thể attention |
| [BERT](https://aclanthology.org/N19-1423.pdf) | §3.1/Appendix C.2: token mục tiêu, 80/10/10, NSP | Sửa nghĩa objective, không benchmark lại checkpoint local |
| [Shimizu, CoNLL 2006](https://aclanthology.org/W06-2936/) | Maximum spanning tree cho dependency parsing có hướng | Không khẳng định mọi graph parser dùng cùng thuật toán |
| [Hugging Face — Perplexity](https://huggingface.co/docs/transformers/perplexity) | Tokenizer và giới hạn context ảnh hưởng PPL | Không coi PPL là thước đo mọi tác vụ |
| [seqeval README](https://github.com/chakki-works/seqeval) | Default/strict modes và IOB2 | Không coi default là partial-overlap evaluator |
| [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Điều kiện contrast chữ | Chưa audit accessibility của app |
| [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | Thông tin cần nhận diện control/state và ngoại lệ | Không bắt mọi đường viền trang trí đạt cùng tiêu chí |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | README, workflow/template là lựa chọn theo mục đích | Không chạy CLI; không yêu cầu cài framework cho demo |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | README: thao tác browser qua accessibility snapshots | Có tool không đồng nghĩa đã kiểm UI; không dùng nó trong lượt này |
| [Hey API](https://heyapi.dev/docs/openapi/typescript/get-started) | Client generation và pin version | Chưa chọn/cài; đường cũ `/openapi-ts` redirect |
| [Orval](https://orval.dev/) | Trang dự án mô tả client generation từ OpenAPI | `/overview` lỗi trong công cụ; dùng trang chính, không nói đã đọc hướng dẫn bị lỗi |

Nguồn local đối chiếu trực tiếp:

- Proposal v1.3 (9 trang), text đã trích; RQ2 và kế hoạch gold/test/market. Hash file gốc ở `originals.json`.
- `notes/08-assets/lab_output.txt`, `slide7_fixed.py`, `mlm_practice.py`: log lịch sử tồn tại; không chạy lại training.
- Snapshot ChoThueGiupViec tại commit `1b45c1f4cce8a5b40bdae9d24ac262437b857b0d`: AGENTS và `harness/verify.sh`; L3 có BE test/FE build, kiểm mẫu dependency/secret. Không chạy harness hoặc gọi GitHub ghi thay đổi.
- Bản thảo v0.2, foundation 09/10, source manifests và note học repo 10/10–11/10: dùng để bắt mâu thuẫn xuyên tài liệu; không xem các tác giả trong repo là người ra chỉ dẫn cho phiên này.

Các kết luận về paper chưa đọc lại, luật/điều khoản chưa rà đầy đủ, video chỉ có description/transcript, X/Bilibili bị chặn vẫn giữ giới hạn của log trước. Không suy từ “đã tải được” thành “đã hiểu và kiểm đúng”.
