# Đọc nguồn địa phương và phản biện đề cương ReNER-VN

Ngày đọc: 09/10/2026. Vai trò: phản biện khoa học, kiểm tra ý nghĩa bài toán và ranh giới kiến trúc. Tài liệu này phân biệt **[Nguồn]** — điều thực sự có trong tài liệu, **[Nhận định]** — kết luận phân tích, và **[Đề xuất]** — phương án chưa được kiểm nghiệm. Số trang dưới đây là trang PDF, đếm từ 1. Không có số liệu thực nghiệm mới trong báo cáo này.

## 1. Nguồn được gửi có sự lệch đề tài

**[Nguồn]** `t07-proposal-quick-guide-VI.pdf` có **13 trang**. Trang 1 ghi “GROUP 7 / PROPOSAL QUICK GUIDE”, nói về vật thể nhỏ có góc xoay trong YOLO; trang 2 trình bày vấn đề gán mẫu, STAL và AI-TOD-R; trang 3–8 hướng dẫn trình bày 18 slide YOLO-OBB. Trang 9 là thuật ngữ object detection; trang 10 hỏi đáp về label assignment; trang 11 là toán hình học lưới; trang 12 là cách tập trình bày; trang 13 đối chiếu bộ 20 slide. Đây là tài liệu ôn thuyết trình cho nghiên cứu thị giác máy tính, **không phải proposal trích xuất bất động sản**.

**[Nguồn]** Ảnh đề tài người dùng gửi lại ghi đề số 8: trích xuất thông tin bất động sản từ bài đăng mạng xã hội, nền tảng Sequence Labeling & Regex, đầu ra bốn trường Giá, Diện tích, Vị trí, Số phòng; mức tối thiểu là bóc tách 10 bài phức tạp bằng regex hoặc prompt LLM. Trong thư mục dự án có `proposal-ReNER-VN-v1.3.pdf`, **9 trang**, khớp ảnh và mục tiêu extension/web của người dùng. Đây là nguồn nội dung chính của bản đọc này.

**[Nhận định]** Phải giữ sự phân biệt này xuyên suốt nghiên cứu. Không lấy YOLO, STAL, AP, AI-TOD-R hay GPU-hour làm nền tảng kỹ thuật cho NER. Phần đáng học từ quick guide là kỷ luật nghiên cứu: phân biệt problem/gap/RQ/hypothesis/objective/contribution ở trang 2; giữ điều kiện đối chứng ở trang 5; pilot trước kế hoạch lớn ở trang 7; không biến kết quả kỳ vọng thành kết quả đã có ở trang 8–10. Đây là nguyên tắc có thể chuyển sang NER, không phải bằng chứng về NER.

**Nguồn gốc:** [Quick guide Nhóm 7](<D:/DEMO kế hoạch kì 5-20260915T034926Z-1-001/DEMO kế hoạch kì 5/DPL302m/NCKH/notes/t07-proposal-quick-guide-VI.pdf>), [ReNER-VN v1.3](<D:/DEMO kế hoạch kì 5-20260915T034926Z-1-001/DEMO kế hoạch kì 5/TMG301/project-realestate-ner/proposal-ReNER-VN-v1.3.pdf>), ảnh đề số 8 người dùng đính kèm. Bản trích chữ đã lưu để truy vết nhưng PDF và ảnh vẫn là nguồn gốc.

## 2. Tôi hiểu chính xác hệ thống dự kiến làm gì

**[Nguồn, v1.3 trang 1–4]** ReNER-VN đã thu hẹp từ bất động sản nói chung sang **cho thuê chỗ ở quanh trường**. Loại hình gồm phòng trọ, chung cư mini, căn hộ dịch vụ, nhà nguyên căn. Phạm vi địa lý là 3–5 phường quanh cơ sở trường chưa được xác định trong đề cương. Mua bán nhà đất, pháp lý nhà, ảnh và định giá giao dịch nằm ngoài phạm vi.

