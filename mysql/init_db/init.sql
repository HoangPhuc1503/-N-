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
    -- NguoiKy NVARCHAR(100),
      NgayDen DATE,
      NgayPhatHanh DATE,
      SoKyHieu VARCHAR(50),
      idNguoiPheDuyet INT,
      idCanBo INT,
    idKhoa INT,
      CanTraLoiVB VARCHAR(10),
      CanXuLyVB VARCHAR(10),
      HanTraLoi DATE,
      SoNgay INT,
      LinkFileVanBan VARCHAR(500),
      TrichYeu VARCHAR(100),
    -- idNguoiKyVanBan INT,
      TrangThaiXuLy INT,
    FOREIGN KEY (idNguoiPheDuyet) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idHinhThuc) REFERENCES HinhThuc(idHinhThuc),
    FOREIGN KEY (idLinhVuc) REFERENCES LinhVuc(idLinhVuc),
    FOREIGN KEY (TinhChatVB) REFERENCES TinhChatVB(idTinhChatVB),
    FOREIGN KEY (idDoKhanCap) REFERENCES DoKhanCap(idDoKhanCap),
    FOREIGN KEY (LoaiVanBan) REFERENCES LoaiVanBan(idLoaiVanBan),
    FOREIGN KEY (idCanBo) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idKhoa) REFERENCES Khoa(idKhoa),
    -- FOREIGN KEY (idNguoiKyVanBan) REFERENCES CanBo(idCanBo),
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
    LinkFileVanBan VARCHAR(500),
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
    idVanBanDi INT,
    idVanBanDen INT,
    idNguoiChuyen INT,
    idNguoiNhan INT,
    ThoiGianChuyen DATETIME,
    YKienChuyen TEXT,
    FOREIGN KEY (idNguoiNhan) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idNguoiChuyen) REFERENCES CanBo(idCanBo),
    FOREIGN KEY (idVanBanDi) REFERENCES VanBanDi(idVanBanDi) 
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (idVanBanDen) REFERENCES VanBanDen(idVanBanDen)
        ON UPDATE CASCADE
        ON DELETE CASCADE
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
(N'Lãnh đạo', 'LD'),
(N'Chuyên viên', 'CV'),
(N'Văn thư', 'VT'),
(N'Giảng viên', "GV");

-- ChucVu table
INSERT INTO ChucVu (TenChucVu) VALUES 
(N'Quản trị viên'),
(N'Lãnh đạo'),
(N'Chuyên Viên'),
(N'Văn thư'),
(N'Giảng viên');

-- ChiTietChucVu table
INSERT INTO ChiTietChucVu (idChucVu, idQuyenTruyCap) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- Khoa table
INSERT INTO Khoa (TenKhoa, MoTa) VALUES 
(N'Công nghệ số', N'Khoa Công nghệ số'),
(N'Điện - Điện tử', N'Khoa Điện - Điện tử'),
(N'Kỹ thuật xây dựng', N'Khoa Kỹ thuật xây dựng'),
(N'CN Hóa học - Môi trường', N'Mô tả Khoa CN Hóa học - Môi trường'),
(N'Sư phạm - Công nghiệp', N'Mô tả Khoa Sư phạm - Công nghiệp');

-- PhongBan table
INSERT INTO PhongBan (TenPhongBan, MoTa) VALUES 
(N'Công tác HS-SV', N'Mô tả Phòng Công tác HS-SV'),
(N'QLKH và HTQT', N'Mô tả Phòng QLKH và HTQT'),
(N'Kế hoạch - Tài chính', N'Mô tả Phòng Kế hoạch - Tài chính'),
(N'Khảo thí và BCLGD', N'Mô tả Phòng Khảo thí và BCLGD'),
(N'Tổ Chức - Hành Chính', N'Mô tả Quản lý hạ tầng CNTT'),
(N'Đào tạo', N'Mô tả Phòng Đào tạo');

