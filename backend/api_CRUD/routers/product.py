from fastapi import FastAPI, APIRouter, status, HTTPException, Path
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Union,Optional, List
from typing_extensions import Annotated
import os


# === App & Router === 
#app = FastAPI()
#router = APIRouter(prefix="/products",tags=["products"], responses={404: {"Message": "Not Found, sorry"}})
router = APIRouter()

#=== Root Data Base Products OS ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data_api", "fashion_products.csv")
df = pd.read_csv(file_path)

# Limpieza de valores NaN o infinitos
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# ==== POO Instance Class ====
class Product(BaseModel):
  user_id: Union[int, None] = Field(..., gt=0)
  product_id: Union[int, None] = Field(..., gt=0)
  product_name: Union[str, None] = Field(description="Name of Product")
  brand: Union[str, None] = Field(title="Name of Brand", description="Name of the Brand at product")
  category: Union[str, None] = Field(min_length=1, max_length=25)
  price: Union[int, None] = Field(gt=0, title="Prices Product", description="Prices of the Products")
  rating: Union[float, None] = Field(title="Rating of Product", description="Value of Client for Product")
  color: Union[str, None] = Field(title="Color of Product")
  size: Union[int,None] = Field(title="Size of Product", description="Size of Product")
  
  #=== Decorator Pydantic - Conversion ===#
  @validator("size", pre=True, always=True)
  def parse_size(cls, value):
    if value is None: 
      return None
    if isinstance(value, int):
      return value
    try: 
      return int(value)
    except ValueError:
      return None

#===#
""" df = df.rename(columns={"Size": "size"}) """

#Asegúrate de que las columnas del DataFrame coincidan con los campos del modelo
columns_data = ["User ID","Product ID","Product Name","Brand","Category","Price","Rating","Color","Size"] 

if not set(columns_data).issubset(df.columns):
  raise ValueError("Las columnas del DataFrame no coinciden con el modelo Pydantic")

# Ajusta los nombres de las columnas para que coincidan con los nombres de los campos en el modelo Pydantic
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

""" # Mapea los nombres de las columnas del DataFrame a los nombres de los campos en el modelo Pydantic
column_mapping = {
    "User ID": "user_id",
    "Product ID": "product_id",
    "Product Name": "product_name",
    "Brand": "brand",
    "Category": "category",
    "Price": "price",
    "Rating": "rating",
    "Color": "color",
    "Size": "size",
}

# Renombra las columnas del DataFrame según el mapeo
df = df.rename(columns=column_mapping) """

#Crea instancias del modelo Pydantic para cada fila del DataFrame y valida los datos & valor a dos decimales.
def create_product_instance(row_data):
  '''
  parse_size es un método y se debe llamar con paréntesis, no corchetes.
  '''
  # Redondea el valor del campo 'rating' a dos decimales
  row_data["rating"] = round(row_data["rating"], 2)
  # Usa el validador para el campo 'size'
  row_data["size"] = Product.parse_size(row_data["size"])
  
  return Product(**row_data)

product_validate = [] 
products_invalidate = []

#Ciclo para iterar en la lista de productos e comprobar e agregar. 
for _, row_data in df.iterrows():
  try: 
    product_instance = create_product_instance(row_data)
    product_validate.append(product_instance)
  except Exception as e: 
    products_invalidate.append({"error": str(e), "data": dict(row_data)})


# Puedes trabajar con los productos válidos e inválidos según tus necesidades
""" print("Products_Validates", product_validate) """

#=== API ROOT REST CRUD ===
@router.get("/", status_code=status.HTTP_200_OK, tags=["products"])
async def product(): 
  product_data = {"products": df.head(5).to_dict(orient="records")}
  #return {"products": df.head(10).to_dict(orient="records")}
  try: 
    if product_data: 
      return product_data
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products Not Found")
  except ValidationError as ve: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Validation Error: {ve.json()}")
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error..., {str(e)}")
  
#===Path Parameters===
@router.get("/{id}",response_model=Product, status_code=status.HTTP_200_OK, tags=["products"])
async def get_id(id: int = Path(..., title="Get ID User", description="Get ID User of Products")):
  '''
  response_model=Product para indicar a FastAPI que el resultado debe seguir la estructura definida en tu modelo Pydantic Product.
  '''
  #product_id = next((product for product in df.to_dict(orient="records") if product["user_id"] == id), None)
  product_id = df[df["user_id"] == id].to_dict(orient="records")
  if product_id:
    product_instance = create_product_instance(product_id[0])
    return product_instance
    #return Product(**product_id[0])
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID Not Found") 
  

#===Query Parameters===