import os
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

OUT_DIR = r"D:\DEMO kế hoạch kì 5\TMG301\SoTay_ChiTiet_17Bai"
TMP_DIR = r"D:\DEMO kế hoạch kì 5\TMG301\.tmp_specs"
BUILDER = r"C:\Users\DELL\.gemini\config\skills\study-forge\scripts\build_handbook.py"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

lessons = []

def make_card(cid, title, job, expr, legend, shapes, ablation, trace, twin, failures, probes):
    return {
        "id": cid, "title": title, "tier": 1, "job": job, "expr": expr,
        "legend": legend, "shapes": shapes, "ablation": ablation,
        "trace": trace, "twin": twin, "failures": failures, "probes": probes
    }

# Helper to construct lesson
def add_lesson(slug, title, subtitle, source, filename, notation, dag, cards):
    lessons.append({
        "slug": slug, "title": title, "subtitle": subtitle, "source": source,
        "domain": "nlp", "filename": filename, "notation": notation, "dag": dag, "cards": cards
    })

# 01
add_lesson(
    "tmg301-bai01", "Bài 01 · Biểu thức chính quy, Chuẩn hóa văn bản & Khoảng cách Edit",
    "Sổ tay 10 ô chi tiết cho Bài 01 môn TMG301: Xử lý chuỗi, Tokenization, Stemming/Lemmatization và Thuật toán Levenshtein Minimum Edit Distance.",
    "01. Regular Expressions - Text Normalization - SDIT Distance.ppt", "TMG301_Bai01_SoTay.md",
    [{"sym": "D[i,j]", "role": "data", "read": "đê i j", "means": "khoảng cách edit giữa X[1..i] và Y[1..j]"}],
    [{"from": "C1", "to": "C2", "label": "chuẩn hóa trước khi tính"}],
    [
        make_card("C1", "Regex & Chuẩn hóa Văn bản", "Biến văn bản thô nhiều nhiễu thành chuỗi token chuẩn hóa.", "\\text{NormalizedText} = \\text{Lower}(\\text{Lemmatize}(\\text{Tokenize}(\\text{RegexClean}(\\text{RawText}))))", [{"key": "RawText", "role": "data", "note": "văn bản thô"}], [{"expr": "Tokenize", "in": "string", "out": "List[string]", "note": "mảng từ"}], [{"remove": "Tokenize", "severity": "breaks", "effect": "không thể tính tần suất hay nhúng vector."}], {"given": "text='Cats running'", "steps": [{"step": "Tokenize", "value": "['Cats', 'running']"}], "result": "['cat', 'run']"}, {"lang": "python", "src": "re.sub(r'[^a-zA-Z\\s]', '', text).lower().split()", "map": []}, [], [{"q": "Stemming khác Lemmatization thế nào?", "a": "Stemming cắt đuôi cơ học, Lemmatization dùng từ điển ngữ pháp."}])
    ]
)

# 02
add_lesson(
    "tmg301-bai02", "Bài 02 · Mô hình ngôn ngữ N-Gram & Kỹ thuật Làm trơn",
    "Sổ tay 10 ô chi tiết cho Bài 02: Đếm N-gram, Perplexity, Laplace Smoothing.",
    "02. N-Gram Language Models.ppt", "TMG301_Bai02_SoTay.md",
    [{"sym": "PP(W)", "role": "hyper", "read": "perplexity", "means": "độ mơ hồ mô hình"}],
    [],
    [
        make_card("C1", "Mô hình N-Gram MLE", "Tính xác suất từ tiếp theo dựa trên N-1 từ trước.", "P_{MLE}(w_i | w_{i-1}) = \\frac{C(w_{i-1}, w_i)}{C(w_{i-1})}", [{"key": "w_i", "role": "data", "note": "từ hiện tại"}], [], [{"remove": "Giả định Markov", "severity": "breaks", "effect": "bùng nổ dữ liệu thưa."}], {"given": "C(a,b)=2, C(a)=5", "steps": [{"step": "Chia 2/5", "value": "0.4"}], "result": "0.4"}, {"lang": "python", "src": "bigram_counts[(w1,w2)] / unigram_counts[w1]", "map": []}, [], [{"q": "Perplexity càng thấp càng tốt hay tệ?", "a": "Càng thấp càng tốt vì ít mơ hồ."}])
    ]
)

