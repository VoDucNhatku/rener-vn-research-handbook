from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
changes = []

def edit(name, replacements, prefix=None, suffix=None):
    p = ROOT / name
    s = p.read_text(encoding='utf-8-sig')
    for old, new in replacements:
        assert old in s, f'Missing expected text: {name}: {old[:100]}'
        s = s.replace(old, new)
    if prefix:
        a, b = s.split('\n', 1)
        s = a + '\n\n' + prefix + '\n' + b
    if suffix:
        s = s.rstrip() + '\n\n' + suffix + '\n'
    p.write_text(s, encoding='utf-8')
    changes.append(name)

edit('TMG301_TongHopKienThuc.md', [
('Dưới đây là hệ thống hóa chi tiết toàn bộ các mảng kiến thức của môn học:', 'Dưới đây là bản đồ khái quát theo cấu trúc học liệu, không phải bản xác nhận đã kiểm tra đầy đủ từng slide hay toàn bộ nội dung thi.'),
('Perplexity càng thấp, mô hình dự đoán càng tốt.', 'Perplexity thấp hơn biểu thị xác suất tốt hơn trên cùng dữ liệu đánh giá và cách tính tương thích. Tokenizer, đơn vị token, xử lý ngữ cảnh và corpus ảnh hưởng chỉ số; không so trực tiếp hai số từ các điều kiện khác nhau, cũng không dùng nó thay chất lượng tác vụ. [Hugging Face](https://huggingface.co/docs/transformers/perplexity).'),
('**hoàn toàn độc lập** với nhau (trong cùng một nhãn phân loại)', '**độc lập có điều kiện khi đã biết nhãn**; đây là giả định của mô hình, không phải sự thật về ngôn ngữ'),
('Từ có ý nghĩa giống nhau sẽ có vector gần nhau.', 'Các từ có ngữ cảnh phân bố tương tự thường có vector gần nhau; gần nhau không bảo đảm đồng nghĩa, vì từ trái nghĩa cũng có thể xuất hiện trong ngữ cảnh tương tự.'),
('Thay thế hoàn toàn RNN/LSTM, xử lý câu song song, không bị hạn chế bởi độ dài chuỗi dài.', 'Transformer gốc dùng attention thay recurrence trong kiến trúc của nó; điều này không có nghĩa mọi bài toán đã thay RNN/LSTM. Có thể tính nhiều vị trí song song khi huấn luyện, nhưng giải mã tự hồi quy vẫn sinh lần lượt. Full self-attention có chi phí bậc hai theo chiều dài chuỗi (với chiều biểu diễn cố định); context và bộ nhớ vẫn hữu hạn. [Vaswani et al., §3–4](https://arxiv.org/html/1706.03762v7).'),
('Dùng thuật toán tìm cây bao trùm nhỏ nhất (Minimum Spanning Tree).', 'Với mô hình cộng điểm trên cạnh, tìm cây phụ thuộc có tổng điểm lớn nhất: maximum spanning arborescence trên đồ thị có hướng. Có thể chuyển thành bài toán cực tiểu nếu đổi dấu điểm thành chi phí; không mặc định là cây bao trùm nhỏ nhất vô hướng. [Shimizu, CoNLL 2006](https://aclanthology.org/W06-2936/).'),
], prefix='> Rà soát 11/10/2026: sửa các diễn giải về Transformer, dependency parsing và điều kiện so sánh perplexity. Đây là ghi chú học tập, chưa được chứng nhận là tài liệu đầy đủ của môn. [Chi tiết phản biện](notes/audit-2026-10-11/BAO-CAO-PHAN-BIEN.md).')