**[Nguồn, trang 5–7]** Extension có hai chế độ. Thu thập đọc bài người dùng gặp khi lướt nhóm, gửi về backend, trích xuất và gộp trùng rồi đưa vào kho. Nhận định xử lý bài người dùng đang quan tâm, tìm nhóm bài tương tự trong kho và trả về so sánh với trung vị. Web là nơi xem bài gốc, các đoạn đã bóc tách, kết quả từng phương pháp, bảng dữ liệu, phân bố giá và đánh giá NLP.

**[Nhận định]** Web “bị động” trong lời người dùng nên hiểu là **backend nhận dữ liệu do tác nhân ngoài gửi vào**. Web không tự nhiên tạo dữ liệu huấn luyện. Extension tạo luồng bài thô; bộ trích xuất biến bài thành bản ghi; người sửa mới tạo nhãn đáng tin. Sau đó, mô hình có thể được huấn luyện ở giai đoạn riêng. Đây là bốn việc khác nhau, tránh gọi tất cả là “training data”.

Một vòng sử dụng hợp lý: sinh viên đọc một tin có giá 5,5 triệu/tháng; extension chỉ ra giá thuê, phí điện, phí nước và cọc; hệ thống tìm các chỗ ở đủ tương tự; trả lời “giá chào này cao hơn trung vị của mẫu đã thu”, kèm nguồn và điều kiện so sánh. Người dùng có thể sửa cách trích xuất hoặc đồng ý đóng góp. Sửa và đóng góp cũng là hai hành động khác nhau: một bản ghi có thể được phân tích riêng nhưng chưa được phép vào kho dùng chung.

**[Nhận định]** Sản phẩm có giá trị trước khi có mô hình định giá. Người dùng nhận được thông tin cấu trúc, phân biệt phí khỏi giá thuê và một tập tin so sánh rõ nguồn. LLM hỗ trợ hiểu văn bản; median/IQR là thống kê; một mô hình hồi quy giá chỉ là bước có thể thêm sau này. Có AI không đồng nghĩa phải dự đoán “giá đúng”.

## 3. Bản đồ proposal v1.3 và các quyết định đã có

| Trang | Nội dung thực sự có | Ý nghĩa và điều cần kiểm chứng |
|---|---|---|
| 1 | Tên, abstract, extension + web, ví dụ CCMN nhiều khoản tiền | Hướng thuê nhà đã nhất quán; ví dụ được ghi là tự tạo |
| 2 | Tổng quan nghiên cứu; khác miền web/Facebook; normalization và ứng dụng | Số liệu được trích từ nguồn khác, không phải kết quả của nhóm; claim thiếu nghiên cứu còn giới hạn theo phạm vi tìm kiếm |
| 3 | RQ1–RQ4 và O1–O6 | Kết nối extraction với thống kê hạ nguồn là câu hỏi có thể đáng nghiên cứu |
| 4 | Phạm vi, 100 gold/300–500 kho, 4 người/4 tuần, rủi ro | Các con số là kế hoạch; chưa có pilot về số nhóm tin tương tự hoặc công gán nhãn |
| 5 | Kiến trúc ba lớp, extension gửi HTML, replay | Hình dễ hiểu; thiếu ranh giới trust, trạng thái công việc và quản trị vòng đời dữ liệu |
| 6 | BIO + FEE, Regex/LLM/Hybrid, normalization, dedup, median/IQR/N | Phân công số cho code tất định tốt; mức tin cậy, comparables và missing price chưa đủ định nghĩa |
| 7 | Hình panel; gold/test/dev; metrics, kappa, room split, RQ4 | Hình là minh hoạ; 10 bài chưa đủ làm bằng chứng paper mạnh; RQ4 phải đo cả lỗi loại bản ghi |
| 8 | Lịch 05/10–01/11/2026, no GPU, 1.000–1.500 API calls, kết quả kỳ vọng | Đây là baseline triển khai đồ án, chưa phải kế hoạch paper hoàn chỉnh |
| 9 | Tài liệu tham khảo | Cần kiểm tra từng claim có thật sự được nguồn hỗ trợ, đặc biệt các hạn chế công trình và thay đổi hành chính |

