# Rà soát proposal v1.1 theo case study mới → danh sách sửa cho v1.2

- **Đối tượng rà soát:** `proposal-ReNER-VN.docx` (26 trang) và `proposal-realestate-ner-v1.1.xlsx` (13 sheet)
- **Worker:** admin · **Ngày:** 2026-10-03
- **Trạng thái:** chưa sửa file — chờ nhóm chốt 3 quyết định ở mục 5

---

## 0. Case study mới (đã thống nhất trong hội thoại 2026-10-03)

- **Phạm vi:** chỉ **thuê nhà để ở** (phòng trọ, chung cư mini, căn hộ dịch vụ, nhà nguyên căn cho thuê), **3–5 phường quanh cơ sở trường** (chưa chốt cơ sở nào).
- **Extension có 2 chế độ:**
  - *Thu thập*: tự động thu bài khi nhóm lướt group → trích xuất → đưa vào **kho thị trường**.
  - *Nhận định*: người dùng bấm trên bài họ quan tâm → trích xuất → so giá với **trung vị của nhóm bài tương tự** (cùng khu vực, loại hình, khoảng diện tích) → hiện N, IQR, 3 bài tương tự nhất; N < 10 thì báo "chưa đủ dữ liệu".
- **Hai tập dữ liệu tách biệt:** tập chuẩn khoảng 100 bài (gán tay, để đánh giá trích xuất) và kho thị trường 300–500 bài (tự trích xuất, chỉ giữ bản ghi tin cậy cao, đã gộp bài đăng lại).
- **RQ4 mới:** lỗi trích xuất làm lệch thống kê thị trường bao nhiêu.

## 1. Kết luận nhanh

- **Lõi NLP giữ nguyên:** bài toán BIO, lý thuyết HMM/CRF, kiến trúc lai Regex + LLM + Validator, cơ chế neo nguồn, các chỉ số P/R/F1, quy trình chống rò rỉ dữ liệu.
- **Phải sửa ở 4 khối:** (1) phạm vi và ví dụ chuyển từ mua bán sang **cho thuê**; (2) thu thập dữ liệu đổi từ **Playwright sang extension**; (3) thêm **module kho thị trường + nhận định** và **RQ4**; (4) các bảng, hình, phụ lục đang dùng ví dụ bài bán.
- Đếm theo bảng dưới: **25 mục bắt buộc sửa, 4 nên sửa, 2 nhỏ**; cần **vẽ lại cả 3 hình**.

## 2. Rà soát từng mục của proposal (docx)

