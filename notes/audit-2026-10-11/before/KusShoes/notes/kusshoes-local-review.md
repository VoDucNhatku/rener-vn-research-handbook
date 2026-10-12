# KusShoes — khảo sát repo và bản chạy local

Ngày: 2026-10-09 (Asia/Saigon). Nguồn: https://github.com/EXE-CAPSTONE-TEAM/KusShoes, nhánh main, commit `fc3e017`. Đây là khảo sát kiến trúc và khả năng chạy demo, chưa phải kiểm toán bảo mật toàn bộ.

## Kết quả

- Website: http://localhost:5173
- Portal khách hàng: http://localhost:5173/login — `user1@example.com` / `LOCAL_DEMO_PASSWORD_REMOVED`.
- Quản trị: http://localhost:5173/admin — `admin2@kusshoes.vn` / `LOCAL_DEMO_PASSWORD_REMOVED`.
- Tài liệu API tự sinh: http://localhost:8000/docs.
- Các tài khoản trên là dữ liệu demo do script có sẵn của repo tạo trong PostgreSQL local. Tài khoản khách hàng yêu cầu xác nhận điều khoản và độ tuổi; người xem tự quyết định ở giao diện.
- Dữ liệu demo được tạo bằng `BE/scripts/seed_demo_data.py`: 14 khách hàng, 54 dự án, 21 bản ghi xuất file, 40 hóa đơn và 44 bản ghi audit, ngoài tài khoản admin/staff. Các con số này mô tả dữ liệu giả lập, không phải số liệu kinh doanh thực tế.

## Repo thực sự gồm những gì?

| Phần | Công nghệ và nhiệm vụ | Nguồn trong repo |
|---|---|---|
| FE | React 19, TypeScript, Vite 8; landing page, sản phẩm, bảng giá, tài khoản, dashboard, dự án, billing, settings và admin | `FE/package.json`, `FE/src/App.tsx` |
| Backend | Python >=3.12, FastAPI, SQLAlchemy async, Alembic; xác thực, phân quyền, dự án, asset, gói dịch vụ, hóa đơn và API cho editor/mobile | `BE/pyproject.toml`, `BE/app/main.py` |
| PostgreSQL | Lưu người dùng, dự án, asset, thiết kế, subscription, invoice, export và audit | `BE/app/models/`, `BE/migrations/` |
| Redis/Celery | Session/OTP/rate limiting và công việc nền như email, bảo trì | `BE/app/infrastructure/`, `BE/app/workers/` |
| S3 | Kho file và URL ký để tải lên/tải xuống; MinIO local hoặc R2 production | `BE/app/infrastructure/storage.py` |
| Tích hợp | Google OAuth, SMTP, PayOS/MoMo, GA4, Sentry, KIRI | `BE/app/config.py`, các module infrastructure |

Luồng backend chính: router nhận HTTP → schema kiểm tra input → service xử lý nghiệp vụ → repository truy cập model/database; infrastructure kết nối dịch vụ phụ trợ. Điểm vào là `BE/app/main.py`. Frontend định tuyến dựa trên URL trong `FE/src/App.tsx`, tải nhiều trang bằng lazy import và gọi API qua `FE/src/api/client.ts`.

**README chưa khớp code:** README mô tả backend Node/Express và hướng dẫn `npm install` ở BE, nhưng backend hiện tại là FastAPI và khai báo dependency bằng `pyproject.toml`/`uv.lock`. Muốn chạy BE phải dùng Python hoặc cấu hình Docker Compose có sẵn.

**Giới hạn repo:** KusStudio desktop, ứng dụng mobile và KIRI relay thuộc dự án `ar-ai-exe`, được chỉ rõ trong `docs/api-contract.md`. API ở repo này có hợp đồng giao tiếp và mở app qua `kusshoes-editor://`, nhưng clone KusShoes không tự cài editor. Vì vậy website/portal chạy được không đồng nghĩa quy trình quét → dựng 3D → thiết kế → bake đã chạy trọn vẹn.

## Môi trường local đã dựng

Máy chưa có Docker. Bản demo dùng frontend Node 24, backend Python 3.12.15, PostgreSQL portable 17.6 ở cổng 55432, Redis Windows 5.0.14.1 ở cổng 56379, API ở 8000, frontend ở 5173 và S3 giả lập Moto ở 9000. Celery chạy pool `solo` để phù hợp Windows. Chưa chạy Celery beat, nên lịch bảo trì định kỳ không hoạt động.