**[Nguồn, trang 6]** Các bản ghi vào kho khi có đồng ý đóng góp, độ tin cậy cao, giá thuê và vị trí. Tin thiếu diện tích vẫn có thể vào kho nhưng không tham gia giá/m². N tối thiểu 10 là quy tắc thiết kế. Hệ thống trả trung vị, P25–P75, độ mới và ba tin gần nhất. Cách này đúng hướng minh bạch hơn một con số đơn lẻ, nhưng chưa đủ để bảo đảm tính đại diện.

## 4. Lõi khoa học: đây là extraction có ngữ nghĩa

**[Nhận định]** “NER bất động sản” là tên thuận tiện; phần việc thực tế rộng hơn nhận dạng tên riêng. Giá và diện tích là biểu thức định lượng; phòng là thuộc tính; vị trí có thể là tên địa danh hoặc quan hệ “gần trường”; mỗi giá trị còn phải gắn đúng căn/phòng trong bài. Do đó cần ít nhất: phân loại intent, nhận dạng span, phân loại vai trò, chuẩn hoá và liên kết theo listing. BIO thể hiện span nhưng không tự giải quyết quan hệ này.

Ví dụ tự tạo: “Cần tìm phòng dưới 4tr. Bạn mình cho thuê 25m2 giá 3tr2, cọc 1 tháng.” Bắt được “4tr” và “3tr2” vẫn chưa hiểu đúng. Số đầu là ngân sách của người tìm; số sau mới là giá chào một tin cho thuê. Ví dụ “phòng A 20m2 2tr8; phòng B 30m2 3tr5” cần hai bản ghi, không ghép giá của A với diện tích B. Khi không chắc cách liên kết, trả trạng thái cần xem hợp lý hơn ép thành một hàng hoàn chỉnh.

**[Nguồn, trang 6]** LLM chỉ xác định đoạn văn và loại; code tất định quy đổi số. Đây là thiết kế tốt vì tách được lỗi tìm span khỏi lỗi tính toán. Tuy nhiên exact substring chỉ chứng minh đoạn chữ tồn tại. LLM vẫn có thể gán “100k/người” thành giá thuê dù nó là giá nước. Nó cũng có thể chọn đúng số nhưng gắn sai phòng. Grounding giảm một lớp bịa, không chứng minh toàn bộ bản ghi đúng.

**[Đề xuất]** Mỗi giá trị cần `raw_text`, `start`, `end`, `entity_type`, `semantic_role`, giá trị chuẩn và phiên bản quy tắc. Nếu cùng chuỗi xuất hiện nhiều lần, quote đơn lẻ chưa đủ định vị; offsets hoặc cách chọn occurrence phải rõ. Giữ văn bản chuẩn làm căn cứ và ánh xạ offset khi tiền xử lý. Không xoá emoji, xuống dòng hoặc viết tắt đến mức mất thông tin phân tách listing.

**[Nhận định]** Câu “regex chính là cách mã hoá thủ công các đặc trưng mà CRF học được” (trang 6) chỉ là ví von. CRF học trọng số từ nhãn và mô hình hoá phụ thuộc chuỗi; regex áp quy tắc xác định. Nên viết “cả hai có thể sử dụng tín hiệu hình thức và ngữ cảnh, nhưng cơ chế suy luận khác nhau”. BIO do regex hoặc LLM tạo không có nghĩa nhóm đã huấn luyện sequence-labeling model.

## 5. Giá sàn, giá chào và dữ liệu thiếu giá

**[Nhận định]** “Giá sàn” dễ làm lệch cả paper lẫn UI. Giá thấp nhất trong mẫu có thể là tin mồi, phòng rất khác, giá theo người, giá ưu đãi tháng đầu hoặc lỗi parser. P25 là phân vị 25% của mẫu, không phải sàn pháp lý, mức giao dịch tối thiểu hay chi phí hợp lý. Trung vị cũng chỉ mô tả mẫu giá chào trong điều kiện chọn dữ liệu.

