# Đề tài 8 — Trích xuất thông tin bất động sản từ bài đăng mạng xã hội (Real Estate NER)

> Tài liệu nghiên cứu lịch sử 03/10/2026. Đính chính 11/10: bỏ khẳng định Hybrid chắc tốt nhất/ngưỡng 300 bài chung; sửa cách gọi metric seqeval. Các số liệu prior work và pháp lý trong phần cũ chưa được thẩm định lại toàn bộ ở lượt này; dùng sổ nguồn foundation ngày 09/10 cho đối chiếu mới hơn. [Phạm vi hiện hành](../../notes/HIEN-TRANG-VA-QUYET-DINH.md).

- **Môn:** TMG301 (NLP / Text Mining) — đề bài nhóm random được (ảnh chụp đề)
- **Loại artifact:** Báo cáo nghiên cứu vòng 1 (research report) — đầu vào cho proposal + file Excel
- **Worker:** admin · **Ngày:** 2026-10-03
- **Trạng thái:** CHỜ NHÓM CHỐT PHẠM VI (mục 9) trước khi xuất Excel

---

## 0. TL;DR

1. Đề có **3 tầng**, không phải 1: *phát hiện đoạn văn (span)* → *chuẩn hoá giá trị* → *phân giải ngữ nghĩa* (giá bán hay giá thuê hay tiền cọc; DT đất hay DT sàn; địa chỉ cũ hay mới). Nhóm làm được cả 3 tầng thì vượt hẳn mức "regex bắt số".
2. Mức sàn của đề rất thấp (4 trường × 10 bài). Điểm cao đến từ **độ chặt khi đánh giá** (gold set, P/R/F1, phân tích lỗi) **cộng** một **giao diện làm hiện rõ quá trình NLP**. Giao diện chỉ đẹp mà không hiện ra phương pháp thì không đủ.
3. Hai sự thật ảnh hưởng thẳng đến kiến trúc: **Facebook Groups API bị gỡ hẳn từ 22/04/2024**, nên "bot tự đọc group" không làm được qua API hợp lệ. **Từ 01/07/2025 VN còn 34 tỉnh và bỏ cấp huyện**, nên trường "Vị trí" phải chuẩn hoá được cả tên cũ lẫn tên mới.
4. Kiến trúc khuyến nghị: **Hybrid Regex + LLM + Validator**. Regex là baseline, đúng chương Regex của môn. LLM trả về JSON có schema và có grounding vào span. Validator đối chiếu hai nguồn để ra độ tin cậy. Khung lý thuyết vẫn là sequence labeling (BIO).
5. Hướng nghiên cứu này có dòng paper tiếng Việt thật (UIT/HCMUS/AISIA, 2021–2022), nhưng **toàn bộ lấy dữ liệu từ website rao vặt** chứ không phải Facebook, và **chưa so sánh với LLM**. Đây là khoảng trống hợp lý để nhóm định vị đồ án (ở mức đồ án môn học, không phải claim nghiên cứu mới).

---

## 1. Đọc đúng đề — giải phẫu từng câu chữ

| Câu chữ trong đề | Nghĩa đen | Nghĩa ẩn / ngầm định | Hệ quả thiết kế |
|---|---|---|---|
| "Nền tảng nghiên cứu: **Sequence Labeling**" | Gán nhãn chuỗi | Giảng viên kỳ vọng nhóm **diễn đạt bài toán dưới dạng BIO tagging**, kể cả khi dùng LLM | Phải có slide/màn hình hiện token + nhãn BIO. Gold set nên gán ở mức span |
| "& **Regular Expressions**" | Regex | Bám chương 1 của môn (Regex, Text Normalization, Edit Distance) | Regex là **baseline bắt buộc**, không phải phương án phụ |
| "**Bot** tự động đọc… trên **Facebook Groups**" | Một con bot | Groups API đã chết (2024), scraping vi phạm ToS của Meta | "Bot" phải hiểu linh hoạt: extension trên trình duyệt, bot Telegram nhận bài forward, hoặc web app dán bài vào |
| "bài đăng **lộn xộn**" | Văn bản nhiễu | Teencode, không dấu, emoji, viết tắt (PN/WC/DT/TL/MT/HXH), nhiều tin trong một bài, thông tin bị giấu ("ib giá") | Cần tầng **tiền xử lý + chuẩn hoá từ vựng** (lexical normalization) |
| "điền vào **bảng cấu trúc chuẩn**" | Ra bảng | "Chuẩn" nghĩa là **giá trị đã chuẩn hoá**, không phải chuỗi thô ("5ty2" → 5 200 000 000 VND) | Cần **schema + bộ chuẩn hoá** cho từng trường; có trạng thái `null` hợp lệ |
| "Giá, Diện tích, Vị trí, Số phòng" | 4 trường | Mỗi trường có mơ hồ riêng (mục 3) | Mỗi trường cần sub-field: loại giá, đơn vị, loại DT, cấp hành chính… |
| "**regex hoặc prompt LLM**" | Chọn một | Chữ "hoặc" cho phép chọn, nhưng **so sánh cả hai** mới là tư duy nghiên cứu | Thiết kế để chạy **song song** 2 phương pháp và đo |
| "thành công… từ **10 bài** thực tế **phức tạp**" | 10 bài | "Phức tạp" phải được **định nghĩa có hệ thống**, không chọn cảm tính | Dựng **taxonomy độ khó** (mục 3); 10 bài phủ đủ các ô khó; 10 bài này là **test giữ riêng**, không dùng để tinh chỉnh regex/prompt |

