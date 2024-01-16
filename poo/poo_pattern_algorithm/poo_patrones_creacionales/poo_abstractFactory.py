########
#TODO: - Pattern Design - === Abstract Factory ===
########
from abc import ABC, abstractmethod
import pandas as pd
import os
from datetime import datetime, timedelta
#import csv

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
  def create_travel(self) -> Trip:
    pass


  @abstractmethod
  def create_travel_duration(self) -> TripDuration:
    pass


class TripWorldDate(ABC): 
  @abstractmethod
  def create_date(self) -> TripDuration:
   pass

class TripWorldTransport(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
      pass


class TripWorldLodging(ABC):
  @abstractmethod
  def create_lodging(self) -> Lodging:
    pass


  @abstractmethod
  def create_lodging_cost(self) -> CostLodging:
    pass


#? ====== Implementations Instance Of Objects - Abstract Factory =======
# 3) Implementaciones concretas para Abstract Factory
class FirstTrip(Trip):
  def __init__(self, trip_id:id, trip_destiny:str):
    self.trip_id = trip_id
    self.trip_destiny = trip_destiny

  def first_travel(self) -> Trip:
    return f"Hello! Confirm your Trip {self.trip_destiny} and 'ID' Token is {self.trip_id}. Thank you."
  

class TimeTrip(TripDuration):
  def __init__(self, trip_id:id, trip_destination:str, start_date:datetime, end_date:datetime, days:int):
    self.trip_id = trip_id
    self.trip_destination = trip_destination
    self.start_date = start_date
    self.end_date = end_date
    self.days = days

  def duration_travel(self):
    return f"Hello, the date of your Trip to {self.trip_destination} with code of {self.trip_id} start {self.start_date.strftime('%m/%d/%Y')} and finished in {self.end_date.strftime('%m/%d/%Y')}. Enjoy this wonderful experience for {self.days} days."
  

#? ==== Implementation Concrete ====
class AmazingTrip(TripWorld):
  def create_travel(self) -> Trip:
    return FirstTrip(1,"London, UK") # Asumiendo que el ID y destino son constantes para este ejemplo
  
  def create_travel_duration(self) -> TripDuration:
    pass


class AmazingDuration(TripWorldDate):
  def create_date(self) -> TripDuration:
    return TimeTrip(1,"London, UK",5/1/2023,5/8/2023,7)

#? ==== === Call & Variables === ====
trip_factory = AmazingTrip()
date_factory = AmazingDuration()

def main_trip():
  unique_travel = set()


  for index, data_travel in df.head(5).iterrows():
    creator = None

    destiny_travel = data_travel["Destination"]
    start_date_travel = data_travel["Start date"]
    duration_days = int(data_travel["Duration (days)"])

    start_date = datetime.strptime(start_date_travel,"%m/%d/%Y")
    end_date = start_date + timedelta(days=duration_days)


    if destiny_travel not in unique_travel:
      unique_travel.add(destiny_travel)
    elif start_date_travel not in unique_travel:
      unique_travel.add(start_date_travel)  
    
    if data_travel["Destination"] == "London, UK":
      creator = trip_factory
    elif duration_days >= 7: # Ajusta esta lógica según tus necesidades
      creator = date_factory


    if creator:
      if isinstance(creator, AmazingTrip):
        trip_data = creator.create_travel()
        print("Trip", trip_data.first_travel())
      elif isinstance(creator, AmazingDuration):
        trip_data_duration = creator.create_date()
        print("Travel Date: ", trip_data_duration.duration_travel())
  

#! ======= === Main === ========
if __name__ == "__main__":
  print("Abstract Factory Result:")
  main_trip()