**[Đề xuất]** MVP nên gọi kết quả là **“tham chiếu giá chào thuê trong dữ liệu đã thu”**. Có thể hiện P25/median/P75, N đơn vị cho thuê riêng biệt, thời gian, tiêu chí nhóm và trạng thái chất lượng. Tách ba khái niệm: giá chào trên bài đăng; giá thoả thuận thực tế; chi phí ở mỗi tháng sau phí. Nguồn hiện tại chủ yếu hỗ trợ khái niệm đầu, chưa có giá giao dịch hay chứng cứ giao dịch.

Quan sát của người dùng “nhà đẹp không để giá, trọ thì bắt buộc công khai giá” đáng dùng làm **giả thuyết hành vi công bố**, chưa phải quy luật được chứng minh hoặc quy định pháp lý. Có thể phòng giá cao thường giấu giá; cũng có thể người đăng bỏ giá vì văn phong hoặc muốn inbox. Không được suy từ không có giá sang giá cao, nhà đẹp hoặc tin xấu. Không được cho LLM tự điền một con số rồi lưu chung với số quan sát.

**[Đề xuất]** Gán trạng thái giá: nêu rõ một số; nêu khoảng; theo người; theo thời hạn khác tháng; “inbox/thỏa thuận”; không đề cập; mâu thuẫn. Lưu trạng thái cho cả tin chưa đủ điều kiện thống kê. Khi chỉ tin có giá vào kho, báo tỷ lệ công khai giá theo nhóm và nguồn. Nếu thiếu giá liên quan đến loại hình hoặc chất lượng, mẫu hoàn chỉnh có thiên lệch; nhiều dữ liệu cùng thiên lệch không tự chữa được vấn đề.

Một tin “2tr/người, ở 2 người” không chắc là phòng 4 triệu: cần xác nhận đó là giá theo đầu người và quy tắc áp dụng. Cọc một tháng là dòng tiền đầu vào, không phải chi phí thuê tháng mới; điện 3.500 đồng/số cần mức tiêu thụ mới quy thành chi phí tháng. Chỉ nên tính tổng khi giả định được hiện rõ; không biến suy luận thành số từ bài.

## 6. Những điểm tốt nên giữ

**[Nhận định]** Thứ nhất, thu hẹp thuê nhà quanh trường giúp dữ liệu có mục đích rõ hơn bất động sản cả nước. Thứ hai, FEE khiến lỗi giá/điện/nước/cọc trở thành đối tượng đo được. Thứ ba, tách LLM nhận dạng khỏi code số giúp kiểm chứng từng tầng. Thứ tư, hệ so sánh Regex/LLM/Hybrid tránh demo chỉ gọi một API. Thứ năm, lưu nguồn, timestamp và phiên bản extractor phục vụ tái lập. Thứ sáu, gộp bài trùng trước thống kê và tách tập theo phòng là nhận thức đúng về đơn vị dữ liệu. Thứ bảy, công nhận số trong hình là minh hoạ và không đặt trước F1 giúp giữ tính trung thực. Thứ tám, RQ4 hỏi lỗi NLP ảnh hưởng ứng dụng bao nhiêu, nối nghiên cứu với ích lợi thật.

Những ưu điểm này là **đặc tính kế hoạch**, chưa là chất lượng triển khai đã được chứng minh. Giữ chúng bằng đặc tả, fixture và đánh giá, không chỉ giữ trong hình kiến trúc.

## 7. Các lỗi trọng yếu cần sửa trước khi triển khai hoặc viết paper

### 7.1 Mức tin cậy đang là heuristic

**[Nguồn, trang 6]** Hai nguồn khớp -> cao; một nguồn -> trung bình; lệch -> thấp. **[Nhận định]** Hai bộ trích xuất có thể cùng sai vì cùng mẫu few-shot, cùng lexicon hoặc cùng ambiguity. Agreement không phải xác suất đúng. Nếu high confidence mới vào kho, filter này còn làm thay đổi cơ cấu mẫu: bài sạch dễ đọc được giữ, bài khó bị loại.

**[Đề xuất]** Ban đầu gọi đó là “trạng thái đồng thuận”, kèm evidence và cờ lỗi. Đo precision, recall và coverage cho từng trạng thái trên gold dev. Chỉ diễn giải thành confidence khi có bằng chứng hiệu chuẩn. So sánh không nên chỉ hỏi F1 của hybrid có tăng không, mà còn hỏi hệ bỏ qua bao nhiêu bài và có ưu tiên loại bỏ loại tin nào.

