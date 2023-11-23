####
#*3)
###
from fastapi import APIRouter,FastAPI
from pydantic import BaseModel

##=== POO ===
class Product(BaseModel):
  id: int 
  name: str
  price: int

## List Products
products_list = [Product(id=1, name="MacBook", price=25000)]

#=== Fast & Router
app = FastAPI()
router = APIRouter()

# === Call Products ===
@router.get("/product/")
async def get_product(): 
  return products_list


## ==== Include ====
app.include_router(router)