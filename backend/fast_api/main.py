##########
#*1) 
######### 
from fastapi import FastAPI
from routers.products import router as product_router
from routers.user import router as user_router
from fastapi.staticfiles import StaticFiles
#from fastapi.responses import HTMLResponse

# === APP ===
app = FastAPI()
#router = products.router

#Router from Products (Reference)
app.include_router(product_router)
app.include_router(user_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

#GET => Root
# === Principal Root ===
@app.get("/", status_code=200)
async def root():
  return {"message": str("Hello, Users!!")}

#Get => HomePage - Type Hints
""" @app.get("/home/") 
async def root_home(query_param: str = None):
  return {"query_param": query_param} """
