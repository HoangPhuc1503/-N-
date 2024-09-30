from fastapi import *
from conn import connection
import math

def getListVBdi(page: int = 1, page_size: int = 10):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT idVanBanDi, TrichYeu, idCanBo, idLoaiVanBan, NgayPhatHanh, HanXuLy, TrangThaiXuLy FROM VanBanDi")
            
            listVBdi = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            listVBdiAll = []
            for item in listVBdi:
                vb_dict = {
                    "idVanBanDi": item[0],
                    "TrichYeu": item[1],
                    "idCanBo": item[2],
                    "idLoaiVanBan": item[3],
                    "NgayPhatHanh": item[4],
                    "HanXuLy": item[5],
                    "TrangThaiXuLy": item[6]
                }
                listVBdiAll.append(vb_dict)
            total_page = math.ceil((len(listVBdiAll) / page_size))
            start_row_index = (page - 1) * page_size
            
            return listVBdiAll[start_row_index:start_row_index + page_size], total_page
            # return list_product
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
    


def get_TkMkCB(tenTaiKhoan: str, matKhau: str):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            # Sử dụng execute với các tham số được truyền an toàn
            cursor.execute("SELECT idCanBo,TenTaiKhoan, MatKhau FROM CanBo WHERE TenTaiKhoan=%s AND MatKhau=%s", (tenTaiKhoan, matKhau))
            
            canbos = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            List_canbo = []
            for item in canbos:
                canbo_dict = {
                    "IDCanBo": item[0],
                    "TenTaiKhoan": item[1],
                    "MatKhau": item[2],
                }
                List_canbo.append(canbo_dict)
            
            return List_canbo
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
    



def get_CanBo(ID: str):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            # Sử dụng execute với các tham số được truyền an toàn
            cursor.execute("SELECT idQuyenTruyCap, HOTEN, GioiTinh, CCCD, DonVi, idPhongBan, SDT, Email, DiaChi, GioiThieu FROM CanBo WHERE  idCanBo=%s", (ID))
            
            canbos = cursor.fetchall()  # Lấy tất cả các dòng dữ liệu từ truy vấn
            List_canbo = []
            for item in canbos:
                canbo_dict = {
                    "QuyenTruyCap": item[0],
                    "HoTen": item[1],
                    "GioiTinh": item[2],
                    "CCCD": item[3],
                    "DonVi": item[4],
                    "IDphongban": item[5],
                    "SDT": item[6],
                    "Email": item[7],
                    "DiaChi": item[8],
                    "GioiThieu": item[9],                   
                }
                List_canbo.append(canbo_dict)
            
            return List_canbo
    except Exception as e:
        # Nếu có lỗi xảy ra trong quá trình truy vấn, ném HTTPException với mã lỗi 500
        raise HTTPException(status_code=500, detail=str(e))
