from fastapi import FastAPI, status


#=== App ===
app = FastAPI()
app.title = "API REST & CRUD with FastAPI"
app.version = "0.0.1"

#=== Add Routes ===


# === REST & CRUD ===
@app.get("/", status_code=status.HTTP_200_OK, tags=["home"])
async def root(): 
  return {"message": str("Hello, User. Welcome at Home")}