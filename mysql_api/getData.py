from fastapi import *
from conn import connection
import math
from datetime import datetime


def convert_date_format(datestr):
    try:
        date_str = str(datestr)
        # Kiểm tra xem ngày có định dạng DD/MM/YYYY không
        datetime.strptime(date_str, '%d/%m/%Y')
        # Nếu không có lỗi, trả về ngày gốc
        return date_str
    except ValueError:
        # Nếu có lỗi, có nghĩa là ngày không đúng định dạng DD/MM/YYYY
        try:
            # Chuyển đổi chuỗi ngày sang đối tượng datetime theo định dạng YYYY-MM-DD
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            # Chuyển đổi đối tượng date sang chuỗi ngày định dạng DD/MM/YYYY
            return date_obj.strftime('%d/%m/%Y')
        except ValueError as e:
            # Xử lý lỗi nếu ngày không đúng định dạng
            print(f"Error converting date: {e}")
            return None

def get_TkMkCB(tenTaiKhoan: str, matKhau: str):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            # Sử dụng execute với các tham số được truyền an toàn
            cursor.execute("SELECT idCanBo, TenTaiKhoan, MatKhau, HoTen FROM CanBo WHERE TenTaiKhoan=%s AND MatKhau=%s", (tenTaiKhoan, matKhau))
            
            canbos = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            # List_canbo = []
            for item in canbos:
                canbo_dict = {
                    "idCanBo": item[0],
                    "TenTaiKhoan": item[1],
                    "MatKhau": item[2],
                    "HoTen": item[3]
                }
                # List_canbo.append(canbo_dict)
            
            return canbo_dict
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))

def getQuyenTruyCap(idQuyenTruyCap: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT TenQuyen FROM QuyenTruyCap WHERE idQuyenTruyCap = %s", (idQuyenTruyCap,))
            
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "Không xác định"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getPhongBan(idPhongBan: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT TenPhongBan FROM PhongBan WHERE idPhongBan = %s", (idPhongBan,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "Không xác định"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getChucVu(idChucVu: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT TenChucVu FROM ChucVu WHERE idChucVu = %s", (idChucVu,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "Không xác định"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_CanBo(idCanBo: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            # Sử dụng execute với các tham số được truyền an toàn
            cursor.execute("SELECT idCanBo, TenTaiKhoan, MatKhau, idQuyenTruyCap, HoTen, GioiTinh, CCCD, DonVi, idPhongBan, SDT, Email, DiaChi, GioiThieu, idChucVu FROM CanBo WHERE idCanBo = %s", (idCanBo,))
            canbos = cursor.fetchone()  # Lấy một hàng kết quả
            
            if canbos:
                QuyenTruyCap = getQuyenTruyCap(canbos[3])
                Phongban = getPhongBan(canbos[8])
                chucvu = getChucVu(canbos[13])
                canbo_dict = {
                    "idCanBo": canbos[0],
                    "TenTaiKhoan": canbos[1],
                    "MatKhau": canbos[2],
                    "QuyenTruyCap": QuyenTruyCap,
                    "HoTen": canbos[4],
                    "GioiTinh": canbos[5],
                    "CCCD": canbos[6],
                    "DonVi": canbos[7],
                    "PhongBan": Phongban,
                    "SDT": canbos[9],
                    "Email": canbos[10],
                    "DiaChi": canbos[11],
                    "GioiThieu": canbos[12],
                    "ChucVu": chucvu  
                }
                return canbo_dict
            else:
                raise HTTPException(status_code=404, detail="Không tìm thấy cán bộ")
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))


def getQuyenTruyCapAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idQuyenTruyCap, TenQuyen FROM QuyenTruyCap")
            result = cursor.fetchall()
            option_quyentruycapvb = []
            for item in result:
                loaivb_dict = {
                    "id": item[0],
                    "name": item[1]
                }
                option_quyentruycapvb.append(loaivb_dict)
            return option_quyentruycapvb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_CanBoAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            # Sử dụng execute với các tham số được truyền an toàn
            querys = 'SELECT c.idCanBo, c.HoTen, k.TenKhoa, qt.TenQuyen, cv.TenChucVu FROM CanBo AS c INNER JOIN Khoa AS k ON c.idKhoa = k.idKhoa INNER JOIN QuyenTruyCap AS qt ON c.idQuyenTruyCap = qt.idQuyenTruyCap INNER JOIN ChucVu AS cv ON c.idChucVu = cv.idChucVu'
            cursor.execute(querys)
            
            canbos = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            List_canbo = []
            for item in canbos:
                canbo_dict = {
                    "id": item[0],
                    "name": item[1],
                    "khoa": item[2],
                    "quyen": item[3],
                    "chucvu": item[4],                 
                }
                List_canbo.append(canbo_dict)
            return List_canbo
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))



def getHinhThucAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idHinhThuc, TenHinhThuc FROM HinhThuc")
            result = cursor.fetchall()
            option_hinhthucvb = []
            for item in result:
                hinhthucvb_dict = {
                    "idHinhThuc": item[0],
                    "TenHinhThuc": item[1]
                }
                option_hinhthucvb.append(hinhthucvb_dict)
            return option_hinhthucvb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getLinhVucAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idLinhVuc, TenLinhVuc FROM LinhVuc")
            result = cursor.fetchall()
            option_linhvucvb = []
            for item in result:
                linhvucvb_dict = {
                    "idLinhVuc": item[0],
                    "TenLinhVuc": item[1]
                }
                option_linhvucvb.append(linhvucvb_dict)
            return option_linhvucvb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getCanBoPheDuyetAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idCanBo, HoTen, idPhongBan, idQuyenTruyCap, idKhoa FROM CanBo")
            result = cursor.fetchall()
            option_canboduyet = []
            for item in result:
                
                tenphongban = getPhongBan(item[2])
                quyentruycap = getQuyenTruyCap(item[3])
                khoa = getKhoa(item[4])
                canboduyet_dict = {
                    "idCanBo": item[0],
                    "HoTen": item[1],
                    "TenPhongBan": tenphongban,
                    "QuyenTruyCap": quyentruycap,
                    "idKhoa": khoa["idKhoa"],
                    "TenKhoa": khoa["TenKhoa"]
                }
                option_canboduyet.append(canboduyet_dict)
            return option_canboduyet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getDoKhanCapAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idDoKhanCap, TenDoKhanCap FROM DoKhanCap")
            result = cursor.fetchall()
            option_dokhancapvb = []
            for item in result:
                dokhancapvb_dict = {
                    "idDoKhanCap": item[0],
                    "TenDoKhanCap": item[1]
                }
                option_dokhancapvb.append(dokhancapvb_dict)
            return option_dokhancapvb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getPhongBanAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idPhongBan, TenPhongBan FROM PhongBan")
            result = cursor.fetchall()
            option_PhongBan = []
            for item in result:
                PhongBan_dict = {
                    "idPhongBan": item[0],
                    "TenPhongBan": item[1]
                }
                option_PhongBan.append(PhongBan_dict)
            return option_PhongBan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getLoaiVanBanAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idLoaiVanBan, TenLoaiVanBan FROM LoaiVanBan")
            result = cursor.fetchall()
            option_loaivb = []
            for item in result:
                loaivb_dict = {
                    "idLoaiVanBan": item[0],
                    "TenLoaiVanBan": item[1]
                }
                option_loaivb.append(loaivb_dict)
            return option_loaivb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getTrangThaiXuLyAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idTrangThai, TenTrangThai FROM TrangThaiVanBan")
            result = cursor.fetchall()
            option_trangthaixlvb = []
            for item in result:
                trangthaixlvb_dict = {
                    "idTrangThai": item[0],
                    "TenTrangThai": item[1]
                }
                option_trangthaixlvb.append(trangthaixlvb_dict)
            return option_trangthaixlvb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
      
