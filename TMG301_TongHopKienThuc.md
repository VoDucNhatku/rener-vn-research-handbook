# Tổng Hợp Chi Tiết Kiến Thức Môn TMG301 (Xử Lý Ngôn Ngữ Tự Nhiên / Text Mining)

> Rà soát 11/10/2026: sửa các diễn giải về Transformer, dependency parsing và điều kiện so sánh perplexity. Đây là ghi chú học tập, chưa được chứng nhận là tài liệu đầy đủ của môn. [Chi tiết phản biện](notes/audit-2026-10-11/BAO-CAO-PHAN-BIEN.md).

Dựa trên cấu trúc thư mục học liệu, môn học TMG301 bám sát giáo trình chuẩn về Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP), tương tự nội dung của cuốn *Speech and Language Processing* (Jurafsky & Martin). Dưới đây là bản đồ khái quát theo cấu trúc học liệu, không phải bản xác nhận đã kiểm tra đầy đủ từng slide hay toàn bộ nội dung thi.

---

## 1. Xử lý văn bản cơ bản & Khoảng cách Edit (Text Normalization & Edit Distance)
- **Regular Expressions (Biểu thức chính quy):** Công cụ mạnh mẽ để tìm kiếm, trích xuất và thay thế các mẫu chuỗi (pattern matching) trong văn bản (ví dụ: tìm email, số điện thoại).
- **Text Normalization (Chuẩn hóa văn bản):**
  - *Tokenization:* Tách câu văn thành các đơn vị nhỏ hơn (từ, dấu câu).
  - *Lemmatization & Stemming:* Đưa từ về dạng gốc. Stemming (như thuật toán Porter) cắt bỏ hậu tố một cách cơ học (ví dụ: `running` $\rightarrow$ `run`), trong khi Lemmatization dùng từ điển để đưa từ về nguyên thể đúng ngữ pháp (ví dụ: `better` $\rightarrow$ `good`).
  - *Sentence Segmentation:* Tách đoạn văn thành các câu.
- **Minimum Edit Distance (Khoảng cách chỉnh sửa tối thiểu / Levenshtein Distance):** Đo lường mức độ khác biệt giữa hai chuỗi bằng số lượng ít nhất các thao tác (Chèn - Insert, Xóa - Delete, Thay thế - Substitute) để biến chuỗi này thành chuỗi kia. Ứng dụng trong kiểm tra lỗi chính tả. Thuật toán giải quyết thường dùng Quy hoạch động (Dynamic Programming).

## 2. Mô hình ngôn ngữ N-Gram (N-Gram Language Models)
- **Mục tiêu:** Tính xác suất của một câu hoặc dự đoán từ tiếp theo trong câu dựa trên ngữ cảnh trước đó.
- **Giả định Markov (Markov Assumption):** Xác suất của một từ chỉ phụ thuộc vào $N-1$ từ liền trước nó thay vì toàn bộ câu.
  - *Unigram (1-gram):* Các từ độc lập với nhau.
  - *Bigram (2-gram):* Phụ thuộc vào 1 từ trước đó.
  - *Trigram (3-gram):* Phụ thuộc vào 2 từ trước đó.