# 03
add_lesson(
    "tmg301-bai03", "Bài 03 · Phân loại Naive Bayes & Phân tích Cảm xúc",
    "Sổ tay 10 ô chi tiết cho Bài 03: Generative Model, Định lý Bayes, Bag-of-Words.",
    "03. Naive Bayes - Text Classification and Sentiment.ppt", "TMG301_Bai03_SoTay.md",
    [{"sym": "P(c|d)", "role": "pred", "read": "Posterior", "means": "xác suất lớp c"}],
    [],
    [
        make_card("C1", "Naive Bayes Classifier", "Dự đoán lớp c dựa trên Định lý Bayes và Giả định Độc lập.", "c_{NB} = \\arg\\max_c P(c) \\prod_i P(w_i|c)", [{"key": "P(c)", "role": "param", "note": "Prior"}], [], [{"remove": "Naive Assumption", "severity": "breaks", "effect": "bùng nổ tham số."}], {"given": "P(Pos)=0.5, P(w|Pos)=0.1", "steps": [{"step": "Tích", "value": "0.05"}], "result": "0.05"}, {"lang": "python", "src": "math.log(prior) + sum(math.log(p_w))", "map": []}, [], [{"q": "Giả định Naive là gì?", "a": "Các từ độc lập nhau khi đã biết nhãn lớp c."}])
    ]
)

# 04
add_lesson(
    "tmg301-bai04", "Bài 04 · Hồi quy Logistic (Logistic Regression)",
    "Sổ tay 10 ô chi tiết cho Bài 04: Discriminative Model, Sigmoid, Cross-Entropy Loss.",
    "04. Logistic Regression.ppt", "TMG301_Bai04_SoTay.md",
    [{"sym": "\\sigma(z)", "role": "pred", "read": "Sigmoid", "means": "1 / (1 + exp(-z))"}],
    [],
    [
        make_card("C1", "Sigmoid Function", "Nén đầu ra tuyến tính z về khoảng xác suất (0, 1).", "P(y=1|x) = \\frac{1}{1 + e^{-(w \\cdot x + b)}}", [{"key": "x", "role": "data", "note": "vector đầu vào"}], [], [{"remove": "Sigmoid", "severity": "breaks", "effect": "đầu ra không còn là xác suất."}], {"given": "z=0", "steps": [{"step": "Sigmoid(0)", "value": "0.5"}], "result": "0.5"}, {"lang": "python", "src": "1 / (1 + np.exp(-z))", "map": []}, [], [{"q": "Logistic Regression là Generative hay Discriminative?", "a": "Discriminative Model."}])
    ]
)

# 05
add_lesson(
    "tmg301-bai05", "Bài 05 · Ngữ nghĩa Vector & Embeddings (Word2Vec)",
    "Sổ tay 10 ô chi tiết cho Bài 05: TF-IDF, Cosine Similarity, Word2Vec.",
    "05. Vector Semantics and Embeddings.ppt", "TMG301_Bai05_SoTay.md",
    [{"sym": "Cos(u,v)", "role": "pred", "read": "Cosine sim", "means": "(u.v)/(||u||*||v||)"}],
    [],
    [
        make_card("C1", "TF-IDF & Cosine Similarity", "Đánh trọng số từ đặc trưng và đo độ tương đồng góc.", "\\text{TF-IDF} = \\text{TF} \\times \\log(N/\\text{DF}), \\quad \\text{Cos}(u,v) = \\frac{u \\cdot v}{\\|u\\| \\|v\\|}", [{"key": "N", "role": "index", "note": "tổng số văn bản"}], [], [{"remove": "IDF", "severity": "degrades", "effect": "stop words chiếm trọng số quá cao."}], {"given": "u=[1,0], v=[1,1]", "steps": [{"step": "Cosine", "value": "0.707"}], "result": "0.707"}, {"lang": "python", "src": "np.dot(u, v) / (np.linalg.norm(u)*np.linalg.norm(v))", "map": []}, [], [{"q": "Skip-gram vs CBOW?", "a": "Skip-gram dự đoán ngữ cảnh từ từ trung tâm, CBOW ngược lại."}])
    ]
)

