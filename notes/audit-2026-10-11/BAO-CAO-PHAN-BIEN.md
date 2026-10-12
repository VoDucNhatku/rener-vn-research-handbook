# Phản biện tài liệu toàn TMG301 — 11/10/2026

**Kết luận:** hồ sơ có nền tảng tốt về quyền dữ liệu, trích xuất có chứng cứ và kiểm soát thay đổi, nhưng chưa đủ để coi là một đặc tả thống nhất đã sẵn sàng triển khai. Có lỗi kiến thức thật, có ví dụ dễ bị hiểu thành bằng chứng đã chạy, và có yêu cầu bị lệch khi viết thêm tài liệu. Lượt này sửa trực tiếp các điểm có căn cứ, giữ bản trước sửa và ghi khoảng trống cần kiểm chứng.

Đọc [bối cảnh hiện hành](../HIEN-TRANG-VA-QUYET-DINH.md) trước khi dùng lại tài liệu cho AI. Mục tiêu vẫn là **học bài bản trên ReNER để làm demo**, rồi chuyển tư duy sang dự án khác. Không tạo web, mở dữ liệu, deploy hay nâng yêu cầu lên 5.000 người.

## 1. Đã kiểm đến đâu?

- Kiểm kê **28 Markdown do dự án tổng hợp**, ban đầu 594.454 ký tự: nghiên cứu nền tảng, kiến trúc, repo/harness, AI workflow, ghi chú môn học, kế hoạch và log.
- Quét cấu trúc/claim trên cả 28; đọc và đối chiếu sâu **các đoạn có rủi ro**, không tuyên bố đã thẩm định từng câu, toàn văn mọi paper hoặc toàn bộ code của các repo nguồn. Chi tiết từng file ở [phạm vi kiểm tra](PHAM-VI-KIEM-TRA.md).
- Đối chiếu proposal v1.3, log lab, snapshot repo và nguồn chính thức liên quan tới lỗi. Repo/vendor/build là tài liệu nguồn để tham chiếu, không phải mã ứng dụng vừa được audit toàn diện.
- [Inventory](inventory.json) lưu hash trước sửa; [bản trước sửa](before) giữ văn bản cũ để truy lại bằng chứng. Bảy proposal/workbook gốc được ghi hash trong [originals.json](originals.json).
- Các kiểm tra link, hash và nội dung sau sửa được lưu riêng trong [verification.json](verification.json). Hash khớp chỉ xác nhận file giống snapshot, không chứng minh mọi kết luận đọc từ nó đều đúng.

## 2. Những lỗi và lệch nghĩa đã sửa

Mức **cao**: có thể dẫn AI làm sai quyền, dữ liệu hoặc coi việc chưa chạy là xong. Mức **vừa**: dễ gây hiểu sai kỹ thuật/phương pháp hoặc tạo quy trình không cần thiết. Đây là mức tác động **của tài liệu**, không phải lỗ hổng runtime đã khai thác.

