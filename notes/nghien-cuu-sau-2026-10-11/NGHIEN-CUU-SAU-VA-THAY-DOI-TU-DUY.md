# Đọc sâu sau phản biện: điều gì làm ReNER giải đúng bài toán?

Hoàn thành nội dung ngày **12/10/2026**, tiếp nối nghiên cứu bắt đầu 11/10. Đây là tài liệu học và đề xuất trên giấy; không phê duyệt kiến trúc, đổi proposal hoặc chứng minh hệ thống đã hoạt động.

**Kết luận chính:** cần nối được *nhu cầu → nghĩa dữ liệu → luật → ví dụ nghiệm thu → kết quả quan sát được*. Biết thêm framework chỉ hữu ích khi giúp giải một mắt xích trong chuỗi này. Rủi ro lớn của ReNER là đưa ra một phép so sánh có vẻ chính xác nhưng thực ra đang so những thứ khác nghĩa.

Đã đọc các phần liên quan của **21 nguồn** gồm tài liệu chính thức, paper và bài engineering; có nguồn đọc lại để kiểm sâu, không phải 21 phát hiện mới. [Sổ nguồn](SO-NGUON-DA-DOC.md) ghi mức đọc; [26 ca phản chứng](BO-CA-PHAN-CHUNG-RENER.md) biến kết luận thành tình huống có thể kiểm sau này. Nguồn tải về không đồng nghĩa đã đọc toàn bộ, và hash đúng không chứng minh diễn giải đúng.

## 1. Từ hồ sơ cũ đến hiểu biết cụ thể hơn

| Điểm xuất phát | Bổ sung lần này | Hệ quả cho cách làm |
|---|---|---|
| Đã chọn người tìm trọ và extension | Nhu cầu, cơ chế nhập và tiêu chí thành công là ba việc khác nhau | Hỏi người xem hiểu gì sau khi xem tin, không chỉ kiểm nút gửi chạy |
| Đã cảnh báo giá thiếu/giá mơ hồ | Bài đăng, tin được tách, căn phòng thật và giao dịch thuê không cùng đơn vị | Không lấy giá rao để khẳng định giá giao dịch hoặc phòng còn trống |
| Có nhiều state trong các note | Phân loại theo trục độc lập và ghép thành ví dụ hợp lệ | Một job thành công vẫn có thể không có giá hoặc chưa được công bố |
| Đã nêu F1, coverage, grounding | Có phản ví dụ hai phòng bị đổi giá cho nhau dù span đều đúng | Chấm cả liên kết trường trong một record, không chỉ hợp các entity |
| Foundation đã yêu cầu ablation | Cụ thể hóa phép đối chứng để trả lời RQ2 | So ba pipeline chỉ cho kết quả tổng thể; không tự tách tác dụng grounding |
| Đã có idempotency/retry | Xét hạn lưu khóa, request đến muộn và retry của SDK | Một job không đồng nghĩa một lần gọi provider hoặc một lần tính phí |
| v0.2 đã yêu cầu snapshot nhất quán | Đối chiếu isolation thật và mục đích SKIP LOCKED | BEGIN mặc định chưa đủ; cách đọc nhất quán phải được chọn khi triển khai |
| Đã nói extension có token/quyền | Phân biệt popup đóng, worker dừng và browser khởi động lại | Thiết kế nối lại công việc từ job của backend, không dựa vào biến RAM |
| Đã có phân quyền và prompt guard | Xét từng tài nguyên, message và side effect | Một role hoặc câu “ignore instructions” chưa là ranh giới bảo vệ |
| Đã nghiên cứu harness | Đọc cách chấm outcome và giới hạn evaluator bằng LLM | AI báo xong, test tự viết pass và người dùng làm được việc là ba mức khác nhau |

Những điểm cũ vẫn đúng được giữ: bỏ cụm trùng của tin đích khỏi tập so sánh; không lấy N≥10 làm bằng chứng đại diện; tách Unicode code point và UTF-16; có lease/revision; kiểm quyền nguồn hiện hành; phân biệt rollback code với dữ liệu. Không ghi chúng thành phát hiện mới.

## 2. Một câu ngắn được chuyển thành yêu cầu như thế nào?