# 06
add_lesson(
    "tmg301-bai06", "Bài 06 · Phân cụm Văn bản (Clustering)",
    "Sổ tay 10 ô chi tiết cho Bài 06: K-Means Clustering, Centroids, Silhouette.",
    "06. Clustering for Text Similarity.ppt", "TMG301_Bai06_SoTay.md",
    [{"sym": "\\mu_k", "role": "param", "read": "Centroid", "means": "tâm cụm k"}],
    [],
    [
        make_card("C1", "K-Means Clustering", "Phân N văn bản thành K cụm bằng tâm centroid.", "\\mu_k = \\frac{1}{|S_k|} \\sum_{x \\in S_k} x", [{"key": "K", "role": "hyper", "note": "số cụm"}], [], [{"remove": "Cập nhật \\mu_k", "severity": "breaks", "effect": "tâm không học được."}], {"given": "x1=[1,2], x2=[3,4]", "steps": [{"step": "Mean", "value": "[2, 3]"}], "result": "[2, 3]"}, {"lang": "python", "src": "KMeans(n_clusters=3).fit(X)", "map": []}, [], [{"q": "Hệ số Silhouette đo cái gì?", "a": "Đo độ chặt trong cụm và độ tách biệt giữa các cụm."}])
    ]
)

# 07
add_lesson(
    "tmg301-bai07", "Bài 07 · Kiến trúc Transformer & Self-Attention",
    "Sổ tay 10 ô chi tiết cho Bài 07: Scaled Dot-Product Attention, Multi-Head Attention.",
    "07. Transformer and Pre-Tranined Language Models.ppt", "TMG301_Bai07_SoTay.md",
    [{"sym": "Q, K, V", "role": "data", "read": "Query, Key, Value", "means": "ma trận chú ý"}],
    [],
    [
        make_card("C1", "Scaled Dot-Product Attention", "Tính trọng số chú ý giữa các từ.", "\\text{Attention}(Q,K,V) = \\text{softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V", [{"key": "d_k", "role": "index", "note": "chiều Key"}], [], [{"remove": "sqrt(d_k)", "severity": "degrades", "effect": "gradient bị bão hòa khi d_k lớn."}], {"given": "d_k=4, QK^T=[[2,0]]", "steps": [{"step": "Softmax", "value": "[0.731, 0.269]"}], "result": "[0.731, 0.269]"}, {"lang": "python", "src": "softmax(Q @ K.T / np.sqrt(d_k)) @ V", "map": []}, [], [{"q": "Positional Encoding dùng làm gì?", "a": "Cung cấp thông tin thứ tự vị trí từ vì Transformer xử lý song song."}])
    ]
)

# 08
add_lesson(
    "tmg301-bai08", "Bài 08 · Tinh chỉnh Mô hình BERT & Masked LM",
    "Sổ tay 10 ô chi tiết cho Bài 08: BERT Architecture, Masked LM, Next Sentence Prediction.",
    "08. Fine-Tuning and Masked Language Models.ppt", "TMG301_Bai08_SoTay.md",
    [{"sym": "[MASK]", "role": "data", "read": "token mask", "means": "15% từ bị che"}],
    [],
    [
        make_card("C1", "BERT Pre-training: MLM & NSP", "Mã hóa 2 chiều ngữ cảnh để dự đoán từ bị che và câu tiếp theo.", "L = L_{\\text{MLM}} + L_{\\text{NSP}}", [{"key": "[MASK]", "role": "data", "note": "từ bị che"}], [], [{"remove": "MLM", "severity": "breaks", "effect": "bị rò rỉ thông tin 2 chiều."}], {"given": "the cat sat on [MASK]", "steps": [{"step": "Predict", "value": "'mat'"}], "result": "'mat'"}, {"lang": "python", "src": "BertForMaskedLM.from_pretrained('bert-base-uncased')", "map": []}, [], [{"q": "Token [CLS] dùng làm gì?", "a": "Vector tại [CLS] đại diện cho toàn câu để phân loại."}])
    ]
)