-- CanBo table
INSERT INTO CanBo (idQuyenTruyCap, idPhongBan, TenTaiKhoan, MatKhau, HoTen, SDT, Email, CCCD, GioiTinh, DonVi, DiaChi, GioiThieu, idChucVu, idKhoa) VALUES 
(1, 1, 'admin123', 'admin123', N'Khánh Công', '0123456789', 'nguyenvana@example.com', '123456789012', N'Nam', N'Quản trị', N'123 Đường Quản trị', N'Trưởng phòng Quản trị', 1, 1),
(2, 2, 'lanhdao123', 'lanhdao123', N'Lãnh đạo A', '0987654321', 'lanhdaoa@example.com', '098765432109', N'Nữ', N'Nhân sự', N'456 Đường Nhân sự', N'Chuyên viên Nhân sự', 2, 2),
(2, 5, 'lanhdao456', 'lanhdao456', N'Lãnh đạo B', '0135792468', 'lanhdaob@example.com', '135792468024', N'Nam', N'Kinh doanh', N'987 Đường hải hồ', N'Nhân viên Kinh doanh', 2, 5),
(2, 3, 'lanhdao789', 'lanhdao789', N'Lãnh đạo C', '0987654325', 'lanhdaoc@example.com', '098765432100', N'Nữ', N'Tài chính', N'456 Đường Tài Chính', N'Chuyên viên Tài chính', 2, 1),
(4, 1, 'vanthu1', 'vanthu', N'Văn Thư 1', '0935733354', 'vanthu1@example.com', '567890123456', N'Nữ', N'Công tác HSSV', N'789 Công tác HSSV', N'Công tác HS-SV', 4, 4),
(4, 3, 'vanthu2', 'vanthu', N'Văn Thư 2', '0342483925', 'vanthu2@example.com', '567890123456', N'Nữ', N'Kế hoạch - Tài chính', N'789 Đường Tài chính', N'Quản lý Tài chính', 4, 2),
(4, 2, 'vanthu3', 'vanthu', N'Văn Thư 3', '0823885745', 'vanthu3@example.com', '567890123456', N'Nữ', N'QLKH và HTQT', N'789 Đường QLKH và HTQT', N'QLKH và HTQT', 4, 2),
(4, 5, 'vanthu4', 'vanthu', N'Văn Thư 4', '0347843633', 'vanthu4@example.com', '567890123456', N'Nữ', N'Tổ Chức - Hành Chính', N'789 Đường Tổ Chức - Hành Chính', N'Tổ Chức - Hành Chính', 4, 1),
(4, 2, 'vanthu5', 'vanthu', N'Văn Thư 5', '0954938584', 'vanthu5@example.com', '135792468024', N'Nữ', N'QLKH và HTQT', N'987 Đường QLKH và HTQT', N'QLKH và HTQT', 4, 5),
(5, 1, 'giangvien1', 'giangvien', N'Giảng Viên 1', '0935733354', 'giangvien1@example.com', '567890123456', N'Nữ', N'Công tác HSSV', N'789 Công tác HSSV', N'Công tác HS-SV', 5, 1),
(5, 3, 'giangvien2', 'giangvien', N'Giảng Viên 2', '0342483925', 'giangvien2@example.com', '567890123456', N'Nam', N'Kế hoạch - Tài chính', N'789 Đường Tài chính', N'Quản lý Tài chính', 5, 3),
(5, 2, 'giangvien3', 'giangvien', N'Giảng Viên 3', '0823885745', 'giangvien3@example.com', '567890123456', N'Nữ', N'QLKH và HTQT', N'789 Đường QLKH và HTQT', N'QLKH và HTQT', 5, 2),
(5, 5, 'giangvien4', 'giangvien', N'Giảng Viên 4', '0347843633', 'giangvien4@example.com', '567890123456', N'Nam', N'Tổ Chức - Hành Chính', N'789 Đường Tổ Chức - Hành Chính', N'Tổ Chức - Hành Chính', 4, 1),
(5, 2, 'giangvien5', 'giangvien', N'Giảng Viên 5', '0954938584', 'giangvien5@example.com', '135792468024', N'Nữ', N'QLKH và HTQT', N'987 Đường QLKH và HTQT', N'QLKH và HTQT', 5, 5);

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
(N'Chờ phê duyệt', N'Đang được xem xét để duyệt'),
(N'Phối hợp xử lý', N'Khoa phối hợp xử lý'),
(N'Quá hạn', N'Quá hạn xử lý');
-- (N'Hoàn thành', N'Đã hoàn thành xử lý');

-- VanBanDen table
INSERT INTO VanBanDen (idHinhThuc, DonViBanHanh, SoDen, idLinhVuc, TinhChatVB, idDoKhanCap, LoaiVanBan, NgayDen, NgayPhatHanh, SoKyHieu, idCanBo, idNguoiPheDuyet, idKhoa, CanTraLoiVB, CanXuLyVB, HanTraLoi, SoNgay, LinkFileVanBan, TrichYeu, TrangThaiXuLy) VALUES 
(1, N'Phòng A', 1, 1, 1, 1, 1, '2024-01-01', '2024-01-01', 'ABC123', 1, 2, 1, N'Không', N'Có', '2024-01-10', 10, 'link1.pdf', N'Trích yếu văn bản 1',  1),
(2, N'Phòng B', 2, 2, 2, 2, 2, '2024-01-02', '2024-01-02', 'DEF456', 2, 2, 2, N'Có', N'Không', '2024-01-12', 10, 'link2.pdf', N'Trích yếu văn bản 2',  2),
(3, N'Phòng C', 3, 3, 3, 3, 3, '2024-01-03', '2024-01-03', 'GHI789', 3, 1, 3, N'Không', N'Có', '2024-01-13', 10,'link3.pdf', N'Trích yếu văn bản 3', 3),
(4, N'Phòng D', 4, 4, 4, 4, 4, '2024-01-04', '2024-01-04', 'JKL012', 6, 4, 4, N'Có', N'Không', '2024-01-14', 10, 'link4.pdf', N'Trích yếu văn bản 4', 4),
(5, N'Phòng E', 5, 5, 5, 5, 5, '2024-01-05', '2024-01-05', 'MNO345', 2, 4, 5, N'Không', N'Có', '2024-01-15', 10, 'link5.pdf', N'Trích yếu văn bản 5', 3);