def getTenNguoiNhap(idNguoiNhap: int) -> str:
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT HoTen FROM CanBo WHERE idCanBo = %s", (idNguoiNhap,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "Không xác định"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getCanBoDuyet(idNguoiPheDuyet: int) -> str:
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idCanBo, HoTen FROM CanBo WHERE idCanBo = %s", (idNguoiPheDuyet,))
            result = cursor.fetchall()
            
            for item in result:
                canboduyet_dict = {
                    "idCanBoDuyet": item[0],
                    "TenCanBoDuyet": item[1]
                }
            return canboduyet_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getHinhThuc(idHinhThuc: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idHinhThuc, TenHinhThuc FROM HinhThuc WHERE idHinhThuc = %s", (idHinhThuc,))
            result = cursor.fetchall()
            
            for item in result:
                hinhthuc_dict = {
                    "idHinhThuc": item[0],
                    "TenHinhThuc": item[1]
                }
            return hinhthuc_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getLinhVuc(idLinhVuc: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idLinhVuc, TenLinhVuc FROM LinhVuc WHERE idLinhVuc = %s", (idLinhVuc,))
            result = cursor.fetchall()
            
            for item in result:
                linhvuc_dict = {
                    "idLinhVuc": item[0],
                    "TenLinhVuc": item[1]
                }
            return linhvuc_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getDoKhanCap(idDoKhanCap: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idDoKhanCap, TenDoKhanCap FROM DoKhanCap WHERE idDoKhanCap = %s", (idDoKhanCap,))
            result = cursor.fetchall()
            
            for item in result:
                DoKhanCap_dict = {
                    "idDoKhanCap": item[0],
                    "TenDoKhanCap": item[1]
                }
            return DoKhanCap_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getLoaiVanBan(idLoaiVanBan: int) -> str:
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idLoaiVanBan, TenLoaiVanBan FROM LoaiVanBan WHERE idLoaiVanBan = %s", (idLoaiVanBan,))
            result = cursor.fetchall()
            for item in result:
                LoaiVanBan_dict = {
                    "idLoaiVanBan": item[0],
                    "TenLoaiVanBan": item[1]
                }
            return LoaiVanBan_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getTrangThai(idTrangThai: int) -> str:
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idTrangThai, TenTrangThai FROM TrangThaiVanBan WHERE idTrangThai = %s", (idTrangThai,))
            result = cursor.fetchall()
            for item in result:
                trangthaivb_dict = {
                    "idTrangThai": item[0],
                    "TenTrangThai": item[1]
                }
            return trangthaivb_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getIdVanBanDi(filevanban: str):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDi, idNguoiPheDuyet FROM VanBanDi WHERE LinkFileVanBan = %s", (filevanban,))
            result = cursor.fetchall()
            idvb_list = []
            for item in result:
                idvb_dict = {
                    "idVanBanDi": item[0],
                    "idNguoiNhan": item[1]
                }
                idvb_list.append(idvb_dict)
            return idvb_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def getListVBdi():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDi, TrichYeu, idCanBo, idLoaiVanBan, NgayPhatHanh, HanXuLy, TrangThaiXuLy, idNguoiPheDuyet FROM VanBanDi")
            
            listVBdi = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdiAll = []
            for item in listVBdi:
                TenNguoiNhap = getTenNguoiNhap(item[2])
                loaivanban = getLoaiVanBan(item[3])
                ngayphathanh = convert_date_format(item[4])
                hanxuly = convert_date_format(item[5])
                trangthaixuly = getTrangThai(item[6])
                vb_dict = {
                    "idVanBanDi": item[0],
                    "TrichYeu": item[1],
                    "TenNguoiNhap": TenNguoiNhap,
                    "TenLoaiVanBan": loaivanban["TenLoaiVanBan"],
                    "NgayPhatHanh": ngayphathanh,
                    "HanXuLy": hanxuly,
                    "TenTrangThai": trangthaixuly["TenTrangThai"],
                    "idNguoiPheDuyet": item[7]
                } 
                listVBdiAll.append(vb_dict)
            
            
            return listVBdiAll
            # return list_product
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))

def search_vbdi(key: str):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDi, TrichYeu, idCanBo, idLoaiVanBan, NgayPhatHanh, HanXuLy, TrangThaiXuLy, idNguoiPheDuyet FROM VanBanDi WHERE TrichYeu LIKE %s", ('%' + key + '%',))

            listVBdi = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdiAll = []
            for item in listVBdi:
                TenNguoiNhap = getTenNguoiNhap(item[2])
                loaivanban = getLoaiVanBan(item[3])
                ngayphathanh = convert_date_format(item[4])
                hanxuly = convert_date_format(item[5])
                trangthai = getTrangThai(item[6])
                vb_dict = {
                    "idVanBanDi": item[0],
                    "TrichYeu": item[1],
                    "TenNguoiNhap": TenNguoiNhap,
                    "TenLoaiVanBan": loaivanban["TenLoaiVanBan"],
                    "NgayPhatHanh": ngayphathanh,
                    "HanXuLy": hanxuly,
                    "TenTrangThai": trangthai["TenTrangThai"],
                    "idNguoiPheDuyet": item[7]
                }
                listVBdiAll.append(vb_dict)
           
            
            return listVBdiAll
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
    
def statistical_vbdi(idTrangThai: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDi, TrichYeu, idCanBo, idLoaiVanBan, NgayPhatHanh, HanXuLy, TrangThaiXuLy, idNguoiPheDuyet FROM VanBanDi WHERE TrangThaiXuLy LIKE %s", (idTrangThai ,))

            listVBdi = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdiAll = []
            for item in listVBdi:
                TenNguoiNhap = getTenNguoiNhap(item[2])
                loaivanban = getLoaiVanBan(item[3])
                ngayphathanh = convert_date_format(item[4])
                hanxuly = convert_date_format(item[5])
                trangthai = getTrangThai(item[6])
                vb_dict = {
                    "idVanBanDi": item[0],
                    "TrichYeu": item[1],
                    "TenNguoiNhap": TenNguoiNhap,
                    "TenLoaiVanBan": loaivanban["TenLoaiVanBan"],
                    "NgayPhatHanh": ngayphathanh,
                    "HanXuLy": hanxuly,
                    "TenTrangThai": trangthai["TenTrangThai"],
                    "idNguoiPheDuyet": item[7]
                }
                listVBdiAll.append(vb_dict)
       
            
            return listVBdiAll
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))