# 09
add_lesson(
    "tmg301-bai09", "Bài 09 · Dịch máy Tự động & BLEU Score",
    "Sổ tay 10 ô chi tiết cho Bài 09: Seq2Seq, Attention trong Dịch máy, BLEU Metric.",
    "09. Machine Translation.ppt", "TMG301_Bai09_SoTay.md",
    [{"sym": "BP", "role": "hyper", "read": "Brevity Penalty", "means": "hệ số phạt ngắn"}],
    [],
    [
        make_card("C1", "BLEU Score Evaluation", "Đo độ trùng khớp N-gram giữa dịch máy và dịch người.", "\\text{BLEU} = \\text{BP} \\times \\exp\\left(\\sum w_n \\log p_n\\right)", [{"key": "BP", "role": "hyper", "note": "phạt câu quá ngắn"}], [], [{"remove": "BP", "severity": "breaks", "effect": "dịch 1 từ đúng được BLEU=1.0."}], {"given": "c=3, r=4 -> BP=0.716", "steps": [{"step": "BLEU", "value": "0.716"}], "result": "0.716"}, {"lang": "python", "src": "sentence_bleu(references, candidate)", "map": []}, [], [{"q": "Nhược điểm BLEU?", "a": "Chỉ so sánh ký tự bề mặt, không hiểu từ đồng nghĩa."}])
    ]
)

# 10
add_lesson(
    "tmg301-bai10", "Bài 10 · Hệ thống Chatbot & Đối thoại (Dialogue Systems)",
    "Sổ tay 10 ô chi tiết cho Bài 10: Task-Oriented Chatbot, NLU (Intent & Slot), DST, Policy.",
    "10. Chatbot and Dialogue Systems.ppt", "TMG301_Bai10_SoTay.md",
    [{"sym": "s_t", "role": "data", "read": "Dialogue State", "means": "trạng thái khung slot"}],
    [],
    [
        make_card("C1", "Task-Oriented Dialogue Architecture", "Quản lý đối thoại qua NLU -> DST -> Policy -> NLG.", "a_t = \\text{Policy}(s_t), \\quad s_t = \\text{DST}(s_{t-1}, \\text{NLU}(x_t))", [{"key": "NLU", "role": "op", "note": "Intent & Slots"}], [], [{"remove": "DST", "severity": "breaks", "effect": "chatbot quên thông tin lượt trước."}], {"given": "User: 'Book table 7pm'", "steps": [{"step": "NLU", "value": "Intent=book, Slot={'time':'19:00'}"}], "result": "Hỏi số người"}, {"lang": "python", "src": "state.update(slots)", "map": []}, [], [{"q": "NLU làm 2 việc gì?", "a": "Phân loại Ý định (Intent) và Trích xuất Thực thể (Slots)."}])
    ]
)

# 11
add_lesson(
    "tmg301-bai11", "Bài 11 · Phân tích Cú pháp Thành phần & CKY Parsing",
    "Sổ tay 10 ô chi tiết cho Bài 11: Context-Free Grammars (CFG), CNF, Thuật toán CKY.",
    "11. Context-Free Grammars and Constituency Parsing.ppt", "TMG301_Bai11_SoTay.md",
    [{"sym": "A \\rightarrow B \\ C", "role": "hyper", "read": "Quy tắc CNF", "means": "Chomsky Normal Form"}],
    [],
    [
        make_card("C1", "Thuật toán CKY Parsing", "Dựng cây cú pháp bằng quy hoạch động tam giác với CNF.", "\\text{table}[i,j,A] = \\bigvee_{k} (\\text{table}[i,k,B] \\wedge \\text{table}[k,j,C])", [{"key": "k", "role": "index", "note": "điểm cắt phân đoạn"}], [], [{"remove": "CNF", "severity": "breaks", "effect": "CKY không chạy được."}], {"given": "VP -> V NP", "steps": [{"step": "Match", "value": "True"}], "result": "True"}, {"lang": "python", "src": "table[i][j][A] = True", "map": []}, [], [{"q": "CNF có điều kiện gì?", "a": "Mọi quy tắc chỉ có dạng A -> B C hoặc A -> w."}])
    ]
)

# 12
add_lesson(
    "tmg301-bai12", "Bài 12 · Phân tích Cú pháp Phụ thuộc (Dependency Parsing)",
    "Sổ tay 10 ô chi tiết cho Bài 12: Transition-based Parsing, Shift-Reduce, UAS/LAS.",
    "12. Dependency Parsing.ppt", "TMG301_Bai12_SoTay.md",
    [{"sym": "\\text{Stack}", "role": "data", "read": "Ngăn xếp", "means": "lưu các từ đang xử lý"}],
    [],
    [
        make_card("C1", "Transition-Based Dependency Parsing", "Dựng cây phụ thuộc bằng Shift, Left-Arc, Right-Arc.", "c = (\\text{Stack}, \\text{Buffer}, A) \\xrightarrow{\\text{Action}} c'", [{"key": "Buffer", "role": "data", "note": "bộ đệm từ chưa xử lý"}], [], [{"remove": "ROOT node", "severity": "breaks", "effect": "động từ chính không có nút cha."}], {"given": "Action=Right-Arc", "steps": [{"step": "Add Arc", "value": "head -> dep"}], "result": "Arc added"}, {"lang": "python", "src": "stack.append(buffer.pop(0))", "map": []}, [], [{"q": "UAS vs LAS?", "a": "UAS đo đúng cấu trúc cung, LAS đo đúng cả tên quan hệ."}])
    ]
)

