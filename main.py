## Request API FastAPI ##
from fastapi import FastAPI


# App Server #
app = FastAPI()

@app.get('/')
def get_home():
  return [4, 5, 7, 10]