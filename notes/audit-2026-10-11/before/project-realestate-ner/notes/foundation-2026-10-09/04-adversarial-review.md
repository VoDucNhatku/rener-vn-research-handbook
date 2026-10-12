# Phản biện độc lập bản nền tảng ReNER-VN

Ngày: 09/10/2026. Đối tượng: `KIEN-THUC-NEN-TANG-RENER-VN.md` (30 mục tại thời điểm đọc), đối chiếu `02-research-evidence.md`, `03-system-architecture.md` và proposal v1.3. Vai trò: giáo sư phản biện cấu trúc nhiệm vụ, thí nghiệm và khả năng chuyển từ nghiên cứu thành sản phẩm. Không sửa các file được phản biện.

**Verdict có điều kiện:** tài liệu đủ tốt để làm bản định hướng và học nền tảng; chưa nên dùng như schema chuẩn hoặc protocol thí nghiệm đã đóng băng. Ba vấn đề cần sửa trước triển khai/gán nhãn diện rộng là trạng thái giá, định nghĩa đơn vị đo và phạm vi phép đo downstream. Hai vấn đề tiếp theo cần sửa trước claim ablation hoặc generalization. Chưa có kết quả thực nghiệm, dữ liệu gold mới hay hệ thống runnable để đánh giá hiệu quả thực tế.

Đây là phản biện **bản thiết kế**, không kết luận code đang có các lỗi dưới đây. Các con số ví dụ trong review là giả định để minh hoạ, không phải dữ liệu dự án.

## 1. [P1] Trạng thái nguồn và quyết định của extractor chưa tách rõ; ba schema chưa thống nhất

**Đoạn cần sửa:** main §10–11, đặc biệt enum `price.visibility` (`ambiguous`: “có biểu thức tiền nhưng chưa xác định được giá chính”); architecture §6 và ví dụ B ở §14; evidence §3 bảng trạng thái giá. Main dùng `disclosed/hidden_explicit/missing/negotiable_only/ambiguous/not_applicable`; architecture dùng `explicit/range/starting_from/negotiable_without_amount/not_stated/ambiguous/image_only_unread/not_applicable`. Trong ví dụ B, “inbox nhận giá” được chuyển thành `negotiable_without_amount`, trong khi main xác định đúng đó là `hidden_explicit`.

**Vì sao ảnh hưởng khoa học:** “nguồn có giá mơ hồ” khác “model không giải được giá rõ ràng”. Nếu cả hai cùng là `ambiguous`, model có thể đẩy lỗi của mình thành đặc tính gold của bài. Một tin rõ “3tr5/th” nhưng parser yếu không được biến thành nguồn mơ hồ. Macro-F1 về visibility và tỷ lệ công khai giá sẽ không còn đo một nhiệm vụ độc lập. “Range” hay “starting_from” là dạng của giá đã công bố, không phải mức độ công khai; nên không trộn cùng enum với “missing”.

**Vì sao ảnh hưởng sản phẩm:** `inbox giá` không có nghĩa người đăng chấp nhận thương lượng; người dùng sẽ thấy lời diễn giải sai. Đồng bộ web/extension/backend bằng enum khác nhau dễ làm một bản ghi được lọc khác giữa nơi nhập và dashboard. Giá chỉ trên ảnh là nguồn **chưa quan sát đầy đủ**, không thể coi như chắc chắn không đề cập giá khi MVP chỉ đọc text.

**Cách sửa đề xuất:** dùng một schema chuẩn với các chiều độc lập:

- `source_price_state`: `disclosed/hidden_explicit/not_stated/negotiable_only/source_ambiguous/not_applicable`, do gold guideline xác định trên phần nguồn có quyền đọc.
- `amount_form`: `exact/range/starting_from/none`; số chuẩn và period/basis riêng.
- `extraction_decision`: `answered/abstained/needs_review/failed`; `abstention_reason` ghi vì lỗi mô hình, thiếu ngữ cảnh, nguồn mơ hồ, chưa đọc ảnh hay không đủ bằng chứng.
- `input_modality_coverage`: mô tả phần text/ảnh/comments đã thực sự có trong đầu vào; không suy toàn bài từ text thiếu.

`source_ambiguous` chỉ dùng khi chính nguồn không giải quyết được theo guideline, có ví dụ/adjudication; `abstained` là trạng thái hệ thống. Tạo bảng mapping ba tài liệu về enum chuẩn và sửa ví dụ B thành `hidden_explicit`. Mọi threshold, payload, UI và scorer dùng cùng schema version. Đây là giải pháp thiết kế; tên enum cuối có thể đổi, các chiều ngữ nghĩa cần giữ.