GOV.UK đặt nhu cầu ở vấn đề người dùng cần giải quyết; Example Mapping tổ chức một câu chuyện bằng luật, ví dụ và câu hỏi. Hai nguồn giúp làm rõ yêu cầu trước khi chọn màn hình. Không cần cài Cucumber để dùng cách suy nghĩ này. [User needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs), [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/).

**Bài tập giả lập:** người dùng nói “tìm cho tao phòng dưới 3 triệu”. Đây không phải yêu cầu mới đã được chủ dự án chốt.

| Thành phần | Bản diễn giải thử |
|---|---|
| Nhu cầu | Tìm được các lựa chọn có chi phí hiểu được, không bị nhầm giá/người thành giá cả phòng |
| Giả định để luyện | “Dưới” là nhỏ hơn, ngân sách áp dụng cho giá thuê cơ bản mỗi phòng mỗi tháng |
| Luật thử | Chỉ so các tin có đúng đơn vị và phạm vi; thiếu giá không được đổi thành 0 |
| Ví dụ đạt | 2,8 triệu/phòng/tháng có thể nằm trong bộ lọc này, nếu các điều kiện khác hợp lệ |
| Ví dụ không đạt | 3 triệu/phòng/tháng không nhỏ hơn 3 triệu; 2 triệu/người/tháng không tự thành 2 triệu/phòng |
| Ví dụ chưa quyết được | “Từ 2,8 triệu”, “2,8 triệu, phí riêng”, “ib giá”, nhiều phòng không gắn được giá |
| Câu hỏi có tác động | Người tìm cần tiền thuê cơ bản hay tổng chi phí; có nhận khoảng giá; có cần điều kiện còn phòng? |
| Ngoài bài tập này | Thanh toán, đặt cọc, xác thực chủ nhà, dự đoán giá giao dịch |

AI có thể tự chọn cách trình bày bảng, tên hàm hoặc vị trí component. AI cần đưa ra lựa chọn dễ hiểu khi thay đổi *nghĩa* của “giá” hay quyền sử dụng dữ liệu. Không cần ép người dùng tự viết một prompt rất dài.

Luồng học cần đi được bằng lời: **chọn tin → xem phần văn bản sẽ gửi → backend kiểm quyền và nhận việc → trích xuất → xác định điều gì biết/chưa biết → kiểm điều kiện so sánh → hiển thị căn cứ hoặc lý do chưa so được**. Đóng góp vào catalog nội bộ và admin duyệt là một nhánh riêng; hoàn thành phân tích cá nhân chưa đồng nghĩa được chia sẻ.

### Chia thành ba việc có thể duyệt mà chưa cần code

| Việc | Đầu vào | Đầu ra để kiểm | Điều kiện kết thúc |
|---|---|---|---|
| T1 — thống nhất nghĩa | Câu ngắn và các quyết định đã có | Một bảng như trên, ghi giả định và câu hỏi còn mở | Hai người đọc phân loại giống nhau các ví dụ, hoặc ghi rõ điểm bất đồng |
| T2 — lần theo một tin | Bảng nghĩa + hai trường hợp mơ hồ | Flow bình thường, nhánh thiếu thông tin và nhánh mất kết nối; dữ liệu đi qua mỗi bước | Không có bước tự biến unknown thành con số hoặc tự cấp quyền |
| T3 — lập bằng chứng nghiệm thu | Flow và luật thử | Bộ ca có input, expected, lớp kiểm, cách quan sát và NOT RUN | Mỗi luật quan trọng có ca đạt, ca bị từ chối và ca chưa đủ thông tin |

T1–T3 là mẫu phân việc cho giai đoạn học. Chưa mở ticket/branch hoặc thực hiện phỏng vấn. Khi được yêu cầu triển khai, chọn một lát cắt đi hết luồng và chứng minh nó trước, rồi mới mở rộng chức năng.

## 3. Làm rõ “mình đang biết gì” trước khi nói “mình lưu trường gì”

### 3.1 Bốn đối tượng rất dễ đánh đồng

**Bài đăng** là một nội dung quan sát được tại một thời điểm. Nó có thể nói về **nhiều tin cho thuê**; một tin có thể nói về **một loại phòng hoặc nhiều phòng thật**; cuối cùng **giao dịch thuê** có thể có giá khác giá rao. Chưa có bằng chứng nối các đối tượng thì không nên tự gộp chúng.

