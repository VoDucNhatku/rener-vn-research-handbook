# Thư viện ReNER đã dùng cho giao diện thử

[Về chặng](README.md) · Nguồn: `apps/web/package.json` trên nhánh [`feat/web-ui-prototype`](https://github.com/VoDucNhatku/rener-vn/tree/feat/web-ui-prototype) của repo sản phẩm, commit `56988b7`. Phiên bản dưới đây là bản đã cài thật trong `node_modules` ngày 22/10/2026 (**Đã quan sát**).

## 1. Thư viện chạy trong app

| Thư viện | Phiên bản | Dùng làm gì | Vì sao chọn |
|---|---|---|---|
| `next` | 15.5.28 | App Router, trang server đọc dữ liệu, route `/`, `/tim-tro`, `/tin/[id]` | Đúng stack trong [ADR-0001](https://github.com/VoDucNhatku/rener-vn/blob/main/docs/decisions/ADR-0001-stack-demo.md) của repo sản phẩm |
| `react`, `react-dom` | 19.1.1 | UI | Đi cùng Next 15 |
| `gsap` (+ `ScrollTrigger`) | 3.13.0 | Hero ghim theo cuộn, nghiêng theo chuột (`quickTo`), hiện dần theo cuộn (`ScrollTrigger.batch`) | Học trực tiếp từ KusShoes; có `matchMedia` để tắt khi giảm chuyển động. Import động để không chặn lần paint đầu |
| `motion` (tên mới của framer-motion) | 12.23.12 | Lưới thẻ tin trượt về chỗ mới khi lọc (`layout`, `AnimatePresence`), tab panel extension (`layoutId`) | Hợp cho vào/ra component; `MotionConfig reducedMotion="user"` |
| `lucide-react` | 0.540.0 | Icon nét | Như KusShoes, một bộ icon duy nhất |
| `@fontsource/be-vietnam-pro` | 5.2.6 | Chữ thân, hỗ trợ đầy đủ tiếng Việt | Tự host, không phụ thuộc Google Fonts lúc build |
| `@fontsource-variable/newsreader` | 5.2.8 | Chữ tiêu đề serif, có subset tiếng Việt | Hợp chủ đề "bài đăng, tờ báo" |
| `@fontsource-variable/jetbrains-mono` | 5.2.6 | Chỉ cho bảng BIO / mã luật trong Lab | Không dùng mono để trang trí |
| `server-only` | 0.0.1 | Chặn module đọc file dữ liệu local bị import vào client | Dữ liệu thật không được lọt xuống trình duyệt qua bundle |

Dev: `typescript` 5.9.2, `@types/*`. Chưa có test runner, linter hay Storybook (**Chưa biết** khi nào thêm; đề xuất Vitest + Testing Library cho `EvidenceHighlighter` và `maskPhones`).

## 2. Công cụ ngoài app

| Công cụ | Dùng làm gì | Giới hạn |
|---|---|---|
| Playwright + Chromium có sẵn trong máy ảo | Chụp màn hình từng nhịp hero, mobile 390 px, trang tìm trọ/chi tiết để tự review | Chỉ Chromium; ảnh chụp toàn trang không kích hoạt reveal theo cuộn, phải cuộn dần rồi chụp |
| Claude Design (artifact canvas) | Bản xem trước landing để chủ dự án sửa trực tiếp, không cần chạy code | Định dạng `.dc.html`: không tải script ngoài, chỉ Google Fonts; hiệu ứng làm bằng **CSS scroll-driven animation** thuần |
| Node `--experimental-strip-types` | Chạy thử `maskPhones` với các dạng số giả E5 | Kiểm tay, chưa thành test tự động |

## 3. Đã cân nhắc nhưng không dùng

| Lựa chọn | Lý do chưa dùng |
|---|---|
| Three.js / react-three-fiber | ReNER không có vật thể 3D thật; CSS 3D (`perspective`, `preserve-3d`, `translateZ`) đủ cho "tách lớp bài đăng" và nhẹ hơn nhiều |
| Tailwind / shadcn | Repo dự kiến `styles/tokens.css` + CSS Modules giống KusShoes; tránh giao diện mặc định dễ nhận ra |
| Lenis (cuộn mượt) | Cuộn gốc đủ; taste-skill khuyên không chiếm quyền cuộn |
| GSAP SplitText | Tách chữ tiếng Việt theo ký tự dễ vỡ dấu; nếu dùng thì tách theo từ hoặc dòng |
| React Bits, Aceternity | Hiệu ứng có sẵn quá phô; chỉ đọc để học công thức (TiltedCard, FoldText) |

## 4. Hai cách làm chuyển động cùng một câu chuyện

| | Code Next.js (`ReadingHero.tsx`) | Bản Claude Design (`Main.dc.html`) |
|---|---|---|
| Kỹ thuật | GSAP timeline + ScrollTrigger `pin`, `scrub` | CSS `view-timeline` trên khung cao 4800 px + sân khấu `sticky`, `animation-range: contain …` |
| Số nhịp | 4: bài gốc → gán nhãn → chuẩn hóa → so sánh | 6: thêm "che thông tin" và "kết luận" có 5 bài mẫu bấm thử |
| Nghiêng chuột | `gsap.quickTo` | Handler đặt biến CSS `--tx/--ty`, chỉ khi `(hover:hover) and (pointer:fine)` |
| Trình duyệt | Mọi trình duyệt có JS | Chrome/Edge/Safari 26; nơi khác có bố cục tĩnh |
| Tắt chuyển động | `gsap.matchMedia('(prefers-reduced-motion: no-preference)')` | Toàn bộ chế độ cuộn nằm trong `@media (prefers-reduced-motion: no-preference)` |

Kế hoạch (**Đề xuất**): khi chủ dự án chốt bản Claude Design, chuyển 6 nhịp vào code bằng GSAP, thêm `Flip` cho cảnh "nhãn bay vào phiếu giá".