## 2. [P1] Đơn vị coverage và hai tỷ lệ “unsupported” chưa đủ cụ thể để so sánh công bằng

**Đoạn cần sửa:** main §10 công thức coverage, §17 bảng metric/công thức unsupported-fill; evidence §8 `Unsupported-value rate`; architecture §5–7 về multi-listing và validator.

Main định nghĩa coverage là “số quyết định hệ thống trả lời / số quyết định cần đánh giá”, nhưng chưa chốt một quyết định là một field trên gold listing, một predicted field, hay cả record. Main `Unsupported-fill rate` dùng mẫu số số listing gold không có giá số; evidence `Unsupported-value rate` dùng mẫu số tất cả giá trị được xuất. **Hai tỷ lệ này có thể đều hữu ích và công thức không tự sai, nhưng là hai estimand khác nhau**, không được gọi thay thế nhau trong bảng kết quả.

**Vì sao ảnh hưởng khoa học:** câu hỏi chính yêu cầu “cùng coverage”. Nếu hệ A tách một bài thành 2 listing, hệ B thành 1, denominator tự lấy theo output sẽ khác. Nếu `null` đúng vì source missing bị tính như model abstention, hệ trả lời đúng trạng thái thiếu sẽ có coverage thấp một cách sai lệch. Nếu FP listing không được phạt, model có thể sinh thêm bản ghi rồi trông như phủ nhiều hơn.

**Ví dụ minh hoạ:** 100 listing gold có 20 listing không có giá số; hệ điền sai 2 trong nhóm đó và xuất tổng cộng 80 giá số. False-fill trên nonnumeric gold là 2/20=10%; unsupported trên numeric outputs là 2/80=2,5% nếu hai output đó là toàn bộ output unsupported. Không thể dùng 2,5% để tuyên bố chỉ 2,5% tin giấu/thiếu giá bị tự điền.

**Cách sửa đề xuất:**

1. Chốt gold units: listing identity/mention được match với prediction theo protocol cố định; field decision là cặp `(gold_listing, field)`. Báo unmatched predicted listings qua precision/record hallucination riêng.
2. Tách coverage của **phân loại source state**, coverage của **trả numeric value khi có bài toán numeric**, và coverage của **record đủ điều kiện analytics**. `not_stated` đúng là một câu trả lời source-state, không phải abstention.
3. Đặt tên riêng: `false_numeric_fill_on_nonnumeric_gold` với mẫu số nhóm gold thích hợp; `unsupported_output_fraction` với mẫu số outputs; phân biệt evidence không tồn tại, role sai, unit sai và association sai trong error audit.
4. Với giá nguồn mơ hồ, chốt trước gold set chấp nhận được hoặc đánh giá riêng; không âm thầm tính mọi giá numeric là FP chỉ vì model/gold đang khác cách diễn giải.
5. Risk–coverage phải ghi risk theo loss nào và không thay unit giữa các hệ. Bảng paired evaluation nên giữ nguyên denominator gold và báo supports/abstentions/errors.

## 3. [P1] RQ-C hiện đo lỗi giá trị có điều kiện, chưa đo sai lệch toàn bộ chức năng so sánh

**Đoạn cần sửa:** main §15 RQ-C (“giữ nguyên tập listing và nhóm so sánh”), §17 `Downstream distortion` (“so cùng tập/filter”); đối chiếu architecture §8–10 vì sản phẩm có eligibility, dedup, identity, freshness và comparables trước snapshot.

**Vì sao ảnh hưởng khoa học:** giữ membership và filter gold cố định là phép đo tốt để cô lập lỗi normalization/value. Tuy nhiên khi triển khai, extractor còn có thể làm sai intent/khu/loại hình, bỏ bài thiếu price/location, đổi cluster hoặc confidence khiến bản ghi không được vào kho. Các lỗi này quyết định N và các căn được so. Chỉ phép đo có điều kiện có thể kết luận “median ít lệch”, trong khi chức năng sản phẩm trả nhóm sai hoặc từ chối nhiều hơn.

**Ví dụ minh hoạ:** một nhóm gold có 10 căn đủ điều kiện; pipeline làm mất 2 vì location sai. So median trên 8 căn giữ lại có thể thấy sai số giá nhỏ, nhưng rule N≥10 đã khiến hệ không trả nhận định. Câu hỏi user-facing là cả **có so sánh được không và so đúng nhóm không**, chưa được phép đo median có điều kiện giải quyết.

