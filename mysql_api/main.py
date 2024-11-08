from fastapi import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from getData import *
from delete import *
from insert import *
from update import *


from fastapi.responses import StreamingResponse
from openpyxl import Workbook
from typing import Optional
import io, os, shutil




# import xuất file
from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime
import io
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import urllib.parse



app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# UPLOAD_FOLDER = 'FileUpload/'
# Lấy đường dẫn tuyệt đối của file hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Xây dựng đường dẫn tuyệt đối tới thư mục FileUpload/
UPLOAD_FOLDER = os.path.join(current_dir, 'FileUpload')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    try:
        return templates.TemplateResponse("login.html", {"request": request})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/checklogin")
def checkLogin(tenDN: str, mK: str):
    user_info = get_TkMkCB(tenDN, mK)
    if user_info:
        return {"success": True, "user_info": user_info}
    else:
        return None

@app.get("/logout")
def logout():
    try:
        # return templates.TemplateResponse("login.html", {"request": request})
        return RedirectResponse("/login")
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))




@app.get("/phanquyen")
def phanquyen(request: Request, id:int):
    try:
        canbo = get_CanBo(id)
        return templates.TemplateResponse("phanquyen.html", {"request": request, 
                                                            "canbo": canbo})

    except Exception as e:
        # Xử lý lỗi tương tự như trước
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/phanquyen_data")
def phanquyen_data(request: Request):
    try:
        listCB = get_CanBoAll()  # Replace with your function to fetch CanBo data
        listQTC = getQuyenTruyCapAll()  # Replace with your function to fetch QuyenTruyCap data

        # Convert lists to JSON format
        data = {"listCB": listCB, "listQTC": listQTC}

        # Return JSON response with correct content type
        return data

    except Exception as e:
        # Handle errors appropriately (e.g., logging, returning a specific error response)
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/phanquyen_put/idCanBo={idCanBo}&idQuyenTruyCap={idQuyenTruyCap}", response_model=dict)
def phanquyen_put(idCanBo: int, idQuyenTruyCap: int):
    try:
        return update_ChucVu(idCanBo, idQuyenTruyCap)
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    # return {"idCanBo": idCanBo, "idQuyenTruyCap": idQuyenTruyCap}



@app.get("/hethong", response_class=HTMLResponse)
async def trangchu(request: Request, id: int):
    try:
        canbo = get_CanBo(id)
        return templates.TemplateResponse("index.html", {"request": request,
                                                        "canbo": canbo})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/hethong/thongtincanhan", response_class=HTMLResponse)
async def thongtincanhan(request: Request, id: int):
    try:
        canbo = get_CanBo(id)
        return templates.TemplateResponse("thongtincanhan.html", {"request": request,
                                                                   "canbo": canbo})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/hethong/thongtincanhan/update/{id}")
async def capnhatthongtin(request: Request, id: int):
    try:
        thongtincanhan = await request.json()
        # Add the idVanBanDi to the update data
        thongtincanhan['idCanBo'] = id

        # Gọi hàm capnhatthongtincb để lưu vào cơ sở dữ liệu
        capnhatthongtincb([thongtincanhan])

        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/hethong/vanbandi", response_class=HTMLResponse)
