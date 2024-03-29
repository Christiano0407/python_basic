from fastapi import APIRouter, status, HTTPException, Path, Query, Depends
from abc import ABC, abstractmethod
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from typing import Union, Optional, List, Dict
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from routers.jwt_auth.auth import get_current_user
from routers.jwt_auth.jwt_token import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
import pandas as pd
import numpy as np
import os

#* === app & API Router ===
router = APIRouter()


#! === Call Data Base ==
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data_base", "Travel details dataset.csv")
df = pd.read_csv(file_path)
print(df.iloc[:, :5])
#! ==> Clean of values: "NAN" and "Infinites" <== 
df.replace([np.inf - np.inf], np.nan, inplace=True)
df.dropna(inplace=True)


#? ==== === Instance Of Class / Pattern: Abstract Factory === ====
#*1) = Family of Objects =
class Trip(ABC):
  @abstractmethod
  def trip_user(self):
    pass


class TripDuration(ABC): 
  @abstractmethod
  def trip_date(self) -> None: 
    pass


class TripTransport(ABC): 
  @abstractmethod
  def trip_transport(self) -> None: 
    pass


class TripLodging(ABC): 
  @abstractmethod
  def trip_lodging(self) -> None: 
    pass


#*2) == Abstract Factory for create families of Objects ==
class UserTrip(ABC): 
  def create_trip_user(self) -> Trip: 
    pass


class DurationTrip(ABC): 
  def create_date_trip(self) -> TripDuration: 
    pass


class TransportTrip(ABC): 
  def create_transport(self) -> TripTransport: 
    pass


class LodgingTrip(ABC): 
  def create_lodging(self) -> TripLodging:
    pass


#* CP) ==> Instance of Class Principal <== 
#=== Method Of Instance the Object >
class Travels(BaseModel): 
  trip_users: List[Dict[str, Union[int, str, float]]] = Field(description="Information of the User Trip")
  #trip_user: Union[int, None] = Field(description="Information of the User Trip")
  trip_duration: List[Dict[str, Union[int, str, float]]] = Field(description="Information about to the duration travel")
  trip_transport: List[Dict[str, Union[int, str, float]]] = Field(description="Information about to transport and lodging")
  trips_lodging: List[Dict[str, Union[int, str, float]]] = Field(description="Information about the Lodging Travel User")

  # > Getters <
  def getters_get(self) -> str: 
    return f"This Information about the User Trip is private {self.trip_users}. Thank you for contact to us"
  
  #=== Method Of Instance Of Class - Decorators >
  @property
  def get_private_trip_user(self) -> str:
    return self.trip_users


#*3) ===  Implementation Concrete ===
class TravelFly(UserTrip): 
  def create_trip_user(self) -> Trip:
    return TripFirst()
  

class TripFirst(Trip): 
  def trip_user(self, id):
    id_user_new = (df[df["Trip ID"] == id].iloc[:, :5].to_dict(orient="records"))
    return id_user_new
  

class DurationTravel(DurationTrip): 
  def create_date_trip(self) -> TripDuration:
    return DurationFirst()
  

class DurationFirst(TripDuration): 
  def trip_date(self, duration): 
    duration_user_new = (df[df["Duration (days)"] == duration].iloc[:, :5].to_dict(orient="records"))
    return duration_user_new
  

class TransportTravel(TransportTrip):
  def create_transport(self) -> TripTransport:
    return TransportFirst()
  

class TransportFirst(TripTransport): 
  def trip_transport(self, transport): 
    transport_user_new = (df[df["Transportation type"] == transport].iloc[:, :5].to_dict(orient="records"))
    return transport_user_new


class LodgingTravel(LodgingTrip): 
  def create_lodging(self) -> TripLodging:
    return LodgingFirst()


class LodgingFirst(TripLodging): 
   def trip_lodging(self, lodging): 
     lodging_user_new = (df[df["Accommodation type"] == lodging].iloc[:, :5].to_dict(orient="records"))
     return lodging_user_new



