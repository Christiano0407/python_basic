from fastapi import APIRouter, status, HTTPException, Path, Query
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Union, Optional 
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


#? ==== API ROOT / REST / CRUD ====
@router.get("/", status_code=status.HTTP_200_OK, tags=["travels"])
async def travel(): 
  return {"message": str("Hi! It's my first trip")} 