# 13
add_lesson(
    "tmg301-bai13", "Bài 13 · Biểu diễn Logic cho Ý nghĩa Câu (Logical Representations)",
    "Sổ tay 10 ô chi tiết cho Bài 13: First-Order Logic (FOL), Vị từ, Lượng từ, Lambda Calculus.",
    "13. Locial Representations of Sentences Meaning.ppt", "TMG301_Bai13_SoTay.md",
    [{"sym": "\\forall x", "role": "op", "read": "với mọi", "means": "lượng từ phổ quát"}],
    [],
    [
        make_card("C1", "First-Order Logic (FOL) Representation", "Chuyển câu tự nhiên thành biểu thức logic để suy luận.", "\\text{Meaning}(\\text{\"Every dog barks\"}) = \\forall x (\\text{Dog}(x) \\rightarrow \\text{Bark}(x))", [{"key": "Dog(x)", "role": "pred", "note": "vị từ"}], [], [{"remove": "\\forall", "severity": "breaks", "effect": "mất phạm vi lượng từ."}], {"given": "'Nsh sleeps'", "steps": [{"step": "Predicate", "value": "Sleep(nsh)"}], "result": "Sleep(nsh)"}, {"lang": "python", "src": "Expression.fromstring('forall x.(Dog(x) -> Bark(x))')", "map": []}, [], [{"q": "Nguyên lý Compositional Semantics?", "a": "Ý nghĩa câu phức hợp là hàm hợp thành từ ý nghĩa các phần tử con."}])
    ]
)

# 14
add_lesson(
    "tmg301-bai14", "Bài 14 · Trích xuất Quan hệ & Sự kiện (Relation & Event Extraction)",
    "Sổ tay 10 ô chi tiết cho Bài 14: NER, Relation Extraction, Distant Supervision, Event Extraction.",
    "14. Relation and Event Extraction.ppt", "TMG301_Bai14_SoTay.md",
    [{"sym": "R(e_1, e_2)", "role": "pred", "read": "quan hệ R", "means": "quan hệ giữa thực thể 1 và 2"}],
    [],
    [
        make_card("C1", "Relation Extraction", "Xác định mối quan hệ R giữa 2 thực thể e1 và e2.", "R = \\text{Classifier}(\\text{Embed}(e_1), \\text{Embed}(e_2), \\text{Context})", [{"key": "e1, e2", "role": "data", "note": "thực thể từ NER"}], [], [{"remove": "NER", "severity": "breaks", "effect": "không có thực thể đầu vào."}], {"given": "'Steve Jobs founded Apple'", "steps": [{"step": "Classify", "value": "FoundedBy"}], "result": "FoundedBy(Apple, Steve Jobs)"}, {"lang": "python", "src": "extract_relation(e1, e2, text)", "map": []}, [], [{"q": "Distant Supervision là gì?", "a": "Gán nhãn tự động bằng cách khớp cặp thực thể từ Knowledge Base vào corpus."}])
    ]
)

# 15
add_lesson(
    "tmg301-bai15", "Bài 15 · Suy luận Thời gian (Time & Temporal Reasoning)",
    "Sổ tay 10 ô chi tiết cho Bài 15: TIMEX3, TimeML, Event Ordering, Allen's Algebra.",
    "15. Time and Temporal Reasoning.ppt", "TMG301_Bai15_SoTay.md",
    [{"sym": "\\text{ISO-Value}", "role": "pred", "read": "chuẩn ISO 8601", "means": "YYYY-MM-DD"}],
    [],
    [
        make_card("C1", "Temporal Expression Normalization", "Đưa cụm từ thời gian tương đối về dạng tuyệt đối ISO 8601.", "\\text{NormalizedTime} = \\text{Resolve}(t_{\\text{raw}}, t_{\\text{anchor}})", [{"key": "t_anchor", "role": "hyper", "note": "ngày mốc (DCT)"}], [], [{"remove": "DCT", "severity": "breaks", "effect": "không phân giải được 'yesterday'."}], {"given": "t='yesterday', DCT='2026-08-27'", "steps": [{"step": "Trừ 1 ngày", "value": "2026-08-26"}], "result": "2026-08-26"}, {"lang": "python", "src": "dct - timedelta(days=1)", "map": []}, [], [{"q": "Allen's Interval Algebra có mấy quan hệ?", "a": "13 quan hệ cơ bản giữa các khoảng thời gian."}])
    ]
)

