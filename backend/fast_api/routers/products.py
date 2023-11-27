#######
#*3)
#TODO: @app.get("/") define una ruta en la raíz de tu aplicación. async def read_csv(): es la función que se ejecutará cuando se realice una solicitud GET a la ruta especificada. return {"data": df.head(5).to_dict(orient="records")} devuelve las primeras 5 filas del DataFrame df como un diccionario JSON.
#TODO: En el contexto de la función to_dict de pandas, el parámetro orient especifica el formato en el que se devolverá el diccionario. El valor "records" significa que los datos se representarán como una lista de registros, donde cada registro es un diccionario que contiene los datos de una fila del DataFrame.
#* OS: Path => System Operator
#? Prefixed => Ya no es necesario poner todo el "output".
#? Tags => Dividir por parámetros la documentación (API) y ("path operations in this router").
#######
from fastapi import APIRouter,FastAPI, HTTPException
from pydantic import BaseModel
import os 
import pandas as pd

##=== POO ===
class Product(BaseModel):
  id: int 
  name: str
  price: int

## List Products
#products_list = [Product(id=1, name="MacBook", price=25000)]

# === Fast & Router ===
app = FastAPI()
router = APIRouter(prefix="/products", tags=["products"], responses={404: {"Message": "Not Found, sorry"}}) #prefix="/products"
# === Leer el archivo CSV (Excel) al cargar la aplicación ===
#df = pd.read_csv("./data_products/fashion_products.csv")
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data_products", "fashion_products.csv")
df = pd.read_csv(file_path)

# === Call Products ===
""" @router.get("/products/", status_code=200)
async def product(): 
  return products_list """

@router.get("/", status_code=200)
async def products(): 
  return {"products": df.head(5).to_dict(orient="records")}

#Path Parameters
@router.get("/{id}")
async def products(id: int):
  '''
  En este código, he utilizado next junto con una expresión generadora para encontrar el primer producto con el ID correspondiente. Si no se encuentra ningún producto con ese ID, se lanza una HTTPException con un código de estado 404.
  Ajustamos el nombre de la columna según tu DataFrame
  '''
  name_id = "Product ID"
  #return {"products": df.head(5).to_dict(orient="records")}
  product_id = next((product for product in df.to_dict(orient="records") if product[name_id] == id), None)
  if product_id: 
    return {"product": product_id}
  else: 
    raise HTTPException(status_code=404, detail="Sorry! Your product with the ID {id} it's not found or Not exist.")
  

@router.get("/",status_code=200)
async def product_brand(id:int, name: str, brand: str):
  id_product = "Product ID"
  product_name = "Product Name"
  brands = "Brand"

  products_brands = next((p for p in df.to_dict(orient="records") if p[id_product] == id and p[product_name].lower() == name.lower and p[brands].lower() == brand.lower()), None)
  try: 
    if products_brands: 
      return {"products_brands": products_brands}#__dict__
    else: 
      raise HTTPException(status_code=404, detail="Sorry, These products not founds.")
  except: 
    return {"error:" "Add your search product."}

#Query Parameters

## ==== Include ====
app.include_router(router)