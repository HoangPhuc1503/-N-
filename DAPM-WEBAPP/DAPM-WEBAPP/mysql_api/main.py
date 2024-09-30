from fastapi import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/hethong", response_class=HTMLResponse)
def newVBDen(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
        
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