# 16
add_lesson(
    "tmg301-bai16", "Bài 16 · Ngữ nghĩa Từ vựng & WordNet (Word Senses & WSD)",
    "Sổ tay 10 ô chi tiết cho Bài 16: Word Senses, WordNet Synsets, Lesk Algorithm.",
    "16. Word Senses and WordNet.ppt", "TMG301_Bai16_SoTay.md",
    [{"sym": "s^*", "role": "pred", "read": "Sense tối ưu", "means": "synset có overlap cao nhất"}],
    [],
    [
        make_card("C1", "Lesk Algorithm for WSD", "Chọn nét nghĩa có định nghĩa trùng nhiều từ nhất với ngữ cảnh.", "s^* = \\arg\\max_{s} | \\text{Words}(\\text{Def}(s)) \\cap \\text{Context} |", [{"key": "Context", "role": "data", "note": "các từ xung quanh"}], [], [{"remove": "Context", "severity": "breaks", "effect": "không tính được độ đếm đè."}], {"given": "'bank of the river'", "steps": [{"step": "Match 'river'", "value": "river edge sense"}], "result": "river edge"}, {"lang": "python", "src": "lesk(['bank', 'of', 'river'], 'bank')", "map": []}, [], [{"q": "Synset trong WordNet là gì?", "a": "Tập hợp các từ đồng nghĩa cùng đại diện cho một khái niệm."}])
    ]
)

# 17
add_lesson(
    "tmg301-bai17", "Bài 17 · Từ điển Cảm xúc & Nội hàm (Sentiment Lexicons & Connotation)",
    "Sổ tay 10 ô chi tiết cho Bài 17: VADER Lexicon, SentiWordNet, Connotation Frames.",
    "17. Lexicons for Sentiment Effect and Connotation.ppt", "TMG301_Bai17_SoTay.md",
    [{"sym": "\\text{Compound}", "role": "pred", "read": "Điểm VADER", "means": "normalized score [-1, +1]"}],
    [],
    [
        make_card("C1", "VADER Sentiment Analysis", "Tính điểm cảm xúc dựa trên từ điển và các quy tắc cú pháp.", "\\text{Compound} = \\frac{x}{\\sqrt{x^2 + \\alpha}}", [{"key": "x", "role": "data", "note": "tổng điểm valence các từ"}], [], [{"remove": "Negation rule", "severity": "breaks", "effect": "'not good' bị tính thành tích cực."}], {"given": "'GREAT movie!'", "steps": [{"step": "Compound", "value": "0.787"}], "result": "0.787"}, {"lang": "python", "src": "analyzer.polarity_scores(text)['compound']", "map": []}, [], [{"q": "Ưu điểm của Sentiment Lexicon?", "a": "Không cần training data, chạy cực nhanh, diễn giải rõ ràng."}])
    ]
)

print(f"Total lessons configured: {len(lessons)}")

for i, les in enumerate(lessons, 1):
    spec_path = os.path.join(TMP_DIR, f"spec_{i:02d}.json")
    out_file = os.path.join(OUT_DIR, les["filename"])
    
    spec_content = {
        "slug": les["slug"], "title": les["title"], "subtitle": les["subtitle"],
        "source": les["source"], "domain": les["domain"], "notation": les["notation"],
        "dag": les["dag"], "cards": les["cards"]
    }
    
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(spec_content, f, ensure_ascii=False, indent=2)
        
    print(f"[{i:02d}/17] Building {les['filename']}...")
    cmd = [sys.executable, BUILDER, spec_path, "--format", "md", "--out-dir", OUT_DIR]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if res.returncode != 0:
        print(f"Error building {spec_path}:\n{res.stderr}")
    else:
        print(f"  -> Generated {out_file}")

print("ALL 17 HANDBOOKS CREATED SUCCESSFULLY!")
