##########
#*1) 
#TODO Fast API & Uvicorn 
#TODO Siempre que llamamos a un Servidor tiene que ser Asíncrona 
#TODO Use: /home/?query_param=Home
######### 
from fastapi import FastAPI
from routers.products import router as product_router
#from fastapi.responses import HTMLResponse

# === APP ===
app = FastAPI()
#router = products.router

#Router from Products
app.include_router(product_router)

#GET => Root
@app.get("/", status_code=200)
async def root():
  return {"message": str("Hello, Users!!")}

#Get => HomePage - Type Hints
@app.get("/home/") 
async def root_home(query_param: str = None):
  return {"query_param": query_param}
