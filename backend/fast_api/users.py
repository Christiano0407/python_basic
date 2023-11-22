'''
#TODO Create My First API  with Framework fastApi, With Server Uvicorn and Insomnia (CRUD)
#TODO Used: POO ( Programming Oriented Objects) & API CRUD
#TODO En general, los path parameters se utilizan para identificar un recurso específico en tu API, mientras que los query parameters se utilizan para filtrar o ordenar los resultados de una consulta.
#* Use: Path Parameters & Query Parameters
#* /userQuery/?query_param=Midudev (My Example)
'''
from fastapi import FastAPI
from pydantic import BaseModel
# === POO (Instancia y Entidad del Objeto) ===
#A)
class User(BaseModel):
  id: int
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

# My List Users 
users_list =  [User(id= 1, name="Mouredev", url="http://mouredev.dev", age=35), 
               User(id= 2, name="Midudev", url="http://midudev.dev", age=38), 
               User(id= 3, name="Fazt", url="http://fazt.dev", age=28), 
               User(id= 4, name="Oscar", url="http://oscardev.dev", age=34), 
               User(id= 5, name="DeGranda", url="http://deGrandadev.dev", age=33)]

# ==== App Web Server with FastAPI ====
app = FastAPI()

#GET 
@app.get("/")
async def root():
  return {"message": str("Hello Users")}


@app.get("/users/")
async def users():
  return users_list

#GET: Path Parameter (int:id)
@app.get("/user/{id}")
async def user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]#[0]
  except: 
    return {"error": "Add a new User"}

#GET: Query Parameter (str:name) / (To read data)
@app.get("/userDev/")
async def user_query(id: int, name: str):
  return search_user(id, name)


def search_user(id: int, name: str): 
    '''
     #users = filter(lambda user: user.id == id, users_list) 
     #user == "u"
     /userDev/?id=2&name=Midudev
     Se agregó un name: str al parámetro de la función user_query para permitir la búsqueda por name en los query parameters.
     Se utilizó la expresión generadora next para buscar el usuario de manera más eficiente.
     Se comparan los nombres de manera insensible a mayúsculas y minúsculas (name.lower()) para hacer la búsqueda del usuario no sensible a mayúsculas/minúsculas.
    '''
    user = next((u for u in users_list if u.id == id and u.name.lower() == name.lower()), None)
    try:
      if user:
        return user.__dict__
      else: 
        return {"error": "Error 404. Not Found User"}
    except: 
      return {"error": "Add a new User"}
    

@app.get("/userQuery/")
async def user_query(query_param: str = None):
  if query_param: 
    filter_user = [user for user in users_list if query_param.lower() in user.name.lower()]
    return {"users": [user.__dict__ for user in filter_user]}
  else: 
    return {"users": [user.__dict__ for user in users_list]}

#POST (To create data)
@app.post("/users/")
async def create_users(user: User):
    if type(search_user(user.id, user.name)) == User:
     return {"error": str("User Exist.")}
    else:
     users_list.append(user)
#=== Other Option ===    
""" @app.post("/users/")
async def create_user(user: User): 
  if search_user(user.id, user.name):
    return { "error": str("User already exist")}
  else :
    users_list.append(user)
    return { "Message": str("New User Created successfully.")} """

#PUT (To update data)
@app.put("/users/")
async def user(user: User): 
  user_found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      user_found = True

  if not user_found: 
     return {"error": "Sorry! This User Not Exist. Add a new User."}


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