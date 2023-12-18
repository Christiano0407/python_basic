from fastapi import FastAPI, APIRouter, status, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
from typing import Union,Optional, List
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
  category: Union[str, None] = Field(min_length=1, max_length=15)
  price: Union[int, None] = Field(gt=0, title="Prices Product", description="Prices of the Products")
  rating: Union[int, None] = Field(min_length=0, max_length=10, title="Rating of Product", description="Value of Client for Product")
  color: [str, None] = Field(title="Color of Product")
  size: [str, Union] = Field(title="Size of Product", description="Size of Product")


#Asegúrate de que las columnas del DataFrame coincidan con los campos del modelo
columns_data = ["user_id", "product_id", "product_name", "brand", "category", "price", "rating", "color", "size"] 
if not set(columns_data).issubset(df):
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sorry, your Data it's not found.")

#Crea instancias del modelo Pydantic para cada fila del DataFrame y valida los datos
def create_product_instance(row_data):
  data_product = dict(row_data)
  return Product(**data_product)

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
print("Products_Validates", product_validate)

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
  except ValueError as ve: 
    raise  HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(ve)}")
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error..., {str(e)}")