- **Ước lượng xác suất (MLE):** Đếm tần suất xuất hiện (Count) của N-gram chia cho tần suất của ngữ cảnh.
- **Đánh giá mô hình (Perplexity):** Chỉ số đo độ "mơ hồ" của mô hình. Perplexity thấp hơn biểu thị xác suất tốt hơn trên cùng dữ liệu đánh giá và cách tính tương thích. Tokenizer, đơn vị token, xử lý ngữ cảnh và corpus ảnh hưởng chỉ số; không so trực tiếp hai số từ các điều kiện khác nhau, cũng không dùng nó thay chất lượng tác vụ. [Hugging Face](https://huggingface.co/docs/transformers/perplexity).
- **Smoothing (Làm trơn):** Giải quyết vấn đề từ chưa từng xuất hiện (Zero probability). Các kỹ thuật: Laplace (Add-1), Add-k, Interpolation, Kneser-Ney.

## 3. Phân loại Naive Bayes & Phân tích cảm xúc (Naive Bayes & Sentiment)
- **Bài toán:** Phân loại văn bản (Text Classification), ví dụ: Phân tích cảm xúc tích cực/tiêu cực (Sentiment Analysis).
- **Mô hình Naive Bayes:** Là mô hình sinh (Generative Model) dựa trên Định lý Bayes.
- **Giả định Naive (Ngây thơ):** Căn bản giả định các đặc trưng (các từ) xuất hiện trong văn bản là **độc lập có điều kiện khi đã biết nhãn**; đây là giả định của mô hình, không phải sự thật về ngôn ngữ.
- **Bag of Words (BoW):** Biểu diễn văn bản dưới dạng một tập hợp các từ và tần suất của chúng, bỏ qua thứ tự từ.
- **Tính toán:** Áp dụng Log-Probabilities để tránh hiện tượng underflow (số quá nhỏ khi nhân nhiều xác suất). Có sử dụng Laplace Smoothing.

## 4. Hồi quy Logistic (Logistic Regression)
- **Đặc điểm:** Là mô hình phân biệt (Discriminative Model), trái ngược với Naive Bayes. Mô hình học trực tiếp ranh giới quyết định (decision boundary) giữa các lớp.
- **Hàm Sigmoid:** Biến đổi đầu ra tuyến tính ($w \cdot x + b$) thành xác suất (từ 0 đến 1).
- **Cross-Entropy Loss:** Hàm mất mát dùng để đánh giá sự khác biệt giữa dự đoán của mô hình và nhãn thực tế.
- **Tối ưu hóa (Gradient Descent):** Thuật toán lặp để cập nhật trọng số $w$ nhằm cực tiểu hóa hàm loss.

## 5. Ngữ nghĩa Vector và Word Embeddings
- **Ngữ nghĩa học từ vựng (Lexical Semantics):** Tính đồng nghĩa, trái nghĩa, độ tương đồng ngữ nghĩa.
- **TF-IDF:** Kỹ thuật gán trọng số cho từ trong văn bản. TF (Term Frequency) đo tần suất trong tài liệu, IDF (Inverse Document Frequency) đánh trọng số thấp cho các từ quá phổ biến (như "the", "a").
- **Word Embeddings (Nhúng từ):** Biểu diễn từ dưới dạng vector số thực trù mật (dense vectors) trong không gian n-chiều. Các từ có ngữ cảnh phân bố tương tự thường có vector gần nhau; gần nhau không bảo đảm đồng nghĩa, vì từ trái nghĩa cũng có thể xuất hiện trong ngữ cảnh tương tự.
- **Word2Vec:** Mô hình học embeddings nổi tiếng với 2 kiến trúc:
  - *Skip-gram:* Dự đoán ngữ cảnh (các từ xung quanh) từ từ trung tâm.
  - *CBOW (Continuous Bag of Words):* Dự đoán từ trung tâm từ ngữ cảnh xung quanh.
- **Cosine Similarity:** Thường dùng để tính độ tương đồng (góc) giữa 2 vector từ.

## 6. Phân cụm văn bản (Clustering for Text Similarity)
- **Phân cụm (Clustering):** Phương pháp Học không giám sát (Unsupervised Learning) để nhóm các văn bản tương đồng vào cùng một cụm.
- **K-Means Clustering:** Thuật toán phổ biến, chia dữ liệu thành K cụm bằng cách gán điểm dữ liệu vào centroid (tâm) gần nhất, rồi cập nhật lại centroid.
- **Hierarchical Clustering (Phân cụm phân cấp):** Tạo ra một cấu trúc cây (Dendrogram) biểu diễn quan hệ nhóm (Bottom-up hoặc Top-down).
- **Đánh giá:** Sử dụng các metric như Purity (Độ thuần khiết), Silhouette Coefficient.

## 7 & 8. Transformer & Mô hình ngôn ngữ tiền huấn luyện (Pre-Trained LMs / Fine-tuning)
- **Kiến trúc Transformer:** Transformer gốc dùng attention thay recurrence trong kiến trúc của nó; điều này không có nghĩa mọi bài toán đã thay RNN/LSTM. Có thể tính nhiều vị trí song song khi huấn luyện, nhưng giải mã tự hồi quy vẫn sinh lần lượt. Full self-attention có chi phí bậc hai theo chiều dài chuỗi (với chiều biểu diễn cố định); context và bộ nhớ vẫn hữu hạn. [Vaswani et al., §3–4](https://arxiv.org/html/1706.03762v7).
- **Cơ chế Attention (Self-Attention):** Giúp mô hình tập trung vào các từ quan trọng trong câu khi mã hóa một từ cụ thể (tính trọng số phụ thuộc giữa các từ). Multi-head Attention giúp học nhiều góc độ ngữ nghĩa khác nhau.
- **Positional Encoding:** Thêm thông tin về vị trí của từ vào vector do Transformer xử lý song song.
- **Pre-trained LMs (BERT, GPT):** Mô hình được huấn luyện trước (Pre-train) trên lượng dữ liệu khổng lồ để hiểu ngôn ngữ, sau đó **Fine-tune** (tinh chỉnh) lại trên bộ dữ liệu nhỏ gọn cho task cụ thể (như phân loại, hỏi đáp).
- **Masked Language Modeling (MLM):** (Như BERT) Che đi một vài từ ngẫu nhiên trong câu và bắt mô hình dự đoán từ bị che (Học ngữ nghĩa 2 chiều).

## 9. Dịch máy (Machine Translation)
- **Bài toán:** Dịch tự động từ ngôn ngữ nguồn sang ngôn ngữ đích.
- **Seq2Seq (Sequence-to-Sequence):** Kiến trúc cơ bản gồm một Encoder (mã hóa câu nguồn thành context vector) và một Decoder (giải mã tạo ra câu đích).
- **Attention trong Dịch máy:** Khắc phục điểm yếu của context vector cố định bằng cách cho phép Decoder "nhìn lại" (attend) vào các phần khác nhau của câu nguồn tại mỗi bước sinh từ.
- **Đánh giá (BLEU Score):** So sánh số lượng n-gram trùng khớp giữa câu dịch của máy và (các) câu dịch chuẩn của người.

## 10. Hệ thống Chatbot & Đối thoại (Dialogue Systems)
- **Rule-based & ELIZA:** Dựa trên các quy tắc regex và kịch bản (script) định sẵn.
- **Hệ thống đối thoại định hướng tác vụ (Task-oriented):** (Ví dụ: đặt vé máy bay). Gồm các module:
  - *NLU (Natural Language Understanding):* Nhận diện Ý định (Intent detection) và Trích xuất thực thể (Slot filling).
  - *DST (Dialogue State Tracking):* Theo dõi trạng thái cuộc hội thoại.
  - *Dialogue Policy:* Quyết định hành động tiếp theo của hệ thống.
  - *NLG (Natural Language Generation):* Sinh câu trả lời.
- **Chatbot sinh văn bản (Generative/Chit-chat):** Dựa trên mô hình ngôn ngữ lớn để trả lời tự do.

## 11 & 12. Phân tích cú pháp (Constituency & Dependency Parsing)
- **Constituency Parsing (Phân tích thành phần):** Dựa trên Văn phạm phi ngữ cảnh (CFG). Phân tích câu thành các cụm từ (Danh ngữ NP, Động ngữ VP). Sử dụng thuật toán CKY (Quy hoạch động) để dựng cây cú pháp.
- **Dependency Parsing (Phân tích phụ thuộc):** Xác định mối quan hệ trực tiếp giữa các từ (đâu là chủ ngữ, tân ngữ của động từ chính).
  - *Transition-based Parsing:* Thuật toán tuần tự dạng Shift-Reduce.
  - *Graph-based Parsing:* Với mô hình cộng điểm trên cạnh, tìm cây phụ thuộc có tổng điểm lớn nhất: maximum spanning arborescence trên đồ thị có hướng. Có thể chuyển thành bài toán cực tiểu nếu đổi dấu điểm thành chi phí; không mặc định là cây bao trùm nhỏ nhất vô hướng. [Shimizu, CoNLL 2006](https://aclanthology.org/W06-2936/).

## 13, 14 & 15. Khai phá thông tin, Sự kiện & Thời gian (Information & Event Extraction)
- **Logical Representations:** Chuyển câu sang biểu diễn logic (First-Order Logic - FOL), sử dụng vị từ, lượng từ để máy tính hiểu ý nghĩa suy luận.
- **Relation Extraction (Trích xuất quan hệ):** Tìm kiếm mối quan hệ giữa các thực thể (VD: "Steve Jobs" [Người sáng lập] "Apple"). Áp dụng học có giám sát, bán giám sát hoặc Distant Supervision.
- **Event Extraction:** Trích xuất các sự kiện cụ thể (Ai, làm gì, ở đâu, khi nào).
- **Time/Temporal Reasoning:** Trích xuất các biểu thức thời gian (Timex) và phân giải chúng về chuẩn, đồng thời xác định thứ tự thời gian (trước, sau, trong khi) giữa các sự kiện.

## 16 & 17. Ngữ nghĩa từ & Từ điển Cảm xúc (Word Senses & Lexicons)
- **Từ đa nghĩa (Word Senses):** Một từ có thể có nhiều nghĩa (Bank = ngân hàng / bờ sông).
- **WordNet:** Cơ sở dữ liệu từ vựng lớn phân cấp theo mạng lưới ngữ nghĩa (Synsets, Hypernyms, Hyponyms).
- **Word Sense Disambiguation (WSD):** Bài toán gỡ rối đa nghĩa (xác định đúng nghĩa của từ trong ngữ cảnh cụ thể). Thuật toán Lesk (dựa trên độ chồng chéo của định nghĩa từ vựng) hoặc các phương pháp Machine Learning.
- **Sentiment Lexicons:** Các từ điển phân loại sẵn điểm số cảm xúc của từ (VADER, SentiWordNet). Ứng dụng kết hợp với quy tắc để phân tích cảm xúc nhanh chóng và tính toán độ nội hàm (Connotation).

---
*Tài liệu này đóng vai trò là "Bản đồ học tập" (Study Guide). Dựa vào đây, sinh viên có thể hệ thống hóa lại mạch kiến thức của cả kỳ học theo dạng từ cơ bản (tiền xử lý, học máy truyền thống) lên đến nâng cao (Deep Learning, Transformer, và Ứng dụng thực tế).*