| ID / mức | Bằng chứng ở bản trước sửa | Vì sao có vấn đề | Sửa trong lượt này |
|---|---|---|---|
| F01 / cao | `TU-VIBE…` §5.1–5.2: duyệt/snapshot “công khai”; `SO-TAY…` EX09/S4: catalog công khai; v0.2 §3/§6: pilot nội bộ | Đổi audience mà không ghi quyết định có thể làm lộ dữ liệu đóng góp | Sửa ví dụ thành catalog nội bộ có quyền; công bố Internet là thay đổi phạm vi riêng |
| F02 / cao | `TU-VIBE…` §6: `Running → NeedsReview → Done` | Job đã xử lý xong vẫn bị treo theo quyết định người dùng; nhầm chạy thành công với được duyệt | Đổi thành `Succeeded`; giải thích review có vòng đời riêng. Sơ đồ chỉ là ví dụ, không phải state contract đầy đủ |
| F03 / cao | Thiết kế §16.1: `DOMAIN → DB`, `NLP → DB`; prompt §6.2: domain → repository; bảng §16.2 cấm domain gọi SQL | Sơ đồ và luật hướng AI theo hai cách trái nhau; adapter có thể bị hiểu được ghi vượt kiểm lease/revision | Use case/repository chịu I/O; domain thuần; bước lưu kết quả có điều kiện. Giữ nguyên stack đề xuất |
| F04 / cao | Prompt §7, §8.3, §9, §13.2: path `review.py:41`, 14 unit/2 E2E pass, Postgres 17, 20 fixtures | Không có bằng chứng các ví dụ là hiện trạng ReNER; số cụ thể nhìn giống báo cáo thực thi | Thay bằng placeholder và `NOT RUN`; đánh dấu toàn bộ cây file/API/lệnh là khuôn phải xác minh khi áp dụng |
| F05 / cao | Prompt §13.2: `5tr5/th` → `per_room` | Chuỗi chỉ nêu số tiền và tháng, chưa xác định giá/phòng; trái yêu cầu không tự điền nghĩa | Ca dương ghi rõ `/tháng/phòng`; thêm ca thiếu basis phải giữ unknown nếu không có luật ngữ cảnh đủ căn cứ |
| F06 / vừa | Prompt §2/§7/§8/§14: 150 dòng, 5 file, 400 dòng diff, ba lần sửa, mỗi task đủ quyền/UI/E2E | Biến kinh nghiệm thành luật áp mọi việc; task NLP/docs cũng bị ép điều kiện không liên quan, scaffold không thể bắt đầu | Áp kiểm chứng theo rủi ro; dựa trên tiến triển/ngân sách; cho đọc caller/policy khi review; không ép số file/dòng hoặc agent |
| F07 / cao | Prompt §3: quy tắc 1–6 “được script ép” | Scope-check/hook không chứng minh đúng nghiệp vụ, số lần suy luận hay mọi hành động bị chặn | Tách hướng dẫn Markdown, checks CI và quyền công cụ; không gọi harness là sandbox bảo đảm an toàn |
| F08 / vừa | Prompt §8.2: mọi “viền control ≥3:1”, screenshot mỗi PR | Thiếu điều kiện WCAG và dễ đồng nhất kiểm màu với toàn bộ accessibility | Ghi đúng text/non-text, thông tin cần nhận biết và ngoại lệ; thêm bàn phím/focus/label theo thay đổi. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) |
| F09 / vừa | Ghi chú TMG301 §7–8: Transformer không bị giới hạn chuỗi; §11–12: minimum spanning tree | Sai giới hạn tính toán và cách tối ưu điểm dependency graph; perplexity cũng thiếu điều kiện so sánh | Sửa full-attention bậc hai/context hữu hạn, phân biệt train song song với decoding, maximum directed tree và điều kiện PPL. [Transformer](https://arxiv.org/html/1706.03762v7), [MST parsing](https://aclanthology.org/W06-2936/), [PPL](https://huggingface.co/docs/transformers/perplexity) |
| F10 / vừa | Note bài 08 §1/§7: giữ tham số gốc; MASK không bao giờ xuất hiện khi inference; loss chỉ vị trí MASK | Nhầm khởi tạo với đóng băng; bỏ qua fill-mask và mục tiêu 80/10/10 | Sửa cập nhật trọng số, loss trên mọi vị trí đã chọn, không chỉ token MASK; không dùng tên key checkpoint như bằng chứng duy nhất về pretraining. [BERT](https://aclanthology.org/N19-1423/) |
| F11 / vừa | Báo cáo 03/10 §7: strict & partial bằng `seqeval` | Default/strict của thư viện không phải exact/overlap matching | Sửa strict BIO; partial cần định nghĩa credit/matching riêng và ca chấm tay. [seqeval](https://github.com/chakki-works/seqeval) |
| F12 / vừa | Báo cáo 03/10 §5/claim card, ledger C-1: Hybrid cao nhất; cần ≥300 gold/công bố corpus/CRF hoặc PhoBERT | Chưa có benchmark để xếp hạng; không có một ngưỡng/bộ điều kiện chung cho mọi venue; public corpus còn tùy quyền | Bỏ khẳng định ưu thế/ngưỡng chung, ghi điều kiện thực nghiệm; ledger giữ lịch sử kèm đính chính. Không thêm fine-tune vào demo |
| F13 / cao | Foundation có hướng 12 tuần/300–500 gold, proposal 4 tuần/~100 gold; tài liệu mới dùng các scope khác nhau mà chưa có trang phân xử | AI có thể lấy nghiên cứu mở rộng làm yêu cầu hiện hành, tăng việc mà không tăng giá trị demo | Thêm trang bối cảnh, phân loại xác nhận/đề xuất/quan sát/thực nghiệm/chưa biết; nối index và tài liệu liên quan |

F01–F08 là lỗi hồi quy/diễn giải xuất hiện trong quá trình tổng hợp, không đổ cho repo nguồn. F12 đã được foundation 09/10 nói thận trọng hơn, nhưng bản cũ còn lời khuyên quá mạnh; sửa để người đọc không dùng nhầm. F13 giải quyết điều hướng, chưa đồng nghĩa mọi schema giữa các bản thảo đã hợp nhất.

## 3. Những điểm đã có từ trước và vẫn đúng hướng

Không cần “phát hiện lại” hoặc thêm kiến trúc mới cho các vấn đề đã được bản thảo nhận diện:

- Loại **toàn bộ cụm trùng của tin đích** khỏi tập so sánh, không chỉ loại một ID; v0.2 B10/AT10.
- Span dùng Unicode code points trên text version cố định; frontend phải xử lý khác UTF-16; AT06.
- Idempotency theo owner và payload; cùng khóa khác payload phải xung đột, không âm thầm trả tin khác.
- Lưu submission và job cùng transaction; worker có lease/fencing; retry không bảo đảm provider chỉ tính phí đúng một lần.
- Gỡ nguồn xét snapshot/cache; restore cần áp lại yêu cầu xóa; AT16/AR08.
- N≥10 là heuristic sản phẩm, không bảo đảm đại diện thị trường; IQR không phải khoảng tin cậy của median.
- Neo span đúng chưa đủ: tiền cọc có thể bị gán làm tiền thuê; phải kiểm vai trò, đơn vị, liên kết cùng listing.
- Tách dữ liệu tổng hợp để demo khỏi dữ liệu thật dùng đánh giá; nguồn/điều khoản chưa kiểm đủ không được coi là đã có quyền.

Đây đều là **quy tắc/ca kiểm dự kiến**, chưa chứng minh app đã thực thi và vượt test.

## 4. Khoảng trống còn mở — quan trọng hơn tìm thêm framework

| Ưu tiên / gap | Đã biết gì, còn thiếu gì? | Đầu ra nên làm để đóng gap |
|---|---|---|
| G01 — giá trị và dữ liệu đầu vào | Người dùng ưu tiên đã rõ; chưa có quan sát chứng minh họ hoàn thành việc tìm/so sánh với dataset dự kiến | Thử một tác vụ trên bản nháp bằng fixture ghi nhãn; riêng tính khả thi nguồn phải dùng dữ liệu có quyền. Ghi người dùng hiểu sai/chỗ không đủ thông tin, không bịa conversion |
| G02 — từ điển contract thống nhất | Các note dùng `withheld`, `hidden_explicit`, `not_stated`, `unavailable_input`, `needs_review` ở các lớp khác nhau; chưa có mapping máy kiểm | Một bảng tách capture completeness, price visibility, decision/abstain, execution và publication; ví dụ cho từng trạng thái, mapping và migration nếu đổi tên. Chưa tự chốt enum mới |
| G03 — RQ2 và ablation | Proposal hỏi tác dụng neo nguồn/đối chiếu, nhưng so Regex–Grounded LLM–Hybrid chưa tự cô lập hiệu ứng từng phần. Foundation đã đề xuất ablation; chưa nối thành run manifest của demo | Bảng RQ → đối chứng → biến giữ cố định → metric → dataset/run. Nếu nguồn lực không đủ, thu hẹp claim; không gán toàn bộ cải thiện cho grounding |
| G04 — bộ chấm thực thi | Đã có định nghĩa nhiều metric; chưa có evaluator/fixtures đã chạy để xác nhận matching nhiều listing, null, zero denominator, offset và normalized values | Bảng expected bằng tay cho vài ca điển hình → scorer tests → khóa protocol trước final test. `seqeval` không giải quyết record matching thay mình |
| G05 — đủ dữ liệu sau lọc | ~100 gold và 300–500 market là kế hoạch. Chưa có tỷ lệ sống sót qua permission/capture/đúng loại/đúng đơn vị/duyệt/trùng/thời gian/nhóm | Bảng đếm từng bước và lý do loại, theo địa bàn/phân khúc. Nếu thiếu, thu hẹp phạm vi rõ ràng hoặc trả insufficient_data, không âm thầm nới nhóm |
| G06 — nguồn, quyền và tuổi thọ | Có gate, retention và yêu cầu xóa trong bản thảo; chưa có nguồn thật được duyệt hay cách xử lý dữ liệu hết hạn được thực nghiệm | Sổ nguồn/đích dùng, quyền xem/lưu/gửi provider/chia sẻ; ngày kiểm, thời hạn, thủ tục rút. Đánh giá metadata riêng tư còn trong text/URL/ảnh; che số điện thoại không đủ |
| G07 — vận hành có kiểm chứng | Có thiết kế retry, quota, revision, auth; chưa chứng minh với crash/restart/race bằng chương trình thật | Khi được triển khai: phép thử hai request trùng, worker chết, revision đổi, quyền bị thu hồi, quota hết và restore. Hiện giữ là NOT RUN |
| G08 — tải và chi phí | Đã phân biệt user đăng ký, đồng thời và RPS; chưa có workload hoặc số đo để chọn máy | Nếu sau này cần: đo tần suất request, service time, job arrival/throughput, DB pool và chi phí retry; CPU/RAM là một phần. Không thêm microservice theo số user giả định |
| G09 — bằng chứng từ repo/nội dung | 10 repo là mẫu có chủ đích, không đại diện mọi kiến trúc; có video chỉ đọc transcript/description và X/Bilibili bị chặn | Giữ commit/ngày/phạm vi đọc. Muốn kết luận xu hướng/hiệu quả phải có phép so sánh; chưa gọi danh sách là “10 repo tốt nhất thế giới” hoặc đã xem toàn video |
| G10 — bàn giao và đổi yêu cầu | Có CR/rollback/SOW, nhưng chưa diễn tập trên một thay đổi ReNER và chưa có khách thật | Bài tập giấy: “giá thuê → tổng chi phí” → tác động dữ liệu/API/UI/test/ngân sách/nghiệm thu; phân biệt đổi yêu cầu với bug, revert code với phục hồi dữ liệu |

Các gap này không đòi làm tất cả ngay. G01–G05 là ưu tiên học trước vì quyết định liệu phần còn lại có đang giải đúng việc. G06 bắt buộc trước khi dùng nguồn thật; G07–G08 chỉ chạy khi đã có phạm vi triển khai phù hợp.

## 5. Tư duy bổ sung để tránh hồ sơ lớn nhưng dự án vẫn yếu

### 5.1 Thay vì hỏi “stack chuẩn nhất”, hỏi “điều gì có thể làm mất giá trị?”

Với ReNER, dữ liệu cùng đơn vị và đủ nguồn quan trọng hơn số dashboard. Sai giá/phòng thành giá/người có thể khiến UI chạy mượt mà vẫn dẫn người xem tới kết luận sai. Tên framework không giải quyết nghĩa dữ liệu.

**Đề xuất cách ưu tiên, không phải công thức đã chứng minh:** đánh giá ảnh hưởng nếu sai, mức chưa biết và công sức kiểm. Thử điểm rủi ro cao nhưng kiểm rẻ trước. Quy tắc 80/20 là lời nhắc tìm phần quyết định kết quả, không phải cam kết chính xác 20% task tạo 80% chất lượng.

### 5.2 Hai dòng nghiệm thu phải nối với nhau

| Dòng | Thành công nghĩa là gì? | Ví dụ thất bại dù dòng kia tốt |
|---|---|---|
| Sản phẩm | Người tìm trọ hiểu tin, tìm/lọc và so sánh có giới hạn rõ | F1 cao nhưng người xem không biết giá đang tính theo người hay phòng |
| Nghiên cứu/đồ án | Phương pháp, dữ liệu, baseline, metric và kết luận khớp RQ | Website đẹp nhưng không có test khóa hoặc nhãn chuẩn để chứng minh extraction |

Một lát dọc nên có cả kết quả người dùng và phép kiểm nghĩa dữ liệu. Không lấy “demo chạy được” thay kết luận khoa học, cũng không lấy bảng F1 thay kiểm tính hữu dụng.

### 5.3 Đếm dòng dữ liệu bị loại, không chỉ đếm số đã thu

Ví dụ **hoàn toàn giả lập**: 400 tin nhận → 250 đủ quyền/nội dung → 180 đúng loại và đơn vị → 120 quan sát sau gộp trùng → 8 tin cùng nhóm với tin đích. Tổng thu lớn vẫn không đủ ngưỡng 10 của nhóm này. Các tỷ lệ không độc lập, nên cần đếm thực tế từng bước thay nhân các tỷ lệ tưởng tượng. “Distinct cluster” cũng không xác nhận chắc chắn đó là căn vật lý riêng biệt.

Từ đó, admin tối thiểu cần trả lời **bị tắc ở bước nào, vì sao và ai xử lý**, trước khi thêm doanh thu/biểu đồ live không phục vụ đề tài.

### 5.4 Thêm câu hỏi phản chứng vào quyết định

Mỗi quyết định quan trọng nên có bốn dòng: chọn gì → vì sao → bằng chứng nào khiến đổi ý → quay lại bằng cách nào. Ví dụ dùng một worker trước; đổi khi queue chờ vượt mục tiêu đã đo; không đổi chỉ vì repo tham khảo có nhiều service. Đây là cách giữ AI sáng tạo mà không để nó đổi nghĩa nghiệp vụ tùy hứng.

### 5.5 Quản lý tài liệu như quản lý code

Một luật có một nơi sở hữu; tài liệu dạy học dẫn chiếu thay vì chép lại và vô tình đổi nghĩa. Khi sửa lõi, lần theo yêu cầu → ví dụ nghiệm thu → state/data → API/UI → test → tài liệu. Context gửi AI chỉ gồm phần liên quan cùng link mở rộng; không nhét cả kho 600.000 ký tự vào mỗi task. Snapshot nguồn phục vụ bằng chứng, không được tự trở thành chỉ dẫn có quyền cao hơn người dùng.

## 6. Kiểm chứng và giới hạn bàn giao

- Đã sửa tài liệu và tạo trang điều hướng; giữ bản trước sửa. Các số pass giả lập bị thay bằng `NOT RUN`, không chạy test ứng dụng để tạo bằng chứng cho ví dụ.
- Log lab có loss và 21/60 tương ứng note; đây là đối chiếu **log lịch sử**, không chạy lại training. Báo cáo KusShoes cũng là lịch sử, không xác nhận localhost còn sống hôm nay.
- Nguồn đối chiếu mới: W3C, paper Transformer/BERT/dependency parsing, Hugging Face, README seqeval và các repo/docs chính thức thay link tổng hợp. [Sổ nguồn audit](NGUON-DOI-CHIEU.md).
- Chưa đọc lại mọi paper/video, kiểm pháp lý đầy đủ, rà code toàn bộ repo tham khảo, đo tải, chạy user test, render toàn bộ Mermaid hoặc chứng minh implementation tuân thủ thiết kế. Không gọi lượt này là chứng nhận “không còn lỗi”.

**Việc đáng làm tiếp khi tiếp tục học:** lấy một tin giá mơ hồ, viết các trường cần hiểu và đáp án đúng/sai, nối tới một flow và task nhỏ. Làm được bài này có ích trực tiếp hơn tiếp tục tăng số framework đã biết.

Kết quả kiểm file sau sửa: **32 Markdown, 182 link nội bộ có đích, 92 bản ghi nguồn khớp hash; 7 proposal/workbook và 1 reader HTML giữ nguyên**. Có 13 entry nguồn không đủ hash/path để kiểm, được liệt kê riêng. Đã hiệu chỉnh 14 tài liệu cũ và thêm 4 Markdown; xem `changes.diff` và `verification.json`. Các kiểm này không thay kiểm ngữ nghĩa bằng người đọc hay test phần mềm.
