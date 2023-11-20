########## 
# Fast API & Uvicorn 
#! Siempre que llamamos a un Servidor tiene que ser Asíncrona 
#* Use: /home/?query_param=Home
######### 
from fastapi import FastAPI
#from fastapi.responses import HTMLResponse

app = FastAPI()
#Root
@app.get("/")
async def root():
  return {"message": "Hello World"}
#HomePage - Type Hints
@app.get("/home/") 
async def root_home(query_param: str = None):
  return {"query_param": query_param}