### Nhận định về giả thuyết của nhóm ("muốn điểm cao phải làm tốt giao diện")

**Đồng ý một phần.** Đề có chữ "Định hướng sản phẩm" và "Bot", nên demo sản phẩm chắc chắn được chấm. Nhưng đây là môn **NLP**, nên giảng viên gần như chắc chắn hỏi: *"Sequence labeling nằm ở đâu? Regex của em sai ở đâu? Đo bằng gì?"* Nếu giao diện đẹp mà không trả lời được ba câu này thì dễ bị xem là "app gọi ChatGPT".

→ **Chiến lược đề xuất:** giao diện là **cửa sổ nhìn vào NLP** (explainable extraction UI):
- Bôi màu từng span trên bài gốc theo loại thực thể. Người xem *thấy* sequence labeling.
- Mỗi giá trị có nhãn nguồn (Regex rule #7 / LLM) và độ tin cậy.
- Chế độ so sánh Regex vs LLM vs Gold, có dashboard P/R/F1 chạy trực tiếp.
- Người dùng sửa span thì bản sửa thành gold label (human-in-the-loop).

Giao diện kiểu này vừa đẹp vừa chứng minh được phương pháp. Đó là điểm khác biệt với các nhóm khác.

---

## 2. Bản chất kỹ thuật: bài toán có 4 tầng

| Tầng | Tên | Việc phải làm | Kiến thức môn TMG301 tương ứng |
|---|---|---|---|
| 0 | Lọc & phân loại bài (post classification) | Bài này là **bán / cho thuê / cần mua / cần thuê / spam**? Bài "cần thuê tầm 10tr" thì giá là **ngân sách**, không phải giá chào | Naive Bayes / Logistic Regression (phân loại văn bản) |
| 1 | Phát hiện span (span detection) | Tìm đoạn chữ chứa giá, DT, vị trí, số phòng — chính là **sequence labeling** | Regex · NER/BIO · Transformer fine-tune (PhoBERT) · slot filling (chương Dialogue: NLU = intent + slot) |
| 2 | Chuẩn hoá giá trị (value normalization) | "5ty2" → 5 200 000 000; "4x16" → 64 m²; "2N2VS" → 2 phòng ngủ | Regex + Text Normalization |
| 3 | Phân giải ngữ nghĩa (semantic resolution) | Nhiều số tiền thì số nào là giá? Giá/m² hay tổng giá? Địa chỉ cũ (Quận 7) ánh xạ sang mới thế nào? | Information Extraction · Edit Distance (fuzzy match tên địa danh) |

**Ví dụ BIO (bài tự tạo để minh hoạ):**

```
Bán   nhà  hẻm  Huỳnh  Tấn    Phát   Q7     ,  DT  4x16    ,  3PN     ,  giá  5ty2
O     O    O    B-LOC  I-LOC  I-LOC  I-LOC  O  O   B-AREA  O  B-ROOM  O  O    B-PRICE
```

Lưu ý tiếng Việt: PhoBERT yêu cầu **tách từ** (word segmentation, ví dụ VnCoreNLP), nên `Huỳnh_Tấn_Phát` có thể thành một token. Ranh giới token ảnh hưởng trực tiếp đến cách gán nhãn BIO.

---

## 3. Bản đồ độ khó dữ liệu (taxonomy) — cơ sở để chọn "10 bài phức tạp"

> Ví dụ bên dưới **do tôi tự tạo để minh hoạ hiện tượng**, không phải dữ liệu thật.

### 3.1 Giá (PRICE)
| Hiện tượng | Ví dụ | Giá trị chuẩn kỳ vọng |
|---|---|---|
| Viết tắt + số lẻ kiểu nói | `5ty2`, `5 tỷ 2`, `5t2` | 5 200 000 000 VND |
| Giá thuê theo tháng | `6tr5/th`, `6.5 triệu/tháng` | 6 500 000 VND/tháng, `price_type=rent_monthly` |
| Giá theo m² | `45tr/m2` (đất 100m2) | `unit_price`=45 000 000/m²; tổng = 4.5 tỷ (suy ra, đánh dấu `derived`) |
| Khoảng giá | `3-3.5 tỷ`, `tầm 12-15tr` | min / max |
| Số gây nhiễu | `cọc 2 tháng`, `phí QL 15k/m2`, SĐT `0909…` | **Không** phải giá |
| Nhiều giá | `giá cũ 3.2 tỷ, nay chỉ 2.9 tỷ` | 2.9 tỷ (giá hiện hành) |
| Ẩn giá | `giá ib`, `inbox giá tốt` | `null` + `reason=hidden` |
| Thương lượng | `TL`, `còn TL nhẹ`, `thỏa thuận` | cờ `negotiable=true` |
| Tiếng lóng | `5 tỏi`, `2 xị` | cần từ điển lóng |

### 3.2 Diện tích (AREA)
| Hiện tượng | Ví dụ | Chuẩn |
|---|---|---|
| Kích thước ngang × dài | `4x16`, `4 x 16m`, `DT 4*16` | 64 m² (`derived`) |
| Nở hậu | `4x16 nở hậu 4.5` | 64 m² (ghi chú `irregular`) |
| Nhiều loại DT | `đất 100m2, xây 80m2, DTSD 240m2` | `land_area`, `floor_area`, `usable_area` |
| Đơn vị đa dạng | `60m2`, `60m²`, `60 mét vuông`, `60 m vuông` | 60 m² |
| Công nhận | `CN 60m2` (công nhận) | 60 m² (`certified=true`) |

### 3.3 Vị trí (LOCATION) — khó nhất
| Hiện tượng | Ví dụ | Ghi chú |
|---|---|---|
| Đơn vị hành chính **cũ** | `Q7`, `quận Bình Thạnh`, `huyện Nhà Bè` | Từ 01/07/2025 **không còn cấp huyện/quận**. Cần lưu `raw` + `legacy (63 tỉnh)` + `new (34 tỉnh)` |
| Mốc tương đối | `gần Lotte Mart Q7`, `cách chợ 200m` | Là POI, không phải địa chỉ hành chính |
| Tên dự án / khu dân cư | `Vinhomes Grand Park`, `KDC Him Lam` | Cần gazetteer dự án |
| Tên đường + loại mặt tiền | `MT Lê Văn Lương`, `HXH Huỳnh Tấn Phát` | MT = mặt tiền, HXH = hẻm xe hơi |
| Viết sai / không dấu | `binh thanh`, `Bình Thạn` | Edit distance / fuzzy match |
| Nhập nhằng | `Phú Mỹ` (nhiều nơi trùng tên) | Cần ngữ cảnh tỉnh |

### 3.4 Số phòng (ROOMS)
| Hiện tượng | Ví dụ | Chuẩn |
|---|---|---|
| Viết tắt miền Nam | `3PN 2WC`, `1 trệt 2 lầu` | bedrooms=3, bathrooms=2; floors=3 |
| Viết tắt miền Bắc | `2N2VS`, `căn 3 ngủ` | bedrooms=2, bathrooms=2 |
| Cộng thêm | `2PN+1` | bedrooms=2, `plus_room=true` |
| Ngầm định | `studio`, `phòng trọ` | bedrooms=0/1 (quy ước, phải ghi vào guideline) |
| Nhầm lẫn tầng vs lầu | `1 trệt 2 lầu` = 3 tầng | quy đổi |

### 3.5 Hiện tượng cấp bài
- **Nhiều tin trong một bài** (môi giới đăng 5 căn) → output là **danh sách bản ghi**.
- **Bài cầu** (cần thuê/cần mua) → giá là ngân sách.
- **Spam/nhiễu** (ViND: khoảng 18% bài web là nhiễu; trên Facebook dự kiến cao hơn — `[suy luận]`).
- Emoji, CHỮ IN HOA, hashtag, xuống dòng lộn xộn, không dấu, teencode.

→ **10 bài test nên phủ được ít nhất 1 ô khó của mỗi trường + 3 hiện tượng cấp bài.**

---

## 4. Tổng quan nghiên cứu (literature landscape)

### 4.1 Dòng nghiên cứu NER bất động sản tiếng Việt (gần nhất với đề)
| Năm | Công trình | Điểm chính | Hạn chế → cơ hội cho nhóm |
|---|---|---|---|
| 2012 | Pham & Pham — *IE for Vietnamese Real Estate Advertisements* (KSE 2012) | Hệ **rule-based**, F-measure 91 trên tin rao web | Đây chính là "regex approach" thời tiền deep learning, làm baseline lịch sử |
| 2021 | Huynh et al. — *NER for Vietnamese Real Estate Advertisements* (NICS 2021) | **Bộ NER BĐS tiếng Việt đầu tiên**: 3 152 tin từ propzy.vn, nhadat247.com.vn, batdongsan.com.vn | Dữ liệu từ website (bán cấu trúc), không phải MXH. Bộ nhãn cụ thể `[chưa kiểm chứng — cần đọc full text]` |
| 2022 | Nguyen B.T. et al. — *End-to-End NER Platform… and Analytical Applications* (IEEE Access 10) | Pipeline đầu-cuối: thu thập → NER → kho dữ liệu → phân tích. MishWindowEncoder micro-F1 90.72% | **Có phần ứng dụng/phân tích**: mẫu tham khảo tốt cho phần "sản phẩm" |
| 2022 | Tran K.Q. et al. — *SEND / ViND* (PACLIC 36) | 12 862 bài từ 5 website, khoảng 18% là nhiễu. PhoBERT-large macro-F1 0.9024. **Lọc nhiễu trước giúp NER tăng 0.0239 F1** | Bằng chứng ủng hộ **tầng 0 (lọc bài)** trong kiến trúc |
| 2025 | Nguyen D. et al. — *Fake Advertisements Detection… Vietnamese Real Estate* (arXiv preprint) | Phát hiện tin giả đa phương thức, accuracy 91.5% | Hướng mở rộng (không thuộc phạm vi chính) |

**Khoảng trống quan sát được:** (a) chưa có bộ dữ liệu công khai cho **Facebook Groups**, (b) chưa có công trình tiếng Việt **so sánh regex vs LLM vs fine-tune** cho miền này, (c) chưa xử lý **chuẩn hoá địa chỉ sau sáp nhập 2025**. `[suy luận từ kết quả tìm kiếm — chưa làm tổng quan hệ thống]`

### 4.2 Nền tảng NLP tiếng Việt
| Công trình | Vai trò trong đồ án |
|---|---|
| PhoBERT (Findings EMNLP 2020) | Encoder tiếng Việt để fine-tune token classification (nếu chọn phương án D) |
| PhoNER_COVID19 (NAACL 2021) | Mẫu chuẩn về **guideline gán nhãn NER tiếng Việt** (PhoBERT-large 94.5 micro-F1) |
| ViLexNorm (EACL 2024) | Bộ chuẩn hoá từ vựng MXH tiếng Việt đầu tiên (>10 000 cặp câu). Chứng minh chuẩn hoá giúp task hạ nguồn |
| PAP_NER (PLOS ONE) | NER văn bản hành chính VN: PhoBERT vượt XLM-R +2.08 F1 dù nhỏ hơn một nửa |
| VMLU (ACL 2025) | Benchmark LLM tiếng Việt, tham khảo khi chọn LLM |

### 4.3 LLM cho trích xuất thông tin (2024–2026)
| Công trình | Ý chính | Dùng thế nào |
|---|---|---|
| Xu et al. — *LLMs for Generative IE: A Survey* (Frontiers of CS 2024) | Phân loại toàn bộ kỹ thuật LLM-IE | Khung lý thuyết cho phần Related Work |
| UniversalNER (ICLR 2024) | **Chưng cất (distill)** ChatGPT thành model nhỏ, vượt ChatGPT 7–9 F1 | Ý tưởng: LLM gán nhãn bạc → train model nhỏ |
| GLiNER (NAACL 2024) / **GLiNER2** (EMNLP 2025 Demo) | Encoder nhỏ (<500M), zero-shot NER + trích xuất theo schema, chạy CPU | Phương án "AI nhẹ, không tốn API". Hỗ trợ tiếng Việt `[cần thử]` |
| **LangExtract** (Google, Apache-2.0, v1.6.0) | LLM trích xuất theo few-shot. **Mỗi giá trị gắn vị trí chính xác trong văn bản gốc** (source grounding). Sinh **HTML tương tác** để bôi màu | Gần như đúng "UI làm lộ NLP"; hỗ trợ Gemini/OpenAI/Ollama |
| JSONSchemaBench (ICML 2025) | Constrained decoding thường **gãy với schema phức tạp** | Giữ schema **phẳng, đơn giản**; luôn validate |

### 4.4 Trích xuất BĐS bằng LLM ở nước ngoài (mới nhất)
| Công trình | Điểm chính |
|---|---|
| *Incorporating LLMs in Automated Real Estate Valuation* (J. Real Estate Research, 2025) | LLM trích đặc trưng từ mô tả nhà (Oslo, 9 842 giao dịch) để định giá |
| *Feature Extraction for Real Estate Images and Titles with LLMs* (SAUCIS) | Recall thuộc tính tăng tới 44.26% |
| *Attribute-Value Extraction: Real Estate Observatory* (JAIIO 2024, Argentina) | So sánh nhiều cách attribute-value extraction trên mô tả BĐS |
| *Structured Data Extraction from Real Estate Documents…* (arXiv 2607.06012, 07/2026) | DeepSeek R1, 35 thuộc tính, 2 766 bản ghi hợp lệ — mới nhất tìm được |
| *Real Estate Attribute Value Extraction Using LLMs* (bộ RAVE) | Tin rao Slovakia `[chưa truy cập được full text]` |

### 4.5 Bối cảnh pháp lý & thực tế (ảnh hưởng trực tiếp đến kiến trúc)
| Sự kiện | Ngày | Hệ quả |
|---|---|---|
| Meta gỡ **Facebook Groups API** (Graph API v19) | Công bố 23/01/2024, gỡ 22/04/2024 | Không có đường API hợp lệ để bot đọc group |
| CrowdTangle đóng; thay bằng **Meta Content Library** (chỉ cho học thuật/phi lợi nhuận, không export) | 14/08/2024 | Không khả thi cho đồ án ngắn hạn |
| **Luật BVDLCN 91/2025/QH15** | Thông qua 26/06/2025, hiệu lực **01/01/2026** (đang có hiệu lực) | Bài đăng có SĐT, tên: **phải ẩn danh** trong dataset/demo |
| Sáp nhập còn **34 tỉnh**, **bỏ cấp huyện** | Hiệu lực 01/07/2025 | Trường Vị trí cần ánh xạ cũ → mới (có thư viện `vietnamadminunits`, `vietnam-address-converter`) |

---

## 5. Kiến trúc ứng viên

| | A. Regex + luật | B. Prompt LLM thuần | **C. Hybrid Regex + LLM + Validator** (khuyến nghị) | D. C + fine-tune PhoBERT (BIO) |
|---|---|---|---|---|
| Ý tưởng | Pattern + từ điển viết tắt + bộ chuẩn hoá | LLM trả JSON theo schema, few-shot | Regex bắt trường "số" (giá, DT, phòng). LLM lo vị trí + ca mơ hồ. Validator đối chiếu → độ tin cậy | Thêm model sequence labeling train trên nhãn LLM gán trước rồi người sửa |
| Bám môn | Rất sát (chương Regex) | Yếu nếu không giải thích được | Sát (Regex + IE + slot filling) | Rất sát (Fine-tuning, NER) |
| Độ chính xác dự kiến | Cao cho giá/DT/phòng, thấp cho vị trí `[suy luận]` | Cao nhưng có rủi ro **bịa giá trị** khi bài không nêu | Giả thuyết có lợi trong phạm vi hẹp; chưa có benchmark nội bộ | Chất lượng và nhu cầu nhãn phải đo qua pilot/learning curve; chưa có ngưỡng đủ chung |
| Chi phí | 0 | API hoặc GPU local | Thấp (LLM chỉ gọi khi cần) | Cao (gán nhãn + train) |
| Tiềm năng UI | Hiện được rule nào bắt | Khó giải thích | **Tốt nhất**: badge nguồn, độ tin cậy, so sánh | Tốt + hiện nhãn BIO thật từ model |
| Rủi ro | Vỡ khi gặp văn phong lạ | Hallucination, chi phí, không ổn định | Phức tạp hơn A, B | Thiếu thời gian |

**Pipeline phương án C (đề xuất sơ bộ):**

```
Input (dán bài / extension / bot)
  → Tiền xử lý: Unicode NFC · bỏ emoji · map teencode/viết tắt · tách tin
  → Tầng 0: phân loại bài (bán / thuê / cần mua / cần thuê / spam)
  → Tầng 1: [Regex extractor]  ║  [LLM extractor: JSON schema + span grounding]
  → Tầng 2: Normalizer (tiền VND · m² · số phòng · địa chỉ 63→34 tỉnh)
  → Tầng 3: Validator/Reconciler (2 nguồn khớp → tin cậy cao; lệch → cờ "cần xem";
            luật sanity: giá thuê/tháng < giá bán, DT trong khoảng hợp lý…)
  → Lưu (SQLite / Google Sheet) → UI → Xuất Excel/CSV
```

---

## 6. Giao diện — hướng "UI làm lộ NLP"

| # | Màn hình | Nội dung | Vì sao ăn điểm |
|---|---|---|---|
| 1 | Nhập bài | Dán text / import nhiều bài / nhận từ extension hoặc bot | Thao tác demo nhanh |
| 2 | **Trích xuất** | Trái: bài gốc **bôi màu span** theo trường. Phải: thẻ kết quả đã chuẩn hoá + nhãn nguồn (Regex/LLM) + độ tin cậy. Bật/tắt hiện nhãn BIO | Người xem *thấy* sequence labeling |
| 3 | **So sánh** | Regex vs LLM vs Gold đặt cạnh nhau, highlight chỗ lệch | Chứng minh tư duy nghiên cứu |
| 4 | Bảng dữ liệu | Bảng chuẩn (4 trường + sub-field), lọc giá/DT/khu vực, **bản đồ** (tuỳ chọn), biểu đồ giá/m² | Đúng chữ "bảng cấu trúc chuẩn", có giá trị sử dụng |
| 5 | **Đánh giá** | P/R/F1 theo từng trường, ma trận lỗi theo taxonomy mục 3 | Thể hiện độ chặt khoa học |
| 6 | Sửa & gán nhãn (HITL) | Click sửa span → thành gold → metric cập nhật | Vòng phản hồi, "wow factor" |

**Hình thức sản phẩm (chờ nhóm chọn):** web app · Chrome extension side panel ngay trên Facebook (người dùng bấm "Trích xuất" trên bài đang xem — là bot "do người dùng kích hoạt", rủi ro ToS thấp hơn scraping hàng loạt `[suy luận, không phải tư vấn pháp lý]`) · bot Telegram (forward bài → trả thẻ + ghi Google Sheet).

---

## 7. Kế hoạch đánh giá (evaluation)

- **Gold set:** 10 bài showcase (đề yêu cầu) làm **test giữ riêng**, cộng 30–90 bài dev để tinh chỉnh regex/prompt. Nếu tinh chỉnh trên đúng 10 bài test rồi báo 100% thì đó là **rò rỉ dữ liệu (data leakage)** và dễ bị hỏi vặn.
- **Gán nhãn:** Label Studio hoặc doccano (span-level), viết **annotation guideline** 1–2 trang (quy ước studio, nở hậu, giá/m²…). Hai người gán chéo 20 bài, tính độ đồng thuận (Cohen's kappa) nếu kịp.
- **Metrics:**
  - Span-level: strict P/R/F1 với quy ước BIO và ranh giới thống nhất. `seqeval` có default/strict, không đồng nghĩa hai chế độ strict/partial overlap. Nếu báo partial, phải định nghĩa matching/credit riêng và kiểm bằng ca tay; không dùng nó thay strict. [README seqeval](https://github.com/chakki-works/seqeval).
  - Field-level: exact match trên **giá trị đã chuẩn hoá** (ví dụ giá lệch 0 VND).
  - Null accuracy: trả `null` đúng khi bài không có thông tin, để đo hallucination.
  - Chi phí & độ trễ trên mỗi bài (LLM vs regex).
- **Phân tích lỗi** theo taxonomy mục 3: biến lỗi thành insight trình bày.

---

## 8. Rủi ro chính

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Thu thập dữ liệu Facebook vi phạm ToS / dữ liệu cá nhân | Cao | Thu thủ công bài **công khai**, ẩn SĐT/tên (Luật 91/2025), không scrape hàng loạt |
| LLM bịa giá trị | Trung bình | Bắt buộc grounding span; validator; đo null accuracy |
| API LLM tốn phí / hết quota | Trung bình | Regex làm fallback; model local (Ollama) hoặc GLiNER2 |
| Địa chỉ cũ/mới lẫn lộn | Trung bình | Lưu cả raw + legacy + new; dùng thư viện mapping |
| UI ngốn hết thời gian, NLP mỏng | Cao | Khoá phạm vi NLP trước, UI dựng trên kết quả thật |

---

## 9. Quyết định đã chốt (hỏi đáp 2026-10-03)

| Câu hỏi | Lựa chọn |
|---|---|
| Kiến trúc lõi | **C. Hybrid Regex + LLM + Validator** |
| Hình thức sản phẩm | **Bot đọc Facebook Groups (Playwright) + Web app workbench** (chốt lại sau khi nhóm yêu cầu làm bot đúng đề) |
| Dữ liệu | **10 bài test + 40–90 bài dev**, thu thủ công, ẩn danh |
| LLM | **Gemini API free tier** (spike ngày 1: tài liệu chính thức không nói rõ free tier có structured output; hạn mức xem trong AI Studio) |
| Stack | **Next.js + FastAPI** |
| Thời gian / nhân lực | **3–4 tuần · 4 người** |
| Kiến thức | Regex + chuẩn hoá + BIO + metrics · LLM IE (prompt, schema, grounding) · HMM/CRF cổ điển (trình bày). **PhoBERT: ngoài phạm vi** |

Phát hiện thêm: danh sách slide TMG301 (00–17) **không có chương Sequence Labeling / HMM / CRF** → nhóm tự học từ SLP3.

### 9.1 Bot đọc Facebook Groups (bổ sung v1.1)

- **Vì sao vẫn làm được:** API chính thức đã gỡ, nhưng bot có thể đọc qua trình duyệt thật bằng Playwright. Rủi ro chính là **khoá tài khoản** vì điều khoản Meta cấm thu thập tự động. Tham khảo vụ Meta v. Bright Data (23/01/2024): tòa xử bên cào **không vi phạm** khi cào dữ liệu công khai lúc **không đăng nhập**; nội dung group thường phải đăng nhập nên không thuộc trường hợp này.
- **Thiết kế (B1–B4):** Chrome có giao diện, phiên đăng nhập lưu sẵn → cuộn group từ từ, ≤50 bài/lượt → bấm "Xem thêm", lấy text + permalink + thời gian → khử trùng, ẩn SĐT → đẩy vào pipeline → bảng trên web app tự điền (SSE).
- **Ranh giới:** gặp checkpoint/CAPTCHA thì **dừng và báo**. Không dùng proxy xoay vòng, không giải CAPTCHA, không giả dấu vân tay trình duyệt.
- **Phương án dự phòng cho demo:** chế độ **Replay** đọc lại HTML snapshot đã lưu qua đúng parser; nhập tay; video quay sẵn.
- Phân công: TV4 = Bot & Data Lead; script đánh giá chuyển sang TV1.

→ Proposal đầy đủ: `../proposal-realestate-ner-v1.1.xlsx` (13 sheet; v1.0 cũ giữ nguyên vì đang mở trong Excel).
→ Thuyết minh đề cương theo template AiTA Lab: `../proposal-ReNER-VN.docx` (26 trang, 35 tài liệu tham khảo).

### Venue Claim Card

- Proposal: ReNER-VN — bot lai Regex + LLM trích xuất thông tin BĐS từ bài đăng Facebook Groups tiếng Việt (đồ án TMG301).
- Novelty tier: **T1 — recipe**: kết hợp kỹ thuật đã có (regex, prompting LLM, neo nguồn, đối chiếu); không có thay đổi kiến trúc mô hình.
- Venue band: **không nhắm venue — mức đồ án môn học.** Nếu sau này muốn nộp hội nghị sinh viên/workshop trong nước, cần kiểm yêu cầu cụ thể của venue, quyền dữ liệu, chất lượng thực nghiệm, baseline phù hợp và tính mới. Không có điều kiện chung “≥300 bài là đủ”; không bắt buộc công bố raw corpus khi không có quyền. CRF/PhoBERT là ứng viên so sánh khi phù hợp RQ và tài nguyên, không phải nghĩa vụ mới của demo.
- Downgrade triggers: tìm thấy công trình đã công bố so sánh regex/LLM trên bài đăng MXH BĐS tiếng Việt.
- Confidence: medium — mới tìm kiếm nhanh, chưa tổng quan hệ thống.
- Ledger: C-1 (`claims-ledger.md`).

---

## 10. Nguồn (đã kiểm chứng trong phiên này)

| # | Nguồn | Năm | Venue / loại | Mức kiểm chứng | Link |
|---|---|---|---|---|---|
| 1 | Huynh S. et al. — NER for Vietnamese Real Estate Advertisements | 2021 | NICS 2021 (IEEE), tr. 23–28 | Metadata qua Crossref; số liệu qua abstract | https://doi.org/10.1109/NICS54270.2021.9701519 |
| 2 | Nguyen B.T. et al. — End-to-End NER Platform for Vietnamese RE Ads | 2022 | IEEE Access 10:87681–87697 | Metadata qua Crossref; F1 qua abstract | https://doi.org/10.1109/ACCESS.2022.3195496 |
| 3 | Tran K.Q. et al. — SEND (ViND) | 2022 | PACLIC 36, tr. 647–656 | **Đọc full-text PDF** | https://aclanthology.org/2022.paclic-1.71/ |
| 4 | Pham L.V., Pham S.B. — IE for Vietnamese RE Ads | 2012 | KSE 2012, tr. 181–186 | Metadata qua Crossref; F qua trang repository | https://doi.org/10.1109/KSE.2012.27 |
| 5 | Nguyen D. et al. — Fake Ads Detection, Vietnamese RE | 2025 | arXiv preprint | Abstract | https://arxiv.org/abs/2501.10848 |
| 6 | Nguyen D.Q., Nguyen A.T. — PhoBERT | 2020 | Findings EMNLP 2020 | Trang ACL Anthology | https://aclanthology.org/2020.findings-emnlp.92/ |
| 7 | Truong T.H. et al. — COVID-19 NER for Vietnamese | 2021 | NAACL 2021 | arXiv | https://arxiv.org/abs/2104.03879 |
| 8 | Nguyen T.N. et al. — ViLexNorm | 2024 | EACL 2024 | ACL Anthology | https://aclanthology.org/2024.eacl-long.85 |
| 9 | PAP_NER — Vietnamese administrative NER | `[năm chưa xác minh]` | PLOS ONE | Kết quả tìm kiếm | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0353166 |
| 10 | VMLU Benchmarks | 2025 | ACL 2025 | ACL Anthology | https://aclanthology.org/2025.acl-long.563 |
| 11 | Xu D. et al. — LLMs for Generative IE: A Survey | 2024 | Frontiers of CS 18(6) | DOI | https://doi.org/10.1007/s11704-024-40555-y |
| 12 | Zhou W. et al. — UniversalNER | 2024 | ICLR 2024 | Proceedings | https://arxiv.org/abs/2308.03279 |
| 13 | Zaratiana U. et al. — GLiNER | 2024 | NAACL 2024 | ACL Anthology | https://aclanthology.org/2024.naacl-long.300 |
| 14 | Zaratiana U. et al. — GLiNER2 | 2025 | EMNLP 2025 System Demos | arXiv | https://arxiv.org/abs/2507.18546 |
| 15 | Google — LangExtract (Apache-2.0) | 2025–2026 | Thư viện mã nguồn mở | README GitHub | https://github.com/google/langextract |
| 16 | Geng S. et al. — JSONSchemaBench | 2025 | ICML 2025 | arXiv | https://arxiv.org/abs/2501.10868 |
| 17 | LLMs in Automated Real Estate Valuation | 2025 | J. Real Estate Research | Kết quả tìm kiếm | https://doi.org/10.1080/08965803.2025.2587313 |
| 18 | Arslan A. et al. — Feature Extraction for RE Images and Titles with LLMs | 2026 | SAUCIS 9(3):690–699 | Metadata Crossref (sửa: trước ghi nhầm 2025) | https://dergipark.org.tr/en/pub/saucis/article/1829206 |
| 19 | Attribute-Value Extraction: Real Estate Observatory | 2024 | JAIIO (Argentina) | Kết quả tìm kiếm | https://revistas.unlp.edu.ar/JAIIO/article/view/17910 |
| 20 | Shehbaz & Moreno-García — Structured Data Extraction from RE Documents | 2026 | arXiv preprint | Abstract | https://arxiv.org/abs/2607.06012 |
| 21 | RE Attribute Value Extraction Using LLMs (RAVE) | 2025 | `[chưa truy cập được]` | Chỉ có tiêu đề | https://www.researchgate.net/publication/391167717 |
| 22 | STRUCTSENSE — HITL structured IE | 2025 | arXiv | Kết quả tìm kiếm | https://arxiv.org/abs/2507.03674 |
| 23 | Meta — Graph API v19 changelog (Groups API deprecation) | 2024 | Tài liệu chính thức | Kết quả tìm kiếm | https://developers.facebook.com/docs/graph-api/changelog/version19.0/ |
| 24 | CrowdTangle → Meta Content Library | 2024 | Báo chí | Kết quả tìm kiếm | https://www.theregister.com/2024/06/18/metas_decision_to_withdraw_misinformation/ |
| 25 | Luật BVDLCN 91/2025/QH15 | 2025 | Văn bản luật | Kết quả tìm kiếm | https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Law-91-2025-QH15-Personal-Data-Protection-665440.aspx |
| 26 | Sáp nhập 34 tỉnh (PwC snapshot) | 2025 | Báo cáo tư vấn | Kết quả tìm kiếm | https://www.pwc.com/vn/en/publications/vietnam-publications/vietnam-administrative-reform.html |
| 27 | vietnamadminunits (63→34 tỉnh) | 2025 | Thư viện Python | README | https://github.com/tranngocminhhieu/vietnamadminunits |
| 28 | vietnam-address-converter | 2025 | Thư viện Python | PyPI | https://pypi.org/project/vietnam-address-converter/ |

**Đã loại:** một bài blog (dev.to) đưa số liệu chi phí regex vs LLM (68% / 96% / 98%) — không phải nguồn uy tín, **không dùng**.

---

## Thuật ngữ (Glossary)

| English | Tiếng Việt | Giải thích ngắn |
|---|---|---|
| Sequence labeling | Gán nhãn chuỗi | Gán một nhãn cho từng token trong câu |
| BIO tagging | Gán nhãn BIO | B = bắt đầu thực thể, I = bên trong, O = ngoài |
| Named Entity Recognition (NER) | Nhận dạng thực thể có tên | Tìm và phân loại span thực thể |
| Slot filling | Điền khe thông tin | Trích giá trị cho các "khe" định sẵn (giá, DT…) — tên gọi trong hệ hội thoại |
| Value normalization | Chuẩn hoá giá trị | Đưa chuỗi thô về giá trị chuẩn ("5ty2" → 5 200 000 000) |
| Lexical normalization | Chuẩn hoá từ vựng | Đổi teencode/viết tắt về dạng chuẩn |
| Source grounding | Neo nguồn | Mỗi giá trị trích ra gắn với vị trí chính xác trong văn bản gốc |
| Constrained decoding | Giải mã ràng buộc | Ép LLM sinh đúng cấu trúc JSON/schema |
| Human-in-the-loop (HITL) | Có người trong vòng lặp | Người sửa kết quả máy, bản sửa thành dữ liệu huấn luyện/đánh giá |
| Data leakage | Rò rỉ dữ liệu | Tinh chỉnh trên chính tập test → kết quả ảo |
| Gazetteer | Từ điển địa danh | Danh sách tên địa danh/dự án để đối chiếu |
| Hallucination | Ảo giác (bịa) | LLM sinh giá trị không có trong văn bản |
