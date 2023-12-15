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