# #TODO: === Token ===
from fastapi import FastAPI, HTTPException, status, Depends, status, Request
from fastapi import status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials
from starlette.middleware.base import BaseHTTPMiddleware
from typing_extensions import Annotated
from pydantic import BaseModel
from typing import Optional
from jose import JWTError, jwt
import os 
import dotenv # Importar el archivo de configuración

# ==== OAuth2 ==== ==> Authenticated & Access <==
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
#=== 1) Validation Token ====
def decode_token(token:str):
  try: 
    # Define la clave secreta para firmar el token
    secret_key = get_secret_key()
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # Decodifica el token
    claims = jwt.decode(token, secret_key, algorithm=["HS256"])
    return claims
    #username = claims["sub"]
    #email = claims.get("email") # Solo extrae el email si existe
    #return {"username": username, "email": email}
    # Verifica la validez del token y El tiempo a expirar ("exp").
  except JWTError:
    return credentials_exception

""" if "exp" in claims and claims["exp"] < time.time():
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Expired Authentication Token." #Token de autenticación caducado
      )

    return claims """

#=== 2) Authentication User ===
async def get_current_user(
    token:Annotated[str, Depends(oauth2_scheme)]
):
   try: 
        # Decodifica el token
        claims = decode_token(token)
        # Extrae la información del usuario del token
        username = claims["username"] #Subject
        # Crea un objeto User (Instance POO)
        user = User(username=username, email=claims.get("email"))
  
        return user
   except JWTError: 
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
   except Exception as e: 
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
      detail="Internal Server Error",
      )
   
# === Middleware === 
class AuthMiddleware(BaseHTTPMiddleware): 
  async def handle(self, request: Request, call_next: callable):
    token = request.headers.get("Authorization", None)
    if not token or not token.startswith("Bearer "): 
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or Invalid authorization Token")
    try: 
      claims: decode_token(token.split(" ")[1])
    except JWTError:
      HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token") 

    # Extraer información del usuario del token
    username = claims["sub"]
    email = claims.get("email") 
    # Crea un objeto User con la información del token
    user = User(username=username, email=email)
    # Agrega el usuario autenticado al request context
    request.state.user = user

    response = await call_next(request)

    return response