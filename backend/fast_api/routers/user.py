#########
#*2)
#########
from fastapi import APIRouter, FastAPI, HTTPException 
from pydantic import BaseModel
#import pandas as pd
# === POO (Instancia y Entidad del Objeto) ===
#A)
class User(BaseModel):
  id: int
  name: str 
  url: str 
  age: int


# My List Users 
users_list =  [User(id= 1, name="Mouredev", url="http://mouredev.dev", age=35), 
               User(id= 2, name="Midudev", url="http://midudev.dev", age=38), 
               User(id= 3, name="Fazt", url="http://fazt.dev", age=28), 
               User(id= 4, name="Oscar", url="http://GNDX.dev", age=34), 
               User(id= 5, name="DeGranda", url="http://deGranda.dev", age=33),
               User(id= 6, name="Alarcon", url="http://alarcondev.dev", age=32)]

# ==== App Web Server with FastAPI ====
app = FastAPI()
router = APIRouter()



#GET 
""" @router.get("/", status_code=200)
async def root():
  return {"message": str("Hello Users", list)} """


@router.get("/users/")
async def users():
  return users_list

#GET: Path Parameter (int:id)
@router.get("/users/{id}", tags=["users"], status_code=200)
async def user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]#[0]
  except: 
     raise HTTPException(status_code=404, detail="These Users not founds. Sorry!!")
    #return {"error": "Add a new User"}

#GET: QueryP Parameter
@router.get("/userDev/", status_code=200)
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
         raise HTTPException(status_code=404, detail="These Users not founds. Sorry!!")
    except: 
      return {"error": "Add a new User"}
    

@router.get("/userQuery/", status_code=200)
async def user_query(query_param: str = None):
  if query_param: 
    filter_user = [user for user in users_list if query_param.lower() in user.name.lower()]
    return {"users": [user.__dict__ for user in filter_user]}
  else: 
    return {"users": [user.__dict__ for user in users_list]}


#POST (To create data)
@router.post("/users/", tags=["users"], response_model=User, status_code=201)
async def create_users(user: User):
    if type(search_user(user.id, user.name)) == User:
      raise HTTPException(status_code=204, detail="User Not Found")
     #return {"error": str("User Exist.")}
    else:
     users_list.append(user)

#PUT (To update data)
@router.put("/users/", tags=["users"])
async def user(user: User): 
  user_found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      user_found = True

  if not user_found: 
     raise HTTPException(status_code=204, detail="User Not Found")
  
  return user

#Delete
@router.delete("/users/", tags=["users"])
async def user_delete(id: int, name: str):
  '''
  A) En este código, enumerate() se utiliza para obtener tanto el usuario como su índice en la lista users_list. (índice y elemento)
  B) Usamos pop(index) para eliminar el usuario de la lista en base a su índice.
  C) Este enfoque asegura que el usuario correcto se elimine en caso de que haya usuarios duplicados con el mismo id y name.
  '''
  for index, user in enumerate(users_list): 
    if user.id == id and user.name.lower() == name.lower():
      try: 
        users_list.pop(index)
        return { "message": str("User Delete successfully")}
      except Exception as e: 
        return {"error":  f"{str(e)}"}
      
  return {"Error": "User Not Found"}
      


app.include_router(router)