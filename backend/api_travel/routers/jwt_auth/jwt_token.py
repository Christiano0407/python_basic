#################
#TODO: Token:  === JWT & Auth ===
#* - Acceso único (Por un tiempo estimado) -
#? - Token of Access -
########===#######
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt
import os

# === ENV - Token - ===
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# === Esquema de OAuth2 para manejar la autenticación mediante nombre de usuario y contraseña ===
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# === Función para verificar las credenciales del usuario (simulada) ===
async def authenticate_user(username: str, password:str):
   # En un entorno real, aquí verificarías las credenciales en tu base de datos u otro sistema de almacenamiento seguro
  if username == "user" and password == "password":
    return True
  else:
    return False

# === Función para generar un token de acceso ===
def create_access_token(data:dict, expire_delta:timedelta):
  to_encode = data.copy()
  expire = datetime.utcnow() + expire_delta
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

# Auth ErrorError: Not Found
# OAuth2PasswordBearer (OAuth2, password)