-- VanBanDi table
INSERT INTO VanBanDi (idNguoiPheDuyet, idHinhThuc, idLinhVuc, idDoKhanCap, idLoaiVanBan, idCanBo, HanXuLy, TrichYeu, SoDen, NgayPhatHanh, SoKyHieu, LinkFileVanBan, TrangThaiXuLy) VALUES 
(2, 1, 1, 1, 1, 1, '2024-01-20', N'Trích yếu văn bản đi A11', 1, '2024-01-01', 'PQR678', 'link1.pdf', 1),
(4, 2, 2, 2, 2, 1, '2024-01-21', N'Trích yếu văn bản đi A12', 2, '2024-01-02', 'STU901', 'link2.pdf', 2),
(3, 3, 3, 3, 3, 1, '2024-01-22', N'Trích yếu văn bản đi A13', 3, '2024-01-03', 'VWX234', 'link3.pdf', 3),
(6, 4, 4, 4, 4, 1, '2024-01-23', N'Trích yếu văn bản đi A14', 4, '2024-01-04', 'YZA567', 'link4.pdf', 4),
(3, 5, 5, 5, 5, 1, '2024-01-24', N'Trích yếu văn bản đi A15', 5, '2024-01-05', 'BCD890', 'link5.pdf', 2);

-- ThongTinXuLy table
INSERT INTO ThongTinXuLy (idCanBo, ChuDaoLanhDao, XuLySoBo, idCanBoVP, idPhongBan, HanXuLy, BangSo, DonViPhoiHopXL, NguoiPhoiHopXL, idVanBanDen, idKhoa) VALUES 
(1, N'Chỉ đạo 1', N'Xử lý sơ bộ 1', 2, 1, '2024-01-10', 1, N'Đơn vị phối hợp 1', N'Nguyễn Văn A', 1, 1),
(2, N'Chỉ đạo 2', N'Xử lý sơ bộ 2', 3, 2, '2024-01-11', 2, N'Đơn vị phối hợp 2', N'Trần Thị B', 2, 2),
(3, N'Chỉ đạo 3', N'Xử lý sơ bộ 3', 4, 3, '2024-01-12', 3, N'Đơn vị phối hợp 3', N'Lê Văn C', 3, 3),
(4, N'Chỉ đạo 4', N'Xử lý sơ bộ 4', 2, 4, '2024-01-13', 4, N'Đơn vị phối hợp 4', N'Hoàng Thị D', 4, 4),
(2, N'Chỉ đạo 5', N'Xử lý sơ bộ 5', 1, 5, '2024-01-14', 5, N'Đơn vị phối hợp 5', N'Phạm Văn E', 5, 5);

-- ButPheLanhDao table
INSERT INTO ButPheLanhDao (idVanBanDi, idVanBanDen, idNguoiChuyen, idNguoiNhan, ThoiGianChuyen, YKienChuyen) VALUES 
(1, null, 2, 3, '2024-01-01 08:00:00', N'Vui lòng xem xét'),
(1, null, 3,  4, '2024-01-02 09:00:00', N'Để thông tin'),
(1, null, 4,  5, '2024-01-02 09:00:00', N'Để thông tin'),
(2, null, 4, 2, '2024-01-01 08:00:00', N'Vui lòng xem xét'),
(2, null, 2, 3, '2024-01-02 09:00:00', N'Để thông tin'),
(null, 1,  2, 3, '2024-01-01 08:00:00', N'Vui lòng xem xét'),
(null, 1,  3,  4, '2024-01-02 09:00:00', N'Để thông tin'),
(null, 1,  4,  5, '2024-01-02 09:00:00', N'Để thông tin'),
(null, 2,  4, 2, '2024-01-01 08:00:00', N'Vui lòng xem xét'),
(null, 2,  2, 3, '2024-01-02 09:00:00', N'Để thông tin');
-- (3, '2024-01-03 10:00:00', N'Cần phê duyệt'),
-- (4,  '2024-01-04 11:00:00', N'Vui lòng xử lý'),
-- (5,  '2024-01-05 12:00:00', N'Xem xét và xác nhận');

-- VanBanKhoa table
INSERT INTO VanBanKhoa (idVanBanDen, idKhoa, idCanBo) VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 2);
