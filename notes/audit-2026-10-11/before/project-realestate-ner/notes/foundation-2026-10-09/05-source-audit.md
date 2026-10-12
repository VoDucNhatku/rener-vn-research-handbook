# Audit nguồn và claims — snapshot 09/10/2026

Áp dụng hallucination-guard, kiểm tra `KIEN-THUC-NEN-TANG-RENER-VN.md` §§9, 19, 25, 31 và toàn bộ `BAO-CAO-HIEU-DE-TAI.md`. **Kết quả: PASS có giới hạn về claims học thuật**, không xác nhận hệ thống chạy, độ chính xác, quyền thu dữ liệu hay khả năng công bố. Hai điểm trạng thái/lịch đã được kiểm tra lại sau xử lý của tác giả tổng hợp. Audit không sửa hai tài liệu chính.

## Claims đối chiếu được

| Nhóm claim | Bằng chứng và kết luận |
|---|---|
| CRF/PhoBERT, §9 | CRF gốc là mô hình nhãn có cấu trúc; PhoBERT là encoder tiếng Việt dùng dữ liệu tách từ. Baseline được ghi đề xuất, chưa tuyên bố thắng. PASS. [CRF postprint](https://web.cs.ucla.edu/~yzsun/classes/2014Spring_CS7280/Papers/Probabilistic_Models/crf_sequence.pdf), [PhoBERT](https://aclanthology.org/2020.findings-emnlp.92/). |
| Prior work, §31 | NICS 2021, Access 2022 và SEND 2022 có thật; title/DOI trong bảng không nhầm. Bản Access là toàn văn tác giả tải lên ResearchGate, không dùng tóm tắt của nền tảng làm nguồn phương pháp. SEND §2–3 hỗ trợ claim về noise. [Official PDF SEND](https://aclanthology.org/anthology-files/pdf/paclic/2022.paclic-1.71.pdf). |
| Giá thiếu/giá chào, §19 | Seaman hỗ trợ sự cần thiết của giả định missingness, không xác nhận bất động sản Việt Nam MNAR. Main giữ cơ chế giấu giá là giả thuyết. Conformal được mô tả có điều kiện, không bảo đảm mọi phường hoặc biến asking thành transaction. PASS. [Seaman](https://arxiv.org/pdf/1306.2812), [conformal](https://arxiv.org/pdf/2107.07511), [beyond exchangeability](https://arxiv.org/pdf/2202.13415). |
| Vòng học, §25 | Snorkel/Raykar hỗ trợ nhãn yếu và độ tin cậy annotator; main không đồng nhất silver/correction với gold. Settles được ghi ABS đúng mức đọc. Strategy active learning là thiết kế cần thí nghiệm, chưa có projected gain. PASS. [Snorkel](https://arxiv.org/pdf/1711.10160), [Raykar](https://jmlr.csail.mit.edu/papers/volume11/raykar10a/raykar10a.pdf). |
| Browser/policy, §31 và báo cáo §4 | Meta Newsroom 2021 nêu automated collection cần permission; Chrome activeTab là quyền tạm thời khi người dùng kích hoạt. Câu “quyền kỹ thuật khác quyền nguồn” được hỗ trợ. Chrome docs/policies trong bảng mở được; không suy ra extension chắc chắn được Store duyệt. [Meta](https://about.fb.com/news/2021/04/how-we-combat-scraping/), [activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab). |

Trang Công báo xác nhận Luật 91/2025/QH15 và cổng Chính phủ xác nhận Nghị định 356/2025/NĐ-CP, cùng hiệu lực 01/01/2026. Main ghi **metadata, chưa legal audit toàn văn**, đúng với bằng chứng đã xem. Không nâng thành kết luận nguồn Facebook hay dataset cụ thể được phép sử dụng. [Luật](https://congbao.chinhphu.vn/van-ban/luat-so-91-2025-qh15-45578.htm), [Nghị định](https://vanban.chinhphu.vn/?classid=1&docid=216387&pageid=27160).

Báo cáo phân biệt đúng PDF hướng dẫn YOLO với ReNER-VN. Text extraction có 13 và 9 page markers; các mốc khoảng 100 gold, 10 complex test, bốn tuần và hạn 01/11/2026 xuất hiện trong proposal ReNER-VN. Chúng được ghi là kế hoạch, không bị biến thành dữ liệu đã có. T1 là đánh giá nội bộ theo skill/claims-ledger, không phải chuẩn phân loại của cộng đồng khoa học.

## Hai điểm đã được xử lý và kiểm tra lại

1. **Lịch báo cáo §7:** ngày 09/10 tới hạn 01/11 chỉ còn 23 ngày. Câu “pilot bốn tuần” ban đầu đã được sửa thành “phần còn lại của kế hoạch pilot 05/10–01/11; từ 09/10 đến hạn có 23 ngày”. Đọc lại dòng 58 xác nhận sửa đúng, không đổi deadline nguồn. **RESOLVED**.
2. **Artifact báo cáo §8:** `LO-TRINH-TRUC-QUAN.html` chưa có ở snapshot đầu vì build song song; kiểm tra lại đã có file, 113.405 bytes. **RESOLVED về existence**. Nhánh nguồn này chưa kiểm render hoặc interaction HTML; kiểm browser thuộc verification của tác giả tổng hợp.

## Nguồn chưa đọc đủ hoặc bị chặn

- NICS 2021: abstract tác giả và conference program đã xem; chưa toàn văn. Không xác nhận dataset tải được, nhãn đầy đủ hoặc license corpus.
- IEEE DOI endpoint không đọc được trong lượt đầu; identity đối chiếu metadata và bản tác giả. Đây là giới hạn truy cập publisher, không phủ nhận paper tồn tại.
- Settles PDF trả timeout khi fetch lại; chỉ dùng abstract chính chủ UW cho claim nhập môn.
- Canonical SEND PDF có fetch lỗi; official `anthology-files/pdf/paclic` đọc được và đúng ID/title.
- Meta v19 trả HTTP 429; automated collection terms chuyển sang login/temporarily blocked trong audit. Main nêu giới hạn này đúng. Không claim kiểm chứng toàn bộ API/terms hiện hành.

**Provenance đã sửa trong note 02:** công thức quantile được gắn `[design] [cần thực nghiệm]`, kèm phạm vi phân bố giá chào quan sát; không có bảo đảm đại diện thị trường. Kiểm tra lại đoạn sửa thấy tag/lý do hiện diện. Không có số hiệu năng mới, venue promise hoặc reference bịa trong phạm vi đã audit. Độ chắc chắn cao về identity/đoạn nguồn đọc được; chưa biết feasibility và chất lượng thực nghiệm dự án.