#? ==== API / REST / CRUD / Root & Routers ==== Path Parameters or Query Parameters ===
#===GET
#=== Path Parameter ===
#Endpoint: http://127.0.0.1:8000/travels/user/1
@router.get("/user/{id}", status_code=status.HTTP_200_OK, tags=["travels"])
async def travel_id(id:int = Path(..., title="Get ID Of The User", description="User ID that Trip")): 

  user_trip_instance = TravelFly().create_trip_user()
  id_user_trip = user_trip_instance.trip_user(id) if user_trip_instance else None
  #>Call Private: Getter <
  #private_users_trip = Travels().get_private_trip_user

  print(f"ID del Usuario {id}")
  print(f"User Information: {id_user_trip}")
  
  try: 
    if id_user_trip: 
      return f"{Travels(trip_users = id_user_trip, trip_duration=[], trip_transport=[], trips_lodging=[])}"
    else : HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id User Trip Not Found")
  except ValidationError as ve:
    return JSONResponse(content={"detail": f"Validation Error: {ve.json()}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
  except Exception as e: 
    return JSONResponse(content={"detail": f"Internal Server: {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

#=== Query Parameter ===
#Endpoint: http://127.0.0.1:8000/travels/duration?duration=5
@router.get("/time/duration", status_code=status.HTTP_200_OK, tags=["travels"])
async def get_destiny(duration:int = Query(title="Duration Travel", description="Duration Travel Information Destination")):
  
  duration_travel = DurationTravel().create_date_trip()
  duration_travel_user = duration_travel.trip_date(duration) if duration_travel else None
  # === http://127.0.0.1:8000/travels/duration/?duration=5 => Endpoint === 
  print(f"Duration To Travel: {duration}")
  print(f"Duration User Travel: {duration_travel_user}")

  try: 
    if duration_travel_user: 
      return Travels(trip_users=[], trip_duration=duration_travel_user, trip_transport=[], trips_lodging=[])
    else: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Duration to Travel Not Found")
  except ValidationError as ve:
     return JSONResponse(content={"detail": f"Validation Error: {ve.json()}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
  except Exception as e: 
      return JSONResponse(content={"detail": f"Internal Server: {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

@router.get("/trip/transport", status_code=status.HTTP_200_OK, tags=["travels"])
async def get_transport(transport:str = Query(title="Travel Transport", description="Travel Transport for the User")): 
  
  transport_travel = TransportTravel().create_transport()
  transport_travel_user = transport_travel.trip_transport(transport) if transport_travel else None

  print(f"Transport Travel: {transport}")
  print(f"Transport User Travel: {transport_travel_user}")

  try: 
    if transport_travel_user: 
      return Travels(trip_users=[], trip_duration=[], trip_transport=transport_travel_user, trips_lodging=[])
    else: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transport Not Found...")
  except ValidationError as ve: 
    return JSONResponse(content={"detail": f"Validation Error: {ve.json()}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
  except Exception as e: 
    return JSONResponse(content={"details": f"Internal Server: {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

  
@router.get("/users/lodging", status_code=status.HTTP_200_OK, tags=["travels"])
async def get_lodging(lodging:str = Query(title="Lodging Travel", description="Lodging Travel for User")):
  
  lodging_travel = LodgingTravel().create_lodging()
  lodging_travel_user = lodging_travel.trip_lodging(lodging) if lodging_travel else None

  print(f"Lodging Travel: {lodging}")
  print(f"Lodging User Travel: {lodging_travel_user}")

  try: 
    if lodging_travel_user: 
      return Travels(trip_users=[], trip_duration=[], trip_transport=[], trips_lodging=lodging_travel_user)
    else: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lodging It's not Found or Not Contract...")
  except ValidationError as ve: 
    return JSONResponse(content={"details": f"Validation Error {ve.json()}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
  except Exception as e: 
    return JSONResponse(content={"details": f"Internal Server {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


#===POST
@router.post("/user/{id}", status_code=status.HTTP_200_OK, tags=["travels"])
async def post_travels(id:int, travels_input:Travels): 
  #=== Validar los "travels" en Pydantic >
  try: 
    travel_flight = travels_input.dict()
    print("Execute Travel, Ok: ", travel_flight)
    validation_travel = Travels(**travel_flight)
    print("Validation Of Travel: ", validation_travel)

    # Asegúrate de que el ID del producto o Travel no exista ya en la base de datos
    if df[df["Trip ID"] == id].iloc[:, :5].empty:
    # Agregar el nuevo producto al DataFrame
      df = df.append(travel_flight, ignore_index=True)
    # Guardar el DataFrame de vuelta al archivo CSV (o tu base de datos externa)
      df.to_csv(file_path, index=False)
      return validation_travel
    else: 
     raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Travels ID. All ID of Users Travel")
  except ValidationError as ve: 
    return JSONResponse(content={"details": f"Validation Error {ve.json()}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
  except Exception as e: 
    return JSONResponse(content={"details": f"Internal Server {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


#===PUT
@router.put("/user/{id}", status_code=status.HTTP_200_OK, tags=["travels"])
async def update_travel(id:int, travels_update:Travels): 
  try: 
  # Verificar si el ID del viaje existe en la base de datos
    if not df[df["Trip ID"] == id].empty: #empty es un método de los objetos de pandas, que se utiliza para verificar si un DataFrame está vacío, es decir, si no contiene ninguna fila.
  # Actualizar los campos del viaje en el DataFrame
    #loc es un método de acceso basado en etiquetas en pandas. Permite seleccionar y asignar valores a un DataFrame utilizando etiquetas de fila y columna.
      df.loc[df["Trip ID"] == id, "trip_users"] = travels_update.trip_users
      df.loc[df["Trip ID"] == id, "trip_duration"] = travels_update.trip_duration
      df.loc[df["Trip ID"] == id, "trip_transport"] = travels_update.trip_transport
      df.loc[df["Trip ID"] == id, "trips_lodging"] = travels_update.trips_lodging 
  # Guardar el DataFrame de vuelta al archivo CSV (o tu base de datos externa)
      df.to_csv(file_path, index=False)
      return {"Message:": f"Travel With ID {id} Update Successfully"}
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Travel with the ID {id} not found")
  except ValidationError as ve: 
    return JSONResponse(content={"details": f"Validation Error {ve.json()}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
  except Exception as e: 
    return JSONResponse(content={"details": f"Internal Server {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)    

#===Delete
  
#* === Login Auth & Token Access / Protected Login Route ===
@router.post("/access/token", response_model=dict,  status_code=status.HTTP_200_OK, tags=["travels"])
async def login_token_access(form_data: OAuth2PasswordRequestForm = Depends()):
  # - Verificar las Credenciales del Usuario -
  if not await authenticate_user(form_data.username, form_data.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Could Not Validate Credentials",
      headers={"WWW-Authenticate": "Bearer"},
    )
  # Si las credenciales son válidas, generar un token de acceso
  access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
    data={"sub": form_data.username}, expire_delta=access_token_expire
  )
  return {"access_token": access_token, "token_type": "bearer"}
  

@router.get("/token/protected-route", tags=["travels"])
async def protected_route(current_user : str = Depends(get_current_user)): 
   return {"message": "This route is protected and only accessible to authenticated users."}
#current_user es el nombre del parámetro que representa al usuario autenticado