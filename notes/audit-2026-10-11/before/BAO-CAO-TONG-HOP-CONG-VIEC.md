# Báo cáo tổng hợp công việc — nghiên cứu web ReNER-VN

**Thời gian tổng hợp:** 10/10/2026; bổ sung 11/10/2026. **Phạm vi công việc đã ghi nhận:** 09–11/10/2026.

**Kết quả hiện tại:** đã chạy thử KusShoes local, khảo sát các repo tham khảo, soạn bản thảo logic/kiến trúc ReNER-VN và hệ thống tài liệu học tập có nguồn, có log. Chưa xây dựng web ReNER-VN mới.

## 1. Yêu cầu của người dùng

- Nghiên cứu repo **KusShoes**, chạy local để xem; học cấu trúc code, flow sản phẩm, sidebar/admin/dashboard và animation.
- Đọc **proposal ReNER-VN v1.3**, rút kiến thức từ repo mẫu để làm web khai thác thông tin giá thuê trọ từ Facebook.
- Phân tích người dùng, chức năng, bên nhận giá trị/bỏ công, scope và MVP; đi từ tính năng cốt lõi rồi mở rộng P1/P2. Lập bản thảo theo quy trình Waterfall trước khi code.
- Tìm khoảng **10 repo web đa lĩnh vực**: bán hàng, shop, quản trị; học kiến trúc, hướng dẫn phát triển và cách tổ chức GitHub/giao việc.
- Nghiên cứu sâu thêm về khả năng chịu tải, AI tạo web, nguồn template/motion, local/deploy và repo liên quan extension/NLP.
- Phân tích **ChoThueGiupViec**, đặc biệt flow, harness và cơ chế hỏi tên để xác định phần việc.
- Chia việc **tuần tự**, có kế hoạch trước, log sau từng phần; lưu kiến thức và báo cáo trong **TMG301**.

**Các lựa chọn đã xác nhận:** ưu tiên người tìm trọ tìm/lọc tin và so sánh giá; đầu vào qua extension để người dùng chọn và gửi từng tin. Chỉ dẫn mới nhất: **mục tiêu demo, hiện tập trung học và bản thảo; chưa thiết kế thêm hoặc code**. “5.000 người” chỉ là ví dụ nghiên cứu tải.

## 2. Công việc đã thực hiện

| Nhóm việc | Kết quả đã làm | Trạng thái/giới hạn |
|---|---|---|
| KusShoes local | Clone và khảo sát stack; dựng frontend, API, database, Redis và storage giả lập; tạo dữ liệu demo; thử đăng nhập, admin và API; có script bật/tắt | Đã chạy thử ở lượt trước; không xác nhận các dịch vụ vẫn đang chạy tại thời điểm báo cáo |
| Proposal và kế hoạch | Đọc proposal 9 trang; đối chiếu tài liệu nền; lập chặng C0–C7, xác định actor chính và luồng extension từng tin | Các chỉ tiêu dataset trong proposal chưa phải dữ liệu đã thu được |
| UI, sidebar và motion | Nhận diện các nhóm menu, trạng thái, vùng tài khoản và pipeline; khảo sát code/nguồn GSAP, Motion và mẫu giao diện | Chưa walkthrough đầy đủ từng component/trạng thái; “Interactive motion” chưa có URL xác nhận |
| 10 repo web | Khảo sát Medusa, Saleor, Vercel Commerce, React-admin, Refine, Tabler, FastAPI Full Stack Template, Cal.diy, Outline, Immich; lưu nguồn, commit, star và điểm học được | Đọc tài liệu/code chọn lọc; chưa chạy hoặc audit toàn bộ 10 repo |
| Bản thảo ReNER-VN | Soạn actor/quyền, scope P0/P1/P2, flow, module, ERD/API, admin/dashboard và wireframe dạng văn bản; tổng hợp thành v0.2 | Có 14 yêu cầu, 15 luật nghiệp vụ, 21 tình huống nghiệm thu và 8 kiểm tra kiến trúc dự kiến; chưa triển khai hoặc chạy các kiểm tra này |
| GitHub và harness | Đọc CI/PR mẫu KusShoes; nghiên cứu sâu hơn spec, team, ticket, branch, allowed paths, hooks, verify và PR/issue của ChoThueGiupViec | Chưa tạo repo GitHub mới hoặc áp dụng harness vào ReNER |
| Scale, AI và deploy | Giải thích tài khoản/DAU/concurrent/RPS; điểm nghẽn CPU/RAM/DB/network/quota; luồng context → code → kiểm chứng; phân biệt local/LAN/tunnel/cloud | Kiến thức và ví dụ giả định; chưa benchmark tải, chọn hosting hoặc deploy ReNER |
| 8 repo sát đề tài | Bổ sung WXT, Plasmo, Chrome Samples, Doccano, Label Studio, LangExtract, Scrapy, PropertyWebBuilder | Đọc README/docs; đọc thêm một số code Chrome và LangExtract; chưa build/test các repo này |
| Hồ sơ học tập | Cập nhật sổ kiến thức v0.6, chuyên đề, nguồn có commit/hash, index và log tuần tự | Có thể truy lại kết luận và phần chưa kiểm chứng |

## 3. Kết quả kiểm chứng và phát hiện chính

**KusShoes — kết quả đã ghi ở lượt chạy local:** frontend build thành công; backend unit test **42 pass**; smoke test đăng nhập/API/DB/Redis/upload–download storage thành công. Frontend có **205 test pass, 13 skip nhưng tiến trình exit 1** do hai lỗi unhandled rejection liên quan GSAP; không coi toàn bộ test xanh. Chưa kiểm chứng đầy đủ luồng 3D/editor, OAuth, email, thanh toán thật hoặc toàn bộ backend integration.

