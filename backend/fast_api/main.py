#####
#Fast API & Uvicorn
####
from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def get_list():
  lst:[str] = list([2,4,7])
  return f"My list: {lst}"