| Mục | Hiện tại (v1.1) | Cần sửa (v1.2) | Mức |
|---|---|---|---|
| Tên đề tài | "Bot trích xuất và chuẩn hoá thông tin BĐS … lai Regex–LLM có neo nguồn" | "Trích xuất thông tin và nhận định giá thuê nhà từ bài đăng Facebook Groups bằng phương pháp lai Regex–LLM có neo nguồn" + tên tiếng Anh tương ứng | Bắt buộc |
| Tóm tắt (239 từ) | Bot Playwright, 4 trường, RQ1–RQ3 | Thêm extension 2 chế độ, kho thị trường, nhận định theo trung vị, RQ4; phạm vi thuê nhà quanh trường; vẫn ≤ 250 từ | Bắt buộc |
| Từ khoá | — | Thêm "so sánh giá thuê", "tiện ích mở rộng trình duyệt", "phát hiện bài trùng" | Nhỏ |
| Mục 1 – ví dụ mở đầu | Bài **bán**: "5ty2, 4x16 nở hậu, 1 trệt 2 lầu, cọc 50tr" | Bài **cho thuê** nhiều số gây nhiễu, ví dụ: "Cho thuê phòng 22m2 gác lửng WC riêng gần ĐH…, giá 3tr5/th, điện 3k5/số, nước 100k/người, cọc 1 tháng" | Bắt buộc |
| 1.1 Tổng quan | Đủ tài liệu trong và ngoài nước | Giữ; viết lại đoạn ứng dụng để nhấn mạnh hướng phân tích thị trường ([Nguyen 2022], [Tanevitch 2024], [Faxvaag 2025]) làm cơ sở cho module nhận định. Không cần tài liệu mới | Nên |
| 1.2 Hạn chế | L1–L7 | Thêm **L8**: các công trình dừng ở trích xuất hoặc dashboard tổng hợp, chưa đưa ra nhận định cho từng tin dựa trên dữ liệu mạng xã hội (trong phạm vi tìm kiếm); ảnh hưởng của lỗi trích xuất lên thống kê hạ nguồn hiếm khi được định lượng | Bắt buộc |
| 1.3.1 Vấn đề nghiên cứu | 3 bước: loại bài, bản ghi, null | Thêm bước (4): so giá bài người dùng chọn với trung vị nhóm bài tương tự trong kho; báo N và IQR; N < 10 thì không kết luận | Bắt buộc |
| 1.3.2 RQ và giả thuyết | RQ1–RQ3 | Thêm **RQ4 + H4** (không đặt trước con số). H3 cập nhật: số gây nhiễu chính là cọc, điện, nước, phí dịch vụ | Bắt buộc |
| 1.3.3 Tính mới | 4 điểm | Thêm: nhận định giá theo nhóm tương tự, minh bạch độ bất định (N, IQR); đo ảnh hưởng của lỗi trích xuất lên thống kê. Giữ câu "tính mới ở mức đồ án môn học" | Bắt buộc |
| 2. Mục tiêu | O1–O6 | O2: bot Playwright → extension 2 chế độ; thêm **O7**: kho thị trường + module nhận định + RQ4; O5: cập nhật danh sách màn hình | Bắt buộc |
| 3. Phạm vi (Bảng 3) | BĐS nói chung, cả mua lẫn thuê | Chỉ thuê nhà để ở; 3–5 phường quanh [trường]; hai tập dữ liệu. **Ngoài phạm vi:** mua bán, giá giao dịch, định giá hay lời khuyên tài chính, đăng lại bài công khai | Bắt buộc |
| 4.1 Khả thi dữ liệu | 30 bài chép tay + bot, khoảng 100 bài | Thêm kho thị trường 300–500 bài; tốc độ thu qua extension phải đo ngay ngày 1; cách gộp bài trùng | Bắt buộc |
| 4.5 Pháp lý | Bot Playwright, dừng khi gặp checkpoint | Extension: ít bị chặn hơn nhưng **vẫn là thu thập tự động**; kho chỉ dùng nội bộ để thống kê, không đăng lại; bài tương tự hiển thị ở dạng đã ẩn danh | Bắt buộc |
| 4.6 Rủi ro (Bảng 5) | 7 rủi ro | Thêm: không đủ N cho nhóm tương tự; bài đăng lại làm lệch thống kê; lỗi trích xuất lan sang nhận định; hạn mức Gemini khi xử lý 300–500 bài | Bắt buộc |
| 5.2 Kiến trúc (Hình 1, Bảng 6) | B1–B4 Playwright | E1 content script (thu thập / nhận định), E2 side panel hiện nhận định, E3 gửi về API; thêm **M8 Gộp trùng** (TF-IDF + cosine), **M9 Thống kê & nhận định**, kho thị trường. **Vẽ lại Hình 1** | Bắt buộc |
| 5.3 Thu thập | Playwright, phiên đăng nhập, lịch chạy | Viết lại cho extension (Manifest V3): tự thu khi feed tải, bấm "Xem thêm", gửi HTML thô + permalink về backend. Parser vẫn viết bằng Python nên Replay vẫn dùng được | Bắt buộc |
| 5.4 Phân loại bài | bán / cho thuê / cần mua / cần thuê / spam | cho thuê / cần thuê / ở ghép / bán (loại khỏi phạm vi) / spam | Nên |
| 5.5 BIO (Bảng 7) | Ví dụ "Huỳnh Tấn Phát Q7 · 4x16 · 3PN" | Đổi sang ví dụ bài thuê; nếu chốt nhãn FEE thì tập nhãn tăng từ 9 lên 11 | Nên |
| 5.6 Regex (Bảng 8) | P1 "tỷ", P3 giá/m², A1 "4x16"… | Bỏ hoặc giảm luật chỉ có ở bài bán (tỷ, giá/m², nở hậu). Thêm luật phí: điện "3k5/số", nước "100k/người", dịch vụ, gửi xe, wifi, cọc; giá theo người (ở ghép); "bao điện nước" | Bắt buộc |
| 5.8 Chuẩn hoá (Bảng 9) | Giá bán/thuê; DT đất/xây; PN/WC/tầng | **Giá:** chỉ giá thuê theo tháng, giá theo người, cờ "bao điện nước"; các khoản phí tách thành trường riêng. **Số phòng:** thêm loại hình (phòng trọ / CCMN / CHDV / nguyên căn), gác lửng. **Vị trí:** mốc "gần trường", phường mới | Bắt buộc |
| 5.9 Validator | Ngưỡng hợp lý theo bán/thuê | Cập nhật ngưỡng giá thuê theo loại hình (quy tắc thiết kế, cần thực nghiệm) | Nhỏ |
| **Mục mới: Kho thị trường & nhận định** | — | Tiêu chí vào kho (tin cậy cao, có giá thuê + diện tích + vị trí); gộp trùng (TF-IDF + cosine, ngưỡng là quy tắc thiết kế); phân nhóm (phường × loại hình × khoảng diện tích); trung vị, IQR, thứ hạng phần trăm; N tối thiểu 10 (quy tắc thiết kế); 3 bài tương tự nhất; câu chữ nhận định + miễn trừ trách nhiệm ("giá chào thuê, không phải định giá") | Bắt buộc |
| 5.10 Giao diện (Hình 2, Bảng 10) | 7 màn web, S0 điều khiển bot | Thêm **panel nhận định trong extension**; màn web mới **"Thị trường"** (trung vị theo phường/loại hình, phân bố giá); S0 → trạng thái extension và kho; S6 HITL hạ xuống Could. **Vẽ lại Hình 2** (bài thuê + thẻ nhận định) | Bắt buộc |
| 5.11 Đánh giá (Bảng 11) | RQ1–RQ3, một tập dữ liệu | Tách rõ 2 tập. Cách đo RQ4: trên tập chuẩn, so trung vị theo nhóm tính từ nhãn tay với trung vị tính từ kết quả hệ thống; tỉ lệ bản ghi bị loại vì độ tin cậy thấp. Thêm dòng RQ4 vào Bảng 11 | Bắt buộc |
| 5.12 Công nghệ (Bảng 12) | Playwright, APScheduler | Chrome Extension MV3 (JS/TS); scikit-learn cho TF-IDF; bỏ Playwright (hoặc giữ ở mức Could) | Bắt buộc |
| 6. Kế hoạch (Bảng 13, Hình 3, Bảng 14) | Các việc của bot Playwright | Thay bằng extension; thêm các buổi thu kho thị trường (tuần 1–3), module gộp trùng + thống kê (tuần 3), panel nhận định + màn Thị trường (tuần 3–4), phân tích RQ4 (tuần 4). Ước lượng lượt gọi Gemini tăng lên khoảng 1.000–1.500 → giãn theo ngày, hoặc chỉ gọi LLM khi regex không chắc. **Vẽ lại Hình 3** | Bắt buộc |
| 7. Kết quả dự kiến (Bảng 15) | 5 sản phẩm | Thêm: kho thị trường đã ẩn danh (chỉ công bố thống kê tổng hợp), chức năng nhận định, kết quả RQ4 | Bắt buộc |
| Phụ lục A (Bảng 16) | PRICE gồm giá bán và giá thuê | PRICE = giá thuê; nếu chốt FEE thì định nghĩa FEE = cọc, điện, nước, dịch vụ, gửi xe, wifi | Bắt buộc |
| Phụ lục B (Bảng 17) | 25 hiện tượng, nhiều cái chỉ có ở bài bán (P3, P8, A2, A3, L3) | Thay bằng taxonomy bài thuê; giữ các hiện tượng dùng chung | Bắt buộc |
| Phụ lục C | JSON của bài bán | JSON của bài thuê + khối `assessment` (median, IQR, N, percentile, similar_posts) | Bắt buộc |
| Tài liệu tham khảo | 35 mục | Bỏ [Playwright] nếu bỏ hẳn; thêm tài liệu Chrome Extensions MV3 (phải kiểm chứng trước khi thêm). Gộp trùng bằng TF-IDF/cosine có trong SLP3 (đã trích) nên không cần thêm tài liệu | Nên |

