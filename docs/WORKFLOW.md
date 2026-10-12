# Quy trình nghiên cứu, chia việc và kiểm thay đổi

[README](../README.md) · [Đóng góp](../CONTRIBUTING.md) · [Task mẫu](../templates/TASK.md)

## 1. Giai đoạn và đầu ra

| Giai đoạn | Đầu ra cần nhìn được | Điều kiện chuyển bước |
|---|---|---|
| Hiểu đề / discovery | Actor, nhu cầu, dữ liệu/nguồn, phạm vi, giả định | Nói được vấn đề cần giải và chưa biết gì |
| Yêu cầu | Luật, ví dụ đúng/sai/thiếu thông tin, ưu tiên lõi | Các quyết định ảnh hưởng nghĩa/quyền được làm rõ |
| Thiết kế trên giấy | Flow, state, ownership, dữ liệu/API, quyền, lỗi và cách phục hồi | Lần được một hành trình trọn vẹn cùng nhánh lỗi |
| Chuẩn bị triển khai | Task nhỏ, acceptance, phạm vi tự chủ AI, cách kiểm | Không còn câu hỏi nghiệp vụ quyết định task nhưng chưa chốt |
| Thực hiện | Thay đổi trong branch, diff dễ đọc và bằng chứng phù hợp | Kết quả khớp tiêu chí; các phần chưa thử được nêu rõ |
| Review / bàn giao | Review, kiểm hồi quy liên quan, log, điều kiện khôi phục | Chủ dự án hiểu thay đổi và giới hạn của nó |

Hiện repo ở các giai đoạn nghiên cứu/yêu cầu/thiết kế trên giấy. Thêm backlog không phải lệnh cho AI tự viết app.

## 2. Luồng Git cho một người

Một vấn đề có mục tiêu rõ → issue → branch → các commit có nghĩa → PR → kiểm tài liệu/kết quả liên quan → review → merge → cập nhật log. Nếu sửa lỗi chữ đơn giản, không cần dựng cả thủ tục lớn. Với thay đổi nghĩa giá, quyền, dữ liệu hoặc metric, dùng đầy đủ task/decision và kiểm ảnh hưởng.

Tên branch gợi ý: `research/price-semantics`, `docs/fix-evidence-state`; commit gợi ý: `docs: clarify rent basis`. Đây là quy ước, không phải branch đã tồn tại. Main giữ bản đọc nhất quán; không ghi secret vào bất kỳ branch nào.

Pull request trả lời bốn câu: vấn đề gì, thay gì, bằng chứng nào, còn giới hạn gì. [PR template](../.github/pull_request_template.md) giúp nhớ, không bắt điền dữ liệu giả cho đủ ô. CODEOWNERS chỉ định người review mặc định; chưa có branch protection thì không được coi nó là cổng bắt buộc.

## 3. Quyền tự chủ của AI

AI được tự chọn chi tiết dễ đảo trong phạm vi: tổ chức đoạn giải thích, tên biến nội bộ, cách trình bày ví dụ. Khi thay nhu cầu, nghĩa dữ liệu, quyền công bố, ngân sách dịch vụ hoặc điều kiện nghiệm thu, AI phải trình bày quyết định và tác động để chủ dự án chọn. Không hỏi lại việc đã được ủy quyền trong phiên.

Test do AI viết cần truy về ví dụ nghiệp vụ. Nếu agent sửa expected hoặc đổi rule để test xanh, review phần thay đổi đó trước khi chấp nhận. Model/evaluator đồng ý với nhau chưa là bằng chứng độc lập.

## 4. Khi thay tính năng lõi

Ghi change request: yêu cầu cũ/mới → lý do → ví dụ → tác động lên dữ liệu/API/UI/job/cache/quyền/test/tài liệu → kế hoạch chuyển đổi → điều kiện quay lại. Ví dụ chuyển rent sang total cost cần thông tin phí và mức dùng; thiếu phí không tự thành 0.

Phân biệt bug với đổi yêu cầu. Revert Git xử lý phiên bản code/tài liệu; không tự phục hồi DB, xóa side effect ngoài hoặc trả lại dữ liệu đã mất. Chưa triển khai thì làm impact map trên giấy; có implementation mới diễn tập migration/rollback phù hợp.

## 5. Ghi nguồn và nhật ký

Nguồn mới ghi URL, ngày, phần đã đọc, claim được hỗ trợ, phần mình suy luận và giới hạn. Sau mỗi phân vùng việc, log đầu vào → công việc → kết quả → bằng chứng → việc còn mở. Không dùng số tài liệu hoặc số token làm thước đo hoàn thành.

Log dài theo chặng nằm ở `notes/kusshoes-to-rener-vn/WORK_LOG.md`; việc xuất bản GitHub nằm ở `notes/github-publication-2026-10-12/`. Khi thay luật, ưu tiên sửa nơi sở hữu luật rồi liên kết, tránh sao chép cùng một đoạn qua nhiều sổ tay.

## 6. Kiểm trước push

Chạy `python scripts/validate_docs.py`, xem `git diff --check`, đọc lại diff của các ví dụ/claim bị đổi. Nếu sửa danh mục hoặc thêm tài liệu, chạy `python scripts/build_catalog.py` trước kiểm. Bằng chứng NLP/UX/vận hành phải kiểm riêng; script tài liệu không chứng minh chúng.

Workflow Actions được cung cấp ở [mẫu kiểm tài liệu](workflow-templates/check-docs.yml). Bản xuất đầu không kích hoạt Actions: phiên GitHub CLI hiện có quyền `repo` nhưng không có scope OAuth `workflow` để tạo/sửa workflow. Có thể cấu hình sau bằng tài khoản có quyền thích hợp; không ghi token vào repository. Lệnh local đã đủ để kiểm nội dung bàn giao hiện tại. Không gắn badge CI xanh khi chưa có run.
