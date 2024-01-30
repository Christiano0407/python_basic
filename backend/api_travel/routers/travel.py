from fastapi import APIRouter, status, HTTPException, Path, Query
from abc import ABC, abstractmethod
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


class TripTransportLodging(ABC): 
  @abstractmethod
  def trip_transport_lodging(self) -> None: 
    pass


#*2) == Abstract Factory for create families of Objects ==
class UserTrip(ABC): 
  def create_trip_user(self) -> Trip: 
    pass


class DurationTrip(ABC): 
  def create_date_trip(self) -> TripDuration: 
    pass


class TransportLodging(ABC): 
  def create_transport_lodging(self) -> TripTransportLodging: 
    pass



#* CP) ==> Instance of Class Principal <== 
class Travels(BaseModel): 
  trip_user: List[Dict[str, Union[int, str, float]]] = Field(description="Information of the User Trip")
  #trip_user: Union[int, None] = Field(description="Information of the User Trip")
  trip_duration: List[Dict[str, Union[int, str, float]]] = Field(description="Information about to the duration travel")
  trip_transport_lodging: List[Dict[str, Union[int, str, float]]] = Field(description="Information about to transport and lodging")

#*3) ===  Implementation Concrete ===
class TravelFly(UserTrip): 
  def create_trip_user(self) -> Trip:
    return TripFirst()
  

class TripFirst(Trip): 
  def trip_user(self, id):
    id_user_new = (df[df["Trip ID"] == id].iloc[:, :5].to_dict(orient="records"))
    return id_user_new


#? ==== API ROOT / REST / CRUD ==== Path Parameters or Query Parameters ===
#=== Path Parameter ===
@router.get("/{id}", status_code=status.HTTP_200_OK, tags=["travels"])
async def travel_id(id:int = Path(..., title="Get ID Of The User", description="User ID that Trip")): 

  user_trip_instance = TravelFly().create_trip_user()
  id_user_trip = user_trip_instance.trip_user(id) if user_trip_instance else None

  print(f"ID del Usuario {id}")
  print(f"User Information: {id_user_trip}")
  
  try: 
    if id_user_trip: 
      return Travels(trip_user = id_user_trip) 
    else : HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id User Trip Not Found")
  except ValidationError as ve:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Validation Error: {ve.json()}")
  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=F"Internal Server: {str(e)}")