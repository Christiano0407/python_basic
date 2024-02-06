###############
#TODO: Auth: ==== Authentication & Token === === JWT & Auth ===
#* - Autenticación de Usuario y los Permisos de Acceso -
#? - Authentication & Authorization -
#? - Token of Access -
#######===######
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

# === Auth & env ===
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# === Get User Auth & Token ====
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exceptions = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could Not Validate Credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )

  try: 
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub") # sub = subname
    if username is None: 
      raise credentials_exceptions # HTTP 401
  except JWTError:
    raise credentials_exceptions