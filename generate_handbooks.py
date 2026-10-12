import os
import json
import subprocess

OUT_DIR = r"D:\DEMO kế hoạch kì 5\TMG301\SoTay_ChiTiet_17Bai"
TMP_DIR = r"D:\DEMO kế hoạch kì 5\TMG301\.tmp_specs"
BUILDER = r"C:\Users\DELL\.gemini\config\skills\study-forge\scripts\build_handbook.py"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

lessons_data = [
    {
        "slug": "bai01-regex-normalization-editdistance",
        "title": "Bài 01 · Biểu thức chính quy, Chuẩn hóa văn bản & Khoảng cách Edit",
        "subtitle": "Sổ tay 10 ô chi tiết cho Bài 01 môn TMG301: Xử lý chuỗi, Tokenization, Stemming/Lemmatization và Thuật toán Levenshtein Minimum Edit Distance.",
        "source": "01. Regular Expressions - Text Normalization - SDIT Distance.ppt",
        "domain": "nlp",
        "filename": "TMG301_Bai01_SoTay.md",
        "notation": [
            {"sym": "D[i,j]", "role": "data", "read": "đê i j", "means": "khoảng cách edit giữa chuỗi nguồn độ dài i và chuỗi đích độ dài j"},
            {"sym": "w_{sub}", "role": "hyper", "read": "vê sub", "means": "chi phí thay thế ký tự (thường = 2 hoặc 1)"},
            {"sym": "w_{ins}", "role": "hyper", "read": "vê ins", "means": "chi phí chèn ký tự (thường = 1)"},
            {"sym": "w_{del}", "role": "hyper", "read": "vê del", "means": "chi phí xóa ký tự (thường = 1)"}
        ],
        "dag": [
            {"from": "C1", "to": "C2", "label": "chuẩn hóa dữ liệu cho"},
            {"from": "C2", "to": "C3", "label": "đo độ tương đồng chuỗi bằng"}
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
                        {"step": "3. So sánh 'a' và 'a'", "value": "giống nhau -> sub cost = 0. min(2+1, 2+1, 0+0) = 0 thêm từ trước -> D['ca','ha']=2"},
                        {"step": "4. So sánh 't' và 't'", "value": "giống nhau -> D['cat','hat'] = 2"}
                    ],
                    "result": "Levenshtein distance = 2 (thay 'c' bằng 'h' tốn 2 điểm)."
                },
                "picture": {
                    "kind": "plot",
                    "plot": {
                        "xlabel": "i (Chuỗi X)",
                        "ylabel": "j (Chuỗi Y)",
                        "xmin": 0, "xmax": 4, "ymin": 0, "ymax": 4,
                        "curves": [
                            {"expr": "x", "domain": "0:4", "style": "main", "legend": "Đường đi tối ưu"}
                        ]
                    },
                    "caption": "Đường đi ma trận DP từ góc trên trái (0,0) xuống góc dưới phải (n,m)."
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
    }
]

print("Done preparing template script.")
