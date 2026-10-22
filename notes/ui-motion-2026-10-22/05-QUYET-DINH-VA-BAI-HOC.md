# Quyết định thiết kế và bài học khi dựng giao diện ReNER

[Về chặng](README.md)

## 1. Vòng 1 — "bút dạ quang trên giấy"

**Ý tưởng:** nhãn NER (GIÁ · DT · VT · PN · PHÍ) là chất liệu chính của sản phẩm. Hình 2 trong proposal v1.3 đã vẽ đúng kiểu này, nhãn chữ nằm phía trên đoạn bôi màu. Từ đó ra hệ thống:

- mỗi nhãn một màu bút dạ quang, **luôn kèm chữ nhãn** để người mù màu vẫn đọc được;
- một màu nhấn mực xanh `#2337C6` (chữ trắng trên nền này đạt 8,9:1);
- nền giấy ấm, tiêu đề serif Newsreader, thân Be Vietnam Pro.

**Hero code:** bài đăng là vật thể chính đi qua 4 nhịp, như chiếc giày của KusShoes.

**Đã thực nghiệm:** chụp Playwright từng nhịp ở 1440 × 900 và mobile 390 px. Hai lỗi đã sửa: chữ "đ" của giá bị rớt dòng, thẻ "Đã chuẩn hóa" che bài đăng.

## 2. Vòng 2 — sửa theo 10 repo skill

Đối chiếu với [10 repo UI/UX](03-REPO-UI-UX-VA-3D.md) cho thấy vòng 1 trùng các dấu hiệu "AI slop": nền kem, serif, kẻ dòng mảnh, eyebrow chữ hoa, đánh số 01–04, mũi tên "→", hiện dần ở mọi section.

Quyết định:

- giữ bút dạ quang vì nó gắn với chủ đề thật;
- bỏ hết các chi tiết chỉ để làm dáng;
- dồn độ táo bạo vào một khoảnh khắc: chồng giấy 3D ở hero;
- hover chỉ bật khi dùng chuột;
- thêm nút dừng cho dải chữ chạy;
- style `::selection` thành màu dạ quang, focus ring hai lớp đọc được trên cả nền sáng và nền tối.

**Bài học (Đề xuất):** trước khi dựng, viết 4–6 mã màu và hướng thiết kế rồi tự hỏi "đây có phải mặc định của AI không". Khi hướng thiết kế trùng một dấu hiệu slop, nó chỉ được giữ nếu bắt nguồn từ nội dung sản phẩm.

## 3. Vòng 3 — câu chuyện ghim 6 nhịp

Chủ dự án hỏi: "đây mới là lớp ngoài phải không, như cái giày còn mấy lớp nữa?" (**Người dùng xác nhận** mong muốn: có nhiều lớp, có 3D, như KusShoes).

| Nhịp | Vật thể | Ý nghĩa sản phẩm |
|---|---|---|
| 1 Bài gốc | Bài nghiêng 3D bên phải | Bài cho thuê lộn xộn |
| 2 Che thông tin | Vệt quét; số điện thoại và tên đổi thành `[SĐT]`, "Người đăng đã ẩn" | Extension che trên máy trước khi gửi |
| 3 Gán nhãn | Quay isometric, tách 3 lớp theo `translateZ` | Văn bản / nhãn BIO / số chuẩn hóa |
| 4 Chuẩn hóa | Nhãn bay vào phiếu giá; giá đếm tới 5.500.000 đ | Regex + LLM → code đổi số, phí đứng riêng |
| 5 So sánh | 14 chấm bay từ 3D về trục giá, chấm "Tin này" bay vào | Trung vị, P25–P75, N |
| 6 Kết luận | Thẻ nhận định "đóng dấu"; 5 bài mẫu bấm thử | Tương đương đổi colorway; có cả ca "Giá ib" và "Chỉ 7 tin" |

Khi giảm chuyển động, màn hẹp hoặc trình duyệt không hỗ trợ, cùng nội dung xếp dọc. Ở chế độ canvas (không cuộn), artboard hiện khung cuối.

**Chưa biết:** hiệu ứng có chạy đúng trong chế độ Play của Claude Design hay không. Tác giả không tự mở để kiểm, theo quy định của loại artifact; chờ chủ dự án xem.

## 4. Review extension `tro` của nhóm

Đọc toàn bộ `extension/`, chạy `npm test`: **48/48 pass** (Đã thực nghiệm, 22/10/2026). Đối chiếu với đặc tả extension của repo sản phẩm:

