##########
#*1) 
#TODO Fast API & Uvicorn 
#TODO Siempre que llamamos a un Servidor tiene que ser Asíncrona 
#TODO Use: /home/?query_param=Home
#?Static: Para todo tipo de assets. (http://127.0.0.1:8000/static/images/astronauta_nave.jpg).Cuando tienes muchos archivos (imágenes) y vas a usar StaticFiles, es importante tener en cuenta el rendimiento. El StaticFiles de FastAPI está diseñado para ser eficiente con archivos pequeños, pero puede ser menos eficiente con archivos grandes. Puedes usar un CDN (Cloudinary).
#*OAuth 2.0 es un protocolo de autorización que permite a los usuarios autorizar a aplicaciones de terceros a acceder a sus datos sin tener que compartir sus credenciales de inicio de sesión.OAuth 2.0 funciona mediante la creación de un flujo de autorización en el que el usuario autoriza a la aplicación de terceros a acceder a sus datos.
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