- `BE/.env` chỉ kết nối dịch vụ local, không dùng database production. SMTP trỏ localhost và OAuth/payment chưa có khóa thật.
- `FE/.env.local` dùng base URL rỗng để gọi API cùng origin; `.local/vite-demo.config.ts` kế thừa cấu hình FE và proxy `/api`, `/health` sang backend 127.0.0.1:8000. Đây là cấu hình riêng cho demo sau khi quan sát kết nối cross-origin trên trình duyệt không ổn định; không sửa `FE/vite.config.ts`. ID analytics/Sentry để trống.
- MinIO không tải được: endpoint tải bản Windows trả HTTP 410. Moto là bộ giả lập S3 cho demo, chưa xác minh tương đương MinIO ở mọi API. Moto giữ file trong bộ nhớ và mất file khi dừng server. PostgreSQL giữ dữ liệu trong `.local/pgdata`.
- Redis client của backend được cài phiên bản 5.3.1 trong venv local để dùng RESP2 với Redis Windows 5; phiên bản khóa trong repo là 8.1.0 và thử thực tế báo `unknown command HELLO`. Không thay đổi `pyproject.toml` hay `uv.lock`; chạy `uv sync` lại sẽ cần áp dụng cấu hình demo này lại hoặc đổi Redis server.
- PostgreSQL cần đường dẫn ASCII trên Windows: junction `C:\Users\Asus\kusshoes-local-runtime` trỏ tới `.local` của repo. Không di chuyển thư mục repo khi các dịch vụ đang chạy.
- Alembic đã áp dụng migration tới head. Đọc `alembic.ini` bằng UTF-8 qua Config API để tránh lỗi giải mã cp1252 trên Windows.
- Không sửa mã ứng dụng và không push lên GitHub. `.local`, `notes` được exclude ở Git local; `.env` và build/dependency đã được gitignore.

## Đã kiểm tra

- `npm ci`: thành công; `npm run build`: TypeScript + Vite build thành công.
- `npm run test:run`: 35 file test pass, 1 file skip; 205 test pass, 13 skip, **exit 1** do 2 unhandled rejection liên quan GSAP khi teardown jsdom; canvas cũng có cảnh báo thiếu implementation. Không khẳng định toàn bộ frontend test xanh.
- `pytest unit_tests -q`: **42 pass**, có 1 cảnh báo Authlib deprecated. Log: `.local/logs/backend-unit-tests.log`. Chưa chạy toàn bộ integration test backend.
- `.local/check-local.py`: readiness DB/Redis/storage đều `ok`; 3 gói dịch vụ; login customer/admin và các API user/project/subscription/admin stats trả HTTP 200; upload/download S3 bằng presigned URL khớp dữ liệu. Kết quả: `.local/logs/smoke-results.json`.
- Giao diện trình duyệt: landing tiếng Việt hiển thị; login khách hàng thành công và dashboard lấy được 7 dự án của user1 phía sau màn xác nhận điều khoản. Trang quản trị đã đăng nhập qua proxy local; xem ảnh trong `.local/logs/admin-preview.jpg`.
- Harness `harness/verify.sh` không chạy được trên máy này vì yêu cầu engine tuyệt đối `/home/tak/openclaw/harness/verify.sh` không có. Không xem harness là đã pass.

## Điều chưa hoạt động / chưa xác minh

- Quét thật, reconstruction KIRI, chỉnh sửa/bake trên KusStudio: cần repo/app đi kèm và khóa dịch vụ.
- OAuth Google, email OTP, thanh toán thật và dữ liệu GA4: cần cấu hình của nhóm; chưa test.
- Seed tạo bản ghi asset/export nhưng không mang theo file giày GLB hoặc file xuất thật. Tải file/model demo có thể 404. Việc S3 smoke pass chỉ chứng minh upload/download một file kiểm tra.
- Chưa kiểm toán toàn bộ phân quyền/bảo mật, chưa test tải cao hay triển khai production.

## Chạy lại / dừng

Từ thư mục KusShoes trong PowerShell:

```powershell
& .\.local\start.ps1
& .\BE\.venv\Scripts\python.exe .\.local\check-local.py
# Khi không xem nữa:
& .\.local\stop.ps1
```

Start script dùng dependency đã cài, giữ database, khởi tạo bucket khi Moto khởi động mới và chỉ start các cổng chưa có listener. Không tự seed lại. Log nằm trong `.local/logs`, log Vite của lần khởi động đầu ở `vite.local.log`.

Đã thử dừng và bật lại bằng hai script trên, sau đó chạy lại kiểm tra API/S3 qua proxy cổng 5173. Database demo được giữ nguyên; các dịch vụ đã được bật lại để người dùng xem.

Thứ tự đọc code gợi ý: `FE/src/App.tsx` → `FE/src/api/client.ts` → trang cụ thể; backend: `BE/app/main.py` → router tương ứng → service → repository → model; xem hợp đồng tích hợp tại `docs/api-contract.md` và tài liệu phát sinh ở `/docs`.
