# Log xuất bản GitHub

## L0 — nhận yêu cầu và chọn cách tổ chức

12/10/2026. Dùng admin theo nhánh tiếp nối, làm tuần tự. GitHub CLI đã đăng nhập VoDucNhatku; tên rener-vn-research-handbook chưa tồn tại. TMG301 chưa là Git repo, nên tạo bản xuất riêng trong TMG301 để không đưa nhầm toàn bộ source/dependency của KusShoes lên remote mới. Chọn private mặc định, đã báo người dùng. Chưa tạo remote.

## L1 — kiểm kê và xác định phạm vi

12/10/2026. Rà notes, project-realestate-ner, báo cáo local KusShoes và các file tổng hợp/generator ở gốc. notes có cả clone ChoThueGiupViec và snapshot bên ngoài; project-realestate-ner có dependency Python phục vụ dựng reader. Các phần này không phải kiến thức do dự án tự viết. Giữ báo cáo/ghi chú, proposal các phiên bản, log/audit, script tự tạo, reader và bằng chứng giao diện; giữ nguồn dẫn URL/commit/hash. Dữ liệu chạy local, tiến trình, env, credentials, binary và package cài sẵn không thuộc bản xuất.


## L2 — tổ chức lớp đọc và giữ nội dung nghiên cứu

12/10/2026. Bản xuất ban đầu gồm 147 file nhập khoảng 6 MB. Thêm README, lộ trình 6 lượt đọc, bản đồ 12 mảng, status, workflow, packaging, roadmap, changelog và notice. Catalog hiện liệt kê 46 tài liệu nghiên cứu/điều hướng nguồn; sổ nguồn tổng hợp 179 bản ghi metadata/163 URL khác nhau và liên kết trong các bài phân tích. Những con số này không chứng minh đã đọc trọn mọi nguồn. 14 tham chiếu repo được nối tới commit nguồn đã kiểm, hai tài nguyên local còn có trang giải thích.

## L3 — quy trình GitHub và kiểm bản xuất

12/10/2026. Thêm issue/PR template, CODEOWNERS, task/decision/experiment template và hai script Python chuẩn tạo danh mục/kiểm tài liệu. Có workflow mẫu chưa kích hoạt vì token CLI hiện không có scope workflow. Chưa có branch protection hoặc CI run; không ghi badge xanh. Kiểm file/link/manifest, bảo toàn bảy proposal gốc, rà pattern credential và kiểm tình huống lỗi giả cho chính validator trước khi push. Bản before và snapshot verification lịch sử được giải thích tách khỏi kết quả kiểm bản xuất.


## L4 — tạo remote và backlog

12/10/2026. Đã tạo repo private VoDucNhatku/rener-vn-research-handbook, push main thành công với commit đầu a648c5a3b6a39250a3d05fb6f44b7428645df6c1. Bản đầu có 198 file tracked. Cấu hình mô tả, năm topic, Issues và tự xóa branch sau merge; tạo nhãn research/correction/decision và bốn issue mở về nghĩa giá, protocol đánh giá, quyền nguồn và walkthrough KusShoes. Không tạo fake lịch sử nghiên cứu, PR hoặc kết quả thực nghiệm.

## L5 — kiểm bản clone và trạng thái GitHub

12/10/2026. Clone thật từ remote private vào thư mục kiểm riêng và chạy validate_docs.py: 110 Markdown, 845 link local, 147 file nhập, bảy proposal gốc; không có error/warning. Rà 28 bản forensic theo chính sách riêng; không kiểm link của các bản before lịch sử. API GitHub xác nhận private, main, bốn issue mở, branch protection=false và chưa có Actions workflow hoạt động. Giới hạn này được ghi trong WORKFLOW; mẫu CI chưa phải CI run.

Bổ sung thông tin bàn giao, chỉ mục và log vào commit tiếp theo; kiểm lại tài liệu rồi đồng bộ commit cuối. Kết quả kiểm Markdown/file không xác nhận app, NLP, nguồn thật, quyền pháp lý hoặc tải production.
