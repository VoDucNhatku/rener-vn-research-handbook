import os
import json
import subprocess
import sys

OUT_DIR = r"D:\DEMO kế hoạch kì 5\TMG301\SoTay_ChiTiet_17Bai"
TMP_DIR = r"D:\DEMO kế hoạch kì 5\TMG301\.tmp_specs"
BUILDER = r"C:\Users\DELL\.gemini\config\skills\study-forge\scripts\build_handbook.py"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

all_lessons = [
    # Bai 1
    {
        "slug": "tmg301-bai01",
        "title": "Bài 01 · Biểu thức chính quy, Chuẩn hóa văn bản & Khoảng cách Edit",
        "subtitle": "Sổ tay 10 ô chi tiết cho Bài 01 môn TMG301: Xử lý chuỗi, Tokenization, Stemming/Lemmatization và Thuật toán Levenshtein Minimum Edit Distance.",
        "source": "01. Regular Expressions - Text Normalization - SDIT Distance.ppt",
        "domain": "nlp",
        "filename": "TMG301_Bai01_SoTay.md",
        "notation": [
            {"sym": "D[i,j]", "role": "data", "read": "đê i j", "means": "khoảng cách edit giữa chuỗi nguồn độ dài i và chuỗi đích độ dài j"},
            {"sym": "w_{sub}", "role": "hyper", "read": "vê sub", "means": "chi phí thay thế ký tự"},
            {"sym": "w_{ins}", "role": "hyper", "read": "vê ins", "means": "chi phí chèn ký tự"},
            {"sym": "w_{del}", "role": "hyper", "read": "vê del", "means": "chi phí xóa ký tự"}
        ],
        "dag": [
            {"from": "C1", "to": "C2", "label": "chuẩn hóa dữ liệu trước khi tính"}
        ],
        "cards": [
            {
                "id": "C1",
                "title": "Regex & Chuẩn hóa Văn bản (Text Normalization)",
                "tier": 1,
                "job": "Biến văn bản thô nhiều nhiễu thành chuỗi các token chuẩn hóa trước khi đưa vào các mô hình NLP.",
                "expr": "\\text{NormalizedText} = \\text{Lower}(\\text{Lemmatize}(\\text{Tokenize}(\\text{RegexClean}(\\text{RawText}))))",
                "legend": [
                    {"key": "RawText", "role": "data", "note": "chuỗi văn bản đầu vào chưa qua xử lý"},
                    {"key": "RegexClean", "role": "op", "note": "loại bỏ ký tự đặc biệt, HTML tag, khoảng trắng thừa bằng Regular Expressions"},
                    {"key": "Tokenize", "role": "op", "note": "tách chuỗi thành danh sách các từ/dấu câu (tokens)"},
                    {"key": "Lemmatize", "role": "op", "note": "đưa từ về nguyên thể đúng ngữ pháp (vd: 'better' -> 'good')"}
                ],
                "shapes": [
                    {"expr": "Tokenize(text)", "in": "string", "out": "List[string]", "note": "tách 1 chuỗi thành m mảng các từ"},
                    {"expr": "Lemmatize(tokens)", "in": "List[string]", "out": "List[string]", "note": "giữ nguyên độ dài danh sách nhưng đổi từ dạng biến thể về gốc"}
                ],
                "ablation": [
                    {"remove": "RegexClean", "severity": "degrades", "effect": "văn bản lẫn ký tự lạ, HTML tag làm nổ từ điển từ nhiễu (vocabulary explosion)."},
                    {"remove": "Lower", "severity": "subtle", "effect": "'The' và 'the' bị coi là 2 từ khác nhau, làm giảm tần suất từ chuẩn."},
                    {"remove": "Tokenize", "severity": "breaks", "effect": "không thể tính tần suất hay nhúng vector vì toàn bộ đoạn văn chỉ là 1 chuỗi duy nhất."}
                ],
                "trace": {
                    "given": "text = 'The 2 cats are running fast!'",
                    "steps": [
                        {"step": "1. RegexClean (bỏ dấu câu, số)", "value": "'The cats are running fast'"},
                        {"step": "2. Lowercase", "value": "'the cats are running fast'"},
                        {"step": "3. Tokenize", "value": "['the', 'cats', 'are', 'running', 'fast']"},
                        {"step": "4. Lemmatize", "value": "['the', 'cat', 'be', 'run', 'fast']"}
                    ],
                    "result": "Dạng chuẩn hóa cuối cùng sẵn sàng đưa vào mô hình N-gram hoặc BoW."
                },
                "picture": {
                    "kind": "flow",
                    "flow": {
                        "dir": "vertical",
                        "nodes": [
                            {"id": "n1", "text": "Raw Text", "type": "start", "width": "35mm"},
                            {"id": "n2", "text": "Regex Clean", "type": "proc", "width": "40mm"},
                            {"id": "n3", "text": "Tokenization", "type": "proc", "width": "40mm"},
                            {"id": "n4", "text": "Lemmatization", "type": "proc", "width": "40mm"}
                        ],
                        "edges": [
                            {"from": "n1", "to": "n2"},
                            {"from": "n2", "to": "n3"},
                            {"from": "n3", "to": "n4"}
                        ]
                    },
                    "caption": "Quy trình chuẩn hóa văn bản 4 bước chuẩn trong NLP."
                },
                "twin": {
                    "lang": "python",
                    "src": "import re\ndef clean_and_tokenize(text):\n    text = re.sub(r'[^a-zA-Z\\s]', '', text).lower()\n    return text.split()",
                    "map": [
                        {"sym": "RawText", "var": "text"},
                        {"sym": "RegexClean", "var": "re.sub(...)"}
                    ]
                },
                "failures": [
                    {"symptom": "Từ 'don't' bị tách thành 'don' và 't'", "cause": "regex split theo dấu nháy đơn không chuẩn", "fix": "sử dụng spaCy/NLTK word_tokenize thay vì regex đơn giản"},
                    {"symptom": "Từ 'meeting' bị stem thành 'meet' nhưng danh từ 'meeting' (cuộc họp) mất nghĩa", "cause": "dùng Stemming thay vì Lemmatization", "fix": "chuyển sang dùng WordNetLemmatizer với đúng POS tag"}
                ],
                "probes": [
                    {"q": "Stemming và Lemmatization khác nhau cốt lõi ở điểm nào?", "a": "Stemming cắt đuôi cơ học theo quy tắc (có thể ra từ không có nghĩa), Lemmatization dùng từ điển ngữ pháp để đưa về từ nguyên thể đúng thực tế."},
                    {"q": "Vì sao Regex [a-zA-Z]+ lại bỏ mất các từ tiếng Việt có dấu?", "a": "Vì bảng mã ASCII [a-zA-Z] không bao gồm các ký tự Unicode như á, à, ả, ẽ, ê... Cần dùng mã Unicode regex \\p{L} hoặc chuẩn hóa UTF-8."},
                    {"q": "Khi nào KHÔNG nên lowercase toàn bộ văn bản?", "a": "Trong bài toán Nhận dạng thực thể tên riêng (NER), chữ hoa giúp phân biệt tên người/địa danh với từ thường (vd: 'Apple' vs 'apple')."},
                    {"q": "Tokenization theo Subword (BPE - Byte Pair Encoding) giải quyết vấn đề gì so với Word Tokenization?", "a": "Giải quyết vấn đề từ ngoài từ điển (OOV - Out of Vocabulary) bằng cách tách từ hiếm thành các mảnh subword quen thuộc."},
                    {"q": "Biểu thức chính quy r'\\bcat\\b' match những từ nào?", "a": "Chỉ match đúng từ đứng độc lập 'cat', không match 'cat' nằm trong 'caterpillar' hay 'bobcat' nhờ biên từ \\b."}
                ]
            },
            {
                "id": "C2",
                "title": "Khoảng cách Edit Tối thiểu (Minimum Edit Distance - Levenshtein)",
                "tier": 1,
                "job": "Tính số thao tác ít nhất (chèn, xóa, thay thế) để biến đổi chuỗi X thành chuỗi Y bằng quy hoạch động.",
                "expr": "D[i,j] = \\min \\begin{cases} D[i-1, j] + c_{del} \\\\ D[i, j-1] + c_{ins} \\\\ D[i-1, j-1] + c_{sub}(X_i, Y_j) \\end{cases}",
                "legend": [
                    {"key": "D[i,j]", "role": "data", "note": "khoảng cách edit giữa X[1..i] và Y[1..j]"},
                    {"key": "c_{del}", "role": "hyper", "note": "chi phí xóa 1 ký tự từ X (thường = 1)"},
                    {"key": "c_{ins}", "role": "hyper", "note": "chi phí chèn 1 ký tự vào Y (thường = 1)"},
                    {"key": "c_{sub}", "role": "hyper", "note": "chi phí thay thế (0 nếu X_i == Y_j, 2 hoặc 1 nếu khác nhau)"}
                ],
                "shapes": [
                    {"expr": "D", "in": "Matrix(n+1, m+1)", "out": "scalar D[n,m]", "note": "n = len(X), m = len(Y); ma trận quy hoạch động"}
                ],
                "ablation": [
                    {"remove": "c_{sub} cost=0 khi trùng", "severity": "breaks", "effect": "thuật toán tính chi phí cả với ký tự giống nhau -> kết quả sai hoàn toàn."},
                    {"remove": "khởi tạo D[i,0]=i và D[0,j]=j", "severity": "breaks", "effect": "thiếu điều kiện biên -> ma trận DP không tính được."}
                ],
                "trace": {
                    "given": "X = 'cat', Y = 'hat', chi phí sub=2 nếu khác, ins=1, del=1",
                    "steps": [
                        {"step": "1. Khởi tạo hàng 0 và cột 0", "value": "D[0,0]=0, D[1,0]=1, D[0,1]=1"},
                        {"step": "2. So sánh 'c' và 'h'", "value": "khác nhau -> sub cost = 2. min(1+1, 1+1, 0+2) = 2"},
                        {"step": "3. So sánh 'a' và 'a'", "value": "giống nhau -> sub cost = 0. D['ca','ha'] = 2"},
                        {"step": "4. So sánh 't' và 't'", "value": "giống nhau -> D['cat','hat'] = 2"}
                    ],
                    "result": "Levenshtein distance = 2 (thay 'c' bằng 'h' tốn 2 điểm)."
                },
                "twin": {
                    "lang": "python",
                    "src": "def min_edit_distance(target, source):\n    n, m = len(target), len(source)\n    dp = [[0]*(m+1) for _ in range(n+1)]\n    for i in range(n+1): dp[i][0] = i\n    for j in range(m+1): dp[0][j] = j\n    for i in range(1, n+1):\n        for j in range(1, m+1):\n            cost = 0 if target[i-1] == source[j-1] else 2\n            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)\n    return dp[n][m]",
                    "map": [
                        {"sym": "D[i,j]", "var": "dp[i][j]"},
                        {"sym": "c_{sub}", "var": "cost"}
                    ]
                },
                "failures": [
                    {"symptom": "Khoảng cách giữa 'a' và 'a' ra 1 thay vì 0", "cause": "quên set cost = 0 khi 2 ký tự trùng nhau", "fix": "kiểm tra điều kiện target[i-1] == source[j-1]"},
                    {"symptom": "IndexError: list index out of range", "cause": "tạo ma trận kích thước n x m thay vì (n+1) x (m+1)", "fix": "khởi tạo mảng cỡ (n+1) x (m+1) để chứa cả chuỗi rỗng gốc"}
                ],
                "probes": [
                    {"q": "Độ phức tạp thời gian và không gian của thuật toán Levenshtein chuẩn là bao nhiêu?", "a": "Thời gian O(n*m) và không gian O(n*m) với n, m là độ dài 2 chuỗi."},
                    {"q": "Sự khác biệt giữa Levenshtein Distance và Damerau-Levenshtein Distance là gì?", "a": "Damerau-Levenshtein bổ sung thêm thao tác Đảo vị trí 2 ký tự kề nhau (Transposition) với chi phí = 1."},
                    {"q": "Làm thế nào để giảm bộ nhớ không gian từ O(n*m) xuống O(min(n,m))?", "a": "Vì D[i,j] chỉ phụ thuộc vào hàng i và hàng i-1, ta chỉ cần lưu 2 hàng gần nhất thay vì toàn bộ ma trận."},
                    {"q": "Ứng dụng thực tế chính của Minimum Edit Distance trong NLP là gì?", "a": "Sửa lỗi chính tả tự động (Spelling Correction), so sánh trình tự gen (DNA Alignment), gợi ý gõ từ (Autocomplete)."},
                    {"q": "Nếu chi phí Substitute là 1 thay vì 2, khoảng cách giữa 'cat' và 'hat' bằng bao nhiêu?", "a": "Bằng 1 (thay 'c' thành 'h' với chi phí = 1)."}
                ]
            }
        ]
    },

    # Bai 2
    {
        "slug": "tmg301-bai02",
        "title": "Bài 02 · Mô hình ngôn ngữ N-Gram & Kỹ thuật Làm trơn (Smoothing)",
        "subtitle": "Sổ tay 10 ô chi tiết cho Bài 02 môn TMG301: Đếm N-gram, Perplexity, Laplace (Add-1) Smoothing và Kneser-Ney Smoothing.",
        "source": "02. N-Gram Language Models.ppt",
        "domain": "nlp",
        "filename": "TMG301_Bai02_SoTay.md",
        "notation": [
            {"sym": "P(w_i | w_{i-N+1}^{i-1})", "role": "pred", "read": "xác suất w_i cho trước N-1 từ trước", "means": "xác suất N-gram"},
            {"sym": "C(w_{i-N+1}^i)", "role": "data", "read": "tần suất N-gram", "means": "số lần chuỗi N từ xuất hiện"},
            {"sym": "V", "role": "index", "read": "kích thước từ điển", "means": "tổng số từ phân biệt trong từ điển"},
            {"sym": "PP(W)", "role": "hyper", "read": "perplexity", "means": "độ mơ hồ của mô hình trên chuỗi W"}
        ],
        "dag": [
            {"from": "C1", "to": "C2", "label": "đánh giá bằng"},
            {"from": "C1", "to": "C3", "label": "xử lý xác suất 0 bằng"}
        ],
        "cards": [
            {
                "id": "C1",
                "title": "Mô hình N-Gram & Ước lượng Cực đại (MLE)",
                "tier": 1,
                "job": "Tính xác suất của một từ tiếp theo dựa trên N-1 từ ngay trước nó (Giả định Markov).",
                "expr": "P_{MLE}(w_i | w_{i-1}) = \\frac{C(w_{i-1}, w_i)}{C(w_{i-1})}",
                "legend": [
                    {"key": "w_i", "role": "data", "note": "từ hiện tại cần tính xác suất"},
                    {"key": "w_{i-1}", "role": "data", "note": "từ ngữ cảnh ngay trước nó (Bigram model)"},
                    {"key": "C(w_{i-1}, w_i)", "role": "data", "note": "số lần cặp từ (w_{i-1}, w_i) xuất hiện trong tập huấn luyện"},
                    {"key": "C(w_{i-1})", "role": "data", "note": "tổng số lần từ w_{i-1} xuất hiện"}
                ],
                "shapes": [
                    {"expr": "P_{MLE}", "in": "counts / counts", "out": "scalar [0, 1]", "note": "xác suất của từ w_i"}
                ],
                "ablation": [
                    {"remove": "Giả định Markov", "severity": "breaks", "effect": "phải tính xác suất phụ thuộc toàn bộ lịch sử từ đầu văn bản -> không đủ dữ liệu đếm."},
                    {"remove": "C(w_{i-1}) ở mẫu", "severity": "degrades", "effect": "trở thành tổng số lần xuất hiện thuần túy, không còn là xác suất chuẩn hóa."}
                ],
                "trace": {
                    "given": "C('sam', 'iam') = 2, C('sam') = 5",
                    "steps": [
                        {"step": "1. Đếm số lần 'sam iam'", "value": "2"},
                        {"step": "2. Đếm số lần 'sam'", "value": "5"},
                        {"step": "3. Chia 2/5", "value": "0.4"}
                    ],
                    "result": "P('iam' | 'sam') = 0.4"
                },
                "twin": {
                    "lang": "python",
                    "src": "def bigram_prob(word, prev_word, bigram_counts, unigram_counts):\n    return bigram_counts.get((prev_word, word), 0) / unigram_counts.get(prev_word, 1)",
                    "map": [
                        {"sym": "C(w_{i-1}, w_i)", "var": "bigram_counts[(prev_word, word)]"},
                        {"sym": "C(w_{i-1})", "var": "unigram_counts[prev_word]"}
                    ]
                },
                "failures": [
                    {"symptom": "Xác suất cả câu bằng 0", "cause": "chỉ cần 1 N-gram chưa bao giờ xuất hiện trong tập train (Zero probability)", "fix": "áp dụng kỹ thuật làm trơn (Smoothing) như Add-1 hoặc Kneser-Ney"},
                    {"symptom": "ZeroDivisionError", "cause": "từ ngữ cảnh w_{i-1} chưa bao giờ xuất hiện trong tập train", "fix": "dùng từ đặc biệt <UNK> để thay thế từ ngoài từ điển"}
                ],
                "probes": [
                    {"q": "Với câu độ dài N, mô hình Bigram tính xác suất toàn bộ câu theo công thức nào?", "a": "P(w_1..w_N) = P(w_1|<BOS>) * P(w_2|w_1) * P(w_3|w_2) * ... * P(w_N|w_{N-1})."},
                    {"q": "Vì sao trong thực tế người ta thường lấy Log của xác suất (Log-Probability) thay vì nhân xác suất trực tiếp?", "a": "Để tránh hiện tượng Tràn số âm (Underflow) khi nhân hàng trăm số thập phân nhỏ hơn 1 lại với nhau."},
                    {"q": "Ưu và nhược điểm của việc tăng N từ Bigram (N=2) lên 4-gram là gì?", "a": "Ưu điểm: Ngữ cảnh dài hơn, dự đoán tự nhiên hơn. Nhược điểm: Bộc phát thưa thớt dữ liệu (data sparsity), từ điển n-gram phình to."},
                    {"q": "Thẻ <BOS> và <EOS> trong N-gram dùng để làm gì?", "a": "Đánh dấu bắt đầu câu (Beginning Of Sentence) và kết thúc câu (End Of Sentence) để mô hình học xác suất từ mở đầu và độ dài câu."},
                    {"q": "Nếu tập dữ liệu nhỏ, nên chọn Unigram, Bigram hay Trigram?", "a": "Nên chọn Unigram hoặc Bigram vì dữ liệu nhỏ không đủ đếm tần suất Trigram chuẩn xác."}
                ]
            },
            {
                "id": "C2",
                "title": "Đánh giá Mô hình bằng Perplexity (PP)",
                "tier": 1,
                "job": "Đo độ mơ hồ của mô hình ngôn ngữ trên tập kiểm thử (Perplexity càng thấp mô hình càng giỏi).",
                "expr": "PP(W) = P(w_1, w_2, ..., w_N)^{-\\frac{1}{N}} = \\sqrt[N]{\\prod_{i=1}^N \\frac{1}{P(w_i | w_{i-1})}}",
                "legend": [
                    {"key": "N", "role": "index", "note": "tổng số từ trong tập kiểm thử W"},
                    {"key": "P(w_i|w_{i-1})", "role": "pred", "note": "xác suất dự đoán từ w_i từ ngữ cảnh w_{i-1}"},
                    {"key": "PP(W)", "role": "hyper", "note": "giá trị Perplexity (luôn >= 1)"}
                ],
                "shapes": [
                    {"expr": "PP(W)", "in": "probabilities list", "out": "scalar >= 1", "note": "chỉ số đánh giá độ mơ hồ"}
                ],
                "ablation": [
                    {"remove": "mũ -1/N", "severity": "breaks", "effect": "không trung bình hóa theo độ dài câu -> câu càng dài Perplexity càng nổ to."}
                ],
                "trace": {
                    "given": "Câu gồm N=2 từ, xác suất P(w1)=0.5, P(w2|w1)=0.5",
                    "steps": [
                        {"step": "1. Tích xác suất câu P(W)", "value": "0.5 * 0.5 = 0.25"},
                        {"step": "2. Nghịch đảo 1/P(W)", "value": "1 / 0.25 = 4"},
                        {"step": "3. Căn bậc N=2", "value": "sqrt(4) = 2.0"}
                    ],
                    "result": "Perplexity PP(W) = 2.0 (tương đương chọn ngẫu nhiên giữa 2 từ)."
                },
                "twin": {
                    "lang": "python",
                    "src": "import math\ndef calculate_perplexity(probs):\n    N = len(probs)\n    log_sum = sum(math.log2(p) for p in probs)\n    return 2 ** (-log_sum / N)",
                    "map": [
                        {"sym": "PP(W)", "var": "2 ** (-log_sum / N)"},
                        {"sym": "N", "var": "len(probs)"}
                    ]
                },
                "failures": [
                    {"symptom": "Perplexity = infinity (vô cùng)", "cause": "có ít nhất một từ trong test set có P=0", "fix": "áp dụng Smoothing để không từ nào có xác suất bằng 0"},
                    {"symptom": "Perplexity < 1", "cause": "tính sai công thức log hoặc nhân xác suất > 1", "fix": "kiểm tra lại tổng xác suất có chuẩn hóa sum(P)=1 không"}
                ],
                "probes": [
                    {"q": "Nếu một mô hình đoán hoàn toàn ngẫu nhiên trên từ điển có |V|=10000 từ, Perplexity của nó bằng bao nhiêu?", "a": "Bằng 10000 (độ mơ hồ đúng bằng số lượng lựa chọn từ điển)."},
                    {"q": "Perplexity có quan hệ như thế nào với Entropy H(W)?", "a": "PP(W) = 2^{H(W)}, trong đó H(W) là cross-entropy của mô hình trên tập kiểm thử."},
                    {"q": "Có thể so sánh Perplexity giữa 2 mô hình sử dụng 2 bộ Vocabulary khác nhau không?", "a": "Không, Perplexity chỉ so sánh được khi 2 mô hình dùng CHUNG một Vocabulary và cùng tập Test."},
                    {"q": "Tại sao Perplexity thấp hơn lại tương ứng với mô hình tốt hơn?", "a": "Vì Perplexity đo số lượng từ rủi ro mà mô hình phải đắn đo; càng ít từ đắn đo tức là dự đoán càng chính xác."},
                    {"q": "Khi Perplexity bằng 1 có nghĩa là gì?", "a": "Có nghĩa là mô hình dự đoán chính xác 100% không chút nghi ngờ tại mọi bước (xác suất = 1)."}
                ]
            },
            {
                "id": "C3",
                "title": "Làm trơn Laplace (Add-1 Smoothing)",
                "tier": 1,
                "job": "Cộng 1 vào tần suất của mọi N-gram để tránh xác suất bằng 0 cho các từ chưa xuất hiện.",
                "expr": "P_{Laplace}(w_i | w_{i-1}) = \\frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + |V|}",
                "legend": [
                    {"key": "C(w_{i-1}, w_i)", "role": "data", "note": "tần suất Bigram thực tế"},
                    {"key": "1", "role": "hyper", "note": "hệ số ảo cộng thêm"},
                    {"key": "|V|", "role": "index", "note": "kích thước từ điển (thêm vào mẫu để tổng xác suất bằng 1)"}
                ],
                "shapes": [
                    {"expr": "P_{Laplace}", "in": "(count+1)/(count+|V|)", "out": "scalar (0, 1)", "note": "xác suất sau làm trơn"}
                ],
                "ablation": [
                    {"remove": "|V| ở mẫu số", "severity": "breaks", "effect": "tổng xác suất trên toàn từ điển sum_w P(w|w_{i-1}) sẽ > 1 (vi phạm quy tắc xác suất)."}
                ],
                "trace": {
                    "given": "C('sam', 'iam')=0, C('sam')=10, |V|=1000",
                    "steps": [
                        {"step": "1. Tử số C + 1", "value": "0 + 1 = 1"},
                        {"step": "2. Mẫu số C + |V|", "value": "10 + 1000 = 1010"},
                        {"step": "3. Chia 1 / 1010", "value": "0.00099"}
                    ],
                    "result": "Xác suất không còn bằng 0 mà là 0.00099."
                },
                "twin": {
                    "lang": "python",
                    "src": "def laplace_smooth(word, prev_word, bigram_counts, unigram_counts, vocab_size):\n    c_2 = bigram_counts.get((prev_word, word), 0)\n    c_1 = unigram_counts.get(prev_word, 0)\n    return (c_2 + 1) / (c_1 + vocab_size)",
                    "map": [
                        {"sym": "1", "var": "1"},
                        {"sym": "|V|", "var": "vocab_size"}
                    ]
                },
                "failures": [
                    {"symptom": "Xác suất các từ phổ biến bị sụt giảm quá nhiều", "cause": "Add-1 dồn quá nhiều khối lượng xác suất (probability mass) cho các từ hiếm khi |V| quá lớn", "fix": "chuyển sang Add-k (k=0.01) hoặc Kneser-Ney Smoothing"}
                ],
                "probes": [
                    {"q": "Add-k Smoothing nâng cấp Laplace Smoothing như thế nào?", "a": "Thay vì cộng 1, Add-k cộng một số k nhỏ (vd 0.01 hay 0.1) vào tử số và k*|V| vào mẫu số."},
                    {"q": "Nhược điểm lớn nhất của Laplace Smoothing trong thực tế là gì?", "a": "Nó chuyển quá nhiều xác suất từ từ quen thuộc sang từ hiếm, làm méo lệch phân phối thực tế khi |V| lớn."},
                    {"q": "Kneser-Ney Smoothing vượt trội hơn Laplace nhờ nguyên lý gì?", "a": "Dùng khái niệm 'Absolute Discounting' và tính xác suất nối tiếp (Continuation Probability) của từ dựa trên việc nó hay xuất hiện sau nhiều từ khác nhau."},
                    {"q": "Stupid Backoff hoạt động thế nào trong mô hình N-gram lớn (Google N-gram)?", "a": "Nếu N-gram không có, lùi về (N-1)-gram và nhân với hệ số cố định 0.4 thay vì tính xác suất chuẩn hóa."},
                    {"q": "Tổng xác suất sum_{w in V} P_{Laplace}(w | w_{i-1}) bằng bao nhiêu?", "a": "Luôn bằng 1.0 nhờ đã cộng |V| vào mẫu số."}
                ]
            }
        ]
    }
]

print(f"Loaded {len(all_lessons)} sample lessons so far...")
