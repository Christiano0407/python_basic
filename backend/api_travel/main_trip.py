from fastapi import FastAPI, status
from routers.travel import router as travel_router


#*=== App ===
app = FastAPI()
app.title  = "API REST & CRUD with FastAPI"
app.version = "0.0.1"


#* ==== Add Router ==== 
app.include_router(travel_router, prefix="/travels", tags=["travels"])

#? ===== REST & CRUD =====
@app.get("/", status_code=status.HTTP_200_OK, tags=["home"])
async def home(): 
  return {"message": str("Hello! Welcome at Home. Enjoy To Travel")}