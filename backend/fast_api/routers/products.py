####
#*3)
#TODO: @app.get("/") define una ruta en la raíz de tu aplicación. async def read_csv(): es la función que se ejecutará cuando se realice una solicitud GET a la ruta especificada. return {"data": df.head(5).to_dict(orient="records")} devuelve las primeras 5 filas del DataFrame df como un diccionario JSON.
#TODO: En el contexto de la función to_dict de pandas, el parámetro orient especifica el formato en el que se devolverá el diccionario. El valor "records" significa que los datos se representarán como una lista de registros, donde cada registro es un diccionario que contiene los datos de una fila del DataFrame.
###
from fastapi import APIRouter,FastAPI
from pydantic import BaseModel
import pandas as pd

##=== POO ===
class Product(BaseModel):
  id: int 
  name: str
  price: int

## List Products
products_list = [Product(id=1, name="MacBook", price=25000)]

# === Fast & Router ===
app = FastAPI()
router = APIRouter()
# === Leer el archivo CSV (Excel) al cargar la aplicación ===
df = pd.read_csv("./data_products/fashion_products.csv")

# === Call Products ===
@router.get("/products/")
async def product(): 
  return products_list

@router.get("/data/")
async def data(): 
  return {"data": df.head(4).to_dict(orient="records")}


## ==== Include ====
app.include_router(router)