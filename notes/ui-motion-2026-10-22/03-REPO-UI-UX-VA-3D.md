# 10 repo UI/UX và 10 repo 3D/scroll — mỗi cái dạy gì

[Về chặng](README.md) · Đọc ngày 22/10/2026 bằng hai lượt nghiên cứu: clone repo công khai rồi đọc file được nêu. Số sao lấy từ trang GitHub hoặc trang thống kê bên thứ ba vào ngày đọc, **xấp xỉ, không kiểm chéo** (API GitHub bị chặn trong phiên). Commit đã đọc ở [manifest](sources/manifest.json).

## 1. Repo "skill thiết kế" cho AI agent

| Repo | ~Sao | Cho gì | Quy tắc cụ thể đáng giữ (file đã đọc) |
|---|---|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 138,6k | Cơ sở dữ liệu CSV về style, màu, font, motion, stack; CLI tra cứu | `templates/base/quick-reference.md`: thứ tự ưu tiên a11y → touch → hiệu năng → style; `color-not-only`; số dạng `tabular`; mỗi màn hình chỉ 1–2 phần tử chuyển động chính; animation lúc thoát nhanh hơn lúc vào (~60–70%); stagger 30–50 ms |
| [anthropics/skills](https://github.com/anthropics/skills) `frontend-design` | 182,8k | Quy trình thiết kế và danh sách tránh | Lấy ý tưởng hình ảnh từ chính chủ đề; tránh eyebrow chữ hoa, đánh số 01/02 khi không phải trình tự, "→" trên nút, nhãn mono; "dồn táo bạo vào một chỗ"; bỏ một phụ kiện trước khi giao |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 100,7k | Bộ "dấu hiệu AI slop", motion, scene, critique | `references/tells.md`: kem + serif + kẻ dòng là "làn sóng thứ ba" của slop; `motion.md`: ease-out `cubic-bezier(.16,1,.3,1)`, reveal 600–1000 ms, giảm chuyển động thì giữ opacity, bỏ di chuyển; `scenes.md`: sân khấu sticky cao (giữ + 1) màn hình, 2–3 scene mỗi trang; `critique.md`: 14 lượt review |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 84,6k | Sàn chất lượng và "overdrive" | `craft-floor.md`: đoạn văn 65–75 ký tự, tracking không chặt hơn −0,04em, style cả selection/caret/focus; `overdrive.md`: View Transitions, `animation-timeline` sau `@supports`, WebGL chỉ tạo gần viewport, nhắm 60 fps |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | 16,9k | Skill GSAP chính thức (KusShoes cũng cài) | `useGSAP` có `scope`; `gsap.matchMedia()` cho reduced motion; ghim parent, animate con; không trộn `scrub` với `toggleActions`; SplitText `mask:"lines"`, `aria:"auto"` |
| [emilkowalski/skill](https://github.com/emilkowalski/skill) | 48,5k | Chuẩn review animation | `review-animations/STANDARDS.md`: không animate thao tác làm 100 lần/ngày; UI dưới 300 ms; không bắt đầu từ `scale(0)`; `:active` scale 0.97; hover chỉ khi `(hover:hover) and (pointer:fine)` |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 30,6k | 58 cổng "slop test" | Không hero căn giữa toàn bộ; không `transition: all`; focus ring hiện ngay; mỗi keyframe có fallback giảm chuyển động; màu nhấn ≤ 3–5% diện tích; không `#000`/`#fff` thuần |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 122,8k | 84 file `DESIGN.md` của các thương hiệu | Dùng làm **khuôn định dạng** (token YAML + mục Elevation, Shapes, Do/Don't), không chép thương hiệu |
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | 49,9k | 215+ component hiệu ứng (MIT + Commons Clause) | `TiltedCard`: perspective 800, biên độ ×0,3 khi giảm chuyển động; `FoldText`: gập giấy bằng `rotateX`. Dùng tối đa một hiệu ứng, phải restyle |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 1,0k | Prompt audit giao diện | Dùng `…` không dùng `...`; `text-wrap: balance`; vòng lặp trang trí dừng khi giảm chuyển động; autoplay > 5 s cần nút dừng; state trên URL; `Intl.*` để định dạng |

Phát hiện quan trọng nhất (**Đã quan sát**): hai repo nhiều sao nhất (`frontend-design`, `taste-skill`) đều xếp **nền kem + serif hiển thị + kẻ dòng mảnh kiểu báo** vào nhóm dấu hiệu giao diện AI hàng loạt. Bản thiết kế đầu của ReNER rơi đúng vào đó. Xử lý ở [quyết định thiết kế](05-QUYET-DINH-VA-BAI-HOC.md#2-vòng-2--sửa-theo-10-repo-skill).

`shadcn/ui`, `magicui`, `aceternity-ui` là thư viện component, không kiểm có hướng dẫn thiết kế bằng chữ nên không đưa vào bảng.

## 2. Repo 3D, parallax và kể chuyện bằng cuộn

| Repo | ~Sao | Kỹ thuật (file đã đọc) | Dùng cho ReNER |
|---|---|---|---|
| [argyleink/gui-challenges](https://github.com/argyleink/gui-challenges) | 2,9–3k | `scifi-scroll`: chỉ CSS, `@supports (animation-timeline: scroll(root))` + `@media (prefers-reduced-motion: no-preference)`; `game-menu/mouse-parallax.js` ~10 dòng đặt `--x/--y`, CSS `clamp` góc nghiêng | Khuôn bọc chế độ cuộn; nghiêng theo chuột bằng biến CSS |
| [flackr/scroll-timeline](https://github.com/flackr/scroll-timeline) | ~955 | Polyfill ScrollTimeline/ViewTimeline; `timeline-scope`, khoảng `cover/contain/entry/exit` | Hiểu các khoảng `animation-range` |
| [bramus/sda-utilities](https://github.com/bramus/sda-utilities) | chưa xác minh | `trackProgress()` đọc tiến độ animation cuộn để đồng bộ JS | Bộ đếm số theo cuộn nếu cần |
| [nolimits4web/atropos](https://github.com/nolimits4web/atropos) | ~3,6k | `data-atropos-offset` là dịch 2D tỉ lệ với góc nghiêng, không phải `translateZ`; vệt lóa radial 200% | Vệt sáng lóa chạy theo chuột trên bài đăng |
| [micku7zu/vanilla-tilt.js](https://github.com/micku7zu/vanilla-tilt.js) | ~3,95k | Công thức nghiêng, throttle bằng `requestAnimationFrame`, glare theo `atan2` | Tham khảo công thức; không có kiểm tra reduced motion |
| [codrops/StickySections](https://github.com/codrops/StickySections) | chưa xác minh | `position: sticky` + `perspective`, GSAP scrub `rotationX: -90`, `scale: .9` khi section thoát | Sân khấu ngả ra sau khi hết câu chuyện |
| [codrops/OnScrollLayoutFormations](https://github.com/codrops/OnScrollLayoutFormations) | chưa xác minh | Rải phần tử theo z/góc tỉ lệ khoảng cách tới tâm, rồi scrub về lưới | 14 chấm bay từ không gian 3D về trục giá |
| [pmndrs/drei](https://github.com/pmndrs/drei) + [react-three-fiber](https://github.com/pmndrs/react-three-fiber) | ~9,7k / ~30,3k | `ScrollControls`: `range()`, `curve()`, `visible()`; `Float`: nhấp nhô bằng sin/cos | Ánh xạ sang `animation-range` và keyframe 0/50/100% |
| [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) | ~13,6k | Cuộn mượt mà vẫn giữ `sticky`; `damp()`; mặc định tôn trọng reduced motion | Làm mượt góc nghiêng nếu cần |
| [chokcoco/CSS-Inspiration](https://github.com/chokcoco/CSS-Inspiration) | ~10,9k | Chiều sâu chỉ bằng CSS: `perspective` + `preserve-3d` + `translateZ` | Tách lớp bài đăng không cần JS |

`theatre-js/theatre`: commit công khai cuối 04/2024, README nói chuyển sang repo riêng, nên không dùng.

## 3. Những lỗi 3D dễ mắc (Đã quan sát qua tài liệu, một phần đã thực nghiệm khi dựng)

- `opacity < 1`, `filter`, `overflow: hidden`, `clip-path` trên phần tử `preserve-3d` làm **dẹt** cảnh 3D. Đặt hiệu ứng lên phần tử con.
- Tổ tiên có `overflow: hidden` (kể cả `overflow-x: hidden`) làm hỏng `position: sticky`. Dùng `overflow: clip`.
- Trục thời gian lấy từ **khung cao không ghim**, không lấy từ sân khấu sticky.
- Biến đổi theo cuộn và theo chuột phải ở **hai wrapper khác nhau**.
- Shorthand `animation` đặt lại `animation-timeline`. Khai báo `animation-timeline` **sau** shorthand.
- Hỗ trợ trình duyệt (theo hiểu biết, chưa kiểm bảng hỗ trợ): Chrome/Edge 115+, Safari 26; Firefox cần bật cờ. Luôn có bố cục tĩnh dự phòng.
