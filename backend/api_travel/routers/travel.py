from fastapi import APIRouter, status, HTTPException, Path, Query
from abc import ABC, abstractmethod
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from typing import Union, Optional, List, Dict
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


#===PUT
  

#===Delete