**Giữ nguyên, không cần sửa:** lý thuyết HMM/CRF và công thức (1)–(3); cơ chế neo nguồn và phân công LLM/mã tất định ở 5.7; quy tắc đối chiếu ở 5.9; quy trình đóng băng và chạy test một lần; phần pháp lý về Luật BVDLCN và Nghị quyết 202.

## 3. Thay đổi trong Excel (v1.1 → v1.2)

| Sheet | Sửa |
|---|---|
| 00_TongQuan | Tên đề tài, mục tiêu (O2, thêm O7), RQ4, phạm vi trong/ngoài, quyết định đã chốt |
| 01_HieuDe | Dòng "Bot": extension 2 chế độ; thêm tầng 4 "nhận định" |
| 02_Schema | Bỏ sub-field chỉ dùng cho bài bán; thêm `fees.*` (cọc, điện, nước, dịch vụ), `price.per_person`, `price.utilities_included`, `rooms.unit_type`, `assessment.*` |
| 03_DoKho | Thay taxonomy bài bán bằng taxonomy bài thuê |
| 04_KienTruc | B1–B4 → E1–E3; thêm M8, M9 |
| 05_GiaoDien | Panel nhận định (extension), màn Thị trường, S6 hạ xuống Could |
| 06_DanhGia | Thêm bảng RQ4 (trung vị từ nhãn tay vs từ hệ thống, có công thức sai lệch %) |
| 07_KienThuc | Thêm K12: TF-IDF/cosine và phân cụm (bài 05–06), thống kê bền (trung vị, IQR); thêm câu vấn đáp về RQ4 và "trung bình thị trường" |
| 08_KeHoach / 09_PhanCong | Thay việc của bot Playwright; thêm việc kho, thống kê, màn Thị trường, RQ4; cân lại khối lượng |
| 10_RuiRo | Thêm 4 rủi ro mới (mục 2, dòng 4.6) |
| 11_NguonTK | Đồng bộ với tài liệu tham khảo của docx |

