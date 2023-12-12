# #TODO: === Token ===
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi import status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from pydantic import BaseModel
from typing import Optional
from jose import JWTError, jwt
import time
import os 
import dotenv # Importar el archivo de configuración

# ==== OAuth2 ==== 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# === DotEnv === 
dotenv.load_dotenv()

def get_secret_key(): 
  return  os.environ.get("SECRET_KEY")

#password: str => La contraseña no debe ser parte de la información del usuario que se maneja en la aplicación.
class User(BaseModel):
  username: str 
  email: Optional[str] = None
  

#=== Token y oAuth2 ===
def decode_token(token:str):
  # Define la clave secreta para firmar el token
  secret_key = get_secret_key()
  # Decodifica el token
  claims = jwt.decode(token, secret_key, algorithm=["HS256"])
  # Verifica la validez del token y El tiempo a expirar ("exp").
  if "exp" in claims and claims["exp"] < time.time():
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Expired Authentication Token." #Token de autenticación caducado
    )
  
  return claims


async def get_current_user(
    token:Annotated[str, Depends(oauth2_scheme)]
):
   # Decodifica el token
   claims = decode_token(token)
   # Extrae la información del usuario del token
   username = claims["sub"] #Subject
   # Crea un objeto User
   user = User(username=username)

   return user