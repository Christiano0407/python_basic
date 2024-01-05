########
#TODO: Abstract Factory
########
from abc import ABC, abstractmethod
import pandas as pd
import csv
import os

#* ====  ===== Data Base ===== ====
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../poo_data/Travel details dataset.csv")
df = pd.read_csv(file_path)
print(df.head(5))


#? ======== Interfaces of Products - Abstract Factory ========
# 1) Familia de Objetos para: Viajes
class Trip(ABC):
  @abstractmethod
  def first_travel(self):
    pass


class TripDuration(ABC):
  @abstractmethod
  def duration_travel(self):
    pass


#Familia de Objetos para: Transporte
class Transport(ABC):
  @abstractmethod
  def move_transport(self):
    pass


class CostTransport(ABC):
  @abstractmethod
  def cost_transport(self):
    pass


#Familia de Objetos para: Alojamiento
class Lodging(ABC): 
  @abstractmethod
  def lodging_live(self):
    pass


class CostLodging(ABC):
  @abstractmethod
  def cost_lodging(self):
    pass


#? ===== Abstract Factory - Create Instance of Objects ======
# 2) Abstract Factory para crear familias de objetos
class TripWorld(ABC):
  @abstractmethod
  def create_travel(self) -> str:
    pass


  @abstractmethod
  def create_travel_duration(self) -> str:
    pass


class TripWorldTransport(ABC):
    @abstractmethod
    def create_transport(self) -> str:
      pass


class TripWorldLodging(ABC):
  @abstractmethod
  def create_lodging(self) -> str:
    pass


  @abstractmethod
  def create_lodging_cost(self) -> str:
    pass


#? ====== Implementations Instance Of Objects - Abstract Factory =======
# 3) Implementaciones concretas para Abstract Factory
class FirstTrip(Trip):
  def __init__(self, trip_id:id, trip_destiny:str):
    self.trip_id = trip_id
    self.trip_destiny = trip_destiny

  def first_travel(self):
    return f"Hello! Confirm your Trip {self.trip_destiny} and 'ID' Token is {self.trip_id}. Thank you."
  

#? ==== Implementation Concrete ====
class AmazingTrip(TripWorld):
  def create_travel(self) -> str:
    return FirstTrip()


#? ==== === Call & Variables === ====
def main_trip():
  unique_travel = set()

  for index, data_travel in df.head(5).iterrows:
    pass
  

#! ======= === Main === ========
if __name__ == "__main__":
  main_trip()