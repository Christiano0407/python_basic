##########
#*1) 
#TODO Fast API & Uvicorn 
#TODO Siempre que llamamos a un Servidor tiene que ser Asíncrona 
#TODO Use: /home/?query_param=Home
######### 
from fastapi import FastAPI
from routers import get_product
#from fastapi.responses import HTMLResponse

# === APP ===
app = FastAPI()


#Router from Products
app.include_router(get_product.routers)

#GET => Root
@app.get("/")
async def root():
  return {"message": "Hello World"}

#Get => HomePage - Type Hints
@app.get("/home/") 
async def root_home(query_param: str = None):
  return {"query_param": query_param}