- **Tốt:**
  - nhận diện bài bằng MutationObserver;
  - loại bình luận, không trộn hai bài;
  - mở "Xem thêm" đúng một lần, có giới hạn thời gian chờ;
  - chống trùng trong IndexedDB bằng một transaction;
  - không gửi dữ liệu ra mạng, quyền khai báo hẹp;
  - có trang HTML mẫu để test.
- **Thiếu so với đặc tả:**
  - chưa che số điện thoại;
  - tự chạy, không có công tắc Thu thập;
  - không có danh sách nhóm cho phép;
  - không giới hạn 50 bài;
  - không dừng khi Facebook đòi xác minh;
  - lưu link ảnh;
  - bỏ bài chưa mở được "Xem thêm" thay vì gửi với `text_complete = false`;
  - chưa có thời gian đăng, tên nhóm;
  - chưa đúng schema `ingest-post`;
  - chưa gửi API;
  - chưa có chế độ Nhận định.
- **Rủi ro riêng tư:** `samples/collector-observation.json` có tên và số điện thoại thật. Hai fixture HTML có tên người đăng và link ảnh CDN thật. Cần ẩn danh và xóa khỏi lịch sử git trước khi công khai.
- **Lệch kiến trúc:** `blueprint.md` của extension đặt bước xử lý và trích xuất ở máy từng người. Repo sản phẩm đặt bước này ở backend. Nhóm cần chốt một hướng. Tác giả đề xuất theo repo sản phẩm, vì khóa LLM không được nằm trong extension.

Thứ tự sửa đề xuất: che SĐT + ẩn danh mẫu → xuất JSON đúng schema → công tắc, danh sách nhóm, giới hạn, dừng khi xác minh → gửi API và chế độ Nhận định. Chờ chủ extension đồng ý, theo `AGENTS.md` của repo đó.

## 5. Đưa dữ liệu thật vào giao diện mà không vi phạm luật

**Yêu cầu:** dùng dữ liệu extension cho demo.

**Ràng buộc** từ `AGENTS.md` và `data/README.md` của repo sản phẩm: không commit dữ liệu thật.

Cách làm (**Đã thực nghiệm**):

- File local `data/demo/extension-sample.json` (thư mục `data/` bị git bỏ qua).
- Chỉ giữ chữ bài và link bài, bỏ tên người đăng và link ảnh.
- Web che số điện thoại thêm một lần khi nạp.
- Nhãn gán tay dạng đoạn trích; đoạn không tìm thấy trong chữ bài thì bỏ. Đây là cùng luật áp cho LLM.
- Thẻ tin có nhãn "Bài thật · đã che SĐT" hoặc "Ví dụ tự tạo"; lọc bằng `?nguon=that`.

**Kết quả:** cả 7 bài đều là bản cắt dở, không có giá hay diện tích. UI hiện đúng "Chưa có giá", "Chưa rõ", "Bài không ghi giá, chưa so sánh được".

Đây là bằng chứng thực tế cho hai điều:

- extension phải mở được "Xem thêm" trên Facebook thật thì dữ liệu mới dùng được cho thống kê;
- giao diện đã xử lý được trạng thái thiếu dữ liệu.

## 6. Bài học về cách làm việc

1. **Hỏi "cái giày có mấy lớp" sớm hơn.** Bản đầu chỉ là lớp ngoài vì tác giả hiểu "học KusShoes" là học style. Lần sau, hỏi người dùng thích phần nào của tham chiếu (bố cục, chuyển động hay cảm giác) trước khi dựng.
2. **Bản xem trước trên canvas trước, code sau.** Chủ dự án muốn nhìn và sửa trực tiếp. Claude Design cho làm vậy mà chưa đụng repo.
3. **Tách sản phẩm và tư duy.** Chủ dự án chốt: repo `rener-vn` chỉ chứa sản phẩm, handbook chứa cách làm (**Người dùng xác nhận**, 22/10/2026).
4. **Quyền GitHub là một bước của công việc.** Push bị 403 cho tới khi cài Claude GitHub App. Repo private của người khác (extension) cần chính chủ mở hoặc gửi zip.
5. **Không thể "cài hộ" trên máy người dùng từ máy ảo cloud.** Thay bằng script cài đặt bấm đúp. Script này chưa chạy thử trên Windows: **NOT RUN**.