### 7.2 Comparables đang thiếu feature đáng tin

**[Nguồn]** Phạm vi trang 4 loại “tiện ích” khỏi phạm vi; nhóm tương tự trang 6 lại dùng nội thất. **[Nhận định]** Đây là chỗ cần thống nhất. Nếu không trích xuất nội thất hoặc người không xác nhận, bộ chọn comparables không thể dùng nó như thuộc tính đã biết. “Gần ĐH FPT” cũng chưa xác định phường, bán kính hoặc cơ sở. Nhà nguyên căn và trọ, phòng gác lửng và căn hộ, giá theo người và theo đơn vị thuê phải tách.

**[Đề xuất]** MVP chỉ dùng những feature thật sự quan sát được, ưu tiên cùng loại đơn vị thuê, khu vực đủ xác định, thời hạn và basis giá; sau đó diện tích nếu có. Nếu thiếu feature, hiển thị mức so sánh thô hơn. N=10 chỉ là guardrail cho mẫu quá nhỏ; mười căn rất khác nhau vẫn không trở thành nhóm tốt. P25–P75 mô tả độ phân tán của giá, không phải khoảng tin cậy của median hoặc interval dự báo cho căn đang xem.

### 7.3 Nhãn “cùng phòng” chưa có căn cứ identity

**[Nguồn, trang 6]** TF-IDF + cosine kết hợp vị trí, diện tích, giá dùng gộp trùng. **[Nhận định]** Nhiều phòng trong cùng toà có mô tả mẫu giống nhau; một phòng đổi giá có thể giống kém hơn; môi giới thay câu chữ vẫn là cùng phòng. Vì vậy tương đồng text là bằng chứng hỗ trợ, không phải ID tài sản. Merge sai gây đếm thiếu và mất sự đa dạng; không merge được gây đếm lặp và tăng N giả.

**[Đề xuất]** Tách same-post, likely-repost, same-rental-unit và uncertain cluster. Chỉ same-post có ID/link mới xử lý chắc. Giữ lịch sử các observations và version của cluster; không xoá bài nguồn khi merge. Đánh giá pairwise precision/recall và kiểm tra ảnh hưởng của false merge/nonmerge lên thống kê. Khi identity chưa chắc, báo N observations và N clusters khác nhau thay vì gọi mọi cluster là “căn”.

### 7.4 Ranh giới thu thập và riêng tư chưa được chứng minh

**[Nguồn, trang 4–5]** Proposal nói dữ liệu chỉ nội bộ, người dùng đồng ý đóng góp, ẩn số điện thoại, không lưu tên; extension gửi HTML thô và lưu replay. **[Nhận định]** Đồng ý của người dùng extension không tự xác lập quyền cho mọi dữ liệu của người đăng. HTML thô có thể chứa tên, định danh, comment, link ảnh hoặc thuộc tính DOM ngay cả khi văn bản hiển thị đã ẩn SĐT. Dừng ở checkpoint chỉ là giới hạn vận hành, chưa giải quyết quyền thu thập.

**[Đề xuất]** Đặc tả payload tối thiểu và làm sạch sớm trên máy người dùng. Lưu dữ liệu thô, nguồn, dữ liệu ẩn danh và analytics theo quyền khác nhau; đặt thời hạn lưu và khả năng rút đóng góp. Với replay, dùng fixture đã làm sạch. Nếu gửi text cho API LLM, xác định chính xác dữ liệu nào rời máy và lưu ở đâu. Không kết luận “phù hợp luật” chỉ từ vài biện pháp kỹ thuật; nguồn pháp lý và điều khoản cần đánh giá riêng trong báo cáo evidence.

### 7.5 Tập kiểm thử 10 bài là showcase

