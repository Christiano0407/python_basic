#======================#
#* Create My First API  with Framework fastApi, With Server Uvicorn and Insomnia (CRUD)
#TODO Used: POO for API CRUD
#=====================#
from fastapi import FastAPI
from pydantic import BaseModel
# === POO (Instancia y Entidad del Objeto) ===
#A)
class User(BaseModel):
  name: str
  url: str 
  age: int


#B)
""" class User:
  def __init__(self, name, url):
    self.name = name
    self.url = url

  def __repr__(self) -> str:
    return f"User name: {self.name} and his url: {self.url}" """


# ==== App Web Server with FastAPI ====
app = FastAPI()

#GET 
@app.get("/")
async def root():
  return {"message": str("Hello Users")}

@app.get("/usersClass/")
async def usersClass():
  user_instance = User(name="Mouredev", url="http://mouredev.dev", age=35)
  return user_instance

#POST
@app.post("/users/")
async def create_users(user: User):
  return user

#B)
""" @app.get("/users")
async def get_users():
  users = [
    User("MoureDev", "http://moure.dev"),
    User("MiduDev", "http://midudev.dev")
  ]
  return users """
#Post
""" @app.post("/users")
async def create_users(user: User):
  return user """
#Type Hints
""" @app.get("/usersjson/")
async def usersjson():
  return [{"name": "MoureDev","language": "Kotlin" ,"url": "http://moure.dev","message": str("Hello, Users loved code with Kotlin.")},
           {"name": "MiduDev","language": "Javascript","url": "http://midudev.dev","message": str("Hello, I loved Javascript.")},
           {"name": "Fazt","language": "Rust" ,"url": "http://fazt.dev","message": str("I loved Backend Programming")},
           {"name": "Oscar","language": "Python","url": "http://oscar.dev","message": str("I love Python.")}
          ] """