from fastapi import APIRouter, status, HTTPException, Path, Query
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Union,Optional, List
from typing_extensions import Annotated
import os
import pandas as pd
import numpy as np


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
  price: Union[float, None] = Field(gt=0, title="Prices Product", description="Prices of the Products")
  rating: Union[float, None] = Field(title="Rating of Product", description="Value of Client for Product")
  color: Union[str, None] = Field(title="Color of Product")
  size: Union[int,None] = Field(title="Size of Product", description="Size of Product")

  @staticmethod #@classmethod
  def parse_size(value):
      try:
          if value is None or pd.isna(value): 
            return {"value": None, "error": None}
          
          if value.isdigit():
             size_value = int(value)
             if size_value < 0: 
               raise ValueError("Size should be positive integer")
             return {"value": size_value, "error": None }
          else:
            return {"value": None, "error": "Size should be a valid integer"}
      except (ValueError, TypeError) as e:
        return {"value": None, "error": {str(e)}}



#Asegúrate de que las columnas del DataFrame coincidan con los campos del modelo
columns_data = ["User ID","Product ID","Product Name","Brand","Category","Price","Rating","Color","Size"] 

if not set(columns_data).issubset(df.columns):
  raise ValueError("Las columnas del DataFrame no coinciden con el modelo de Base de Datos y Pydantic.")

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
  try:
      # Redondea el valor del campo 'rating' a dos decimales
      row_data["rating"] = round(row_data["rating"], 2)

      # Usa el validador para el campo 'size'
      size_info = Product.parse_size(row_data["size"])

      # Si hay un error, establece el tamaño en un valor predeterminado (por ejemplo, -1)
      if size_info["error"]:
          row_data["size"] = -1
      else:
          row_data["size"] = size_info["value"]

      return Product(**row_data)
  except (ValidationError, ValueError) as e:
      raise ValueError(f"Error creating product instance: {str(e)}")
  


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
  product_data = {"products": df.head(10).to_dict(orient="records")}
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
async def get_id(id: int = Path(...,title="Get ID User", description="Get ID User of Products")):
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


@router.get("/brand/{brand}",response_model=Product, status_code=status.HTTP_200_OK, tags=["products"])
async def get_brand(brand: str = Path(title="Products Brand", description="Get Brand")): 

  product_brand = df[df["brand"] == brand].to_dict(orient="records")
  
  if product_brand:
        try:
            product_instance = create_product_instance(product_brand[0])
            return product_instance
        except ValueError as ve:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Validation Error: {str(ve)}")
  else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Your Brand it's not found")


#===Query Parameters===
@router.get("/product/", response_class=Product, status_code=status.HTTP_200_OK, tags=["products"])
async def get_product(product_name: Annotated[Union[str, None], Query(...,title="Products Name", max_length=50)], price: Annotated[Union[float, None], Query(...,title="Price of Products")]):
   '''
   endpoint:http://127.0.0.1:8000/products/?product_name=Dress&price=40
   '''
   try: 
      parameters_product = next
      (
          ( 
            product for product in df.to_dict(orient="records") if
              product["product_name"].lower() == product_name.lower() and 
              product["price"] == price
          ),
          None
      )
   
      if parameters_product:
         product_instance = create_product_instance(parameters_product)
         return product_instance
      else: 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Your product and price it's not found.")
   except Exception as e:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error...{str(e)}")
   

#=== PUT === 
   

#=== POST / Endpoint para agregar nuevos productos ===
@router.post("/products/", response_class=Product, status_code=status.HTTP_200_OK, tags=["products"])
async def post_product(product:Product):
   
   try:
      # Validar el producto con Pydantic
      product_dict = product.dict()
      print("Received Products:", product_dict)
      validate_product = Product(**product_dict)
      print("validated product: ", validate_product.dict())

      # Asegúrate de que el ID del producto no exista ya en la base de datos
      if df[df["product_id"] == product.product_id].empty: 
        # Agregar el nuevo producto al DataFrame
         df = df.append(product_dict, ignore_index=True)
        # Guardar el DataFrame de vuelta al archivo CSV (o tu base de datos externa)
         df.to_csv(file_path, index=False)
        # Devolver el nuevo producto creado
         return validate_product
      else:
          raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Product ID already exists.")
   except ValidationError as ve:
        print("Validation Error:", ve.errors())
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Validation Error: {ve.errors()}")
   except Exception as e:
        print("Internal Server Error:", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error...{str(e)}")

#=== Delete ===