**Cách sửa đề xuất:** giữ RQ-C hiện tại làm tầng thứ nhất, đặt tên rõ “distortion do value extraction trên nhóm gold cố định”; thêm hai tầng:

- Tầng grouping/eligibility: cùng corpus gold, chạy labels/filter hệ để đo N thay đổi, group membership thay đổi, exclusion reasons và composition drift.
- Tầng end-to-end: extraction + eligibility + dedup + comparables + gate cùng chạy; báo sai lệch median khi cả hai có output, tỷ lệ mất/đổi nhóm, tỷ lệ đổi quyết định abstain và tỷ lệ đổi câu so sánh. Báo cả các case chỉ gold đủ mẫu nhưng hệ không đủ, không chỉ survivors.

Mọi tầng cần cùng corpus thời điểm và version policy; không đổ biến động mẫu do dữ liệu mới vào lỗi extraction. Đây là phép phân rã nguyên nhân, không bắt buộc MVP làm hết trước demo. Nếu chưa làm tầng đầy đủ, phải giới hạn claim đúng tầng đã đo.

## 4. [P2] Ablation bỏ visibility states có thể tự tạo kết quả “thắng” vì thu hẹp không gian nhãn

**Đoạn cần sửa:** main §18 “bỏ visibility states hoặc quy về null đơn giản”, evidence §6 ablation “bỏ nhãn trạng thái thiếu giá để đo ảnh hưởng trên withheld/not_stated”; đối chiếu main §9 “cùng schema chấm điểm” và §17 visibility macro-F1/record exact match.

**Vì sao ảnh hưởng khoa học:** nếu một arm bị thiết kế không có khả năng xuất hidden/missing/ambiguous rồi bị chấm full-state F1, nó thua theo định nghĩa biểu diễn. Kết quả đó chứng minh schema phong phú biểu diễn được nhiều lớp hơn, chưa chứng minh module giúp trích numeric đúng hơn, giảm unsupported fill hay tăng hữu dụng. Record exact match gồm state cũng có cùng rủi ro nếu baseline không có vocabulary cần thiết.

**Cách sửa đề xuất:** chốt output contract mà mọi baseline **có thể** đạt, còn cơ chế sử dụng visibility là yếu tố can thiệp. Hoặc chia rõ thí nghiệm representation: full schema vs collapsed schema, chỉ so outcome chung (numeric correctness, false fill, coverage, lỗi comparables); full-state F1 của collapsed arm ghi không áp dụng hoặc là chẩn đoán giới hạn biểu diễn, không làm bằng chứng cho hiệu quả NLP. Giữ normalization và trường đầu ra chung cho ablation grounding/role resolution. Báo budget/call counts để hybrid nhiều call không được nhận toàn bộ lợi ích như chỉ do validator.

## 5. [P2] Cluster tài sản và cluster template nên là hai chiều split riêng

**Đoạn cần sửa:** main §16 “xác định cluster tài sản/template… Cluster không bị tách giữa train và test”; đối chiếu architecture §9 đã phân biệt `same_property`, `same_template`, `uncertain`.

**Vì sao ảnh hưởng khoa học:** cùng template môi giới không đồng nghĩa cùng căn. Một template phổ biến có thể nối một thành phần rất lớn của corpus; gộp chung bằng connected components sẽ làm split mất cân bằng hoặc đánh giá thành bài toán “template chưa thấy” mà không nói. Ngược lại, chỉ bỏ exact duplicate chưa ngăn cùng phòng đổi câu chữ lọt hai tập. Mục tiêu holdout tài sản và holdout cách viết cần tách.

**Cách sửa đề xuất:** split chống duplicate/property leakage dựa trên quan hệ tài sản hoặc repost đã có căn cứ. Lưu `template_group` như một thuộc tính khác, audit tỷ lệ overlap và có **template holdout** riêng nếu muốn đo robustness với văn phong mới. Không merge các căn thành cùng entity chỉ để tiện split. Nếu identity không chắc, giữ conservative leak-risk groups và công bố trade-off, không gọi chúng là căn đã xác nhận. Báo số groups và size distribution để phát hiện component quá lớn.

## 6. Những ranh giới đã được xử lý đúng, không nên flag lại