## 4. Hình cần vẽ lại

1. **Hình 1 – Kiến trúc:** thay khối Bot B1–B4 bằng Extension (Thu thập / Nhận định); thêm Kho thị trường, M8, M9; thêm màn Thị trường.
2. **Hình 2 – Wireframe:** bài thuê có bôi màu cả giá thuê lẫn các khoản phí; thẻ nhận định "cao hơn x% so với trung vị N bài tương tự", kèm N, IQR và 3 bài tương tự.
3. **Hình 3 – Gantt:** theo kế hoạch mới.

## 5. Quyết định nhóm cần chốt trước khi sửa

1. **Cơ sở trường và 3–5 phường xung quanh** — để ghi phạm vi, dựng từ điển địa danh và viết ví dụ cho đúng.
2. **Có thêm nhãn phụ FEE không?** Khuyên **có**: việc tách giá thuê khỏi các khoản phí trở thành thứ đo được bằng P/R/F1, đúng điểm khó nhất của bài thuê; 4 trường chính của đề giữ nguyên.
3. **Bỏ hẳn Playwright hay giữ làm phương án dự phòng?** Khuyên **bỏ**: extension đảm nhận cả 2 chế độ, giảm việc cho TV4 để bù cho phần kho và nhận định.

## 6. Rủi ro tiến độ

- **Việc thêm vào:** kho thị trường, gộp trùng, thống kê, panel nhận định, màn Thị trường, phân tích RQ4.
- **Việc bớt đi:** toàn bộ bot Playwright (lịch chạy, phiên đăng nhập).
- **Đề xuất cân lại:**
  - Hạ S6 HITL xuống Could; giữ S3 So sánh vì đó là bằng chứng NLP.
  - Kho thị trường chỉ cần đủ cho **vài nhóm tương tự có N ≥ 10** để demo; không cần phủ mọi phường.
  - Phân tích RQ4 chỉ làm trên tập chuẩn (không tốn thêm công gán nhãn).