edit('notes/08-fine-tuning-mlm-summary.md', [
('thường giữ nguyên kiến trúc và tham số gốc, chỉ thích nghi cho các tác vụ', 'giữ trọng số pre-trained làm điểm khởi tạo, có thể thay head rồi cập nhật một phần hoặc toàn bộ trọng số cho các tác vụ'),
('Đây là bằng chứng BERT gốc được pre-train bằng **hai** mục tiêu là MLM và NSP, dù slide chỉ nhắc MLM (\\*).', 'Checkpoint có head NSP là dấu hiệu phù hợp với kiến trúc; căn cứ cho hai mục tiêu **MLM và NSP** của BERT gốc là [bài báo BERT, §3.1](https://aclanthology.org/N19-1423/), không chỉ riêng tên key trong log (\\*).'),
('câu "GPT-3 thường không fine-tune" đúng về **thói quen dùng**: người ta chủ yếu dùng prompting / in-context learning. Tuy vậy, không nên hiểu là "không thể fine-tune". Nếu thi, trả lời theo slide; khi phỏng vấn, nói thêm sắc thái này.', 'câu "GPT-3 thường không fine-tune" là cách trình bày trong slide; file này không có số liệu để xác nhận tần suất sử dụng thực tế, đặc biệt ở thời điểm hiện tại. Phân biệt prompting/in-context learning với cập nhật trọng số; không suy ra "không thể fine-tune".'),
('Lúc fine-tune và suy luận, token `[MASK]` **không bao giờ xuất hiện**.', 'Trong các tác vụ downstream thông thường không dùng masking, input không có `[MASK]`; riêng suy luận fill-mask vẫn dùng token này.'),
('Input encoding (tokenize + embedding) → Masking → Forward pass qua các encoder → Prediction tại các vị trí `[MASK]` → Loss calculation (so với từ gốc) → giảm loss.', 'Tokenize → chọn vị trí mục tiêu và thay token theo 80/10/10 → embedding + encoder → dự đoán ở mọi vị trí được chọn → loss với token gốc ở các vị trí đó → cập nhật trọng số. Loss gồm cả token được giữ nguyên hoặc thay ngẫu nhiên, không chỉ những vị trí đang mang `[MASK]`.'),
('BERT dự đoán các vị trí bị che **độc lập** với nhau', 'trong một lượt forward, các head dự đoán cùng dựa trên ngữ cảnh đã che và không tự điều kiện hóa trên đáp án vừa sinh ở mask khác'),
], prefix='> Rà soát 11/10/2026: đối chiếu script và log lưu ở `08-assets`; các con số 0,7384/0,5003/0,6198 và 21/60 có trong log lịch sử, chưa chạy lại training trong lượt audit này. Đã sửa diễn giải trọng số, masking và mức bằng chứng. [Báo cáo](audit-2026-10-11/BAO-CAO-PHAN-BIEN.md).')

edit('notes/kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md', [
('đóng góp công khai là hành động riêng', 'đóng góp vào catalog nội bộ là hành động riêng'),
('quyền riêng tư/công khai', 'quyền cá nhân/công bố nội bộ'),
('“duyệt công khai”', '“duyệt công bố nội bộ”'),
('duyệt và snapshot được phép công khai', 'duyệt và snapshot được phép công bố nội bộ'),
('ai được công khai tin', 'ai được công bố tin vào catalog nội bộ'),
('  Running --> NeedsReview: lưu kết quả hợp lệ', '  Running --> Succeeded: lưu kết quả xử lý hợp lệ'),
('  NeedsReview --> Done: người dùng xác nhận\n', ''),
('Ví dụ học tập cho một job trích xuất, không phải đặc tả mới đã chốt:', 'Ví dụ học tập cho **một lần thực thi job**, không phải toàn bộ đặc tả retry/cancel. `Succeeded` chỉ nghĩa xử lý xong; candidate review có vòng đời riêng (`pending → approved | rejected`). Người dùng xem/xác nhận kết quả không làm job mới thành công. Chi tiết concurrency theo bản thảo v0.2 §6.4 và §16.5.'),
], prefix='> Hiệu chỉnh 11/10/2026 sau phản biện: ví dụ ReNER áp dụng pilot có tài khoản và **catalog nội bộ**, không ngầm mở dữ liệu thật ra Internet. Job và review tách state. Xem [bối cảnh hiện hành](../HIEN-TRANG-VA-QUYET-DINH.md); các ví dụ vẫn chưa triển khai.')

edit('notes/kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md', [
('Phân tích cá nhân khác đóng góp công khai', 'Phân tích cá nhân khác đóng góp vào catalog nội bộ'),
('catalog hoặc thống kê công khai', 'catalog hoặc thống kê dùng chung nội bộ'),
('S4 — đóng góp và duyệt để công khai', 'S4 — đóng góp và duyệt vào catalog nội bộ'),
('Một tin đủ điều kiện vào tập công khai', 'Một tin đủ điều kiện vào catalog nội bộ'),
('Tin riêng không tự trở thành tin công khai.', 'Tin riêng không tự trở thành tin dùng chung nội bộ; công bố ngoài Internet là thay đổi phạm vi riêng.'),
], prefix='> Hiệu chỉnh 11/10/2026: “publication” trong ví dụ ReNER là công bố **nội bộ cho tài khoản có quyền**, theo bản thảo v0.2. [Bối cảnh và quyết định hiện hành](../HIEN-TRANG-VA-QUYET-DINH.md).', suffix='## Bổ sung sau phản biện: S0 cần trả lời gì trước khi chia feature?\n\nChọn một điểm có thể làm hỏng toàn bộ giá trị, không mặc định bắt đầu bằng dựng auth hay dashboard: có nguồn được phép; lấy đủ một tin; phân biệt giá/phí/đơn vị; sau lọc còn đủ tin so sánh; người dùng hiểu kết quả. Mỗi thử nghiệm ghi giả định, ví dụ, quan sát và quyết định tiếp tục/thu hẹp. Có thể dùng fixture để kiểm kỹ thuật, nhưng không dùng fixture chứng minh nguồn thật hoặc độ chính xác ngoài đời. Đây là đề xuất thứ tự học; chưa tạo task hay chạy thử nghiệm.')