**[Nguồn, trang 7]** Khoảng 100 gold, 10 complex test, 90 dev; hai người gán chéo 20 bài và kappa; test theo phòng. **[Nhận định]** Mười bài phù hợp mức tối thiểu đồ án nhưng quá ít để kết luận mạnh về sự hơn kém giữa hệ thống, nhất là chia tiếp theo PRICE/AREA/LOC/ROOM/FEE và nhiều loại khó. Một bài có thể chứa nhiều entities, nhưng entities cùng bài không phải mẫu độc lập. Kappa trên token với rất nhiều O có thể cao dù biên entity và normalization chưa tốt.

**[Đề xuất]** Giữ 10 bài để trình diễn; mở tập đánh giá riêng có kích thước dựa trên pilot và lượng entities/missing fields. Gán nhãn theo guideline, giải quyết bất đồng, đo agreement mức span và mức giá trị ngoài chỉ số kappa nếu dùng. Tách theo cluster tài sản trước, thêm test theo thời gian hoặc nhóm Facebook nếu muốn claim chuyển miền. Tập test có nhiều bài không công khai giá để đo false filling; báo correct-null cùng false-positive rate và coverage, tránh hệ trả rỗng mọi nơi có điểm đẹp.

### 7.6 RQ4 phải đo pipeline, không chỉ số giá trên survivors

So median gold với median extracted trên cùng các bài có giá đúng chỉ đo một phần lỗi. Bản ghi nhầm khu, thiếu giá, sai loại phòng, sai dedup hoặc bị low confidence loại bỏ đều có thể làm thay đổi median. Hai sai sót có thể triệt tiêu khiến median ít lệch nhưng từng bản ghi vẫn sai.

**[Đề xuất]** Báo ít nhất ba tầng: ảnh hưởng riêng của giá/normalization trên cùng nhóm gold; ảnh hưởng của phân nhóm và missingness; ảnh hưởng đầy đủ của filter + dedup + extraction. Nêu số nhóm đủ mẫu, số bản ghi bị mất và tỷ lệ bài đổi kết luận so sánh. Với các nhóm quá nhỏ, chỉ mô tả case study và uncertainty, không dựng xu hướng toàn thị trường.

## 8. Paper cần một câu hỏi chính

**[Nhận định]** Đề cương hiện là đồ án có chiều sâu, chưa là một đóng góp paper được xác lập. Sổ `claims-ledger.md` đang xếp recipe/T1 và chưa nhắm venue; đó là cách diễn giải thận trọng đúng. Extension, web đẹp, hybrid và biểu đồ không tự thành novelty. Không có kết quả thực nghiệm tại các nguồn đã đọc; cũng chưa có baseline CRF/PhoBERT trong phạm vi v1.3.

**[Đề xuất]** Câu hỏi trung tâm tốt nhất: **“Trong tin cho thuê tiếng Việt nhiễu, trích xuất có neo nguồn và kiểm tra vai trò số tiền giảm lỗi chuẩn hoá và sai lệch so sánh giá đến đâu, với chi phí/coverage thế nào?”** Đóng góp dự kiến có thể là dataset + guideline thực tế, benchmark công bằng và evidence về propagation của lỗi. Điều này kiểm chứng được; không cần tự nhận mô hình mới.

Thí nghiệm cần Regex; LLM không grounding; LLM grounding; hybrid với cùng normalizer; rồi ablation semantic fee checks và confidence filter. Nếu hybrid chỉ gọi LLM khi regex yếu, phải tách **đánh giá mọi hệ trên cùng gold** khỏi **routing tối ưu chi phí**. Giữ prompt, model/version, decoding, cache và normalization rõ. Chi phí/latency phải đo thật trên thiết bị/điều kiện cố định. Không hứa fine-tune sẽ tốt hơn hoặc vài trăm nhãn bảo đảm có paper.

## 9. Trình tự thực dụng sau khi đọc

**[Đề xuất]** Gate đầu tiên là dữ liệu, không phải dựng dashboard: lấy một pilot nhỏ đa dạng, viết guideline, đo tỷ lệ đủ giá/vị trí/diện tích, lượng bài đăng lại và số nhóm comparables thật sự đủ. Nếu N hiệu dụng không đạt, thu hẹp loại hình/khu thay vì tự suy giá thiếu.

