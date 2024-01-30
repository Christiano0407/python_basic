from fastapi import APIRouter, status, HTTPException, Path, Query
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, ValidationError
from typing import Union, Optional 
import pandas as pd
import numpy as np
import os

#* === app & API Router ===
router = APIRouter()


#! === Call Data Base ==
""" script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data_base", "Travel details dataset.csv")
df = pd.read_csv(file_path)
print(df.iloc[:, :5])

#! ==> Clean of values: "NAN" and "Infinites" <== 
df.replace([np.inf - np.inf], np.nan, inplace=True)
df.dropna(inplace=True) """


#? ==== === Instance Of Class / Pattern: Abstract Factory === ====
#1) = Family of Objects =
class Trip(ABC):
  @abstractmethod
  def trip_user(self):
    pass


class TripDuration(ABC): 
  @abstractmethod
  def trip_date(self): 
    pass


class TripTransportLodging(ABC): 
  @abstractmethod
  def trip_transport_lodging(self): 
    pass


#2) = Abstract Factory for create families of Objects =
class UserTrip(ABC): 
  def create_trip_user(self) -> Trip: 
    pass


class DurationTrip(ABC): 
  def create_date_trip(self) -> TripDuration: 
    pass


class TransportLodging(ABC): 
  def create_transport_lodging() -> TripTransportLodging: 
    pass
  

#3) Instance of Class Principal 
class Travels(BaseModel): 
  trip_user = Union[Trip, None] = Field(..., gt=0, description="Information of the User Trip")
  trip_duration = Union[TripDuration, None] = Field(description="Information of the Duration Travel")
  trip_transport_lodging = Union[TripTransportLodging, None] = Field(description="All Information about Transport and Lodging")


#? ==== API ROOT / REST / CRUD ==== Path Parameters or Query Parameters ===
#=== Path Parameter ===
@router.get("/{id}", status_code=status.HTTP_200_OK, tags=["travels"])
async def travel_id(id:int = Path(..., title="Get ID Of The User", description="User ID that Trip")): 
  #Data Base
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, "../../data_base", "Travel details dataset.csv")
  df = pd.read_csv(file_path)

  df.replace([np.inf - np.inf], np.nan, inplace=True)
  df.dropna(inplace=True)
  #If Exist Equal ID with Data Base
  #id_trip = df[df["Trip Id"] == id].to_dict(orient="records")

  #Lógica para obtener los datos que deseas devolver
  #Puedes utilizar las clases del patrón Abstract Factory para crear las instancias necesarias
  user_trip_instance = UserTrip().create_trip_user()
  duration_trip_instance = DurationTrip().create_date_trip()
  transport_lodging_instance = TransportLodging().create_transport_lodging()

  # Lógica para obtener los datos de cada instancia según tus necesidades, utilizando el DataFrame df
  id_user_trip = user_trip_instance.trip_user(df[df["Trip Id"] == id].iloc[:, :5].to_dict(orient="records")) if user_trip_instance else None
  #duration_trip = duration_trip_instance.trip_date()
  
  try: 
    if id_user_trip and duration_trip_instance and transport_lodging_instance: 
      return id_user_trip, duration_trip_instance, transport_lodging_instance
    else : HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id User Trip Not Found")
  except ValidationError as ve:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Validation Error: {ve.json()}")
  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=F"Internal Server: {str(e)}")


  return Travels(trip_user = id_user_trip) 