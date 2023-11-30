#########
#TODO: FastAPI: Authentic oAuth2 & Open ID Connect
#? OAuth2PasswordBearer : Se encarga de gestionar la autenticación (usuario e contraseña)
#? OAuth2PasswordRequestForm: La forma en como se va a mandar nuestros criterios de autenticación.
#? Token: TokeUrl => Se encarga de gestionar la validación. Un "token" es solo una cadena con algún contenido que podemos usar más adelante para verificar a este usuario. Un "token" es solo una cadena con algún contenido que podemos usar más adelante para verificar a este usuario.Normalmente, un token caduca después de un tiempo. Por lo tanto, el usuario deberá volver a iniciar sesión en algún momento posterior.Y si roban el token, el riesgo es menor. No es como una clave permanente que funcionará para siempre (en la mayoría de los casos).
#TODO: La declaración Annotated toma un tipo de dato existente y un objeto de anotación. El objeto de anotación puede ser cualquier objeto que proporcione el método __call__. El método __call__ se utiliza para obtener los metadatos asociados con el tipo de datos anotado.
#HTTP/1.1 200 OK
 #date: Wed, 29 Nov 2023 17:43:52 GMT
 #server: uvicorn
 #content-length: 49
 #content-type: application/json
########
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing_extensions import Annotated
#from typing import Union

#=== App ===
app = FastAPI()
#===oAuth2 ===
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ========= Crear un modelo de usuario ========
#=== POO User === (Instancia)
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
# Search User Token
def search_user(username: str): 
  '''
   Los dos asteriscos (**) antes de users_db en la línea return UserDB(**users_db[username]) indican que se está utilizando el desempaquetado de diccionarios. El desempaquetado de diccionarios es una característica de Python que permite desempaquetar los pares clave-valor de un diccionario en una llamada a una función.

   En este caso, el diccionario users_db se está desempaquetando en los argumentos del constructor de la clase UserDB. Esto significa que los pares clave-valor del diccionario users_db se pasan como argumentos de posición al constructor de la clase UserDB.
  '''
  if username in users_db: 
    return UserDB(**users_db[username]) #return UserDB(username="mouredev", password="123456")
  
# Validation User Token (Criterio de dependencia)
async def current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  '''
  #Status 401 User Not Authorization but yes authentic user(Usuario sí está autenticado pero, no tiene autorización).
  '''
  user = search_user(token)
  if not user:
    raise HTTPException(
      status_code=401, 
      detail="User not Authorization.", 
      headers={"WWW-Authenticate": "Bearer"})
  
  if user.disabled:
    raise HTTPException(
      status_code=400, 
      detail="User inactive"
    )
  
  return user

#POST (Mandar user & password)
@app.post("/token")
async def token(form: OAuth2PasswordRequestForm = Depends()):
  '''
  Depends es una característica integrada del marco FastAPI para definir dependencias en las rutas de la API. Las dependencias se utilizan para inyectar dependencias en las funciones de la API, lo que puede ser útil para una variedad de propósitos, como:
  -Validación de datos de la solicitud.
  -Obtención de acceso a servicios externos.
  -Restringir el acceso a los recursos. 
  En el contexto de OAuth 2.0, un token bearer es un tipo de token de acceso que se envía en el encabezado Authorization de una solicitud HTTP. El token bearer es simplemente una cadena de caracteres que no tiene ningún significado para el cliente que lo envía. El cliente es simplemente responsable de enviar el token al servidor. El servidor es responsable de validar el token y determinar a qué recursos tiene acceso el cliente.

  El objeto JSON {"access_token", "token_type": "bearer"} es la respuesta de un servidor de autorización OAuth 2.0 que contiene el token bearer. La propiedad access_token contiene la cadena de caracteres del token bearer real. La propiedad token_type siempre es bearer para indicar que el token es un token bearer.

  Los tokens bearer son una forma conveniente de implementar OAuth 2.0 porque son fáciles de usar y no requieren ningún estado del lado del cliente. Sin embargo, los tokens bearer también son menos seguros que otros tipos de tokens de acceso, como los tokens MAC, porque pueden ser fácilmente robados si el cliente está comprometido.
  '''
  user_db = users_db.get(form.username)
  if not user_db:
    raise HTTPException(status_code=404, detail="This user not correct.")
  
  user = search_user(form.username)
  if not form.password == user.password:
     raise HTTPException(status_code=404, detail="This password is not correct.")
  
  return {"access_token": user.username, "token_type": "bearer"}

#GET
@app.get("/users/me")
async def me(user: User = Depends(current_user)):
  return user
