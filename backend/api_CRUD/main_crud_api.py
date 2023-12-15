from fastapi import FastAPI, status
from routers.product import router as product_router


#=== App ===
app = FastAPI()
app.title = "API REST & CRUD with FastAPI"
app.version = "0.0.1"

#=== Add Routes ===
app.include_router(product_router)


# === REST & CRUD ===
@app.get("/", status_code=status.HTTP_200_OK, tags=["home"])
async def root(): 
  return {"message": str("Hello, User. Welcome at Home")}