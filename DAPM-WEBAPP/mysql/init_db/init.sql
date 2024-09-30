CREATE DATABASE hethongvanbanUTE;
USE hethongvanbanUTE;

CREATE TABLE QuyenTruyCap (
    idQuyenTruyCap INT AUTO_INCREMENT PRIMARY KEY,
    TenQuyen VARCHAR(100),
    MaTruyCap VARCHAR(50)
);

CREATE TABLE ChucVu (
    idChucVu INT AUTO_INCREMENT PRIMARY KEY,
    TenChucVu VARCHAR(100)
);

CREATE TABLE ChiTietChucVu (
    idChiTietCV INT AUTO_INCREMENT PRIMARY KEY,
    idChucVu INT,
    idQuyenTruyCap INT,
    FOREIGN KEY (idChucVu) REFERENCES ChucVu(idChucVu),
    FOREIGN KEY (idQuyenTruyCap) REFERENCES QuyenTruyCap(idQuyenTruyCap)
);

CREATE TABLE Khoa (
    idKhoa INT AUTO_INCREMENT PRIMARY KEY,
    TenKhoa VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE PhongBan (
    idPhongBan INT AUTO_INCREMENT PRIMARY KEY,
    TenPhongBan VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE CanBo (
    idCanBo INT AUTO_INCREMENT PRIMARY KEY,
    idQuyenTruyCap INT,
    idPhongBan INT,
    TenTaiKhoan VARCHAR(50),
    MatKhau VARCHAR(50),
    HoTen VARCHAR(100),
    SDT VARCHAR(20),
    Email VARCHAR(100),
    CCCD VARCHAR(20),
    GioiTinh VARCHAR(10),
    DonVi VARCHAR(100),
    DiaChi TEXT,
    GioiThieu TEXT,
    idChucVu INT,
    idKhoa INT,
    FOREIGN KEY (idQuyenTruyCap) REFERENCES QuyenTruyCap(idQuyenTruyCap),
    FOREIGN KEY (idPhongBan) REFERENCES PhongBan(idPhongBan),
    FOREIGN KEY (idChucVu) REFERENCES ChucVu(idChucVu),
    FOREIGN KEY (idKhoa) REFERENCES Khoa(idKhoa)
);

CREATE TABLE HinhThuc (
    idHinhThuc INT AUTO_INCREMENT PRIMARY KEY,
    TenHinhThuc VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE DoKhanCap (
    idDoKhanCap INT AUTO_INCREMENT PRIMARY KEY,
    TenDoKhanCap VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE LinhVuc (
    idLinhVuc INT AUTO_INCREMENT PRIMARY KEY,
    TenLinhVuc VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE LoaiVanBan (
    idLoaiVanBan INT AUTO_INCREMENT PRIMARY KEY,
    TenLoaiVanBan VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE TinhChatVB (
    idTinhChatVB INT AUTO_INCREMENT PRIMARY KEY,
    TenTinhChatVB VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE TrangThaiVanBan (
    idTrangThai INT AUTO_INCREMENT PRIMARY KEY,
    TenTrangThai VARCHAR(100),
    MoTa TEXT
);

CREATE TABLE VanBanDen (
    idVanBanDen INT AUTO_INCREMENT PRIMARY KEY,
    idHinhThuc INT,
    DonViBanHanh VARCHAR(100),
    SoDen INT,
    idLinhVuc INT,
    TinhChatVB INT,
    idDoKhanCap INT,
    LoaiVanBan INT,
    NguoiKy NVARCHAR(100),
    PhuongThucNhan VARCHAR(100),
    NgayDen DATE,
    NgayPhatHanh DATE,
    SoKyHieu VARCHAR(50),
    idCanBo INT,
    idChucVu INT,
    idKhoa INT,
    CanTraLoiVB VARCHAR(10),
    CanXuLyVB VARCHAR(10),
    HanTraLoi DATE,
    SoNgay INT,
    LinkFileVanBan INT,
    TrichYeu VARCHAR(100),
    idNguoiKyVanBan INT,
    TrangThaiXuLy INT,
    FOREIGN KEY (idHinhThuc) REFERENCES HinhThuc(idHinhThuc),
    FOREIGN KEY (idLinhVuc) REFERENCES LinhVuc(idLinhVuc),
    FOREIGN KEY (TinhChatVB) REFERENCES TinhChatVB(idTinhChatVB),
    FOREIGN KEY (idDoKhanCap) REFERENCES DoKhanCap(idDoKhanCap),
    FOREIGN KEY (LoaiVanBan) REFERENCES LoaiVanBan(idLoaiVanBan),
    FOREIGN KEY (idCanBo) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idChucVu) REFERENCES ChucVu(idChucVu),
    FOREIGN KEY (idKhoa) REFERENCES Khoa(idKhoa),
    FOREIGN KEY (idNguoiKyVanBan) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (TrangThaiXuLy) REFERENCES TrangThaiVanBan(idTrangThai)
);

CREATE TABLE VanBanDi (
    idVanBanDi INT AUTO_INCREMENT PRIMARY KEY,
    idNguoiPheDuyet INT,
    idHinhThuc INT,
    idLinhVuc INT,
    idDoKhanCap INT,
    idLoaiVanBan INT,
    idCanBo INT,
    HanXuLy DATE,
    TrichYeu TEXT,
    SoDen INT,
    NgayPhatHanh DATE,
    SoKyHieu VARCHAR(50),
    LinkFileVanBan VARCHAR(100),
    VBCanPhanXL INT,
    TrangThaiXuLy INT,
    FOREIGN KEY (idNguoiPheDuyet) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idHinhThuc) REFERENCES HinhThuc(idHinhThuc),
    FOREIGN KEY (idLinhVuc) REFERENCES LinhVuc(idLinhVuc),
    FOREIGN KEY (idDoKhanCap) REFERENCES DoKhanCap(idDoKhanCap),
    FOREIGN KEY (idLoaiVanBan) REFERENCES LoaiVanBan(idLoaiVanBan),
    FOREIGN KEY (idCanBo) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (TrangThaiXuLy) REFERENCES TrangThaiVanBan(idTrangThai)
);

CREATE TABLE ThongTinXuLy (
    idTTXuLy INT AUTO_INCREMENT PRIMARY KEY,
    idCanBo INT,
    ChuDaoLanhDao TEXT,
    XuLySoBo TEXT,
    idCanBoVP INT,
    idPhongBan INT,
    HanXuLy DATE,
    BangSo INT,
    DonViPhoiHopXL TEXT,
    NguoiPhoiHopXL VARCHAR(100),
    idVanBanDen INT,
    idKhoa INT,
    FOREIGN KEY (idCanBo) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idCanBoVP) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idPhongBan) REFERENCES PhongBan(idPhongBan),
    FOREIGN KEY (idVanBanDen) REFERENCES VanBanDen(idVanBanDen),
    FOREIGN KEY (idKhoa) REFERENCES Khoa(idKhoa)
);

CREATE TABLE ButPheLanhDao (
    idButPheLanhDao INT AUTO_INCREMENT PRIMARY KEY,
    idVanBanDen INT,
    NguoiChuyen VARCHAR(100),
    ChuyenDen VARCHAR(100),
    ThoiGianChuyen DATETIME,
    YKienChuyen TEXT,
    FOREIGN KEY (idVanBanDen) REFERENCES VanBanDen(idVanBanDen)
);

CREATE TABLE VanBanKhoa (
    idVanBanDen INT,
    idKhoa INT,
    idCanBo INT,
    PRIMARY KEY (idVanBanDen, idKhoa, idCanBo),
    FOREIGN KEY (idVanBanDen) REFERENCES VanBanDen(idVanBanDen),
    FOREIGN KEY (idKhoa) REFERENCES Khoa(idKhoa),
    FOREIGN KEY (idCanBo) REFERENCES CanBo(idCanBo)
);



-- QuyenTruyCap table
INSERT INTO QuyenTruyCap (TenQuyen, MaTruyCap) VALUES 
(N'Quản trị viên', 'ADMIN'),
(N'Người dùng', 'USER'),
(N'Quản lý', 'MGR'),
(N'Người xem', 'VIEWER'),
(N'Biên tập viên', 'EDITOR');

-- ChucVu table
INSERT INTO ChucVu (TenChucVu) VALUES 
(N'Giám đốc'),
(N'Trưởng phòng'),
(N'Nhân viên'),
(N'Thư ký'),
(N'Thực tập sinh');

-- ChiTietChucVu table
INSERT INTO ChiTietChucVu (idChucVu, idQuyenTruyCap) VALUES 
(1, 1),
(2, 3),
(3, 2),
(4, 4),
(5, 5);

-- Khoa table
INSERT INTO Khoa (TenKhoa, MoTa) VALUES 
(N'Công nghệ thông tin', N'Khoa Công nghệ thông tin'),
(N'Toán học', N'Khoa Toán học'),
(N'Vật lý', N'Khoa Vật lý'),
(N'Hóa học', N'Khoa Hóa học'),
(N'Sinh học', N'Khoa Sinh học');

-- PhongBan table
INSERT INTO PhongBan (TenPhongBan, MoTa) VALUES 
(N'Phòng CNTT', N'Quản lý hạ tầng CNTT'),
(N'Phòng Nhân sự', N'Quản lý nhân sự'),
(N'Phòng Tài chính', N'Quản lý tài chính'),
(N'Phòng Marketing', N'Quản lý hoạt động marketing'),
(N'Phòng Kinh doanh', N'Quản lý hoạt động kinh doanh');

-- CanBo table
INSERT INTO CanBo (idQuyenTruyCap, idPhongBan, TenTaiKhoan, MatKhau, HoTen, SDT, Email, CCCD, GioiTinh, DonVi, DiaChi, GioiThieu, idChucVu, idKhoa) VALUES 
(1, 1, 'quantri123', 'matkhau123', N'Nguyễn Văn A', '0123456789', 'nguyenvana@example.com', '123456789012', N'Nam', N'Quản trị', N'123 Đường Quản trị', N'Trưởng phòng Quản trị', 1, 1),
(2, 2, 'nguoidung234', 'matkhau234', N'Trần Thị B', '0987654321', 'tranthib@example.com', '098765432109', N'Nữ', N'Nhân sự', N'456 Đường Nhân sự', N'Chuyên viên Nhân sự', 2, 2),
(3, 3, 'quanly345', 'matkhau345', N'Lê Văn C', '0162345678', 'levanc@example.com', '567890123456', N'Nam', N'Tài chính', N'789 Đường Tài chính', N'Quản lý Tài chính', 3, 3),
(4, 4, 'xem456', 'matkhau456', N'Hoàng Thị D', '0198765432', 'hoangthid@example.com', '654321098765', N'Nữ', N'Marketing', N'321 Đường Marketing', N'Chuyên viên Marketing', 4, 4),
(5, 5, 'bientap567', 'matkhau567', N'Phạm Văn E', '0135792468', 'phamvane@example.com', '135792468024', N'Nam', N'Kinh doanh', N'987 Đường Kinh doanh', N'Nhân viên Kinh doanh', 5, 5);

-- HinhThuc table
INSERT INTO HinhThuc (TenHinhThuc, MoTa) VALUES 
(N'Email', N'Gửi qua email'),
(N'Thư', N'Gửi qua thư bưu điện'),
(N'Fax', N'Gửi qua fax'),
(N'Chuyển phát nhanh', N'Gửi qua chuyển phát nhanh'),
(N'Trực tiếp', N'Gửi trực tiếp');

-- DoKhanCap table
INSERT INTO DoKhanCap (TenDoKhanCap, MoTa) VALUES 
(N'Thấp', N'Mức độ khẩn cấp thấp'),
(N'Trung bình', N'Mức độ khẩn cấp trung bình'),
(N'Cao', N'Mức độ khẩn cấp cao'),
(N'Khẩn cấp', N'Mức độ khẩn cấp rất cao'),
(N'Ngay lập tức', N'Cần xử lý ngay lập tức');

-- LinhVuc table
INSERT INTO LinhVuc (TenLinhVuc, MoTa) VALUES 
(N'Giáo dục', N'Liên quan đến giáo dục'),
(N'Y tế', N'Liên quan đến y tế'),
(N'Công nghệ', N'Liên quan đến công nghệ'),
(N'Tài chính', N'Liên quan đến tài chính'),
(N'Hành chính', N'Liên quan đến hành chính');

-- LoaiVanBan table
INSERT INTO LoaiVanBan (TenLoaiVanBan, MoTa) VALUES 
(N'Báo cáo', N'Văn bản báo cáo chính thức'),
(N'Thông báo', N'Thông báo nội bộ'),
(N'Thư', N'Thư chính thức'),
(N'Hóa đơn', N'Hóa đơn tài chính'),
(N'Công văn', N'Công văn chính thức');

-- TinhChatVB table
INSERT INTO TinhChatVB (TenTinhChatVB, MoTa) VALUES 
(N'Bí mật', N'Văn bản bí mật'),
(N'Công khai', N'Văn bản công khai'),
(N'Nội bộ', N'Văn bản nội bộ'),
(N'Bên ngoài', N'Văn bản bên ngoài'),
(N'Hạn chế', N'Văn bản hạn chế truy cập');

-- TrangThaiVanBan table
INSERT INTO TrangThaiVanBan (TenTrangThai, MoTa) VALUES 
(N'Chờ xử lý', N'Đang chờ xử lý'),
(N'Đã phê duyệt', N'Đã được phê duyệt'),
(N'Bị từ chối', N'Bị từ chối'),
(N'Đang xem xét', N'Đang được xem xét'),
(N'Hoàn thành', N'Đã hoàn thành xử lý');

-- VanBanDen table
INSERT INTO VanBanDen (idHinhThuc, DonViBanHanh, SoDen, idLinhVuc, TinhChatVB, idDoKhanCap, LoaiVanBan, NguoiKy, PhuongThucNhan, NgayDen, NgayPhatHanh, SoKyHieu, idCanBo, idChucVu, idKhoa, CanTraLoiVB, CanXuLyVB, HanTraLoi, SoNgay, LinkFileVanBan, TrichYeu, idNguoiKyVanBan, TrangThaiXuLy) VALUES 
(1, N'Phòng A', 1, 1, 1, 1, 1, N'Nguyễn Văn A', N'Email', '2024-01-01', '2024-01-01', 'ABC123', 1, 1, 1, N'Không', N'Có', '2024-01-10', 10, 1, N'Trích yếu văn bản 1', 1, 1),
(2, N'Phòng B', 2, 2, 2, 2, 2, N'Trần Thị B', N'Thư', '2024-01-02', '2024-01-02', 'DEF456', 2, 2, 2, N'Có', N'Không', '2024-01-12', 10, 2, N'Trích yếu văn bản 2', 2, 2),
(3, N'Phòng C', 3, 3, 3, 3, 3, N'Lê Văn C', N'Fax', '2024-01-03', '2024-01-03', 'GHI789', 3, 3, 3, N'Không', N'Có', '2024-01-13', 10, 3, N'Trích yếu văn bản 3', 3, 3),
(4, N'Phòng D', 4, 4, 4, 4, 4, N'Hoàng Thị D', N'Chuyển phát nhanh', '2024-01-04', '2024-01-04', 'JKL012', 4, 4, 4, N'Có', N'Không', '2024-01-14', 10, 4, N'Trích yếu văn bản 4', 4, 4),
(5, N'Phòng E', 5, 5, 5, 5, 5, N'Phạm Văn E', N'Trực tiếp', '2024-01-05', '2024-01-05', 'MNO345', 5, 5, 5, N'Không', N'Có', '2024-01-15', 10, 5, N'Trích yếu văn bản 5', 5, 5);

-- VanBanDi table
INSERT INTO VanBanDi (idNguoiPheDuyet, idHinhThuc, idLinhVuc, idDoKhanCap, idLoaiVanBan, idCanBo, HanXuLy, TrichYeu, SoDen, NgayPhatHanh, SoKyHieu, LinkFileVanBan, VBCanPhanXL, TrangThaiXuLy) VALUES 
(1, 1, 1, 1, 1, 1, '2024-01-20', N'Trích yếu văn bản đi 1', 1, '2024-01-01', 'PQR678', 'link1.pdf', 1, 1),
(2, 2, 2, 2, 2, 2, '2024-01-21', N'Trích yếu văn bản đi 2', 2, '2024-01-02', 'STU901', 'link2.pdf', 2, 2),
(3, 3, 3, 3, 3, 3, '2024-01-22', N'Trích yếu văn bản đi 3', 3, '2024-01-03', 'VWX234', 'link3.pdf', 3, 3),
(4, 4, 4, 4, 4, 4, '2024-01-23', N'Trích yếu văn bản đi 4', 4, '2024-01-04', 'YZA567', 'link4.pdf', 4, 4),
(5, 5, 5, 5, 5, 5, '2024-01-24', N'Trích yếu văn bản đi 5', 5, '2024-01-05', 'BCD890', 'link5.pdf', 5, 5);

-- ThongTinXuLy table
INSERT INTO ThongTinXuLy (idCanBo, ChuDaoLanhDao, XuLySoBo, idCanBoVP, idPhongBan, HanXuLy, BangSo, DonViPhoiHopXL, NguoiPhoiHopXL, idVanBanDen, idKhoa) VALUES 
(1, N'Chỉ đạo 1', N'Xử lý sơ bộ 1', 2, 1, '2024-01-10', 1, N'Đơn vị phối hợp 1', N'Nguyễn Văn A', 1, 1),
(2, N'Chỉ đạo 2', N'Xử lý sơ bộ 2', 3, 2, '2024-01-11', 2, N'Đơn vị phối hợp 2', N'Trần Thị B', 2, 2),
(3, N'Chỉ đạo 3', N'Xử lý sơ bộ 3', 4, 3, '2024-01-12', 3, N'Đơn vị phối hợp 3', N'Lê Văn C', 3, 3),
(4, N'Chỉ đạo 4', N'Xử lý sơ bộ 4', 5, 4, '2024-01-13', 4, N'Đơn vị phối hợp 4', N'Hoàng Thị D', 4, 4),
(5, N'Chỉ đạo 5', N'Xử lý sơ bộ 5', 1, 5, '2024-01-14', 5, N'Đơn vị phối hợp 5', N'Phạm Văn E', 5, 5);

-- ButPheLanhDao table
INSERT INTO ButPheLanhDao (idVanBanDen, NguoiChuyen, ChuyenDen, ThoiGianChuyen, YKienChuyen) VALUES 
(1, N'Nguyễn Văn A', N'Trần Thị B', '2024-01-01 08:00:00', N'Vui lòng xem xét'),
(2, N'Trần Thị B', N'Lê Văn C', '2024-01-02 09:00:00', N'Để thông tin'),
(3, N'Lê Văn C', N'Hoàng Thị D', '2024-01-03 10:00:00', N'Cần phê duyệt'),
(4, N'Hoàng Thị D', N'Phạm Văn E', '2024-01-04 11:00:00', N'Vui lòng xử lý'),
(5, N'Phạm Văn E', N'Nguyễn Văn A', '2024-01-05 12:00:00', N'Xem xét và xác nhận');

-- VanBanKhoa table
INSERT INTO VanBanKhoa (idVanBanDen, idKhoa, idCanBo) VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);