- **Mismatch tài liệu:** main §2 đã nêu rõ quick guide 13 trang là YOLO và ReNER v1.3 9 trang khớp ảnh. Không áp AP/STAL vào NER; bản đọc nguồn có page anchors.
- **Giấu giá và selection bias:** main §6/19 và evidence đã giữ quan sát user thành giả thuyết, không biến thành quy luật hoặc pháp luật; không lấp predicted price vào observed label; phân biệt public-price sample với toàn nguồn.
- **Chưa runnable:** main mở đầu và §15 nói rõ thiết kế chưa có data/model/website chạy; architecture cũng ghi proposed, không xác nhận các acceptance checks đã đạt. Review không phạt tài liệu chỉ vì chưa viết code, nhưng verdict triển khai phải có Phase 0.
- **Nguồn gốc toán:** các tỷ số đếm và diện tích ở main được ghi `[derived]` và có boundary/unit checks; quantile conditional ở evidence ghi `[thiết kế]`. Conformal được gắn giả định và nguồn, IQR không bị gọi CI. Không thấy công thức kết quả mới giả làm thực nghiệm. Vấn đề cần sửa là **estimand/denominator**, không phải đòi trích một paper cho phép chia đếm.
- **Không hứa Q1/venue:** main Venue Claim Card giữ T1 tạm thời, chưa chọn venue; evidence nói không “first/SOTA/Q1 guarantee”. Hướng paper và điều kiện công bố được trình bày thận trọng.
- **Bibliography đang bổ sung:** không flag thiếu appendix khi claim đã có nguồn tại evidence và tài liệu chính còn đang tổng hợp. Trước phát hành nên giữ danh mục nguồn/version/mức đọc, nhưng đây không phải blocker phát hiện chỉ vì appendix chưa hoàn tất.
- **Quyền nguồn:** architecture phân biệt `activeTab`, quyền platform và quyền người đăng; không tự kết luận Facebook thu thập hợp lệ từ quy mô nhỏ hoặc consent người dùng. Các URL Meta bị chặn được ghi giới hạn đọc rõ.

## 7. Điều kiện thông qua

Thông qua **bản báo cáo nền tảng** sau khi sửa ba P1 hoặc ghi rõ các phần ấy là open design decisions; thống nhất enum và metric phải đứng trước việc sinh schema/code/gold. Cho phép bắt đầu pilot từ nguồn được phép, guideline và Regex baseline ngay; chưa khóa scientific protocol và chưa quảng bá chức năng định giá.

Để thông qua **paper thực nghiệm**, cần dataset có quyền dùng/gán nhãn độc lập, split và scorer khóa, outputs thực, budget/version logs và claim đúng phạm vi phép đo. Để thông qua **sản phẩm dùng ngoài nhóm**, cần chứng cứ vertical slice thực thi được, behavior retry/error/deletion/review/source gate đã kiểm tra, và comparables có snapshot tái lập. Không có số lượng data hoặc giao diện đẹp nào thay các bằng chứng đó.

### Snapshot tài liệu đã phản biện

SHA-256 tại thời điểm đọc, để phân biệt với bản được tác giả sửa sau review:

| File | SHA-256 |
|---|---|
| `KIEN-THUC-NEN-TANG-RENER-VN.md` | `D7D0DEE6DA64E694AB191EBF9941765AF8478FB5E9D7ED11585B161DAAD5480C` |
| `02-research-evidence.md` | `823BAE73A162396CC9199F943184343AB4CDAA2FC864E4741C1FB27A9256B62D` |
| `03-system-architecture.md` | `F5BE29C283C2BD814FC31DAD233AEF9222D1C6D3A5958313FF2AF656C4B566E8` |

Review bám section anchors vì main đang bổ sung bibliography; line numbers có thể thay đổi sau sửa. Không nâng finding chỉ vì một tài liệu dùng tên minh hoạ khác; các P1 nêu khác biệt ngữ nghĩa sẽ ảnh hưởng trực tiếp annotation và scoring.

## 8. Re-scan các đoạn đã sửa theo hallucination-guard

Đã đọc lại **các đoạn thay đổi**, không chấm lại toàn bộ bản cũ: main §11, §15–18, §31–32; đối chiếu `BAO-CAO-HIEU-DE-TAI.md` và kiểm tra vật lý sổ `notes/claims-ledger.md`. Quy trình áp dụng từ [hallucination-guard/SKILL.md](C:/Users/Asus/.codex/skills/hallucination-guard/SKILL.md): đọc lại spans sau sửa, phân biệt claim nguồn và design, không xác nhận runs chưa thực hiện. Main tại lúc re-scan có SHA-256 `B43A3AE2883439AA2DF9C1F96DC0A03CDE7ED1293148B3D5A84E8F46291C827F`; bản sau này có thể tiếp tục cập nhật bibliography/artifact.

