# Snapshot khảo sát kiến trúc 10 repo — 10/10/2026

Đọc bổ sung theo commit đã ghim ở [metadata catalog](../web-top10-2026-10-10/github-metadata.json). [Manifest](source-manifest.json) ghi repo, commit, path, URL raw, thời điểm UTC và SHA256 của file tải thành công. Giữ lỗi lịch sử để tra lại, không tính lỗi là nguồn đã đọc.

Phạm vi: Medusa route + workflow tạo sản phẩm; Saleor mutation; Commerce search page; React-admin và Refine product list; Tabler token SCSS chọn lọc; FastAPI template item CRUD; Cal.diy booking access service và setup/case quyền trong test; Outline document policy; Immich asset controller và các phương thức quyền/statistics trong service. Tái sử dụng manifest, README, architecture và CONTRIBUTING đã đọc ở hai snapshot trước.

Hai đường dẫn suy đoán trả 404 đã được giải quyết: Cal.diy BookingsList không có ở vị trí thử, thay bằng service và test được tìm qua GitHub contents API; Medusa core-flows thực tế nằm trong packages/core/core-flows. File README bookings của Cal.diy chỉ có một câu, không dùng làm bằng chứng kiến trúc chi tiết.

Phát hiện đáng chú ý: Cal.diy BookingAccessService khai báo permission checker cục bộ trả true; test mock thay checker. Chỉ kết luận về file/commit này, chưa kết luận khả năng khai thác runtime toàn sản phẩm. Saleor ProductCreate dùng DeprecatedModelMutation; không coi đây là mẫu API mới để copy nguyên.

Nguồn docs chính thức kiểm tra bổ sung: [Medusa architecture](https://docs.medusajs.com/learn/introduction/architecture), [Immich architecture](https://docs.immich.app/developer/architecture/), [React-admin data provider](https://marmelab.com/react-admin/DataProviders.html). Docs online có thể cập nhật khác commit; phát biểu code cụ thể dựa snapshot.

Chưa chạy 10 app/test suite/benchmark. Đây là khảo sát chọn lọc để thiết kế ReNER. Kết quả tổng hợp ở mục 23 của sổ kiến thức; thiết kế đề xuất ở notes/design-rener-vn-waterfall.md mục 16.
