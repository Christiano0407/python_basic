from fastapi import FastAPI, APIRouter, status
import os
import pandas as pd

# === App & Router === 
app = FastAPI()
router = APIRouter( prefix="/products",tags=["products"], responses={{"Message": str("Not Found, sorry")}})

#=== Root Data Base Products OS ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data_api", "amazon_laptop_prices_v01.csv")
df = pd.read_csv(file_path)


#=== API ROOT REST CRUD ===
@router.get("/", status_code=status.HTTP_200_OK, tags=["products"])
async def product(): 
  return {"products": df.head(10).to_dict(orient="records")}