| Finding ban đầu | Trạng thái sau sửa | Bằng chứng trực tiếp | Giới hạn còn lại |
|---|---|---|---|
| 1. Source state trộn extraction state; schema khác nhau | **Resolved ở mức thiết kế** | §11 giới hạn visibility vào nội dung nguồn; source ambiguous không do model yếu; tách capture/unread media/extraction; expression kind và negotiability riêng; inbox→hidden_explicit; canonical override note worker | Chưa có JSON Schema chạy được, guideline adjudication hay offset fixtures để kiểm tra thực thi |
| 2. Coverage/unsupported chưa chốt universe | **Resolved ở mức thiết kế** | §17 chốt cặp listing–field theo manifest; visibility chỉ input đủ, numeric coverage trên gold có numeric price; trả hidden đúng là answered visibility; unsupported-value và unsupported-fill có mẫu số riêng | Trước benchmark cần chốt record matching, loss risk và treatment unmatched/ambiguous cụ thể trong scorer; đây là chi tiết triển khai protocol, không còn mâu thuẫn khái niệm gây blocker báo cáo |
| 3. Downstream chỉ kiểm value lỗi trên survivors | **Resolved ở mức thiết kế** | §15 RQ-C mở rộng; §17 có controlled-value và full-pipeline test, latter chạy eligibility/grouping/dedup, báo N/inclusion/exclusion/group/cluster/distortion/abstain | Chưa có gold snapshots và full-pipeline runs; không kết luận đã giảm sai lệch thống kê |
| 4. Visibility ablation tự thua vì vocabulary | **Resolved ở mức thiết kế** | §18 chỉ chấm outcome chung, không dùng full-state macro-F1 chứng minh lợi thế hiển nhiên; collapsed ontology áp mapping chung và báo riêng | “Record usefulness” và ngân sách ngang nhau phải được vận hành hoá khi viết protocol; chưa có gain đo được |
| 5. Template/property cluster cùng split | **Resolved ở mức thiết kế** | §16 giữ property/repost clusters; template chỉ audit; template holdout riêng; không coi template chung là property | Chưa có cluster audit/size distribution hay manifest split thực để xác nhận chống leakage |

**Tính nhất quán với báo cáo ngắn:** mục tiêu asking-price reference, hai vòng research/product, không tự train từ mọi contribution, hạn pilot bốn tuần và roadmap dài hơn đều khớp main. Báo cáo ngắn giữ quan sát công khai giá thành giả thuyết, không bảo đảm Q1, không khẳng định đã chạy model/hệ thống. Mismatch PDF 13 trang YOLO với ReNER 9 trang vẫn được ghi đúng.

**§31–32:** danh mục nguồn nêu mức đọc và hạn chế; không tự gọi prior NER+dashboard là novelty đầu tiên. Các ca synthetic ghi rõ minh hoạ, chưa phải 10 bài thật hoặc test real-world; phép 4×16 vẫn giữ giả định hình học/derived; case `3.x` tách source ambiguity khỏi extractor abstain. Không có số F1, cải thiện hay giá thị trường dự án được trình bày như kết quả đã đo trong các đoạn thay đổi. Re-scan này đối chiếu nội dung và sổ nguồn địa phương; không phải một lượt mở lại độc lập toàn bộ các bài báo online.

**Điểm hoàn thiện artifact đã báo tác giả:** tại thời điểm đọc, main nhắc C-2 “ghi trong sổ” nhưng sổ vật lý vẫn chỉ có C-1; cần append C-2 hoặc đổi claim thành dự kiến trước phát hành. HTML trong danh sách artifact báo cáo ngắn đang được build, phải kiểm tồn tại ở bước hoàn thiện. Đây là consistency của gói giao nộp, không mở lại năm findings khoa học đã được sửa. Không coi build đang diễn ra là bằng chứng artifact đã tồn tại.

**Verdict sau sửa:** không còn blocker nội dung trong **các đoạn đã re-scan** để giao báo cáo nền tảng. Năm findings đã được xử lý đúng ở mức design. Cho phép tiến đến pilot/schema/scorer; chưa xác nhận protocol đã chạy, data đủ, source collection được phép trong trường hợp cụ thể hay hiệu quả khoa học/sản phẩm. Mức chắc chắn **cao** với việc văn bản đã sửa đúng và nội dung nguồn địa phương đã đọc; **chưa xác minh thực nghiệm** với mọi claims về chất lượng/coverage/latency/khả năng công bố.
