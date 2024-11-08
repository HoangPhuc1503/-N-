from fastapi import *
from conn import connection
import math

from getData import *



def deleteVB(idVanBanDi: int, page: int = 1, page_size: int = 10):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("DELETE FROM VanBanDi WHERE idVanBanDi = %s", (idVanBanDi,))
            connect.commit()
            # listVBdi, total_page = getListVBdi(page, page_size)
            return {"message": f"Deleted van ban with id {idVanBanDi}"}
            # return listVBdi, total_page
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



#văn bản đến 
def deleteVBDen(idVanBanDen: int, page: int = 1, page_size: int = 10):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            
            # Xóa các bản ghi liên quan trong bảng ThongTinXuLy trước
            cursor.execute("DELETE FROM VanBanKhoa WHERE idVanBanDen = %s", (idVanBanDen,))

            # Xóa các bản ghi liên quan trong bảng ThongTinXuLy trước
            cursor.execute("DELETE FROM ThongTinXuLy WHERE idVanBanDen = %s", (idVanBanDen,))

            # Xóa các bản ghi liên quan trong bảng ButPheLanhDao trước
            cursor.execute("DELETE FROM ButPheLanhDao WHERE idVanBanDen = %s", (idVanBanDen,))
            
            # Sau đó xóa bản ghi trong bảng VanBanDen
            cursor.execute("DELETE FROM VanBanDen WHERE idVanBanDen = %s", (idVanBanDen,))
            connect.commit()
            # listVBdi, total_page = getListVBdi(page, page_size)
            return {"message": f"Deleted van ban with id {idVanBanDen}"}
            # return listVBdi, total_page
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))