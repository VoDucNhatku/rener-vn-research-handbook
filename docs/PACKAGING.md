# Phạm vi bản xuất GitHub

[README](../README.md) · [Manifest nhập](../evidence/import-manifest.json) · [Danh sách loại trừ](../evidence/excluded-files.json)

Repo này là bản xuất nghiên cứu từ TMG301, có lớp điều hướng/quy trình mới. Workspace gốc vẫn giữ nguyên tài liệu nguồn và runtime; đây không phải chuyển toàn bộ thư mục máy tính thành Git repo.

## Được đưa lên

Báo cáo/ghi chú do dự án viết; proposal các phiên bản PDF/DOCX/XLSX; sổ kiến thức và bản thảo; log/audit/bản trước sửa; nguồn metadata/URL/commit/hash; reader HTML và bằng chứng kiểm giao diện; script nghiên cứu, lab và helper local tự tạo. Tên file nghiên cứu được giữ để đọc chéo và truy nguồn.

`evidence/import-manifest.json` ghi từng file nhập, hash gốc, hash của bản xuất và trạng thái có đổi hay không. Các tài liệu điều hướng/quy trình sinh riêng cho GitHub không được tính là tài liệu nhập cũ.

## Giữ ở workspace gốc hoặc đọc ở nguồn gốc

Full clone KusShoes/ChoThueGiupViec; source snapshot/code/HTML/paper của bên khác; slide/giáo trình đầu vào bên ngoài; dependency, cache, package/runtime; dữ liệu PostgreSQL/Redis; file env, token và trạng thái tiến trình. Không có dataset tin Facebook thật trong bản xuất.

Nguồn tham khảo được giữ qua [sổ nguồn tập trung](SOURCES.md) và manifest lịch sử. Các link source local có nguồn đã biết được nối sang URL gốc; tài nguyên local không có URL xác minh được có trang giải thích rõ. Việc không tái phân phối full snapshot không làm mất phần phân tích do dự án viết.

## Chỉnh gì khi xuất bản?

Loại giá trị mật khẩu demo local đã xuất hiện trong một số ghi chú; sửa link máy/local để đọc được trên GitHub; ghi các điều chỉnh trong [export-adjustments](../evidence/export-adjustments.json). Proposal gốc giữ byte/hash. Những fingerprint lịch sử mô tả workspace lúc kiểm, không phải mọi file sau chuyển link/redaction.

Các bản `notes/audit-2026-10-11/before/` giữ nội dung cũ để so sánh, không phải tài liệu hiện hành. Link trong bản forensic này có thể phụ thuộc cây thư mục cũ; checker ghi rõ loại trừ khỏi kiểm điều hướng hiện hành. Xem báo cáo audit trước khi dùng bất kỳ khẳng định cũ nào.

## Script nào chạy được trên clone mới?

`scripts/validate_docs.py` và `scripts/build_catalog.py` dùng Python chuẩn, là công cụ của repo xuất bản. Các script cũ `verify_research.py`, `verify_documents.py`, fetch/build/handbook/lab và helper `KusShoes/.local/` được giữ để truy cách làm; chúng có thể cần source snapshot, thư viện, model, clone gốc hoặc runtime trên máy nghiên cứu. Không chạy hàng loạt chúng trong CI và không cam kết clone handbook sẽ khởi chạy KusShoes/ReNER.

Không copy các thư mục dependency để làm mất dấu yêu cầu môi trường. Không xóa tài liệu gốc khi chuyển lên GitHub. Repo chưa có giấy phép chung cho toàn bộ nội dung: xem [NOTICE](../NOTICE.md).
