# Học từ KusShoes — giao diện và chuyển động

[Về chặng](README.md) · Nguồn: [EXE-CAPSTONE-TEAM/KusShoes](https://github.com/EXE-CAPSTONE-TEAM/KusShoes), nhánh `main`, commit `89eac6a` (15/10/2026), đọc ngày 22/10/2026. Đọc code frontend và tài liệu; không chạy lại app trong chặng này (lần chạy local trước: [báo cáo K2](../../KusShoes/notes/kusshoes-local-review.md)).

## 1. Stack frontend (Đã quan sát)

`FE/package.json`: React 19, Vite 8, TypeScript 6, CSS Modules; `gsap` 3.15 cho ScrollTrigger và tilt; `framer-motion` 12 cho chuyển cảnh trong app; `@react-three/fiber`, `drei`, `three` cho phần 3D; Radix UI cho dialog/menu/tooltip; `lucide-react` cho icon; `recharts` cho biểu đồ admin; `i18next` cho tiếng Việt/Anh; `vitest` + Testing Library để test.

Bài học: một sản phẩm "đẹp" dùng **nhiều thư viện, mỗi cái một việc hẹp**. GSAP lo cảnh gắn với cuộn, framer-motion lo vào/ra của component, CSS lo hover và focus. Không có thư viện nào lo tất cả.

## 2. Design system viết thành luật (Đã quan sát)

`docs/DESIGN.md` v1.1 là "nguồn sự thật" về giao diện: khi Figma/Stitch hoặc code lệch thì file này thắng. Điểm đáng học:

- **Danh sách cấm cụ thể**: không shadow trên phần tử trong luồng trang, không hover nhấc card, không gradient/glow/glassmorphism, không icon trong ô màu, không tô màu một chữ trong tiêu đề, không font mono để trang trí, không timestamp ISO thô, không enum thô.
- **Token có số đo**: màu (kèm tỉ lệ tương phản từng màu chữ), cỡ chữ 11–24 px cho app và 16–48 px cho landing, lưới 4 px, bo góc 3–8 px, thời lượng 120/150 ms.
- **Một màu nhấn duy nhất**, tối đa một nút primary mỗi màn hình.
- **Component có kích thước bắt buộc**: nút 32 px, input 32 px, tab 40 px…
- **Ghi rõ quyết định còn mở**, ví dụ chữ trắng trên cam chỉ đạt 2,8:1.

Áp dụng cho ReNER (**Đề xuất**): viết `DESIGN.md` của ReNER theo đúng khuôn này. Riêng danh sách cấm thì không chép nguyên: KusShoes là tool phẳng, ReNER có chủ đề bút dạ quang nên được dùng nền màu cho nhãn, nhưng nhãn luôn phải kèm chữ.

## 3. Hero ghim theo cuộn — cách ShoeHeroExperience hoạt động (Đã quan sát)

File: `FE/src/components/ShoeHeroExperience/ShoeHeroExperience.tsx`.

| Kỹ thuật | Cách làm trong code | Lý do |
|---|---|---|
| Sân khấu ghim | Một `gsap.timeline` với ScrollTrigger `pin: true`, `scrub: 1`, `end: '+=1800'` | Cuộn điều khiển tiến độ, không tự chạy |
| Nhịp (beat) | 4 nhịp có `addLabel`: giày đổi `x`, `scale`, `rotationZ`; thẻ chữ từng bước mờ vào/ra | Một vật thể kể nhiều ý |
| Đổi góc nhìn | Hai ảnh `.webp` chồng nhau, crossfade ở nhịp 3 | Cảm giác 3D mà không cần model WebGL |
| Nghiêng theo chuột | `gsap.quickTo` cho `rotationY`/`rotationX` của wrapper, giới hạn khoảng ±10–12° | Mượt, không tạo tween mới mỗi lần di chuột |
| Bóng sàn | Phần tử riêng, đổi `scaleX`, `x`, `opacity` theo nhịp | Neo vật thể vào mặt đất |
| Chữ "gõ ra" | Component `TypingText`, bật khi nhịp tương ứng đang hiện (`stepFor(time)`) | Nhấn vào từng bước |
| Đổi colorway | Nút swatch ở nhịp cuối đổi ảnh `selectedImg` | Kết thúc bằng một tương tác |
| Code-split | GSAP + ScrollTrigger (~110 KB) import động sau lần paint đầu; boot overlay che trang tới khi timeline đặt khung đầu | Ảnh LCP không chờ GSAP |
| Pin spacer tự quản | Truyền `pinSpacer: pinSpacerRef.current` | Tránh ScrollTrigger bọc lại section làm trình duyệt báo lại LCP |
| Responsive | Toạ độ nhịp khác nhau khi `innerWidth <= 900` và khi có edge art (`> 1100`) | Một timeline, nhiều bố cục |

Landing còn tách tính năng framer-motion (`domAnimation`) ra một chunk riêng, tải sau lần render đầu (`FE/src/pages/Landing/motionFeatures.ts`).

Hai chỗ cần thận trọng khi học (**Đã quan sát**):

- Hero có kiểm tra `prefers-reduced-motion` ở CSS, nhưng trong đoạn timeline đã đọc không thấy `gsap.matchMedia()` cho reduced motion. Không kết luận được là đã tắt đúng.
- Comment "60fps" trong code là ý định, không phải kết quả benchmark.

## 4. Cách tổ chức đặc tả cho AI agent (Đã quan sát)

`.spec/` có `brd.md`, `prd.md`, `spec.md`, `design.md`, `plan.md`, `tasks.md`, `verification.md`, `constitution.md`. Một số file vẫn là template trống (`brd.md`, `prd.md`, `design.md`). `spec.md` và `tasks.md` có nội dung thật: yêu cầu kèm mã (FD-1..FD-8), ticket chia theo "lane" FE / BE+FE / DECISION.

`AGENTS.md` do công cụ OpenClaw sinh ra, giao việc cho Antigravity (`agy`): làm theo ticket, TDD, chạy `./harness/verify.sh`, đọc phần SUMMARY chứ không chỉ exit code, dừng sau hai lần lỗi liên tiếp và chuyển cho Claude Code.

Bài học (**Đề xuất**):

- Tách "đặc tả sản phẩm" (repo sản phẩm) khỏi "cách AI làm việc" (harness, skill). ReNER đã chọn cách này: repo `rener-vn` chỉ có đặc tả và code, handbook giữ phương pháp.
- Ticket theo lane giúp biết việc nào bị chặn bởi quyết định sản phẩm.
- Template trống trong repo không phải tài liệu; đừng tính nó là "đã có PRD".

## 5. Những gì ReNER mượn và không mượn

| Mượn ý tưởng | Không mượn |
|---|---|
| Sân khấu ghim nhiều nhịp, một vật thể chính đi qua các nhịp | Giao diện phẳng xám + cam của KusShoes |
| Nghiêng theo chuột trên wrapper riêng, không đụng timeline | Model 3D WebGL (ReNER không có vật thể 3D thật) |
| Bóng sàn, chữ hiện theo nhịp, tương tác ở nhịp cuối | Boot overlay che trang (ReNER dùng cách che sân khấu ngắn hơn, có hạn 2,5 giây) |
| Code-split GSAP khỏi đường render đầu | Sidebar admin dày đặc cho người tìm trọ |
| `DESIGN.md` có danh sách cấm và token có số | Danh sách cấm áp dụng nguyên văn |

Chủ dự án yêu cầu "làm theo style khác, chỉ tham khảo ý tưởng KusShoes" (**Người dùng xác nhận**, 22/10/2026).