Measurement and Fairness phân biệt khái niệm muốn đo với đại lượng dùng để đại diện. **Áp dụng suy luận cho ReNER:** “giá thấp trong nhóm tin rao đã lọc” có thể đo được từ dữ liệu dự kiến; “rẻ”, “đáng thuê”, “an toàn” và “còn phòng” cần thêm định nghĩa/bằng chứng. Paper không nghiên cứu trực tiếp thị trường trọ Việt Nam. [Measurement and Fairness, mục construct validity](https://arxiv.org/pdf/1912.05511).

Ví dụ: tin vừa được thu hôm nay có thể là tin cũ được đăng lại. Thời điểm *đăng*, *thu*, *xác nhận lại* và *cập nhật trạng thái phòng* không thay thế nhau. Không đủ nguồn thì hiển thị chưa biết; gắn nhãn “đã xác minh” chỉ vì admin bấm duyệt là đổi nghĩa dữ liệu.

### 3.2 Bảy trục trạng thái — bảng khái niệm, chưa phải enum/API

| Trục | Câu hỏi trả lời | Ví dụ |
|---|---|---|
| Độ đầy đủ đầu vào | Đã lấy đủ phần cần phân tích chưa? | Đầy đủ; bị cắt ở “xem thêm”; phần giá nằm trong ảnh chưa xử lý |
| Giá được tiết lộ | Nguồn có công khai giá không? | Có ghi; chủ động giấu/“ib”; không thấy đề cập |
| Nghĩa giá | Con số thuộc loại, đơn vị, chu kỳ nào? | Giá cố định/khoảng/từ; tiền cọc/thuê/phí; người/phòng; ngày/tháng/chưa rõ |
| Quyết định trích xuất | Có đủ căn cứ nhận kết quả không? | Chấp nhận trường; để trống có lý do; cần kiểm lại |
| Thực thi | Chương trình đã làm đến đâu? | Queued, Running, Succeeded, Failed theo bản thảo |
| Duyệt nội dung | Người có trách nhiệm đã quyết gì? | Chưa duyệt; cần sửa; đã duyệt |
| Công bố và quyền nguồn | Ai được xem kết quả ở thời điểm này? | Cá nhân; catalog nội bộ được phép; rút/hết hiệu lực |

Một tổ hợp hợp lệ: đầu vào đầy đủ + “ib giá” + job Succeeded + giá numeric trống + không đủ điều kiện tính trung vị. Một tổ hợp khác: trước đó đã duyệt nhưng nguồn vừa bị rút quyền → không còn được hiển thị trong catalog. “Không đủ điều kiện so sánh” nên tính từ các dữ kiện hiện hành, tránh thêm một cờ độc lập rồi để nó lệch dữ liệu.

Các tên `withheld`, `hidden_explicit`, `not_stated`, `unavailable_input` trong note cũ vẫn cần mapping và quyết định tên canonical trước khi có code. Bảng này làm rõ nghĩa, **chưa đóng G02** bằng một schema thực thi.

### 3.3 Hồ sơ dữ liệu tối thiểu cần trả lời gì?

Datasheets đề nghị ghi động cơ, cấu thành, cách thu/xử lý, cách dùng và bảo trì. Data Statements bổ sung bối cảnh ngôn ngữ và người gán nhãn, đồng thời bàn đến giới hạn riêng tư. [Datasheets, mục 3](https://arxiv.org/pdf/1803.09010), [Data Statements, mục 5](https://aclanthology.org/Q18-1041.pdf).

**Bản nháp cho ReNER:** lưu mô tả đơn vị mẫu; nguồn và thời gian; cách chọn mẫu; điều kiện được dùng; phiên bản text/nhãn; quy tắc gắn trường với listing; cụm trùng và cách chia dev/test; trường thiếu và lý do; năng lực/nguyên tắc hòa giải của người gán nhãn; cách sửa/rút mẫu. Những mục chưa biết được ghi chưa biết. Không đoán tuổi/giới tính/nghề của người đăng để “đủ datasheet”.

Đếm riêng bài thu vào, bài có quyền sử dụng, listing tách được, listing đúng phân khúc/đơn vị, sau loại trùng và còn trong khoảng thời gian. Các bước có thể đổi đơn vị đếm: một bài thành nhiều listing nên không mặc định mọi hàng đều giảm dần. Công bố cả đơn vị và mẫu số, tránh lấy 500 bài làm 500 phòng độc lập.

SEND/ViND coi thiếu thông tin và nhiều tài sản trong bài là các dạng noise, và mục 4.7 thử lọc trước NER. Với mục tiêu ReNER, các trường hợp này còn là đầu vào cần giải thích hoặc tách được. Kết quả lọc của paper không tự chứng minh cách lọc đó tăng giá trị sản phẩm của mình. [SEND/ViND, mục 2.1 và 4.7](https://aclanthology.org/2022.paclic-1.71.pdf). Đây là củng cố lưu ý đã có, không phải lý do tự loại toàn bộ tin khó.

## 4. Từ “F1 bao nhiêu” đến một protocol khó tự đánh lừa

### 4.1 Ba tầng chất lượng trả lời ba câu khác nhau

| Tầng | Câu hỏi | Phản ví dụ |
|---|---|---|
| Span/entity | Có tìm đúng đoạn và loại thực thể không? | Tìm đúng hai giá nhưng gán nhầm phòng |
| Record đã chuẩn hóa | Giá, diện tích, phí có đúng vai trò và đi cùng đúng listing không? | JSON hợp lệ nhưng 3 triệu tiền cọc biến thành tiền thuê |
| Hành trình người tìm trọ | Người xem hiểu được căn cứ và giới hạn so sánh không? | Kết quả đúng nhưng UI giấu đơn vị/ngày/thiếu phí |

**Ví dụ tự soạn:** gold có A=(18 m², 3 triệu/phòng/tháng), B=(25 m², 4 triệu/phòng/tháng). Dự đoán giữ đúng toàn bộ span nhưng trả A=(18,4), B=(25,3). Một bộ chấm chỉ nhìn tập entity có thể cho điểm tốt; chấm record đầy đủ phải nhận ra cả hai liên kết sai.

Một đường cơ sở chấm record trên giấy: chuẩn hóa theo protocol đã khóa, so **đa tập** các record để thứ tự output không gây sai và bản dự đoán lặp vẫn bị tính thừa. Exact record là điểm dễ giải thích nhưng quá khắt khe để chẩn đoán mọi lỗi; cần thêm điểm từng trường với quy tắc ghép gold–prediction được định nghĩa trước. Không để chính model đang được chấm tùy ý chọn cách ghép có lợi cho nó. Đây là đề xuất evaluator, chưa có code hoặc số đo.

### 4.2 Ca hành vi bổ sung cho test set

CheckList dùng MFT (chức năng tối thiểu), INV (biến đổi không nên làm đổi kết quả liên quan) và DIR (thay đổi có hướng mong đợi). Paper minh họa trên các tác vụ khác; các ca ReNER dưới đây do mình suy ra, chưa chạy. [CheckList, phương pháp và Hình 1](https://aclanthology.org/2020.acl-main.442.pdf).

- Thêm emoji đầu tin: **giá trị giá** nên giữ; offset span phải tính lại theo text mới, không được giữ nguyên mọi output.
- Đổi `/phòng` thành `/người`: đơn vị phải đổi và tư cách so sánh phải xét lại; đây không phải ca bất biến.
- Thêm “cọc 1 tháng” vào tin có giá rõ: tiền thuê không được tự tăng gấp đôi; tiền vào ở và tiền hàng tháng là các khái niệm khác nhau.
- Giữ mọi nội dung, đổi giá thành “ib”: không được giữ số cũ do cache hoặc suy đoán theo phòng tương tự.

### 4.3 Đừng thưởng hệ thống vì né hầu hết ca khó

Ví dụ số học **tổng hợp**, mỗi mẫu có đúng một giá cần trích xuất, 10 gold; không phải kết quả model:

| Phương án giả lập | Đúng / sai / bỏ trống | Precision | Recall | F1 | Coverage | Tỷ lệ sai trong phần đã trả |
|---|---|---|---|---|---|---|
| A | 4 / 0 / 6 | 1,00 | 0,40 | 0,5714 | 0,40 | 0/4 |
| B | 6 / 2 / 2 | 0,75 | 0,60 | 0,6667 | 0,80 | 2/8 |

Ở đây một dự đoán sai vừa là FP vừa làm thiếu gold đúng (FN); coverage = số mẫu có trả giá / 10. A ít sai quan sát được nhưng chỉ giúp 4/10 mẫu. B bao phủ nhiều hơn nhưng có hai lỗi. Không thể chọn “tốt nhất” chỉ từ precision; phải xét hậu quả của lỗi và của việc không trả kết quả. 0/4 không có nghĩa rủi ro ngoài đời bằng 0. [Phép tính kiểm lại](toy-metrics.json) chỉ chứng minh số học của ví dụ.

### 4.4 RQ2 cần đối chứng phù hợp với câu muốn kết luận

Giữ ba nhánh Regex, Grounded LLM và Hybrid như proposal để so kết quả tổng thể. Nếu muốn nói riêng **yêu cầu chứng cứ** hoặc **bộ kiểm chứng** tạo ra thay đổi, cần giữ các yếu tố còn lại ổn định. Bảng dưới là gợi ý thực nghiệm thêm, không tự tăng scope bốn tuần:

| Câu hỏi | Đối chứng khả dĩ | Giữ cố định | Báo cáo |
|---|---|---|---|
| Yêu cầu model trả chứng cứ ảnh hưởng gì? | Prompt không yêu cầu evidence so với prompt yêu cầu evidence | Dữ liệu, model/version, trường đích, cách chuẩn hóa và chấm giá trị | Record/field quality, coverage, lỗi không có căn cứ, chi phí |
| Validator loại kết quả thiếu/sai chứng cứ giúp gì? | Chấm cùng output đã thu trước và sau validator | Output model nguyên gốc, quy tắc validator/version | Bao nhiêu lỗi bị chặn, bao nhiêu kết quả đúng bị loại, tỷ lệ còn trả |
| Pipeline nào hữu ích trong demo? | Regex / Grounded LLM / Hybrid trên cùng tập khóa | Split, gold, protocol, giới hạn ngân sách rõ ràng | Chất lượng cùng độ trễ/chi phí, mẫu số và số lần chạy |

Hai phép đầu giúp tách câu hỏi nhưng chưa đo hết tương tác giữa prompting và validator. Muốn kết luận tương tác cần thiết kế thêm; không đủ nguồn lực thì thu hẹp claim. Không dùng test giữ lại để chỉnh prompt rồi gọi nó là đánh giá cuối.

So chất lượng giá trị bằng cùng gold/scorer ở cả hai prompt. Việc tuân thủ yêu cầu trả evidence được chấm riêng ở nhánh có yêu cầu; không đánh trượt đối chứng chỉ vì nó không trả trường chưa từng được yêu cầu. Kiểm giá trị có căn cứ trong nguồn phải dùng một quy tắc chung, không để model tự xác nhận câu trả lời của chính nó.

Manifest thực nghiệm đề xuất gồm: câu hỏi/đối chứng; phiên bản dữ liệu và cụm chia tập; gold/guideline/scorer; prompt/rules/normalizer; provider/model snapshot nếu có; tham số sinh; lần chạy; chính sách retry; lỗi/timeout; số cuộc gọi/token/chi phí; output và lý do loại. Seed hoặc nhiệt độ 0 không tự bảo đảm mọi lần gọi giống nhau.

Dror et al. yêu cầu chọn phép kiểm theo metric và giả định, không chọn một phép kiểm cho mọi bảng. **Đề xuất cho ReNER:** so cặp trên cùng bài/cụm; nếu resampling thì giữ cấu trúc phụ thuộc và tính lại metric, không coi từng token là quan sát độc lập. Với tập test nhỏ, ưu tiên công khai từng lỗi và độ biến động; bootstrap không tạo thêm dữ liệu độc lập hay bảo đảm khái quát thị trường. [Dror et al., mục 2–3](https://aclanthology.org/P18-1128.pdf).

## 5. Backend gọn vẫn cần hiểu những cơ chế này

### 5.1 Một job, nhiều request và nhiều hóa đơn là ba bộ đếm

AWS mô tả retry an toàn bằng định danh ý định, đối chiếu tham số và thời gian giữ thông tin request. Bài về backoff chỉ ra retry nhiều tầng có thể khuếch đại tải. Đây là kinh nghiệm vận hành, không bắt ReNER dùng kiến trúc AWS. [Idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [Timeouts, retries, backoff and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/).

Ví dụ tự tính: worker thử tối đa 3 lần, SDK mỗi lần lại thử tối đa 3 cuộc gọi HTTP → có thể đến 9 cuộc gọi provider. “3 lần thử” phải nói rõ là tổng attempts hay số retries sau lần đầu. Hạn ba lần gọi trong v0.2 cần được nối với cấu hình SDK và bộ đếm thật khi triển khai; chỉ đếm số lần job chạy chưa đủ.

Timeout có thể xảy ra sau khi provider đã xử lý. Khóa chống trùng ở backend không khiến provider miễn phí hay hủy được tác vụ đã nhận. Cần xác định tầng sở hữu retry, tổng deadline/ngân sách, lỗi nào được thử lại, và phản hồi khi budget hết.

**Lỗ hổng contract cần quyết định:** khóa idempotency tồn tại bao lâu so với raw text, job và thời hạn người dùng bấm gửi lại? Trong thời hạn cam kết, cùng khóa/cùng nội dung nối về thao tác cũ; cùng khóa/khác nội dung là xung đột theo bản thảo. Khi hết hạn, backend có còn nhận biết khóa cũ không? Không thể hứa trả “đã hết hạn” nếu đã xóa mọi dấu vết nhận biết nó. Tombstone hoặc receipt có hạn là những lựa chọn phải cân nhắc riêng về dữ liệu/quyền, chưa chọn một cách.

Request đến muộn sau khi nguồn bị rút không được hồi sinh dữ liệu đã rút hoặc trả lại nội dung cũ chỉ để giữ “response giống hệt”. Bảo toàn định danh thao tác phải đi cùng quyền xem hiện hành và hợp đồng retention.

### 5.2 BEGIN không có nghĩa mọi SELECT nhìn cùng một ảnh dữ liệu

Ở PostgreSQL Read Committed, các câu lệnh có thể nhìn các snapshot khác nhau trong cùng transaction. SKIP LOCKED phù hợp với một số cách lấy việc từ queue, và tài liệu cảnh báo nó tạo cách nhìn không nhất quán. [Transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html), [SELECT — locking clause](https://www.postgresql.org/docs/18/sql-select.html).

Phản ví dụ: query đầu đếm N=10; một transaction khác thêm tin hợp lệ rồi commit; query sau lấy giá để tính median trên 11 tin. Hai số riêng lẻ đều “đúng”, nhưng thẻ thống kê ghép chúng lại bị sai nghĩa. Không sửa bằng cách bỏ qua các hàng đang khóa, vì như vậy nhóm so sánh bị thay đổi theo tranh chấp DB.

v0.2 đã yêu cầu snapshot hoặc kiểm revision nên **không kết luận thiết kế đang mắc lỗi này**. Khi triển khai phải chọn cơ chế thật, chẳng hạn cùng statement/snapshot thích hợp hoặc đọc rồi xác nhận revision và làm lại có giới hạn. Snapshot nhất quán không thay thế kiểm quyền nguồn hiện hành khi phục vụ kết quả. Tương tự, ORDER BY ổn định giúp thứ tự xác định; nó không tự đóng băng dữ liệu giữa hai lần phân trang.

## 6. Extension là một chuỗi biên tin cậy và vòng đời

Chrome có thể dừng service worker khi không hoạt động; biến global không bền. `storage.session` có vòng đời khác worker và bị xóa khi browser khởi động lại hoặc extension bị reload/disable/update. Content script được xem là kém tin cậy hơn phần đặc quyền. [Lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle), [Storage](https://developer.chrome.com/docs/extensions/reference/api/storage), [Messaging — security considerations](https://developer.chrome.com/docs/extensions/develop/concepts/messaging).

| Sự kiện | Điều phải chứng minh sau này |
|---|---|
| Đóng popup | Việc backend đã nhận vẫn có thể được tìm lại; UI không được tự tạo job mới vì mất trạng thái màn hình |
| Worker bị dừng rồi khởi động | Không cần biến RAM cũ để biết request nào đã nhận; gửi lại tuân theo idempotency |
| Browser khởi động lại | Không giả định session storage/token vẫn còn; kết nối lại rồi kiểm quyền tìm job |
| Trang gửi message giả hoặc payload lạ | Không được biến service worker thành công cụ fetch tùy ý bằng token của người dùng |

Bản nháp hợp đồng message nên là các hành động hẹp, ví dụ gửi phần text đã preview, hỏi trạng thái job của mình. Phần đặc quyền tự chọn endpoint cố định, kiểm kiểu/kích thước dữ liệu và sender/context phù hợp; không nhận một URL tùy ý rồi gắn token gọi giúp. Dữ liệu trang là input, không phải thẩm quyền cho phép công bố, xóa hoặc đổi quyền.

Không coi click trên trang là bằng chứng mọi dữ liệu được dùng cho mọi mục đích. Chọn một tin để phân tích cá nhân và đồng ý đóng góp vào catalog là hai hành động khác nhau. Kế hoạch lưu draft 24 giờ cũng cần nơi lưu và cơ chế dọn rõ ràng; `storage.session` tự mất lúc restart không thực hiện cam kết đó. Lựa chọn persist gì, ở đâu, bao lâu vẫn mở.

## 7. Phân quyền và AI: chặn đúng hành động thay vì chỉ kiểm lời nói

OWASP yêu cầu mặc định từ chối và kiểm quyền mỗi request. Áp dụng cho ReNER phải xét người gọi, hành động, đối tượng sở hữu, phạm vi chia sẻ và trạng thái nguồn hiện hành. [Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

“Có role user” không đủ để đọc job của user khác; “có role admin” không tự xác lập quyền sử dụng mọi nguồn. Phải xét cả API kết quả, cache và file xuất, không chỉ sidebar. Demo có thể bắt đầu bằng các hàm policy tập trung và ca kiểm rõ ràng; chưa có lý do bắt buộc thêm một policy engine riêng.

OWASP xem nội dung bên ngoài là đường đưa prompt injection vào model, khuyến nghị giới hạn đặc quyền và đánh giá hành động quan sát được. Một lời từ chối ở cuối không chứng minh trước đó chưa có tool call sai. [Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).

Đề xuất tối giản cho tác vụ trích xuất: model nhận dữ liệu và trả candidate; không tự có quyền sửa DB, đổi policy hoặc truy cập URL trong tin. Schema kiểm hình dạng, validator kiểm thêm vai trò/chứng cứ và nghiệp vụ. Một JSON hợp lệ vẫn có thể chứa giá sai. Bộ thử cần quan sát output và side effect được phép, dùng dữ liệu giả; không đưa secret thật vào prompt để thử rò rỉ.

## 8. Harness, giao việc AI và khái niệm “xong”

Anthropic phân biệt task, trial, grader, transcript và outcome; khuyến nghị phối hợp bộ chấm theo loại kết quả và kiểm cả chính bộ chấm. Bài harness sau đó mô tả tách planner/generator/evaluator, nhưng cũng bỏ bớt cơ chế khi model mới xử lý tốt hơn. Đây là kinh nghiệm do nhà cung cấp công bố, không phải phép chứng minh nhiều agent luôn hơn một agent. [Demystifying evals, 09/01/2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Harness design, 24/03/2026](https://www.anthropic.com/engineering/harness-design-long-running-apps).

**Bài học áp dụng:** trước task phải biết sẽ nhìn vào đâu để xác nhận. “Đã phân tích” phải có kết quả đúng và quyền đúng; “đã publish” phải có record/catalog phù hợp; “đã sửa” phải có ca lỗi cũ và bằng chứng nó không còn xảy ra. Dòng chat báo xong không phải outcome.

Tách người sinh code và người kiểm giúp thay góc nhìn, nhưng cùng prompt mơ hồ vẫn có thể khiến cả hai đồng ý sai. Test do AI tự viết chỉ mạnh bằng định nghĩa đúng/sai nó được cung cấp. Giữ một bộ ví dụ nghiệp vụ do chủ dự án hiểu, có mẫu đúng và mẫu sai đã biết để kiểm scorer; dùng tiêu chí công khai, không đánh trượt AI bằng yêu cầu bí mật chưa từng nằm trong task.

Không lấy trọng số “originality” của case thiết kế mỹ thuật áp nguyên cho web tìm trọ. Với ReNER, dễ hiểu giá/phí/nguồn và hoàn thành tác vụ phải được đánh giá riêng; hiệu ứng sáng tạo có chỗ ở hình thức nếu không làm mất thông tin. Tiêu chí càng được tối ưu nhiều càng cần đối chiếu người dùng thật để tránh chỉ đẹp theo điểm của evaluator.

Hai kiểu thử lại cũng khác: “ít nhất một trong nhiều lần thành công” và “mọi lần đều thành công”. Không lấy demo may mắn nhất làm độ tin cậy mặc định. Với một người làm, bắt đầu bằng task rõ → một lượt thực hiện → kiểm outcome → sửa lỗi có bằng chứng; chỉ thêm agent/cơ chế nếu lỗi quan sát được cho thấy cần nó.

## 9. UX và vận hành phải đo được từ phía người làm việc

Google SRE phân biệt định nghĩa SLI với cách đo, và đặt hành trình quan trọng của người dùng vào việc chọn chỉ số. WCAG 4.1.3 giải thích cách đưa thông báo trạng thái tới công nghệ hỗ trợ mà không cần chuyển focus. [Implementing SLOs](https://sre.google/workbook/implementing-slos/), [Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).

Áp dụng trên giấy: HTTP 202 chỉ nói đã nhận, không nói phân tích đã xong. Đo thời gian từ gửi đến kết quả có thể dùng, tỷ lệ thất bại và lý do chưa so được; chất lượng trích xuất còn cần gold/kiểm mẫu, không suy ra từ server xanh. Chưa đặt SLA 99,9% hoặc cam kết độ trễ khi chưa có workload.

Kết quả “chưa đủ dữ liệu so sánh” có thể là phản hồi đúng và dịch vụ vẫn hoạt động, nhưng người dùng chưa đạt mục tiêu so sánh. Cần ghi hai điều này riêng để không làm đẹp tỷ lệ thành công. UI cần giải thích thiếu gì, giữ text/draft phù hợp quyền và cho hành động tiếp theo.

Khi job đổi trạng thái, thông báo ngắn ở vùng status; tránh đọc lại mọi lần poll hoặc giật focus khỏi việc đang làm. Với trang so sánh, đơn vị giá, khoảng thời gian và lý do thiếu dữ liệu quan trọng hơn animation. Đó là giả thuyết thiết kế cần thử bằng một tác vụ thật, chưa phải kết quả user test.

## 10. Khoảng trống nào đã tiến bộ, khoảng nào vẫn nguyên?

| Gap của audit | Tiến bộ trên giấy | Bằng chứng vẫn còn thiếu |
|---|---|---|
| G01 nhu cầu | Một bài tập câu ngắn → luật → nghiệm thu | Người dùng thực tế hiểu và hoàn thành tác vụ |
| G02 ontology | Bảy trục và tổ hợp hợp lệ | Mapping canonical, schema, kiểm máy |
| G03 RQ2 | Đối chứng và manifest dự kiến | Quyết định phạm vi, dữ liệu và kết quả thực nghiệm |
| G04 evaluator | Phản ví dụ record, đa tập, coverage và ca chuẩn | Scorer thực thi, kiểm scorer bằng đầu ra biết trước |
| G05 số mẫu sau lọc | Phân biệt đơn vị bài/listing/cụm, mẫu số | Funnel dữ liệu thật có quyền và đủ nhóm so sánh |
| G06 nguồn/retention | Xét request muộn và quyền khi replay | Nguồn thật được phép; diễn tập thu hồi/xóa |
| G07 vận hành | Các ca race/restart/message/quota cụ thể | Chương trình thật và fault tests |
| G08 tải | Làm rõ retry làm tăng số cuộc gọi | Workload/chi phí thật; hiện không cần mục tiêu 5.000 người |
| G09 chất lượng nguồn | Sổ 21 nguồn, snapshot, mức đọc và giới hạn | Chưa mở rộng lại audit repo/video; chưa xem nội dung bị chặn |
| G10 đổi yêu cầu | Thêm ca chuyển tiền thuê → tổng chi phí | Diễn tập migration/rollback trên implementation và dữ liệu thật |

**Thứ tự đáng học tiếp:** hoàn thiện một bài tập T1–T3; chốt thuật ngữ và ca khó; kiểm bộ chấm bằng ví dụ biết trước; rồi mới dùng dữ liệu được phép để kiểm giá trị. UI chi tiết, chọn máy và tự động hóa nhiều agent đi sau các quyết định ảnh hưởng trực tiếp đến đúng/sai.

Điểm dừng của lượt này là hồ sơ nghiên cứu có thể truy xuất và bộ phản chứng cụ thể. Không tuyên bố mọi lỗ hổng đã đóng, không sửa app, không chạy benchmark/user test, không xác nhận quyền thu thập dữ liệu thật và không thay proposal gốc. Xem [log K0–K5](../kusshoes-to-rener-vn/WORK_LOG.md) và [kết quả kiểm tài liệu](verification.json).