edit('notes/design-rener-vn-waterfall.md', [
('    DOMAIN --> DB[(PostgreSQL: dữ liệu, revision, jobs, snapshot)]', '    UC --> REPO[Repository và transaction]\n    READ --> REPO\n    REPO --> DB[(PostgreSQL: dữ liệu, revision, jobs, snapshot)]'),
('    NLP --> DB', '    NLP --> SAVE[Use case lưu kết quả: kiểm lease, revision, hủy]\n    SAVE --> DOMAIN\n    SAVE --> REPO'),
], prefix='> Đính chính sơ đồ 11/10/2026: mục 16.1 sửa mũi tên để khớp quy tắc mục 16.2 — domain thuần không truy cập DB; use case/repository điều phối I/O. Không đổi lựa chọn stack hoặc phê duyệt baseline v0.2. Xem [bối cảnh hiện hành](HIEN-TRANG-VA-QUYET-DINH.md) và [phản biện](audit-2026-10-11/BAO-CAO-PHAN-BIEN.md).')

edit('project-realestate-ner/notes/01-research-report.md', [
('Span-level: P/R/F1 strict & partial (thư viện `seqeval`).', 'Span-level: strict P/R/F1 với quy ước BIO và ranh giới thống nhất. `seqeval` có default/strict, không đồng nghĩa hai chế độ strict/partial overlap. Nếu báo partial, phải định nghĩa matching/credit riêng và kiểm bằng ca tay; không dùng nó thay strict. [README seqeval](https://github.com/chakki-works/seqeval).'),
('Cao nhất trong thời gian ngắn `[suy luận]`', 'Giả thuyết có lợi trong phạm vi hẹp; chưa có benchmark nội bộ'),
('Cao, nhưng cần ≥300 bài gán nhãn `[suy luận]`', 'Chất lượng và nhu cầu nhãn phải đo qua pilot/learning curve; chưa có ngưỡng đủ chung'),
('cần: tập chuẩn ≥300 bài, công bố bộ dữ liệu đã ẩn danh, thêm baseline học có giám sát (CRF/PhoBERT), kiểm tra tính mới bằng tổng quan có hệ thống.', 'cần kiểm yêu cầu cụ thể của venue, quyền dữ liệu, chất lượng thực nghiệm, baseline phù hợp và tính mới. Không có điều kiện chung “≥300 bài là đủ”; không bắt buộc công bố raw corpus khi không có quyền. CRF/PhoBERT là ứng viên so sánh khi phù hợp RQ và tài nguyên, không phải nghĩa vụ mới của demo.'),
], prefix='> Tài liệu nghiên cứu lịch sử 03/10/2026. Đính chính 11/10: bỏ khẳng định Hybrid chắc tốt nhất/ngưỡng 300 bài chung; sửa cách gọi metric seqeval. Các số liệu prior work và pháp lý trong phần cũ chưa được thẩm định lại toàn bộ ở lượt này; dùng sổ nguồn foundation ngày 09/10 cho đối chiếu mới hơn. [Phạm vi hiện hành](../../notes/HIEN-TRANG-VA-QUYET-DINH.md).')

edit('project-realestate-ner/notes/claims-ledger.md', [], suffix='## Đính chính 11/10/2026\n\nC-1 được giữ để truy lịch sử, nhưng điều kiện “≥300 bài + bắt buộc công bố dataset + CRF/PhoBERT” ở cột venue **không còn là khuyến nghị hiện hành**. Không có ngưỡng phổ quát bảo đảm công bố; yêu cầu venue, RQ, sai số ước lượng và quyền dữ liệu quyết định thiết kế thực nghiệm. C-2 là hướng nghiên cứu mở rộng, không tự thay scope demo. [Bối cảnh hiện hành](../../notes/HIEN-TRANG-VA-QUYET-DINH.md).')

print('\n'.join(changes))
