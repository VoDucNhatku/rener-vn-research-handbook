# Sổ nguồn đọc sâu — 12/10/2026

Mục tiêu: truy từ một kết luận về lại nguồn và phạm vi đã đọc. **21 nguồn dưới đây đã đọc nội dung các phần ghi rõ**, không chỉ tiêu đề/mục lục; không nhận đã đọc trọn sáu paper hoặc cả sách SRE. SEND từng có trong hồ sơ cũ, được đọc lại; số 21 không phải số nguồn mới với toàn dự án.

Nguồn sơ cấp về phương pháp gồm paper và tài liệu tác giả/đơn vị phát triển. Bài AWS/Anthropic là kinh nghiệm kỹ thuật do nhà cung cấp công bố; không dùng làm thống kê phổ quát về năng suất hoặc bằng chứng app ReNER đã đạt chất lượng. Tài liệu PostgreSQL được ghim phiên bản 18 để đọc; chưa quyết định phiên bản triển khai ReNER.

| ID / nguồn trực tiếp | Phần thực sự đọc trong lượt này | Dùng để làm rõ |
|---|---|---|
| S01 — [GOV.UK: User needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) | Nội dung hướng dẫn xác định nhu cầu, chứng cứ nghiên cứu, phân biệt user needs với user stories | Nhu cầu của người tìm trọ khác danh sách màn hình/giải pháp |
| S02 — [Cucumber: Example Mapping](https://cucumber.io/docs/bdd/example-mapping/) | Trang giới thiệu ngắn: story, rule, example, question, giới hạn buổi làm việc | Cụ thể hóa một prompt ngắn bằng ví dụ và điều chưa rõ |
| S03 — [Gebru et al.: Datasheets for Datasets](https://arxiv.org/pdf/1803.09010) | Chọn lọc mục 1.1, 3.1–3.2, đầu 3.3, 3.4–3.5 và 3.7; không đọc toàn appendices | Đơn vị mẫu, missing data, split, xử lý, quyền dùng và bảo trì |
| S04 — [Jacobs & Wallach: Measurement and Fairness](https://arxiv.org/pdf/1912.05511) | Phần mở đầu và mục 3.2, đặc biệt content validity/consequential validity | Phân biệt khái niệm muốn biết với đại lượng quan sát được |
| S05 — [Ribeiro et al.: CheckList](https://aclanthology.org/2020.acl-main.442.pdf) | Giới thiệu phương pháp, Hình 1 và diễn giải MFT/INV/DIR | Ca hành vi cho giá, vai trò, đơn vị và thay đổi đầu vào |
| S06 — [Dror et al.: The Hitchhiker’s Guide to Testing Statistical Significance in NLP](https://aclanthology.org/P18-1128.pdf) | Mục 2 về metric; các đoạn McNemar, sampling/approximate randomization/bootstrap và hướng dẫn chọn test ở mục 3 | Không chọn phép kiểm thống kê chỉ theo thói quen |
| S07 — [SEND/ViND: Vietnamese real estate noise detection](https://aclanthology.org/2022.paclic-1.71.pdf) | Đọc lại định nghĩa noise 2.1, xây dựng/annotation dữ liệu 3, error analysis 4.6, kiểm tác động NER 4.7 và ngữ cảnh bảng 4 | Không đồng nhất “noise” của paper với dữ liệu vô ích của ReNER |
| S08 — [Bender & Friedman: Data Statements for NLP](https://aclanthology.org/Q18-1041.pdf) | Cân bằng mô tả/riêng tư trước mục 5; schema 5.1 từ curation đến annotator và phần speech situation | Ghi bối cảnh chọn mẫu/ngôn ngữ/gán nhãn, tránh suy rộng tùy tiện |
| S09 — [AWS: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) | Định danh request/atomicity; late arriving requests và thời hạn định danh; same ID, different intent | Cam kết chống trùng phải có phạm vi thời gian và quyền |
| S10 — [AWS: Timeouts, retries, backoff and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | Phần timeouts, retry ở nhiều tầng, backoff/jitter | Phân biệt job attempts và provider attempts |
| S11 — [PostgreSQL 18: Transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html) | Read Committed, Repeatable Read và các đoạn Serializable/retry giao dịch | Snapshot cho nhiều query và thời điểm quan sát dữ liệu |
| S12 — [PostgreSQL 18: SELECT](https://www.postgresql.org/docs/18/sql-select.html) | Locking clause với SKIP LOCKED; LIMIT/ORDER BY; không đọc toàn reference SELECT | Lấy việc trong queue khác lấy tập thống kê |
| S13 — [Chrome: Service worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle) | Idle/shutdown, lưu state và lưu ý thay đổi theo Chrome version | Không lấy biến global làm trạng thái bền |
| S14 — [Chrome: Message passing](https://developer.chrome.com/docs/extensions/develop/concepts/messaging) | Security considerations, xử lý dữ liệu an toàn; đoạn async responses và tương thích phiên bản | Message từ content script không tự có quyền hành động |
| S15 — [Chrome: Storage](https://developer.chrome.com/docs/extensions/reference/api/storage) | Storage areas, session/local và access level | Phân biệt worker restart và browser restart |
| S16 — [OWASP: LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Remote/indirect injection; agent/least privilege; model guardrails; grade intended outcome và giới hạn báo cáo | Chấm hành động thật, không chỉ lời từ chối |
| S17 — [OWASP: Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Deny by default, validate every request, giới hạn framework mặc định | Quyền theo đối tượng/hành động, bao gồm đường cache/export |
| S18 — [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | SLI specification/implementation, chọn chỉ số correctness/freshness/quality, critical user journeys | HTTP khỏe và người dùng làm xong việc là hai phép đo |
| S19 — [W3C: Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | Success criterion 4.1.3, intent và ví dụ trạng thái/kết quả tìm kiếm | Thông báo tiến độ có thể tiếp cận, không bắt chuyển focus |
| S20 — [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Định nghĩa eval/outcome/harness; ba loại grader; capability/regression; pass@k/pass^k; các bước 1–3, 6–7 và phối hợp cách đánh giá | Kiểm đúng/sai của chính bộ chấm và mức tin cậy của lời báo xong |
| S21 — [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Failure modes, tiêu chí frontend, planner/generator/evaluator và sprint contract; thay đổi harness theo model; kết quả/giới hạn và bài học cuối; không đọc hết appendix | Tổ chức agent theo lỗi thực tế; tiêu chí sáng tạo không tự thay tiêu chí nghiệp vụ |

## Bằng chứng lưu ở đâu?

- [Danh sách URL](source-list.json) và [manifest nguồn](sources/manifest.json): HTTP status, URL sau redirect, thời gian tải UTC, ngày đọc theo Asia/Saigon, scope và SHA256.
- Trong `sources/`, mỗi ID có bản gốc `.html` hoặc `.pdf` và bản trích text `.txt`. HTML text có thể chứa navigation; các mục lục lặp không được tính là đã đọc nội dung. PDF text có marker số trang để tra lại; lượt này không kiểm toàn bộ hình/công thức bằng render.
- [Script tải nguồn](fetch_sources.py) phục vụ tái truy xuất, không huấn luyện hay chạy app. Nội dung live có thể đổi sau ngày snapshot, vì vậy URL và hash trả lời hai câu khác nhau.
- [Kiểm chứng](verification.json) đối chiếu 21 raw snapshot và 21 text snapshot với hash đã ghi, kiểm liên kết local và bảo toàn các file gốc được theo dõi. Nó không phải chứng nhận hiểu đúng mọi câu nguồn hoặc xác nhận tính an toàn của app.

## Hàng rào suy luận

1. **Nguồn nói gì:** thuật lại cơ chế hoặc phương pháp trong phạm vi đã đọc; trích dẫn gần câu dùng nguồn.
2. **Áp dụng cho ReNER:** đánh dấu đề xuất/suy luận; các case tổng hợp không được đổi thành kết quả thực nghiệm.
3. **Chưa biết:** ghi bằng chứng cần có. Không lấp bằng sao GitHub, thương hiệu tool, một lời khen của evaluator hoặc một con số benchmark của người khác.

Không bổ sung kết luận pháp lý về thu thập Facebook trong lượt này; chưa xác minh nguồn thật được phép. Không nghiên cứu lại đủ 10 repo hay xem thêm các video/X/Bilibili bị chặn. Hai bài Anthropic có ngày công bố 09/01 và 24/03/2026; kết luận của tác giả về model ở thời điểm đó không tự là bảng xếp hạng model hiện tại.