def getItemVanBanDi(idVanBanDi: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idNguoiPheDuyet, idHinhThuc, idLinhVuc, idDoKhanCap, idLoaiVanBan, idCanBo, HanXuLy, TrichYeu, SoDen, NgayPhatHanh, SoKyHieu, LinkFileVanBan, TrangThaiXuLy FROM VanBanDi WHERE idVanBanDi = %s", (idVanBanDi,))
            result = cursor.fetchall()

            # vanban = []
            for item in result:
                canboduyet = getCanBoDuyet(item[0])
                hinhthuc = getHinhThuc(item[1])
                linhvuc = getLinhVuc(item[2])
                dokhan = getDoKhanCap(item[3])
                loaivanban = getLoaiVanBan(item[4])
                tennguoinhap = getTenNguoiNhap(item[5])
                hanxuly = item[6]
                trichyeu = item[7]
                soden = item[8]
                ngayphathanh = item[9]
                sokyhieu = item[10]
                filename = item[11]
                trangthaixuly = getTrangThai(item[12])

                vanban = {
                    "idVanBanDi": idVanBanDi,
                    "idCanBoDuyet": canboduyet["idCanBoDuyet"],
                    "NguoiPheDuyet": canboduyet["TenCanBoDuyet"],
                    "idHinhThuc": hinhthuc["idHinhThuc"],
                    "TenHinhThuc": hinhthuc["TenHinhThuc"],
                    "idLinhVuc": linhvuc["idLinhVuc"], 
                    "TenLinhVuc": linhvuc["TenLinhVuc"], 
                    "idDoKhanCap": dokhan["idDoKhanCap"], 
                    "TenDoKhanCap": dokhan["TenDoKhanCap"], 
                    "idLoaiVanBan": loaivanban["idLoaiVanBan"], 
                    "TenLoaiVanBan": loaivanban["TenLoaiVanBan"], 
                    "idNguoiNhap": item[5],
                    "TenNguoiNhap": tennguoinhap, 
                    "HanXuLy": hanxuly, 
                    "TrichYeu": trichyeu,
                    "SoDen": soden,
                    "NgayPhatHanh": ngayphathanh, 
                    "SoKyHieu": sokyhieu, 
                    "LinkFileVanBan": filename, 
                    "idTrangThai": trangthaixuly["idTrangThai"],
                    "TenTrangThai": trangthaixuly["TenTrangThai"],
                }
                # vanban.append(vanban_dict)

            return vanban

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getButPheVBDi(idVanBanDi: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idNguoiChuyen, idNguoinhan, ThoiGianChuyen, YKienChuyen FROM ButPheLanhDao WHERE idVanBanDi = %s", (idVanBanDi,))
            result = cursor.fetchall()
            
            butpheVBdi = []
            for item in result:
                nguoichuyen = get_CanBo(item[0])
                nguoinhan = get_CanBo(item[1])
                butphe_dict = {
                    "idNguoiChuyen": item[0],
                    "TenNguoiChuyen": nguoichuyen["HoTen"],
                    "TenPhongBanNC": nguoichuyen["PhongBan"],
                    "TenChucVuNC": nguoichuyen["ChucVu"],
                    "idNguoiNhan": item[1],
                    "TenNguoiNhan": nguoinhan["HoTen"],
                    "TenPhongBanNN": nguoinhan["PhongBan"],
                    "TenChucVuNN": nguoinhan["ChucVu"],
                    "ThoiGianChuyen": item[2],
                    "YKienChuyen": item[3],
                    "QuyenTruyCapNC": nguoichuyen["QuyenTruyCap"],
                    "QuyenTruyCapNN": nguoinhan["QuyenTruyCap"]
                }
                butpheVBdi.append(butphe_dict)
            return butpheVBdi
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


#văn bản đến
def getListVBden(page: int = 1, page_size: int = 10):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDen, SoDen, NgayDen, idDoKhanCap, DonViBanHanh, TrichYeu, idNguoiPheDuyet FROM VanBanDen")
            
            listVBdi = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdiAll = []
            for item in listVBdi:
                ngayden = convert_date_format(item[2])
                dokhancap = getDoKhanCap(item[3]) 
                NguoiPheDuyet = get_CanBo(item[6])
                vb_dict = {
                    "idVanBanDen": item[0],
                    "SoDen": item[1],
                    "NgayDen": ngayden,
                    "DoKhanCap": dokhancap["TenDoKhanCap"],
                    "DonViBanHanh": item[4],
                    "TrichYeu": item[5],
                    "NguoiPheDuyet": NguoiPheDuyet["HoTen"],
                    "idNguoiPheDuyet": NguoiPheDuyet["idCanBo"]
                }
                listVBdiAll.append(vb_dict)
            total_page = math.ceil((len(listVBdiAll) / page_size))
            start_row_index = (page - 1) * page_size
            
            return listVBdiAll[start_row_index:start_row_index + page_size], total_page
            # return list_product
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
    
def search_vbden(key: str, page: int = 1, page_size: int = 10):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDen, SoDen, NgayDen, idDoKhanCap, DonViBanHanh, TrichYeu, idNguoiPheDuyet FROM VanBanDen WHERE TrichYeu LIKE %s", ('%' + key + '%',))
            listVBdi = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdiAll = []
            
            for item in listVBdi:
                ngayden = convert_date_format(item[2])
                dokhancap = getDoKhanCap(item[3]) 
                NguoiPheDuyet = get_CanBo(item[6])
                vb_dict = {
                    "idVanBanDen": item[0],
                    "SoDen": item[1],
                    "NgayDen": ngayden,
                    "DoKhanCap": dokhancap["TenDoKhanCap"],
                    "DonViBanHanh": item[4],
                    "TrichYeu": item[5],
                    "NguoiPheDuyet": NguoiPheDuyet["HoTen"],
                    "idNguoiPheDuyet": NguoiPheDuyet["idCanBo"]
                }
                listVBdiAll.append(vb_dict)
            total_page = math.ceil((len(listVBdiAll) / page_size))
            start_row_index = (page - 1) * page_size
            
            return listVBdiAll[start_row_index:start_row_index + page_size], total_page
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
    

def statistical_vbden(idTrangThai: int, page: int = 1, page_size: int = 10):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDen, SoDen, NgayDen, idDoKhanCap, DonViBanHanh, TrichYeu, idNguoiPheDuyet, TrangThaiXuLy FROM VanBanDen WHERE TrangThaiXuLy LIKE %s", (idTrangThai,))
            listVBden = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdenAll = []
            for item in listVBden:
                ngayden = convert_date_format(item[2])
                dokhancap = getDoKhanCap(item[3]) 
                NguoiPheDuyet = get_CanBo(item[6])
                vb_dict = {
                    "idVanBanDen": item[0],
                    "SoDen": item[1],
                    "NgayDen": ngayden,
                    "DoKhanCap": dokhancap["TenDoKhanCap"],
                    "DonViBanHanh": item[4],
                    "TrichYeu": item[5],
                    "NguoiPheDuyet": NguoiPheDuyet["HoTen"],
                    "idNguoiPheDuyet": NguoiPheDuyet["idCanBo"],
                    "TrangThaiXuLy": item[7]
                }
                listVBdenAll.append(vb_dict)
            total_page = math.ceil((len(listVBdenAll) / page_size))
            start_row_index = (page - 1) * page_size
            
            return listVBdenAll[start_row_index:start_row_index + page_size], total_page
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
    


def getTinhChatVanBanAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idTinhChatVB, TenTinhChatVB FROM TinhChatVB")
            result = cursor.fetchall()
            
            tinhchatVB_list = []  # Tạo một danh sách để chứa các dict
            for item in result:
                tinhchatVB_dict = {
                    "idTinhChatVB": item[0],
                    "TenTinhChatVB": item[1]
                }
                tinhchatVB_list.append(tinhchatVB_dict)
            return tinhchatVB_list  # Trả về danh sách các dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getTinhChatVanBan(idTinhChatVB: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idTinhChatVB, TenTinhChatVB FROM TinhChatVB WHERE idTinhChatVB = %s", (idTinhChatVB,))
            result = cursor.fetchall()
            
            for item in result:
                tinhchatVB_dict = {
                    "idTinhChatVB": item[0],
                    "TenTinhChatVB": item[1]
                }
            return tinhchatVB_dict  # Trả về danh sách các dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getKhoaAll():
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idKhoa, TenKhoa FROM Khoa")
            result = cursor.fetchall()
            
            Khoa_list = []  # Tạo một danh sách để chứa các dict
            for item in result:
                Khoa_dict = {
                    "idKhoa": item[0],
                    "TenKhoa": item[1]
                }
                Khoa_list.append(Khoa_dict)
            return Khoa_list  # Trả về danh sách các dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getKhoa(idKhoa: int ):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idKhoa, TenKhoa FROM Khoa WHERE idKhoa = %s", (idKhoa,))
            result = cursor.fetchall()
            
            for item in result:
                Khoa_dict = {
                    "idKhoa": item[0],
                    "TenKhoa": item[1]
                }
            return Khoa_dict  # Trả về danh sách các dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  
     
def getTrangThaiXuLy(idTrangThaiXuLy: int ):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idTrangThai, TenTrangThai FROM TrangThaiVanBan WHERE idTrangThai = %s", (idTrangThaiXuLy,))
            result = cursor.fetchall()
            
            for item in result:
                TrangThai_dict = {
                    "idTrangThai": item[0],
                    "TenTrangThai": item[1]
                }
            return TrangThai_dict  # Trả về danh sách các dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   

def getChiTietVbDen(idVanBanDen: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT  idHinhThuc, DonViBanHanh, SoDen, idLinhVuc, TinhChatVB, idDoKhanCap, LoaiVanBan, NgayDen, NgayPhatHanh, SoKyHieu, idCanBo, idNguoiPheDuyet, idKhoa, CanTraLoiVB, CanXuLyVB, HanTraLoi, SoNgay, LinkFileVanBan, TrichYeu, TrangThaiXuLy, idVanBanDen FROM VanBanDen WHERE idVanBanDen = %s", (idVanBanDen,))
            VanBanDen = cursor.fetchall()           
            for item in VanBanDen:
                HinhThuc = getHinhThuc(item[0])
                DonViBanHanh = item[1]
                SoDen = item[2]
                LinhVuc = getLinhVuc(item[3])
                TinhChatVB = getTinhChatVanBan(item[4])
                DoKhanCap = getDoKhanCap(item[5])
                LoaiVanBan = getLoaiVanBan(item[6])
                NgayDen = item[7]
                NgayPhatHanh = item[8]
                SoKyHieu = item[9]
                NguoiTao = get_CanBo(item[10])
                NguoiPheDuyet = getCanBoDuyet(item[11])
                Khoa = getKhoa(item[12])
                CanTraLoiVB = item[13]
                CanXuLyVB = item[14]
                HanTraLoi = item[15]
                SoNgay = item[16]
                LinkFileVanBan = item[17]
                TrichYeu = item[18]
                TrangThaiXuLy = getTrangThaiXuLy(item[19])
                idVanBanDen = item[20]
                VanBanDen_dict = {
                    "HinhThuc": HinhThuc["TenHinhThuc"],
                    "idHinhThuc": HinhThuc["idHinhThuc"],
                    "DonViBanHanh": DonViBanHanh,
                    "Soden": SoDen,
                    "LinhVuc":LinhVuc["TenLinhVuc"],
                    "idLinhVuc":LinhVuc["idLinhVuc"],
                    "TinhChatVB":TinhChatVB["TenTinhChatVB"],
                    "idTinhChatVB":TinhChatVB["idTinhChatVB"],
                    "DoKhanCap":DoKhanCap["TenDoKhanCap"],
                    "idDoKhanCap":DoKhanCap["idDoKhanCap"],
                    "LoaiVanBan":LoaiVanBan["TenLoaiVanBan"],
                    "idLoaiVanBan":LoaiVanBan["idLoaiVanBan"],
                    "NgayDen": NgayDen,       
                    "NgayPhatHanh":NgayPhatHanh,
                    "SoKyHieu": SoKyHieu,
                    "NguoiTao":NguoiTao["HoTen"],
                    "idNguoiTao":NguoiTao["idCanBo"],
                    "NguoiPheDuyet":NguoiPheDuyet["TenCanBoDuyet"],
                    "idNguoiPheDuyet":NguoiPheDuyet["idCanBoDuyet"],
                    "Khoa": Khoa["TenKhoa"],
                    "idKhoa": Khoa["idKhoa"],
                    "CanTraLoiVB": CanTraLoiVB,
                    "CanXyLyVB" : CanXuLyVB,
                    "HanTraLoi" : HanTraLoi,
                    "SoNgay" : SoNgay,
                    "LinkFileVanBan" : LinkFileVanBan,
                    "TrichYeu": TrichYeu,
                    "TrangThaiXuLy":TrangThaiXuLy["TenTrangThai"],
                    "idTrangThaiXuLy":TrangThaiXuLy["idTrangThai"],
                    "idVanBanDen":idVanBanDen
                }
            return VanBanDen_dict  # Trả về danh sách các dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getButPheVBDen(idVanBanDen: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idNguoiChuyen, idNguoinhan, ThoiGianChuyen, YKienChuyen FROM ButPheLanhDao WHERE idVanBanDen = %s", (idVanBanDen,))
            result = cursor.fetchall()
            
            butpheVBden = []
            for item in result:
                nguoichuyen = get_CanBo(item[0])
                nguoinhan = get_CanBo(item[1])
                butphe_dict = {
                    "idNguoiChuyen": item[0],
                    "TenNguoiChuyen": nguoichuyen["HoTen"],
                    "TenPhongBanNC": nguoichuyen["PhongBan"],
                    "TenChucVuNC": nguoichuyen["ChucVu"],
                    "idNguoiNhan": item[1],
                    "TenNguoiNhan": nguoinhan["HoTen"],
                    "TenPhongBanNN": nguoinhan["PhongBan"],
                    "TenChucVuNN": nguoinhan["ChucVu"],
                    "ThoiGianChuyen": item[2],
                    "YKienChuyen": item[3]
                }
                butpheVBden.append(butphe_dict)
            return butpheVBden
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

