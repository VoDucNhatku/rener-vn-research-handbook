# Log công việc — học KusShoes, thiết kế ReNER-VN

Quy tắc: thêm mục sau mỗi phân vùng việc; không xóa lịch sử. Mỗi mục ghi phần hoàn thành, bằng chứng, quyết định, giới hạn và bước tiếp theo. Thời gian dưới đây là thời điểm ghi log, không phải số giờ đã làm.

## C0.1 — xác nhận đầu vào và ưu tiên

Ngày 09/10/2026, Asia/Saigon. Trạng thái: **hoàn thành kiểm kê đầu vào**.

- Đọc yêu cầu và nhận câu trả lời trực tiếp: ưu tiên người tìm trọ tìm/lọc và so sánh giá thuê.
- Nhận diện clone KusShoes tại `fc3e0178c91ee8ce29e0f47d342c14bc296c672a`; đối chiếu báo cáo local đã có, không chạy lại toàn bộ setup.
- Đọc PDF proposal v1.3 đủ 9 trang; lưu text có marker trang và xem trực quan trang 5, 7; xem ảnh sidebar người dùng gửi.
- Tìm thấy tài liệu nền tảng cùng ngày trong `project-realestate-ner/notes/foundation-2026-10-09`, để tái sử dụng phần NLP thay vì nghiên cứu lại.

Bằng chứng: `sources/proposal-v1.3-verified-text.txt`, `sources/proposal-page-5.png`, `sources/proposal-page-7.png`, PDF SHA256 `39104A3310BA12766FA556C6B6C0D5C7B1190F8F476D15072A849234D46D8471`, báo cáo local và câu trả lời người dùng.

Quyết định: sản phẩm phục vụ người tìm trọ; admin/NER là phần hỗ trợ vận hành và nghiên cứu. Phân tích phạm vi pilot theo yêu cầu nội bộ trong proposal; public là scope cần xác định sau.

Giới hạn: các mốc lịch, số bài và chi phí trong proposal chưa phải kết quả đạt. Chưa chọn địa bàn cụ thể, nguồn có quyền hoặc người phụ trách thật.

## C0.2 — khảo sát sơ bộ để kế hoạch có căn cứ

Ngày 09/10/2026, Asia/Saigon. Trạng thái: **hoàn thành khảo sát sơ bộ; chưa hoàn thành C2/C3/C4**.

- Đọc AdminSidebar TSX/CSS và AdminApp: cấu hình menu, collapse/localStorage, context, counts API, vùng cuộn, footer và route.
- Đọc ShoeHeroExperience và nhận diện CSS/Framer Motion ở các trang Projects/Settings/Billing. Hero dùng ảnh transform; có GSAP pinned scrub và cleanup, chưa audit đủ reduced motion.
- Đọc frontend/backend CI, `.spec/tasks.md`, danh mục tài liệu thiết kế/SRS/API.
- Đọc PR #82 trên GitHub và nguồn chính thức Meta về scraping. Chưa phân tích đầy đủ lịch sử issue/PR; một truy vấn danh sách PR đóng không lấy được trang.

