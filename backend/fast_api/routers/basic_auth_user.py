#########
#TODO: FastAPI: Authentic oAuth2 & Open ID Connect
#? OAuth2PasswordBearer : Se encarga de gestionar la autenticación (usuario e contraseña)
#? OAuth2PasswordRequestForm: La forma en como se va a mandar nuestros criterios de autenticación.
#? Token: TokeUrl => Se encarga de gestionar la validación. 
########
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#=== App ===
app = FastAPI()
#===oAuth2 ===
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#=== POO User === 
class User(BaseModel):
  client_id: int
  username: str
  full_name: str
  email:str
  disabled: bool

# =Herencia=
class UserDB(User): 
  password: str


# === List User
# = Base de Datos "No Relacional" => JSON =
users_db = {
  "mouredev": {
    "client_id": 1,
    "username": "mouredev",
    "full_name": "Braise Moure",
    "email": "braisemoure.com", 
    "disabled": False, 
    "password": "123456"
  },
  "midudev": {
    "client_id": 2,
    "username": "midudev",
    "full_name": "Miguel Dev",
    "email": "midudev.com", 
    "disabled": True, 
    "password": "234567"
  },
  "faztdev": {
    "client_id": 3,
    "username": "faztdev",
    "full_name": "fazt",
    "email": "faztCode.com", 
    "disabled": False, 
    "password": "345678"
  }, 
  "degrandadev": {
    "client_id": 4,
    "username": "deGrandadev",
    "full_name": "Diego deGranda",
    "email": "deGranda.com", 
    "disabled": False, 
    "password": "45678910"
  }, 
  "oscardev": {
    "client_id": 5,
    "username": "oscardev",
    "full_name": "Oscar Barajas",
    "email": "oscarBarajas.com", 
    "disabled": False, 
    "password": "567891011"
  },  
}


# === API CRUD ===
""" app.get("/")
async def get_user(): 
  return users_db """

def search_user(username: str): 
  if username in users_db: 
    return UserDB(users_db[username])
  

#POST (Mandar user & password)
@app.post("/token")
async def token(form: OAuth2PasswordRequestForm = Depends()):
  user_db = users_db.get(form.username)