Gate thứ hai là extraction: hoàn thiện schema + Regex baseline và evaluation trước; sau đó thêm grounded LLM và hybrid. Gate thứ ba là analytics: kiểm tra basis giá, cluster identity và comparables bằng mẫu người duyệt; chỉ mở panel nhận định khi nguồn đủ. Gate thứ tư là đóng băng thí nghiệm và viết paper theo bằng chứng. Web có thể dựng song song một màn nhập/trích xuất với dữ liệu thật, nhưng dữ liệu minh hoạ phải gắn nhãn rõ.

Lịch 4 tuần, no GPU và miễn phí trong v1.3 là kế hoạch cho demo môn học; paper cần thời gian thu/gán nhãn/kiểm tra literature và lặp thí nghiệm riêng. Ước lượng 5–8 giờ cho 100 bài phải tính cả annotation guideline, double-label, reconciliation và lỗi nhiều listing; pilot 10–20 bài mới cho năng suất đáng tin. 1.000–1.500 API calls và dung lượng <1 GB cũng cần kiểm chứng nếu giữ HTML replay hoặc chạy nhiều ablation.

## 10. Các câu nhóm phải trả lời được khi bảo vệ

1. Đơn vị nghiên cứu là bài đăng, listing hay đơn vị thuê? Khi một bài có ba phòng, output và split làm gì?
2. Giá được công bố theo tháng, người hay cả căn? Làm sao không trộn phí nước với tiền thuê?
3. Hệ thống biết trường bị ẩn giá hay chỉ không tìm thấy? LLM trả rỗng có được chấm riêng không?
4. Quote tồn tại có chứng minh vai trò semantic đúng không? Hybrid disagreement xử lý ra sao?
5. N trong panel là bài, người đăng hay căn đã dedup? Tại sao các căn đó tương tự?
6. IQR biểu thị phân bố của mẫu hay độ tin cậy của dự đoán? “Cao hơn 10%” có nghĩa gì nếu loại phòng khác nhau?
7. Việc chỉ giữ high confidence làm mẫu lệch thế nào? Nhóm có đo những bài bị loại không?
8. Khi người dùng sửa/đóng góp, bản sửa được kiểm duyệt và version ra sao? Có làm thay đổi tập test đã đóng băng không?
9. Claim mới nhất là điều đã được literature search loại trừ hay chỉ chưa thấy trong các nguồn đã đọc?
10. Nếu grounded hybrid không hơn LLM, kết quả nào vẫn trả lời được câu hỏi nghiên cứu?

**Kết luận đọc nguồn:** mục tiêu nhất quán khả thi là nền tảng trích xuất và tham chiếu **giá chào thuê**, nhận bài do extension đóng góp, có bằng chứng nguồn và vòng sửa nhãn. Những bước chưa được chứng minh là chất lượng dữ liệu, confidence, comparables, dedup, quyền thu thập và hiệu quả khoa học. Hãy dùng proposal v1.3 làm kế hoạch đồ án ban đầu, nâng thiết kế đánh giá để phục vụ paper; dùng quick guide YOLO chỉ như mẫu cách tư duy/thuyết trình nghiên cứu.

### Tài liệu địa phương đã đọc

- `t07-proposal-quick-guide-VI.pdf`, đủ 13 trang, nguồn user gửi; nội dung YOLO-OBB/STAL.
- `proposal-ReNER-VN-v1.3.pdf`, đủ 9 trang; đọc chữ toàn bộ, kiểm tra trực quan hình kiến trúc trang 5 và panel trang 7 bằng ảnh nhúng gốc PDF.
- `notes/01-research-report.md`, nguồn lịch sử nghiên cứu vòng 1 ngày 03/10/2026; có phạm vi cũ mua/bán và Playwright, không dùng thay trạng thái v1.3.
- `notes/02-proposal-v1.2-change-audit.md`, dấu vết chuyển sang thuê nhà + extension + kho giá, các điểm từng được đề xuất.
- `notes/claims-ledger.md`, C-1, novelty recipe/T1 và chưa chọn venue. Các điều kiện số lượng dataset trong ledger là gợi ý nâng đồ án, không phải tiêu chuẩn chấp nhận paper.