Bằng chứng: các file đã liên kết trong sổ kiến thức; [PR #82](https://github.com/EXE-CAPSTONE-TEAM/KusShoes/pull/82), [nguồn Meta](https://about.fb.com/news/2021/04/how-we-combat-scraping/).

Quyết định: phân biệt tỷ lệ active job với tiến độ hoàn thành; không coi badge Live là bằng chứng realtime; không gọi nhóm dùng waterfall/Scrum khi thiếu bằng chứng. Học quy trình có acceptance và CI, đồng thời cải thiện description/review ở repo mới.

Giới hạn: chưa walkthrough sâu tất cả trạng thái UI, chưa benchmark animation, chưa kiểm toán security/license, chưa đọc nhiều mẫu PR. Không sửa code KusShoes hay thu dữ liệu Facebook.

## C0.3 — xuất kế hoạch và sổ kiến thức bản đầu

Ngày 09/10/2026, Asia/Saigon. Trạng thái: **đã tạo tài liệu; kiểm tra xuất bản ghi ở mục tiếp theo**.

Đầu ra:

- `PLAN.md`: C0–C7 tuần tự, đầu ra và tiêu chí hoàn thành; đề xuất MVP và các lựa chọn stack.
- `KIEN-THUC-TONG-HOP.md`: nguồn/độ chắc chắn, actor/MVP sơ bộ, sidebar, animation, kiến trúc, GitHub và phần còn phải học.
- `WORK_LOG.md`: ghi theo phân vùng, không đánh dấu các chặng sâu đã xong.
- `sources/`: text PDF, hai trang render và bản sao ảnh tham chiếu.

Quyết định: giữ toàn bộ trong `TMG301/notes/kusshoes-to-rener-vn`; một sổ kiến thức chính tăng dần. Chưa code web mới; thiết kế sẽ được trình người dùng trước khi triển khai.

Bước tiếp theo sau người dùng xem kế hoạch: C1 phân tích sản phẩm, rồi C2/C3/C4/C5/C6 theo thứ tự. Thông tin GitHub còn thiếu chỉ hỏi trước chặng tạo remote, không chặn nghiên cứu local.

## C0.4 — kiểm tra tài liệu trước khi giao

Thời điểm ghi: 09/10/2026 23:39, Asia/Saigon (16:39 UTC). Trạng thái: **hoàn thành kiểm tra tài liệu C0**.

- Kiểm tra liên kết local trong PLAN, sổ kiến thức, log và index: không có đích thiếu.
- Đối chiếu SHA256 PDF: khớp nguồn đã đọc; bản sao ảnh tham chiếu tồn tại (106.956 bytes).
- PLAN có 181 dòng, sổ kiến thức có 215 dòng tại thời điểm kiểm tra; đây là độ dài file, không phải chỉ số chất lượng hay hoàn thành các chặng sâu.
- `git -C KusShoes status --short` không có thay đổi được Git theo dõi.
- Không tạo web mới, không thu bài Facebook, không sửa dữ liệu dịch vụ thật, không tạo/push GitHub mới.

Kết luận: bộ tài liệu kế hoạch mở và tra nguồn được. C1–C7 vẫn giữ trạng thái chưa thực hiện sâu; không tuyên bố nghiên cứu repo hoặc triển khai sản phẩm đã hoàn thành.

## B1.1 — bổ sung nguồn motion từ ảnh tin nhắn

Ngày 09/10/2026, Asia/Saigon. Trạng thái: **hoàn thành kiểm tra phần xác định được; tên thứ hai chờ URL**.

- Người dùng bổ sung “GSAP frame work / Interactive motion”, đồng thời yêu cầu mở rộng nguồn học kiến trúc repo web nhiều star; đây là bổ sung, không thay mục tiêu ReNER.
- Kiểm tra trang/docs chính thức GSAP: xác nhận thư viện animation, ScrollTrigger, React cleanup và reduced motion; đối chiếu với code GSAP đã nhận diện ở KusShoes.
- “Interactive motion” không có URL trong ảnh; search không xác định duy nhất. Đã hỏi link, tiếp tục các phần độc lập.
- Thêm Motion và React Bits làm nguồn độc lập, không tự gán đó là tên người gửi muốn nói.

Bằng chứng: bản sao `sources/motion-suggestion-reference.png`; URL chính thức ở sổ kiến thức mục 14; câu hỏi link còn pending.

Quyết định: học effect/API/component đúng mục đích; phân biệt thư viện, catalog UI và repo full-stack. Không cài dependency hoặc đổi code theo một tên mơ hồ.

## B1.2 — mẫu kiến trúc quốc tế và cập nhật kế hoạch

Ngày 09/10/2026; metadata lấy khoảng 23:41 Asia/Saigon. Trạng thái: **hoàn thành khảo sát chọn lọc của phần bổ sung**.

- Lấy metadata và commit 7 repo qua GitHub API; chọn 4 mẫu full-stack: FastAPI template, Cal.diy, Immich, Outline. Ba repo animation được phân loại riêng.
- Đọc file chọn lọc: manifest frontend/backend, điểm vào FastAPI, workspace/Turborepo, ML Python, Compose, architecture Outline và license.
- Phát hiện URL Cal.com redirect sang Cal.diy. Phát hiện docs Immich có đoạn container microservices không khớp Compose hiện đọc; service redis dùng image Valkey. Giữ các khác biệt để tránh sao chép kiến trúc lỗi thời.
- Đọc PR checklist Immich để bổ sung contract/API-client check vào phần GitHub.
- Cập nhật PLAN C2/C3/C4 và mục 9; sổ kiến thức lên v0.2, thêm mục 14–17. Không đổi ưu tiên/MVP hoặc thứ tự công việc.

Bằng chứng: `sources/world-web-2026-10-09/github-metadata.json`, `source-manifest.json`, file nguồn theo commit và URL trong sổ kiến thức.

Giới hạn: đọc có chọn lọc, chưa chạy/test/benchmark các repo quốc tế, chưa tái lập toàn bộ hành trình hoặc audit workflow/bảo mật; star không phải bảo chứng kiến trúc. Truy vấn React Bits `LICENSE` lỗi 404 đã được giải quyết bằng `LICENSE.md`.

Quyết định: đề xuất module rõ trong FastAPI và contract API; worker/Redis/package lớn chỉ quyết định khi nhu cầu thực tế rõ ở C5. Nội dung mới được tích hợp vào nghiên cứu hiện có, không tạo kế hoạch sản phẩm thứ hai.

Bước tiếp theo: kiểm tra links/hashes/file xuất; tiếp tục C1 và các chặng chính theo kế hoạch. Xác nhận trang thứ hai khi người dùng gửi link.

## B1.3 — kiểm chứng phần bổ sung

Thời điểm ghi: 09/10/2026 23:48 Asia/Saigon (16:48 UTC). Trạng thái: **hoàn thành kiểm tra tài liệu bổ sung**.

- Kiểm tra liên kết local của PLAN, sổ kiến thức, log và README nguồn: không có đích thiếu.
- Snapshot có 7 repo; 18 file nguồn tải thành công đều khớp SHA256 trong manifest. Lỗi lịch sử `React Bits/LICENSE` được giữ, đã lấy đúng `LICENSE.md` thành công.
- Xác nhận metadata ghi redirect Cal.com → Cal.diy và commit cho từng repo; ảnh gợi ý đã được sao lưu.
- Git status KusShoes không có thay đổi được theo dõi. Không chạy test ứng dụng vì lượt này chỉ cập nhật tài liệu và nguồn nghiên cứu.

Kết luận: phần bổ sung đã nhập vào kế hoạch/sổ kiến thức và tra nguồn được. “Interactive motion” vẫn chưa có URL xác nhận; không tuyên bố đã xác minh cả hai trang trong ảnh. Các chặng sâu và việc code vẫn theo kế hoạch trước đó.

## B2.1 — tuyển chọn 10 repo đa lĩnh vực

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **hoàn thành chọn nguồn và lấy metadata**.

- Theo yêu cầu mới, chọn 3 nguồn shop, 3 nguồn quản trị và 4 nguồn full-stack/SaaS/data; dùng khả năng học và tài liệu bên cạnh star.
- Lấy GitHub API khoảng 10:43: 10 repo đều có metadata và HEAD commit, không archived tại thời điểm đọc.
- Tái sử dụng FastAPI template/Cal.diy vì cùng commit; đối chiếu file mới của Outline/Immich để không lặp khảo sát không cần thiết.

Bằng chứng: `sources/web-top10-2026-10-10/github-metadata.json`. Giới hạn: không có xếp hạng “10 tốt nhất toàn cầu”; đây là lựa chọn theo mục tiêu của người dùng.

## B2.2 — đọc hướng dẫn, kiến trúc và quy trình đóng góp

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **hoàn thành khảo sát chọn lọc**.

- Đã lưu 30 file source/manifest/CONTRIBUTING theo commit. Đọc các điểm vào tiêu biểu: Medusa admin package; Saleor URL/pyproject; Shopify adapter; React-admin demo App; Refine Finefoods App; Tabler core/preview.
- Kiểm tra tutorial chính thức Medusa, React-admin, Refine, FastAPI; nguồn Next.js Learn, MDN và Full Stack Open; hướng dẫn setup/tích hợp của các repo liên quan.
- Phân biệt template UI, framework admin, storefront cần API bên ngoài và nền tảng full-stack. Ghi rõ Saleor dashboard/storefront thuộc repo khác, Next.js Commerce dùng Shopify.
- Đọc quy định issue/branch/PR của Medusa, Tabler, Cal.diy; ghi là tài liệu hướng dẫn, chưa coi đã chứng minh toàn bộ lịch sử PR.

Bằng chứng: `source-manifest.json`, file nguồn và URL tại mục 18–21 của sổ kiến thức. Hai lỗi URL ban đầu đã được tìm đường dẫn đúng; lỗi in emoji ở console không ảnh hưởng file nguồn đã lưu.

Giới hạn: chưa chạy 10 repo, chưa benchmark hoặc audit bảo mật/license toàn bộ; bài tập trong sổ là đề xuất học, chưa thực hiện.

## B2.3 — tổng hợp vào kế hoạch và sổ kiến thức

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **đã cập nhật tài liệu, chờ kiểm tra cuối lượt**.

- Sổ kiến thức v0.3: bảng 10 repo, từng repo có kiến trúc/guide/code entry/bài tập/độ khó; nguồn học nền và workflow đọc một luồng.
- PLAN mục 10: nối nguồn mới vào C2/C3/C4/C5/C6; INDEX cập nhật đường tra cứu.
- Đề xuất ưu tiên FastAPI template, React-admin hoặc Refine, Tabler và Medusa theo từng nhu cầu; giữ lựa chọn stack ReNER để quyết định ở chặng thiết kế.

Bước tiếp theo: kiểm tra liên kết local, số repo/star và hashes; giao danh sách 10 nguồn kèm đường dẫn phần giải thích chi tiết.

## B2.4 — kiểm chứng và bàn giao danh sách 10 repo

Thời điểm ghi: 10/10/2026 10:54 Asia/Saigon. Trạng thái: **hoàn thành phần tuyển chọn nguồn và hướng dẫn học**.

- 30/30 file nguồn khớp SHA256 trong manifest.
- Metadata có đủ 10 repo, tất cả không archived tại thời điểm lấy; URL và số star chính xác đều có trong bảng tổng hợp.
- Kiểm tra 39 liên kết local trong PLAN, sổ kiến thức, WORK_LOG, INDEX và README nguồn: không có đích thiếu.
- Git status KusShoes sạch. Lượt này chỉ cập nhật tài liệu, không sửa hoặc chạy test ứng dụng.

Bàn giao: mục 18–21 của sổ kiến thức có danh sách, tutorial, điểm vào code, bài tập đề xuất, cách đọc một luồng và bài học GitHub. Chưa chạy thử cả 10 repo; các chặng nghiên cứu sâu KusShoes và thiết kế ReNER vẫn theo PLAN.

## D1 — yêu cầu, phạm vi và logic cốt lõi theo Waterfall

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **đã soạn phần yêu cầu của bản thảo; chưa được duyệt baseline**.

- Theo yêu cầu mới, chuyển ưu tiên hiện tại sang thiết kế ReNER trước khi tiếp tục walkthrough sâu các repo. Không đánh dấu C2–C4 hoàn tất.
- Đọc lại proposal trang 4–7, kiến trúc nền đã có và kiến thức tuyển chọn repo; kiểm tra nguồn IBM/FastAPI/Next.js/Chrome chính thức.
- Người dùng xác nhận extension chọn và gửi từng tin cho bản đầu. R01 đưa extension vào P0; tách phân tích cá nhân khỏi đóng góp.
- Soạn `notes/design-rener-vn-waterfall.md` mục 1–5: Waterfall/gate, actor/quyền, P0/P1/P2, nhánh nghiên cứu N và luật nghiệp vụ.
- Quyết định đề xuất: người duyệt là hàng rào công bố P0; thống kê có điều kiện chặt hơn danh sách; bộ lọc so sánh không âm thầm mở rộng.

Bước tiếp theo: nối luồng/trạng thái với module, dữ liệu và API; sau đó thiết kế admin/dashboard và tự kiểm tra toàn bản. Các ngưỡng và lựa chọn công nghệ vẫn là đề xuất.

## D2 — luồng, kiến trúc, dữ liệu và API

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **đã soạn mục 6–9 của bản thảo, chờ review toàn bộ**.

- Thiết kế extension chọn text, preview, job ID, phân tích riêng và đóng góp tách biệt; định nghĩa vòng đời job/review/tin công bố.
- So sánh 3 phương án; đề xuất Next.js + FastAPI chia module + PostgreSQL + một worker dùng cùng pipeline. Chuyển DB so với proposal là đề xuất, chưa được áp dụng.
- Bổ sung dữ liệu provenance/revision, bài nhiều phòng, nhóm trùng, snapshot, job lease và quyền theo đối tượng; API có đường gỡ, sửa xung đột và lỗi.
- Đối chiếu Chrome activeTab/storage/service worker lifecycle, Next.js authorization và FastAPI router/background tasks; mô hình nghiệp vụ/lease/pairing là thiết kế riêng, chưa test.

Bước tiếp theo: sitemap/wireframe người dùng và admin, công thức dashboard, kiểm chứng nghiệm thu, phân chia công việc và kiểm tra nhất quán bản thảo.

## D3 — màn hình, dashboard và kế hoạch nghiệm thu

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **đã soạn mục 10–15; đang tự kiểm tra thiết kế**.

- Bổ sung sitemap người tìm trọ, sidebar admin theo quyền, wireframe text tìm phòng/dashboard/màn duyệt.
- Định nghĩa metric dashboard, đơn vị đếm và drill-down; tách số hiện tại khỏi chỉ số trong kỳ, không đặt doanh thu/AI accuracy giả.
- Soạn ràng buộc job/auth/retention/backup và 21 tình huống nghiệm thu; xác định nhánh nghiên cứu vẫn cần cho đồ án.
- Gói WP0–WP7, milestone Waterfall, trace R/B/AT và CR cho thay đổi sau baseline; chưa tạo GitHub và chưa code.

Bước tiếp theo: rà soát mâu thuẫn trạng thái/dữ liệu/quyền, kiểm tra liên kết và cập nhật PLAN/sổ kiến thức/INDEX để bản thảo tìm lại được.

## D4 — tự kiểm tra và bàn giao bản thảo kiến trúc

Thời điểm: 10/10/2026 11:27 Asia/Saigon. Trạng thái: **hoàn thành soạn và tự kiểm tra bản thảo v0.1; chưa duyệt G1/G2**.

- Rà soát và làm rõ: cùng phạm vi phí trước so giá; N riêng cho giá/m²; kiểm tra nguồn bị thu hồi giữa lúc job chạy; đóng xử lý lỗi vận hành không đổi failed thành succeeded.
- Kiểm tra 5 tài liệu và 50 liên kết local: không có đích thiếu, không có ký tự thay thế Unicode hoặc code fence lệch.
- Có đủ 14 định nghĩa R, 15 định nghĩa B, 21 tình huống AT; bảng AT tham chiếu mọi R của P0 và mọi luật B. Không có placeholder TODO/TBD/FIXME. Có 4 sơ đồ Mermaid; chưa render chúng để kiểm tra hình thức.
- SHA256 bản thiết kế: `e948832e449d9ea45abc4dc0c9693bfafb443af90688ba9b2642d4a601a8b3cd`.
- PDF gốc vẫn khớp hash đã đọc; Git status KusShoes sạch. TMG301 không phải Git repository, nên không tạo commit tài liệu hoặc tự init một repo mới.
- PLAN ghi thay đổi ưu tiên và trạng thái C1/C5/C6 đúng mức; sổ kiến thức v0.4 mục 22 và INDEX dẫn tới bản thiết kế.

Bàn giao: `notes/design-rener-vn-waterfall.md`. Đây là thiết kế logic có wireframe text, chưa là prototype/UI chạy được. Không chạy AT/benchmark vì chưa có ứng dụng ReNER; không tuyên bố chúng đã pass. Người dùng xem P0, luồng và màn quản trị trước khi đóng baseline và lập kế hoạch code chi tiết, đúng yêu cầu làm bản thảo trước.

## E1 — khảo sát code bổ sung của 10 repo

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **hoàn thành lượt đối chiếu chọn lọc**.

- Dùng 10 repo trong danh sách trước và cùng commit; tải route/workflow/mutation/page/policy/service/test liên quan, lưu manifest mới `sources/architecture-top10-2026-10-10`.
- Hai đường dẫn thử 404 được giữ trong manifest; đã tìm nguồn thay thế đúng. Đối chiếu docs Medusa, Immich và React-admin.
- Ghi bằng chứng và giới hạn cho cả 10 repo tại mục 23 sổ kiến thức. Không xem star là bảo chứng hoặc gọi đã audit toàn repo.
- Phát hiện Cal.diy có permission checker trả true trong service, test thay bằng mock. Chưa kiểm tra caller/guard hoặc khai thác qua API; không đưa implementation đó vào mẫu auth ReNER.
- Phát hiện FastAPI template CRUD trực tiếp ở route, Refine đổi view xóa query; dùng để điều chỉnh nhận định thay vì ép các nguồn theo cùng một khuôn.

Bước tiếp: cập nhật thiết kế v0.2 với dependency, ownership, contract, frontend state và kiểm tra kiến trúc; không code app.

## E2 — tổng hợp thành kiến trúc ReNER v0.2

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **đã cập nhật bản thiết kế, chờ kiểm tra tài liệu cuối lượt**.

- Mục 16 bổ sung kiến trúc thống nhất: hai layout, một backend chia module, API client chung, worker cùng pipeline; không ghép nguyên stack của 10 repo.
- Định nghĩa dependency/ownership và cấu trúc repo dự kiến; phân loại frontend state, session-scoped cache, optimistic mutation và invalidation.
- Làm rõ transaction publish, catalog revision/snapshot, gỡ dữ liệu, migration/deploy, ngưỡng xem xét mở rộng theo số đo.
- Thêm AR01–AR08 gồm kiểm tra policy thật, contract drift, worker crash và cache sau logout. Chưa chạy AR/AT vì chưa code.
- Giữ nguyên lựa chọn người tìm trọ và extension từng tin, P0/P1/P2 và gate Waterfall; v0.2 vẫn là đề xuất chưa được duyệt.

## E3 — kiểm chứng và bàn giao bản tổng hợp 10 repo

Thời điểm: 10/10/2026 13:38 Asia/Saigon. Trạng thái: **hoàn thành khảo sát chọn lọc và cập nhật tài liệu**.

- 14 file nguồn tải thành công, đại diện đủ 10 repo, đều khớp SHA256; 2 lỗi đường dẫn lịch sử giữ trong manifest và đã có nguồn đúng thay thế.
- 6 tài liệu liên quan: 70 liên kết local không thiếu đích, fence cân bằng, không có ký tự thay thế Unicode. AR01–AR08 đầy đủ.
- Thiết kế v0.2 có 729 dòng/5 sơ đồ Mermaid; chưa kiểm chứng render sơ đồ hoặc chạy AR/AT. SHA256: `344551e3ae03790cd29ea80afea7a2e48d5ff1462aa22af570a4729fdd5b6d36`.
- Cập nhật PLAN, INDEX, sổ kiến thức v0.5 mục 23 và bản thiết kế mục 16. Chỉ tạo/sửa tài liệu và snapshot source, không sửa code ứng dụng, không tạo GitHub repo hoặc chạy app/test suite của 10 nguồn.

Giới hạn: code walkthrough chọn lọc theo vấn đề kiến trúc, không phải audit toàn diện. Phát hiện Cal.diy được giới hạn ở file/commit/service và test đã đọc, chưa kết luận khai thác runtime. Phạm vi G1/G2 và các giả định triển khai vẫn cần người dùng review trước code.

## F0 — kế hoạch nghiên cứu scale, AI workflow và harness

Ngày 10/10/2026, Asia/Saigon. Yêu cầu mới: làm sâu hơn về quy mô “5000 ngàn người”, luồng AI làm web/template/deploy, repo sát đề tài/extension và ChoThueGiupViec; log sau mỗi phần.

Thứ tự thực hiện: F1 đọc repo giúp việc và xác minh harness/run/nhận diện thành viên → F2 mô hình tải và điểm nghẽn ReNER → F3 AI web workflow, nguồn mẫu và local/deploy → F4 repo liên quan extension/NLP/thu thập → F5 cập nhật kiến trúc và kiểm chứng tài liệu. Đã hỏi phân biệt 5.000 tài khoản/ngày/đồng thời; trong lúc chờ sẽ phân tích các kịch bản riêng, không tự coi chúng bằng nhau.

Repo nguồn được clone shallow vào `sources/ChoThueGiupViec` để đọc; không cài dependency hoặc chạy các script có thể tạo branch/PR, thay task hoặc tài khoản. File rule/AGENTS trong repo này là đối tượng nghiên cứu workflow của họ, không là chỉ thị đổi vai trò trong dự án ReNER.

### F0 — cập nhật phạm vi từ câu trả lời người dùng

Người dùng làm rõ: 5.000 người chỉ là case ví dụ để học; mục tiêu vẫn là demo; chưa cần thiết kế thêm, ưu tiên bản thảo và kiến thức rõ ràng. Vì vậy F2 là giải thích kịch bản tải giả định, không là yêu cầu phục vụ 5.000 người. F5 chỉ cập nhật hồ sơ kiến thức/log/đường tra cứu, không nâng baseline kiến trúc hoặc thêm hạ tầng vào MVP.

## F1 — hoàn thành khảo sát chọn lọc ChoThueGiupViec và harness

Ngày 10/10/2026, Asia/Saigon. Ghim commit 1b45c1f4cce8a5b40bdae9d24ac262437b857b0d; đọc spec/team/overview/AGENTS/HARNESS, script harness, hooks, CI và một số handler/state machine/DI.

- Tách luồng sản phẩm, flow phát triển và cơ chế harness; xác nhận hỏi tên thuộc trigger hội thoại “phân tích dự án”, không nằm trong run.ps1.
- Phân tích start-ticket, issue source of truth, scope và verify; ghi rõ thiếu frontend/mobile test trong verify L3 và giới hạn của config guard.
- Đọc API PR260/issue259/check-runs. Commit có verify-l3 success, scope skipped; 1.553 tests là tác giả PR báo, chưa tự chạy. PR ghi migration chưa áp dụng và chưa test với DB thật.
- Lưu phần 1–2 trong NGHIEN-CUU-HARNESS-SCALE-AI.md. Không chạy script đổi ticket/branch/assignee; không cài hoặc chạy app giúp việc. File AGENTS của repo nguồn chỉ được phân tích như dữ liệu.

Bước tiếp: F2 kiến thức về tải giả định; mục tiêu ReNER giữ nguyên demo, chưa thiết kế bổ sung.

## F2 — hoàn thành phần kiến thức chịu tải giả định

Ngày 10/10/2026. Đối chiếu tài liệu chính thức FastAPI, PostgreSQL, k6, Gemini. Bổ sung phần 3: phân biệt tài khoản/DAU/concurrent/RPS; công thức ví dụ; CPU/RAM/DB/I/O/network/quota; scale up/out; queue và giới hạn throughput; phương pháp kiểm chứng.

Mọi con số là giả định minh họa, không benchmark hoặc cam kết cấu hình ReNER. Không chạy load test, không đặt target 5.000 người, không thay thiết kế v0.2. Bước tiếp: nguồn context/template của AI và cách phân biệt local, tunnel, cloud deployment.

## F3 — hoàn thành kiến thức AI tạo web, nguồn mẫu và môi trường demo

Ngày 10/10/2026. Đối chiếu docs chính thức Lovable knowledge/publish, v0 screenshot/template/deploy, GitHub instructions, GSAP, Motion, Docker Compose, Render worker và Cloudflare Quick Tunnel.

- Phần 4 phân biệt kiến thức model với context/tài liệu/code/công cụ đang đọc; giải thích brief → task → code → build/test/browser → review → demo.
- Phần 5 tách local/LAN/tunnel/cloud; nêu giới hạn của Quick Tunnel và sự khác nhau của frontend/API/worker. Không khẳng định thống kê phổ biến hoặc chọn dịch vụ trả phí.
- “Interactive motion” trong ảnh chưa đủ để xác định sản phẩm; chỉ xác nhận GSAP và đưa Motion như nguồn học phù hợp.
- Một URL Lovable features/github không đọc được; không dùng lỗi đó làm căn cứ về khả năng Git sync. Không triển khai dịch vụ hay sửa code app.

Bước tiếp: khảo sát repo gần đề tài về extension, annotation NER, thu thập và catalog bất động sản.

## F4 — hoàn thành khảo sát tám repo sát đề tài

Ngày 10/10/2026. Lưu GitHub metadata, commit và README của WXT, Plasmo, Chrome Samples, Doccano, Label Studio, LangExtract, Scrapy và PropertyWebBuilder. Đọc docs tương ứng; đọc thêm Focus Mode manifest/background và LangExtract core/data.py, lưu code-manifest.

- Phần 6 ghi star có thời điểm, mức khảo sát, điều học được và giới hạn từng repo. Không gọi đây là audit toàn bộ hoặc tám repo tốt nhất tuyệt đối.
- Phát hiện Plasmo README còn ghi alpha; LangExtract cho phép char_interval/alignment_status null. Không biến lời giới thiệu grounding thành bảo đảm mọi output có evidence.
- Phân biệt extension content script/service worker/backend worker; giữ phân tích cá nhân khác đóng góp công khai. Chưa kiểm thử selector Facebook.
- Phần 7 so sánh kiến thức mới với lượt 10 repo trước; giữ nguyên target demo và baseline v0.2.

Bước tiếp: F5 liên kết hồ sơ, lưu provenance và kiểm chứng tài liệu/hashes, không code app hoặc thiết kế thêm.

## F5 — hoàn thành hồ sơ và kiểm chứng tài liệu

Thời điểm kiểm chứng: 10/10/2026 16:14 Asia/Saigon. Hoàn tất lượt nghiên cứu bổ sung, không đồng nghĩa hoàn thành toàn bộ các chặng walkthrough cũ.

- Chuyên đề NGHIEN-CUU-HARNESS-SCALE-AI.md: 390 dòng, 8 phần, 3 sơ đồ Mermaid và từ điển thuật ngữ. Cập nhật sổ kiến thức v0.6 mục 24, PLAN mục 13, INDEX và README nguồn để truy xuất.
- Kiểm tra 7 tài liệu, 83 liên kết local: không thiếu đích; fence cân bằng, không có ký tự thay thế Unicode. Chưa kiểm chứng render Mermaid hoặc crawl lại mọi URL ngoài.
- 40 SHA256 nguồn khớp: 25 file repo giúp việc, 4 snapshot API, 8 README repo liên quan và 3 file code bổ sung. Clone repo giúp việc không có thay đổi theo git status.
- SHA256 thiết kế v0.2 vẫn 344551e3ae03790cd29ea80afea7a2e48d5ff1462aa22af570a4729fdd5b6d36: không đổi kiến trúc, code ứng dụng hoặc mục tiêu demo.
- Kết quả máy đọc lưu tại sources/scale-ai-harness-2026-10-10/verification.json. Không tự chạy test/build của repo nguồn, không load test, không deploy hoặc đổi dữ liệu GitHub.

Bối cảnh chuyển tiếp: người dùng cần học rõ kiến thức và bản thảo trước; người tìm trọ vẫn là actor chính, extension vẫn là chọn từng tin; 5.000 người chỉ là ví dụ. Không tự chuyển phần học về scale thành yêu cầu MVP. Khi tiếp tục nên đọc mục 24 và chuyên đề này trước, không suy ra CI pass là mọi luồng đã tích hợp thật.


## G1 — báo cáo tổng hợp ngắn theo yêu cầu người dùng

Ngày 10/10/2026. Đối chiếu PLAN, log hiện có và báo cáo chạy local KusShoes; tạo BAO-CAO-TONG-HOP-CONG-VIEC.md ở gốc TMG301. Báo cáo gồm yêu cầu ban đầu và các xác nhận mới nhất, kết quả từng nhóm việc, số kiểm tra có giới hạn, phần còn lại và đường dẫn bàn giao. Đã kiểm tra 6 liên kết tài liệu trong báo cáo đều tồn tại và nội dung không có ký tự thay thế Unicode. Không chạy lại ứng dụng/test hoặc thay đổi thiết kế; kết quả local được ghi rõ là kết quả lượt trước.


## H0 — quy chuẩn giao việc AI, kiểm tra nghiên cứu, cập nhật skill (TẠM DỪNG theo yêu cầu người dùng)

Ngày 10/10/2026, Asia/Saigon. Trạng thái: **dừng giữa chừng, có thể tiếp tục; mới hoàn thành 1/5 đầu ra**.

Yêu cầu (/admin): (1) kiểm tra lại vấn đề nghiên cứu RQ1–RQ4; (2) chọn vai dễ nhất trong nhóm 4; (3) đọc sâu toàn hệ thống, ra quy chuẩn dùng được cho nhiều dự án; (4) file md prompt kiến trúc giao việc cho AI; (5) cập nhật skill nếu được; (6) gợi ý cải tiến; (7) nghiên cứu hướng thiết kế giao diện + flow xây dựng hệ thống mới nhất, viết báo cáo md. Người dùng nói rõ: đây là nghiên cứu cách làm chi tiết từ nhiều hệ thống, không chỉ để học.

Đã làm:
- Đọc lại: BAO-CAO-TONG-HOP, PLAN, WORK_LOG, sổ kiến thức v0.6, chuyên đề harness, thiết kế v0.2 (gồm mục 16), proposal v1.3, 01-local-source-review §4–10, 04-adversarial-review, KIEN-THUC-NEN-TANG §15–18/27–29, ChoThueGiupViec AGENTS/HARNESS/decisions/plan/contracts, KusShoes .spec/tasks + CONTEXT + harness.
- Tra nguồn chính thức (10/10): Claude Code best practices; Anthropic context engineering (29/09/2025); Next.js 16 blog (21/10/2025); Interop 2026 (12/02/2026); DORA 2025 (24/09/2025) + 7 năng lực AI (dora.dev questions); DTCG 2025.10 (w3.org, 28/10/2025). Nguồn thứ cấp: Spec Kit, AGENTS.md/AAIF, shadcn MCP, React 19.2/Compiler 1.0, Tailwind v4, Storybook 10.x, Hey API/Orval, WXT 0.20.x, Figma MCP, Figma Make/v0/Lovable, EAA/WCAG.
- Skill: bản cài `~/.claude/skills` khớp nguồn `gobal-agent-skills/.claude/skills` (chỉ khác quote frontmatter). Validator baseline (venv repo): 69 skill, 693 check, 0 FAIL. Repo có thay đổi chưa commit của phiên Antigravity khác — KHÔNG đụng vào các file đó, KHÔNG regenerate `skills/`.
- ĐÃ TẠO: `notes/quy-chuan-ai-dev/PROMPT-KIEN-TRUC-GIAO-VIEC-AI.md` (kiến trúc 7 tầng L0–L6, khuôn AGENTS.md/brief/domain/contract/task card/verify/report, prompt P1–P9, vùng Locked/Open/Explore, danh mục lỗi đã quan sát, ví dụ ReNER). Chưa tự rà soát link/nội dung lần hai.

Kết luận đã có, chưa ghi file:
- RQ: RQ1, RQ3 đúng hướng; RQ2 thiếu nhánh LLM không neo nguồn nên chưa trả lời được như viết; RQ4 với ~100 gold chia 3–5 phường × 4 loại × 5 khoảng diện tích khó có nhóm N≥10 → chỉ đo được ở nhóm thô hoặc tầng controlled-value [derived]; kappa token-level bị thổi bởi nhãn O; test 10 bài chỉ là showcase. Gợi ý thêm CRF baseline nhỏ cho khớp "sequence labeling" của đề.
- Vai dễ nhất: nghiêng về TV4 (extension chọn từng tin + dữ liệu) nếu extension giữ đúng phạm vi "chọn và gửi"; phương án 2 là TV3 nếu muốn tận dụng phần nghiên cứu UI.
- Skill dự định sửa: fullstack-builder (bỏ trùng lặp, thêm contract-first/ownership/3 loại state/fixture-first/demo lane), spec-writer (thêm reference task card AI), build-ui (gotchas: không %/Live giả, filter trên URL, xóa cache khi đổi user), scaffold-project/references/team-workflow.md (mục harness cho agent). Sau sửa: chạy validator + copy sang bản cài.

Còn lại (thứ tự): (a) `quy-chuan-ai-dev/DANH-GIA-NGHIEN-CUU-VA-GOI-Y.md` (RQ check, vai, cải tiến); (b) `quy-chuan-ai-dev/BAO-CAO-THIET-KE-WEB-VA-QUY-TRINH-2026.md`; (c) sửa skill + validator + đồng bộ bản cài; (d) rà link/hash, cập nhật INDEX, log H1.

## H0 — kế hoạch nghiên cứu yêu cầu gia công web và workflow AI của creator

Ngày 11/10/2026, Asia/Saigon. Hiểu “hợp đồng web gia công” là công việc nhận thiết kế/lập trình web theo yêu cầu khách hàng. Người dùng muốn nghiên cứu, chưa yêu cầu ký hợp đồng, mua template hoặc triển khai.

Thứ tự: H1 nghiên cứu brief/scope/đầu ra/nghiệm thu/thay đổi/bàn giao trong dự án thuê ngoài → H2 tìm video/creator có bằng chứng về template và AI workflow, đối chiếu docs hiện hành → H3 tổng hợp cách tinh chỉnh và ví dụ áp dụng cho demo → H4 cập nhật hồ sơ và kiểm tra nguồn/liên kết. Phân biệt transcript/trang giới thiệu với việc trực tiếp xem video, và tinh chỉnh UI/prompt với fine-tune trọng số mô hình.

## H1 — hoàn thành khung yêu cầu cho gia công web

Ngày 11/10/2026. Tạo GIA-CONG-WEB-VA-AI-WORKFLOW.md phần 1–3: phân loại dự án, brief/SOW, scope, nội dung, quyền dữ liệu/AI/template, milestone, nghiệm thu, thay đổi, chi phí và bàn giao. Các bảng là khung đề xuất học tập, không hợp đồng pháp lý sẵn để ký.

Đối chiếu UK Model Services Contract Buyer Guidance v2.2A (132 trang, đọc chọn lọc implementation/testing/change/IP), Webflow template license và 21st Terms. Nguồn AIGA PDF và VBPL Việt Nam không tải được (403); không lấy nội dung chưa đọc để suy ra điều luật Việt Nam. Không báo giá thị trường hoặc cam kết chỉ tiêu mới cho ReNER.

## H2 — hoàn thành khảo sát creator/video và đối chiếu docs

Ngày 11/10/2026. Chọn 5 ví dụ: Brock Mesarich, Lukas Margerie, Flux Academy, Astro K Joseph, Lenny/Lazar. Đọc chọn lọc transcript ba video tại trang do Lovable đăng; Astro xác minh mô tả YouTube; Lenny chỉ đọc giới thiệu công khai, không phần trả phí. Không phát/xem toàn bộ video. Metadata ghim ID/ngày đăng của ba video cũ từ VideoObject của trang nguồn.

Phát hiện: Brock nói UI import có nút chưa có chức năng; Lukas dùng từ fine-tuning cho chỉnh sản phẩm bằng prompt; Flux nêu việc khách cập nhật nội dung. Đối chiếu docs Lovable hiện hành: plugin/MCP/.fig khác nhau, .fig không tự import thiết kế tương tác; preview toolbar thay trải nghiệm Visual edits trước. Không lấy video 2025 làm hướng dẫn thao tác hiện hành hoặc benchmark tốc độ.

## H3 — hoàn thành tổng hợp workflow và hướng học cho demo

Ngày 11/10/2026. Chuyên đề phần 4–8 có nguồn mẫu theo loại, giải thích prompt/context/UI iteration khác fine-tune model, thứ tự tinh chỉnh, ba prompt minh họa và lộ trình đọc/xem. Liên hệ brief/acceptance/bàn giao với ReNER nhưng không đổi baseline kiến trúc, không code và không mua template/công cụ.

## H4 — kiểm chứng và bàn giao chuyên đề gia công web/AI workflow

Ngày 11/10/2026, kiểm tra lúc 18:00 Asia/Saigon. Chuyên đề có 237 dòng/8 phần, một sơ đồ quy trình và ba prompt minh họa; cập nhật sổ kiến thức v0.7 mục 25, PLAN mục 14, INDEX và báo cáo tổng hợp mục 6.

- Kiểm tra 7 tài liệu và 92 liên kết local: không thiếu đích, fence cân bằng, không ký tự thay thế Unicode.
- 10 snapshot nguồn tải thành công khớp SHA256. Manifest giữ lỗi tải AIGA; các lỗi VBPL/YouTube và giới hạn transcript đã được ghi trong README/log. Các file text trích xuất chỉ hỗ trợ tra cứu, chưa xác minh bằng nghe/xem video.
- Kiến trúc v0.2 vẫn cùng SHA256 344551e3ae03790cd29ea80afea7a2e48d5ff1462aa22af570a4729fdd5b6d36. Không thực thi prompt mẫu, không thay code ứng dụng, không deploy/mua dịch vụ hoặc liên hệ creator.
- Kết quả kiểm tra lưu tại sources/outsourcing-ai-2026-10-11/verification.json. Chưa kiểm chứng render Mermaid; tài liệu phần hợp đồng là khung học tập, không đánh giá hiệu lực pháp lý cho hợp đồng cụ thể.


## I0 — kế hoạch nghiên cứu solo AI, 80/20 và quản lý thay đổi

Ngày 11/10/2026. Tiếp tục bằng admin nhánh tra cứu/giải thích, làm tuần tự. Thứ tự: I1 nguồn quốc tế/X/Trung Quốc → I2 UX/case study/sách và ưu tiên 80/20 → I3 backend gọn, luồng và chia việc cho một người → I4 thay đổi tính năng lõi/khôi phục → I5 tài liệu thực hành, nguồn và kiểm chứng. Không code ứng dụng hoặc sửa baseline thiết kế v0.2.

Người dùng xác nhận: vướng cả hiểu code, AI sửa hỏng chỗ khác và chia việc; nặng nhất là biến ý tưởng/prompt ngắn thành yêu cầu và task, ưu tiên hiểu luồng giữa các phần. Lo hard rule hạn chế sáng tạo; mục tiêu học đủ để nhận làm web cho khách. Cần tập trung vào phỏng vấn yêu cầu, ví dụ task cụ thể, quyền quyết định của người dùng và kiểm chứng; không bắt đọc mọi dòng code. Tái sử dụng file PROMPT-KIEN-TRUC-GIAO-VIEC-AI.md nhưng phải nêu giới hạn của quy tắc quá cứng trong bản trước.


## I1 — nguồn quốc tế, X và Trung Quốc

Ngày 11/10/2026. Đọc Qwen Code README/docs, TRAE SOLO blog 17/07/2025 và 31/03/2026, Ant Design values tiếng Trung, Anthropic agents/Claude Code và DORA. Đây là bằng chứng về hướng sản phẩm/cách làm, không bảng xếp hạng công nghệ hoặc thống kê toàn thế giới. Không dùng tuyên bố 10x của nhà cung cấp làm kết quả đo.

Đã thử X: post Boris Cherny 2007179842928947333 bị 403; Karpathy 1886192184808149383 và Qwen 1953835877555151134 cũng lỗi fetch. Search thấy profile và bình luận thứ cấp, không đủ chứng minh toàn bộ thread gốc. Bilibili BV1LCRiBwEgh có mô tả được index nhưng mở video lỗi 412; bài cv49747587 trả 0 dòng. Instagram/Reels không tìm được nội dung gốc đủ đọc qua công cụ trong lượt này. Ghi giới hạn, không giả nhận đã xem video/reel hoặc dùng mirror để gán lời chưa xác minh cho tác giả. Chuyển sang tài liệu chính thức đọc được và nguồn video NN/g/Flux có mô tả công khai.


## I2 — hoàn thành đối chiếu UX, case study và 80/20

Ngày 11/10/2026. Tạo TU-VIBE-CODING-DEN-GIAO-WEB.md: đối chiếu Vodafone A/B, Baymard checkout, Ant Design tiếng Trung, NN/g heuristics/motion; sách qua trang tác giả/chương công khai. Nêu rõ tỷ lệ case không áp dụng mặc định ReNER, 80/20 là heuristic chưa đo, và chưa khảo sát người dùng. Bổ sung METR cả nghiên cứu 2025 lẫn cập nhật 24/02/2026 về selection bias để không suy ra năng suất hiện tại từ số cũ.

Người dùng vừa xác nhận: lấy proposal/web ReNER hiện tại làm bài thực hành chính, học thật bài bản để chuyển tư duy sang nhiều dự án; không muốn chuyển sang bài landing page hoặc làm sơ sài qua môn. Đã đưa vào phạm vi tài liệu. Tiếp tục triển khai sổ tay biến ý tưởng thành task và kiểm tra hồi quy.


## I3 — hoàn thành phần backend gọn và chia việc cho một người

Ngày 11/10/2026. Báo cáo mới phần 5–6/8 giải thích modular monolith, luật so với I/O, worker/retry/idempotency/revision/quyền và cách tối ưu theo phép đo. Sổ tay SO-TAY-CHIA-VIEC-CHO-AI.md có brief mẫu, 10 ví dụ giả lập, luồng yêu cầu, S0–S5, task card, 7 prompt và quản lý Git/log. Các cây file/task/state đều minh họa, không giả thành code đã triển khai.

Ưu tiên đổi từ ép người dùng viết prompt dài sang AI phỏng vấn có chọn lọc và chuyển câu ngắn thành ví dụ nghiệm thu. Ranh giới cứng dành cho nghiệp vụ/quyền/dữ liệu; chi tiết dễ đảo cho AI tự chọn. Người dùng chỉ cần bắt đầu bằng hiểu flow nhưng nhận khách vẫn cần kiểm chứng và bàn giao/khôi phục. Chưa tạo branch/ticket/tag hoặc sửa app.

## I4 — hoàn thành cơ chế đổi tính năng lõi và quay lại

Ngày 11/10/2026. Báo cáo phần 7 phân biệt yêu cầu mới với bug; impact map UI/API/luật/DB/job/quyền/test; năm loại khôi phục; ví dụ giá thuê → tổng chi phí. Đối chiếu GitHub revert PR, Feature Toggles, Parallel Change. Nêu rõ Git/checkpoint không phục hồi DB hoặc side effect ngoài, flag không thay phân quyền, expand–migrate–contract có thời điểm không còn rollback đơn giản. Chưa thực hiện migration/rollback hoặc thay thiết kế v0.2. Tiếp theo: snapshot nguồn, liên kết hồ sơ và kiểm chứng I5.


## I5 — hoàn thành hồ sơ và kiểm chứng lượt nghiên cứu solo AI

Ngày 11/10/2026, Asia/Saigon. Bàn giao TU-VIBE-CODING-DEN-GIAO-WEB.md (301 dòng, 9 phần) và SO-TAY-CHIA-VIEC-CHO-AI.md (271 dòng, 8 phần); tổng ba sơ đồ Mermaid. Cập nhật sổ kiến thức v0.8 mục 26, PLAN 15, INDEX, báo cáo tổng hợp mục 7. Cập nhật chọn lọc khung prompt cũ lên v1.1; chưa audit lại toàn bộ khuôn cũ và không chỉnh skill đã cài.

Kiểm chứng: 9 tài liệu, 98 liên kết local đều có đích; code fence cân bằng, không ký tự thay thế Unicode. 17 snapshot nguồn khớp SHA256; 18 lần tải có một lỗi 406 (Steve Krug) nhưng nội dung trang đã đọc qua web/search. Manifest và verification.json lưu trong sources/solo-ai-2026-10-11. Chưa kiểm render Mermaid hoặc kiểm lại toàn bộ URL ngoài.

SHA256 thiết kế v0.2 vẫn 344551e3ae03790cd29ea80afea7a2e48d5ff1462aa22af570a4729fdd5b6d36. Không sửa code ứng dụng, tạo task/branch GitHub, chạy user test/benchmark, migration hoặc deploy. Không tuyên bố đã xem reel/video bị chặn.

Bối cảnh tiếp nối: theo proposal/ReNER làm bài thực hành thật bài bản; học hiểu luồng và biến ý tưởng thành task, giữ khoảng tự chủ cho AI ở chi tiết dễ đảo nhưng kiểm soát nghĩa dữ liệu/quyền/nghiệm thu. Bài gợi ý kế tiếp là lần theo một tin giá mơ hồ để luyện brief → ví dụ → flow → task, chỉ triển khai khi có yêu cầu tiếp theo. Những walkthrough KusShoes chưa xong vẫn chưa xong.


## J0 — kế hoạch phản biện hồ sơ toàn TMG301

Ngày 11/10/2026. Người dùng yêu cầu tự phản biện toàn bộ tài liệu nghiên cứu, tìm sai sót/khoảng trống và bổ sung tư duy. Dùng admin và hallucination-guard, không code app. Thứ tự: J1 kiểm kê và đối chiếu proposal/nghiên cứu → J2 kiến trúc, quyền, flow và AI workflow → J3 kiểm nguồn/số liệu/tính nhất quán → J4 sửa nội dung có căn cứ, lập gaps và kiểm tra lại.

Kiểm kê ban đầu 28 Markdown do dự án tổng hợp (bao gồm ghi chú môn học, báo cáo local và lịch sử), tổng 594.454 ký tự; không coi source clone/vendor/build là tài liệu do mình viết. Lưu hash trước sửa và kết quả quét claim tự động tại notes/audit-2026-10-11. Quét máy không đồng nghĩa đọc sâu từng dòng; báo cáo sẽ ghi mức kiểm tra và giới hạn cho từng file. Proposal gốc và source snapshot giữ nguyên; tài liệu lịch sử được ghi chú thay vì viết lại quá khứ.
