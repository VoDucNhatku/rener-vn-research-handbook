# Báo lỗi có dữ liệu nhạy cảm

Không dán token, mật khẩu, nội dung tin thuê thật hoặc thông tin cá nhân vào issue. Nếu phát hiện secret đã commit, ngừng sử dụng và thu hồi/đổi secret trước; xóa khỏi commit mới không tự xóa lịch sử Git hoặc các bản clone.

Với lỗi trong handbook, mô tả đường dẫn, phạm vi và ví dụ giả lập cho chủ repository. Đây là repo nghiên cứu; chưa có dịch vụ ReNER vận hành để cam kết SLA hoặc quy trình xử lý incident production.

`scripts/validate_docs.py` có kiểm tên file/pattern thông tin nhạy cảm ở dạng phổ biến. Nó không chứng nhận rằng không còn secret, không kiểm mọi nội dung binary và không thay review trước khi mở public.
