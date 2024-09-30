from fastapi import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from getData import *
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/test")
def test(page: int = 1, page_size: int = 5):
    list,totalPage = getListVBdi(page, page_size)
    return list

@app.get("/hethong", response_class=HTMLResponse)
def hethong(request: Request, page: int = 1, page_size: int = 5):
    try:
        listVBdi,totalPage = getListVBdi(page, page_size)


        return templates.TemplateResponse("index.html", {"request": request, "index_page": page, "listVB": listVBdi})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/thongtincanhan", response_class=HTMLResponse)
def thongtincanhan(request: Request):
    try:
        return templates.TemplateResponse("thongtincanhan.html", {"request": request})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
@app.get("/themmoivanbanden", response_class=HTMLResponse)
def themmoivanbanden(request: Request):
    try:
        return templates.TemplateResponse("themmoivanbanden.html", {"request": request})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    
    



@app.get("/dangnhap", response_class=HTMLResponse)
def dangnhap(request: Request):
    try:
        return templates.TemplateResponse("login.html", {"request": request})
        
    except Exception as e:
        # Nếu có bất kỳ lỗi nào xảy ra, ném một HTTPException với mã lỗi 500 và chi tiết lỗi
        raise HTTPException(status_code=500, detail=str(e))
    


@app.get("/checklogin")
def test(tenDN: str, mK: str):
    user_info = get_TkMkCB(tenDN, mK)
    if not user_info:  # Kiểm tra xem danh sách có rỗng không
        # Nếu danh sách rỗng, trả về thông báo
       return RedirectResponse("/dangnhap")
    else:
        # Nếu danh sách không rỗng, chuyển hướng đến trang thongtincanhan
        return RedirectResponse("/thongtincanhan")