**ChoThueGiupViec:** cơ chế “Bạn tên gì?” nằm trong hướng dẫn AI của `AGENTS.md`, kích hoạt bằng “phân tích dự án”. `run.ps1` chỉ điều phối script; không tự hỏi tên hoặc tự code toàn bộ phần việc. Harness giúp nối ticket với phạm vi sửa và bằng chứng kiểm tra, nhưng CI xanh không đồng nghĩa mọi luồng đã chạy với database thật.

**Kiến thức áp dụng:** không ghép nguyên stack của nhiều repo; cần tách luật nghiệp vụ, quyền theo đối tượng, trạng thái dữ liệu và công việc nền. Dữ liệu trích xuất có span vẫn có thể sai đơn vị/loại giá; hàng đợi không tự tăng throughput; thêm CPU/RAM không giải quyết mọi quota hoặc query chậm.

**Tài liệu:** lượt kiểm chứng gần nhất trước báo cáo đã kiểm tra **83 liên kết local và 40 hash nguồn**, không phát hiện lỗi. Kiến trúc v0.2 giữ nguyên sau khi người dùng chuyển ưu tiên sang nghiên cứu. Chưa kiểm chứng render toàn bộ sơ đồ Mermaid.

## 4. Những phần chưa thực hiện

- Chưa hoàn tất walkthrough sâu toàn bộ KusShoes, sidebar/animation và lịch sử phân công GitHub.
- Chưa code web/extension ReNER-VN; chưa thu thập tin Facebook hoặc kiểm thử selector trên Facebook.
- Chưa tạo repo GitHub mới, ticket thực tế, CI/harness riêng cho ReNER.
- Chưa có kết quả đánh giá NLP trên dataset mới, benchmark tải hoặc triển khai production.

Các phần này được giữ là công việc còn lại, phù hợp chỉ dẫn hiện tại: học và làm rõ bản thảo trước.

## 5. Tài liệu bàn giao

| Tài liệu | Nội dung |
|---|---|
| [Sổ kiến thức tổng hợp](notes/kusshoes-to-rener-vn/KIEN-THUC-TONG-HOP.md) | Điểm tra cứu chung: KusShoes, proposal, motion, 10 repo, kiến trúc và chuyên đề bổ sung |
| [Kế hoạch](notes/kusshoes-to-rener-vn/PLAN.md) | Chặng công việc và các thay đổi ưu tiên; mục 13 ghi phạm vi hiện hành |
| [Bản thảo ReNER-VN v0.2](notes/design-rener-vn-waterfall.md) | Logic cốt lõi, admin/dashboard, kiến trúc, dữ liệu/API và nghiệm thu dự kiến |
| [Chuyên đề nghiên cứu bổ sung](notes/kusshoes-to-rener-vn/NGHIEN-CUU-HARNESS-SCALE-AI.md) | ChoThueGiupViec/harness, scale, AI tạo web, deploy, 8 repo và từ điển thuật ngữ |
| [Báo cáo KusShoes local](KusShoes/notes/kusshoes-local-review.md) | Môi trường, cách chạy lại, bằng chứng kiểm tra và giới hạn demo |
| [Log công việc](notes/kusshoes-to-rener-vn/WORK_LOG.md) | Tiến trình, quyết định, nguồn và kiểm chứng sau từng phần |

**Mức hoàn thành:** đã có bộ nghiên cứu và bản thảo để học, thảo luận và chuẩn bị triển khai sau này; chưa phải sản phẩm ReNER-VN hoàn chỉnh.


## 6. Bổ sung ngày 11/10/2026

Theo yêu cầu nghiên cứu gia công web và creator dùng AI: đã soạn khung brief/SOW, scope, nghiệm thu, change request, phí dịch vụ và bàn giao; đối chiếu năm video/creator qua transcript/mô tả/phần giới thiệu công khai; phân loại nguồn template/component và cách tinh chỉnh UI/context khác fine-tune model. Có đối chiếu docs hiện hành và ghi giới hạn truy cập nguồn. Xem [chuyên đề](notes/kusshoes-to-rener-vn/GIA-CONG-WEB-VA-AI-WORKFLOW.md), sổ kiến thức mục 25 và log H0–H4. Chưa ký hợp đồng, mua template, huấn luyện model hoặc code thêm.


## 7. Solo AI và học cách chia việc — 11/10/2026

Yêu cầu: mở rộng quốc tế/X/Trung Quốc; tối ưu code/UI/backend; case study/sách/blog/video; 80/20; điểm quyết định thành bại; đổi tính năng lõi và khôi phục; quản lý dự án một người dùng AI. Người dùng xác nhận khó nhất là chuyển ý tưởng ngắn thành yêu cầu/task, muốn hiểu flow và tiến tới nhận khách; tiếp tục học bài bản theo proposal/ReNER trước.

Đã tạo [báo cáo nghiên cứu](notes/kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md) và [sổ tay thực hành](notes/kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md), có brief, 10 tình huống giả lập, task S0–S5, 7 prompt, giới hạn hard rule và cơ chế thay đổi/khôi phục. Cập nhật chọn lọc khung prompt cũ v1.1 để yêu cầu mới được điều chỉnh baseline và AI tự quyết chi tiết dễ đảo. Nguồn X/Bilibili/Reels có hạn chế đã ghi rõ; không tuyên bố xem hết video/sách. Chưa user test, đo tải, sửa code app hoặc thay thiết kế v0.2. Chi tiết log I0–I5 và hồ sơ nguồn đi kèm.