def vanbandi(request: Request, id: int):
    try:
        canbo = get_CanBo(id)
        listVBdi = getListVBdi()
        option_trangthaixuly = getTrangThaiXuLyAll()
        return templates.TemplateResponse("vanbandi.html", {"request": request, 
                                                            "canbo": canbo,
                                                            "listVB": listVBdi,
                                                             "option_trangthaixuly": option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/hethong/vanbandi/chitiet/{id}/vb{idVanBanDi}")
def chitietVbdi(request: Request, id:int, idVanBanDi: int):
    try:
        canbo = get_CanBo(id)
        chitietVB = getItemVanBanDi(idVanBanDi)
        option_hinhthuc = getHinhThucAll()
        option_linhvuc = getLinhVucAll()
        option_nguoipheduyet = getCanBoPheDuyetAll()
        option_dokhan = getDoKhanCapAll()
        option_loaivb = getLoaiVanBanAll()
        option_trangthaixuly = getTrangThaiXuLyAll()
        option_khoa = getKhoaAll()
        butpheVBdi = getButPheVBDi(idVanBanDi)

        return templates.TemplateResponse("chitietVBdi.html", {"request": request,
                                                                "canbo": canbo,
                                                                "chitietVB": chitietVB,
                                                                "option_hinhthuc": option_hinhthuc,
                                                                "option_linhvuc": option_linhvuc,
                                                                "option_nguoipheduyet": option_nguoipheduyet,
                                                                "option_dokhan": option_dokhan,
                                                                "option_loaivb": option_loaivb,
                                                                "option_trangthaixuly": option_trangthaixuly,
                                                                "option_khoa": option_khoa,
                                                                "butpheVBdi": butpheVBdi})
    
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/hethong/vanbandi/chuyenpheduyet")
def chuyenpheduyetVbDi(
    idNguoiPheDuyet: int = Form(...),
    idHinhThuc: int = Form(...),
    idLinhVuc: int = Form(...),
    idDoKhanCap: int = Form(...),
    idLoaiVanBan: int = Form(...),
    idCanBo: int = Form(...),
    HanXuLy: str = Form(...),
    TrichYeu: str = Form(...),
    SoDen: int = Form(...),
    NgayPhatHanh: str = Form(...),
    SoKyHieu: str = Form(...),
    fileVanBan: str = Form(...),
    TrangThaiXuLy: int = Form(...),
    idNguoiChuyen: int = Form(...),
    ThoiGianChuyen: str = Form(...),
    YKienChuyen: Optional[str] =  Form(None)
    
):
    try:
        vanban = [{
            'idNguoiPheDuyet': idNguoiPheDuyet,
            'idHinhThuc': idHinhThuc,
            'idLinhVuc': idLinhVuc,
            'idDoKhanCap': idDoKhanCap,
            'idLoaiVanBan': idLoaiVanBan,
            'idCanBo': idCanBo,
            'HanXuLy': HanXuLy,
            'TrichYeu': TrichYeu,
            'SoDen': SoDen,
            'NgayPhatHanh': NgayPhatHanh,
            'SoKyHieu': SoKyHieu,
            'LinkFileVanBan': fileVanBan,
            'TrangThaiXuLy': TrangThaiXuLy
        }]

        themmoivanban(vanban)

        listId = getIdVanBanDi(fileVanBan)
        
        if YKienChuyen is None:
            YKienChuyen = ""
        butphe = []
        
        for id in listId:
            butphe_dict = {
                "idVanBanDi": id["idVanBanDi"],
                "idNguoiChuyen": idNguoiChuyen,
                "idNguoiNhan": idNguoiPheDuyet,
                "ThoiGianChuyen": ThoiGianChuyen,
                "YKienChuyen": YKienChuyen
            }
            butphe.append(butphe_dict)
        butphelanhdao(butphe)
        updateTrangThai(vanban)
        return {"success": True}
        # return RedirectResponse(url="/hethong/vanbandi", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/hethong/vanbandi/search/{id}", response_class=HTMLResponse)
def searchVBdi(request: Request, id: int, key: str):
    try:
        canbo = get_CanBo(id)
        listVBdi = search_vbdi(key)
        option_trangthaixuly = getTrangThaiXuLyAll()
        return templates.TemplateResponse("vanbandi.html", {"request": request, 
                                                            "canbo": canbo,
                                                            "listVB": listVBdi,
                                                            "option_trangthaixuly": option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/hethong/vanbandi/statistical/{id}/{idTrangThai}")
def thongkeVbDi(request: Request, id: int, idTrangThai: int):
    try:
        canbo = get_CanBo(id)
        listVBdi = statistical_vbdi(idTrangThai)
        option_trangthaixuly = getTrangThaiXuLyAll()
        
        return templates.TemplateResponse("vanbandi.html", {"request": request,
                                                            "canbo": canbo,
                                                            "listVB": listVBdi,
                                                            "option_trangthaixuly": option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/hethong/vanbandi/delete", response_model=dict)
def deleteVbDi(vb: int):
    try:
        deleteVB(vb)

        return deleteVB(vb)
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
      
@app.get("/hethong/vanbandi/insert", response_class=HTMLResponse)
def insertVbDi(request: Request, id: int):
    try:
        canbo = get_CanBo(id)
        option_hinhthuc = getHinhThucAll()
        option_linhvuc = getLinhVucAll()
        option_nguoipheduyet = getCanBoPheDuyetAll()
        option_dokhan = getDoKhanCapAll()
        option_loaivb = getLoaiVanBanAll()
        option_trangthaixuly = getTrangThaiXuLyAll()

        return templates.TemplateResponse("themvanbandi.html", {"request": request,
                                                                "canbo": canbo,
                                                                "option_hinhthuc": option_hinhthuc,
                                                                "option_linhvuc": option_linhvuc,
                                                                "option_nguoipheduyet": option_nguoipheduyet,
                                                                "option_dokhan": option_dokhan,
                                                                "option_loaivb": option_loaivb,
                                                                "option_trangthaixuly": option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/hethong/vanbandi/insert")
async def taomoivanban(
    idNguoiPheDuyet: int = Form(...),
    idHinhThuc: int = Form(...),
    idLinhVuc: int = Form(...),
    idDoKhanCap: int = Form(...),
    idLoaiVanBan: int = Form(...),
    idCanBo: int = Form(...),
    HanXuLy: str = Form(...),
    TrichYeu: str = Form(...),
    SoDen: int = Form(...),
    NgayPhatHanh: str = Form(...),
    SoKyHieu: str = Form(...),
    fileVanBan: UploadFile = File(...),
    TrangThaiXuLy: int = Form(...)
):
    try:
        # # # Lưu file đính kèm vào hệ thống
        file_location = f"{UPLOAD_FOLDER}{fileVanBan.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(fileVanBan.file, file_object)
    

        # Tạo đối tượng VanBan
        vanban = [{
            'idNguoiPheDuyet': idNguoiPheDuyet,
            'idHinhThuc': idHinhThuc,
            'idLinhVuc': idLinhVuc,
            'idDoKhanCap': idDoKhanCap,
            'idLoaiVanBan': idLoaiVanBan,
            'idCanBo': idCanBo,
            'HanXuLy': HanXuLy,
            'TrichYeu': TrichYeu,
            'SoDen': SoDen,
            'NgayPhatHanh': NgayPhatHanh,
            'SoKyHieu': SoKyHieu,
            'LinkFileVanBan': fileVanBan.filename,
            'TrangThaiXuLy': TrangThaiXuLy
        }]

        # Gọi hàm themmoivanban để lưu vào cơ sở dữ liệu
        themmoivanban(vanban)
        return {"success": True}
        # return RedirectResponse(url="/hethong/vanbandi", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
     
@app.get("/hethong/vanbandi/update/{id}/vb{idVanBanDi}")
def updateVbDi(request: Request, id:int, idVanBanDi: int):
    try:
        canbo = get_CanBo(id)
        chitietVB = getItemVanBanDi(idVanBanDi)
        option_hinhthuc = getHinhThucAll()
        option_linhvuc = getLinhVucAll()
        option_nguoipheduyet = getCanBoPheDuyetAll()
        option_dokhan = getDoKhanCapAll()
        option_loaivb = getLoaiVanBanAll()
        option_trangthaixuly = getTrangThaiXuLyAll()

        return templates.TemplateResponse("updatevanbandi.html", {"request": request,
                                                                "canbo": canbo,
                                                                "chitietVB": chitietVB,
                                                                "option_hinhthuc": option_hinhthuc,
                                                                "option_linhvuc": option_linhvuc,
                                                                "option_nguoipheduyet": option_nguoipheduyet,
                                                                "option_dokhan": option_dokhan,
                                                                "option_loaivb": option_loaivb,
                                                                "option_trangthaixuly": option_trangthaixuly})
    
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/hethong/vanbandi/update/{id}/vb{idVanBanDi}")
async def update_van_ban(idVanBanDi: int, request: Request):
    try:
        # Parse the JSON body of the request
        update_data = await request.json()
        # Add the idVanBanDi to the update data
        update_data['idVanBanDi'] = idVanBanDi

        # Call the update function with the parsed data
        capnhatvanban([update_data])
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dowloadfile/{filename}")
async def get_file(filename: str):
    # Return the file for download if it exists
    file_location = f"{UPLOAD_FOLDER}{filename}"
    return FileResponse(path=file_location, filename=filename)


@app.get("/export_excel", response_class=StreamingResponse)
async def export_excel():
    try:
        data = getListVBdi()
        if not data:
            raise HTTPException(status_code=404, detail="No data found")
        
        wb = Workbook()
        ws = wb.active
        
        headers = ["STT", "Nội dung công việc", "Người nhập", "Loại văn bản", "Ngày nhập", "Hạn xử lý", "Trạng thái"]
        ws.append(headers)
        stt = 0
        for item in data:
            stt = stt + 1
            row = [
                stt,
                item["TrichYeu"],
                item["TenNguoiNhap"],
                item["TenLoaiVanBan"],
                item["NgayPhatHanh"],
                item["HanXuLy"],
                item["TenTrangThai"]
            ]
            ws.append(row)
        
        stream = io.BytesIO()
        wb.save(stream)
        stream.seek(0)
        
        response = StreamingResponse(stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = "attachment; filename=danhsachvb.xlsx"
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#văn bản đến
@app.get("/hethong/vanbanden", response_class=HTMLResponse)
def vanbanden(request: Request, id: int ,page: int = 1, page_size: int = 10):
    try:
        canbo = get_CanBo(id)
        listVBdi, totalPage = getListVBden(page, page_size)
        option_trangthaixuly = getTrangThaiXuLyAll()
        return templates.TemplateResponse("vanbanden.html", {"request": request, 
                                                             "index_page": page, 
                                                             "totalpage": totalPage, 
                                                             "canbo": canbo,
                                                             "listVB": listVBdi,
                                                             "option_trangthaixuly": option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/hethong/vanbanden/search/{id}", response_class=HTMLResponse)
def searchVBden(request: Request, id: int, key: str, page: int = 1, page_size: int = 10):
    try:
        canbo = get_CanBo(id)
        listVBdi, totalPage = search_vbden(key, page, page_size)

        return templates.TemplateResponse("vanbanden.html", {"request": request, 
                                                            "index_page": page, 
                                                            "totalpage": totalPage, 
                                                            "canbo": canbo,
                                                            "listVB": listVBdi})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    


@app.get("/hethong/vanbanden/statistical/{id}/{idTrangThai}")
def thongkeVbDen(request: Request, id: int, idTrangThai: int, page: int = 1, page_size: int = 10):
    try:
        canbo = get_CanBo(id)
        listVBden, totalPage = statistical_vbden(idTrangThai, page, page_size)
        option_trangthaixuly = getTrangThaiXuLyAll()
        
        return templates.TemplateResponse("vanbanden.html", {"request": request, 
                                                            "index_page": page, 
                                                            "totalpage": totalPage, 
                                                            "canbo": canbo,
                                                            "listVB": listVBden,
                                                            "option_trangthaixuly":option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
    

@app.delete("/hethong/vanbanden/delete/id={idVanBanDen}", response_model=dict)
def deleteVbDen(idVanBanDen: int, page: int = 1, page_size: int = 10):
    try:
        deleteVBDen(idVanBanDen)

        return deleteVBDen(idVanBanDen, page, page_size)
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/hethong/vanbanden/insertTTVB", response_class=HTMLResponse)
def insertVbDen(request: Request, id: int):
    try:
        canbo = get_CanBo(id)
        option_hinhthuc = getHinhThucAll()
        option_linhvuc = getLinhVucAll()
        option_tinhchatvanban = getTinhChatVanBanAll()
        option_nguoiduyet = getCanBoPheDuyetAll()              
        option_loaivb = getLoaiVanBanAll()       
        option_trangthaixuly = getTrangThaiXuLyAll()
        option_dokhan = getDoKhanCapAll()
        option_khoa = getKhoaAll()
        return templates.TemplateResponse("themmoivanbanden.html",{"request": request,
                                                                "canbo": canbo,
                                                                "option_khoa":option_khoa,
                                                                "option_hinhthuc": option_hinhthuc,
                                                                "option_linhvuc": option_linhvuc,
                                                                "option_tinhchatvanban" : option_tinhchatvanban,
                                                                "option_nguoiduyet":option_nguoiduyet,
                                                                "option_dokhan": option_dokhan,
                                                                "option_loaivb": option_loaivb,
                                                                "option_trangthaixuly": option_trangthaixuly})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/hethong/vanbanden/insert")
async def taomoivanban(
    TrichYeu: str = Form(...),
    idHinhThuc: int = Form(...),
    DonViBanHanh: str = Form(...),
    SoDen: int = Form(...),
    idLinhVuc: int = Form(...),
    idTinhChatVanBan: int = Form(...),
    idKhoa: int = Form(...),
    NgayDen: str = Form(...),
    NgayBanHanh: str = Form(...),
    SoKyHieu: str = Form(...),
    idCanBoDuyet: int = Form(...),
    idDoKhanCap: int = Form(...),
    idLoaiVanBan: int = Form(...),
    idNguoiNhap: int = Form(...),
    needAnswer: str = Form(...),
    needHandle: str = Form(...),
    HanTraLoi: str = Form(...),
    SoNgay: int = Form(...),
    idTrangThaiVanBan: int = Form(...),
    fileVanBan: UploadFile = File(...)
):
    try:
        file_location = f"{UPLOAD_FOLDER}{fileVanBan.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(fileVanBan.file, file_object)
        
        vanbanden = [{
            'TrichYeu': TrichYeu,
            'idHinhThuc': idHinhThuc,
            'DonViBanHanh': DonViBanHanh,
            'SoDen': SoDen,
            'idLinhVuc': idLinhVuc,
            'idTinhChatVanBan': idTinhChatVanBan,
            'idKhoa': idKhoa,
            'NgayDen': NgayDen,
            'NgayBanHanh': NgayBanHanh,
            'SoKyHieu': SoKyHieu,
            'idCanBoDuyet': idCanBoDuyet,
            'idDoKhanCap': idDoKhanCap,
            'idLoaiVanBan': idLoaiVanBan,
            'idNguoiNhap': idNguoiNhap,
            'needAnswer': needAnswer,
            'needHandle': needHandle,
            'HanTraLoi': HanTraLoi,
            'SoNgay': SoNgay,
            'idTrangThaiVanBan': idTrangThaiVanBan,
            'LinkFileVanBan': fileVanBan.filename
        }]

        themmoivanbanden(vanbanden)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/hethong/vanbanden/update/{id}/vb{idVanBanDen}")
def updateVbDen(request: Request, id:int, idVanBanDen: int):
    try:
        canbo = get_CanBo(id)
        chitietVbDen = getChiTietVbDen(idVanBanDen)
        option_hinhthuc = getHinhThucAll()
        option_linhvuc = getLinhVucAll()
        option_tinhchatvanban = getTinhChatVanBanAll()
        option_nguoiduyet = getCanBoPheDuyetAll()              
        option_loaivb = getLoaiVanBanAll()       
        option_trangthaixuly = getTrangThaiXuLyAll()
        option_dokhan = getDoKhanCapAll()
        option_khoa = getKhoaAll()

        return templates.TemplateResponse("updatevanbanden.html",{"request": request,
                                                                "canbo": canbo,
                                                                "chitietVbDen":chitietVbDen,
                                                                "option_khoa":option_khoa,
                                                                "option_hinhthuc": option_hinhthuc,
                                                                "option_linhvuc": option_linhvuc,
                                                                "option_tinhchatvanban" : option_tinhchatvanban,
                                                                "option_nguoiduyet":option_nguoiduyet,
                                                                "option_dokhan": option_dokhan,
                                                                "option_loaivb": option_loaivb,
                                                                "option_trangthaixuly": option_trangthaixuly})
    
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
@app.put("/hethong/vanbanden/update/{id}/vb{idVanBanDen}")
async def update_van_banden(
    TrichYeu: str = Form(...),
    idHinhThuc: int = Form(...),
    DonViBanHanh: str = Form(...),
    SoDen: int = Form(...),
    idLinhVuc: int = Form(...),
    idTinhChatVanBan: int = Form(...),
    idKhoa: int = Form(...),
    NgayDen: str = Form(...),
    NgayBanHanh: str = Form(...),
    SoKyHieu: str = Form(...),
    idCanBoDuyet: int = Form(...),
    idDoKhanCap: int = Form(...),
    idLoaiVanBan: int = Form(...),
    idNguoiNhap: int = Form(...),
    needAnswer: str = Form(...),
    needHandle: str = Form(...),
    HanTraLoi: str = Form(...),
    SoNgay: int = Form(...),
    idTrangThaiVanBan: int = Form(...),
    idVanBanDenn: int = Form(...),
    fileVanBan: str = Form(...),
    linkFileVanBan: Optional[UploadFile] = None
):
    try:
        if linkFileVanBan is not None:
            file_location = f"{UPLOAD_FOLDER}{linkFileVanBan.filename}"
            with open(file_location, "wb+") as file_object:
                shutil.copyfileobj(linkFileVanBan.file, file_object)
            file = linkFileVanBan.filename
        else:
            file = fileVanBan
    
        vanbanden = [{
            'TrichYeu': TrichYeu,
            'idHinhThuc': idHinhThuc,
            'DonViBanHanh': DonViBanHanh,
            'SoDen': SoDen,
            'idLinhVuc': idLinhVuc,
            'idTinhChatVanBan': idTinhChatVanBan,
            'idKhoa': idKhoa,
            'NgayDen': NgayDen,
            'NgayBanHanh': NgayBanHanh,
            'SoKyHieu': SoKyHieu,
            'idCanBoDuyet': idCanBoDuyet,
            'idDoKhanCap': idDoKhanCap,
            'idLoaiVanBan': idLoaiVanBan,
            'idNguoiNhap': idNguoiNhap,
            'needAnswer': needAnswer,
            'needHandle': needHandle,
            'HanTraLoi': HanTraLoi,
            'SoNgay': SoNgay,
            'idTrangThaiVanBan': idTrangThaiVanBan,
            'LinkFileVanBan': file,
            'idVanBanDenn' :idVanBanDenn
        }]

        capnhatvanbanden(vanbanden)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/hethong/vanbanden/chitiet/{id}/vb{idVanBanDen}")
def chitietVbden(request: Request, id:int, idVanBanDen: int):
    try:
        canbo = get_CanBo(id)
        chitietVbDen = getChiTietVbDen(idVanBanDen)
        butpheVBden = getButPheVBDen(idVanBanDen)
        option_lanhdao = getCanBoPheDuyetAll()
        return templates.TemplateResponse("chitietVBden.html",{"request": request,
                                                                "canbo": canbo,
                                                                "chitietVbDen":chitietVbDen,
                                                                "butpheVBden":butpheVBden,
                                                                "option_lanhdao":option_lanhdao})
    
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/hethong/vanbanden/chuyenpheduyet")
def chuyenpheduyetVbDen(
    idVanBanDen: int = Form(...),
    idNguoiChuyen: int = Form(...),
    idNguoiNhan: int = Form(...),
    ThoiGianChuyen: str = Form(...),
    YKienChuyen: Optional[str] = Form(None)
):
    try:
        if YKienChuyen is None:
            YKienChuyen = ""
        # Tạo đối tượng VanBan
        vanbanden = [{
            "idVanBanDen": idVanBanDen,
            "idNguoiChuyen": idNguoiChuyen,
            "idNguoiNhan": idNguoiNhan,
            "ThoiGianChuyen": ThoiGianChuyen,
            "YKienChuyen": YKienChuyen
        }]
       

        # Gọi hàm themmoivanban để lưu vào cơ sở dữ liệu
        butphelanhdaoVbDen(vanbanden)
        return {"success": True}
        # return RedirectResponse(url="/hethong/vanbandi", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




pdfmetrics.registerFont(TTFont('TimesNewRoman', 'static/font/TimesNewRoman.ttf'))

# Định nghĩa lớp cho dữ liệu đầu vào
class FormDataModel(BaseModel):
    trich_yeu: str
    lanh_dao_phe_duyet: str
    so_ky_hieu: str
    so_den: int
    loai_van_ban: str
    ngay_ban_hanh: Optional[str] = None
    han_xu_ly: Optional[str] = None
    linh_vuc: str
    do_khan: str
    filename: str 


    @validator('ngay_ban_hanh', 'han_xu_ly')
    def validate_date_format(cls, v):
        if v is not None:
            try:
                datetime.strptime(v, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Ngày tháng không hợp lệ. Định dạng phải là 'DD/MM/YYYY'")
        return v

# Định nghĩa API endpoint để xuất PDF
@app.post("/export_pdf")
async def export_pdf(formData: FormDataModel):
    try:
        # Trích xuất dữ liệu từ FormDataModel
        trich_yeu = formData.trich_yeu
        lanh_dao_phe_duyet = formData.lanh_dao_phe_duyet
        so_ky_hieu = formData.so_ky_hieu
        so_den = formData.so_den
        loai_van_ban = formData.loai_van_ban
        ngay_ban_hanh = formData.ngay_ban_hanh
        han_xu_ly = formData.han_xu_ly
        linh_vuc = formData.linh_vuc
        do_khan = formData.do_khan

        filename = formData.filename


        # Tạo một stream byte để lưu file PDF
        stream = io.BytesIO()


        # Tạo một canvas PDF
        c = canvas.Canvas(stream, pagesize=letter)
        c.setTitle(filename)
        c.setFont("TimesNewRoman", 20)  
        # Đo chiều rộng của trang để căn giữa
        width, _ = letter
        # Đo chiều rộng của chuỗi "Trích yếu"
        text_width = c.stringWidth("{}".format(trich_yeu))
        # Tính toán vị trí x để căn giữa tiêu đề
        x_pos = (width - text_width) / 2
        c.drawString(x_pos, 750, "{}".format(trich_yeu))


        c.setFont("TimesNewRoman", 13)  

        c.drawString(50, 730, "Lãnh đạo phê duyệt: {}".format(lanh_dao_phe_duyet))
        c.drawString(50, 710, "Số / Ký hiệu: {}".format(so_ky_hieu))
        c.drawString(50, 690, "Số đến: {}".format(so_den))
        c.drawString(50, 670, "Loại văn bản: {}".format(loai_van_ban))
        if ngay_ban_hanh:
            c.drawString(50, 650, "Ngày ban hành: {}".format(ngay_ban_hanh))
        if han_xu_ly:
            c.drawString(50, 630, "Hạn xử lý: {}".format(han_xu_ly))
        c.drawString(50, 610, "Lĩnh vực: {}".format(linh_vuc))
        c.drawString(50, 590, "Cấp độ khẩn: {}".format(do_khan))


        # Lưu canvas và đóng file PDF
        c.save()
        stream.seek(0)

        # Tạo một StreamingResponse và trả về
        # response = StreamingResponse(stream, media_type="application/pdf")
        # filename = f"document_{trich_yeu}.pdf"
        # response.headers["Content-Disposition"] = "attachment; filename={filename}"

        # Làm sạch tên tệp
        filename = re.sub(r'[^\w\s-]', '', filename).strip().replace(' ', '_')
        filename = f"document_{filename}.pdf"
        encoded_filename = urllib.parse.quote(filename, safe='')

        # Tạo một StreamingResponse và trả về
        headers = {
            "Content-Disposition": f"attachment; filename*=UTF-8''{encoded_filename}"
        }

        # Tạo một StreamingResponse và trả về
        response = StreamingResponse(stream, media_type="application/pdf", headers=headers)


        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))