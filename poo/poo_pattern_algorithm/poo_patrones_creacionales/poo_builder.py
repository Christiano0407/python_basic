######
#TODO: Builder (Constructor) - Pattern Design: Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
######
from abc import ABC, abstractmethod
import pandas as pd
import os
import csv
import datetime as datetime

#? === 1) Definition: Interfaces of builder (Order) / (Methods Abstract) ===
class Trip: 
  def __init__(self): 
    self.destiny_travel = ""
    self.lodging = ""
    self.airplane_ticket = ""
    self.places_visit = []
    self.middle_transport = ""

  def __str__(self): 
    return f"Your Trip {self.destiny_travel} is Tomorrow. Your airplane ticket {self.airplane_ticket} at Five O'clock am. Your Lodging {self.lodging} is ok. Confirm this places for visit {self.places_visit}. Finally your transport is confirm {self.middle_transport}. Thank you. "


#? === 2) Implementation of Builder (Create Object) === 
class Builder:

  def reset(self): 
    pass

  def build_destiny_travel(self):
    pass

  def build_lodging(self):
    pass

  def build_airplane_ticket(self):
    pass

  def build_places_visit(self):
    pass

  def build_middle_transport(self): 
    pass


#? === 3) Create Object (Constructor) / (Order) ===
class TripNewYorkBuilder(Builder):
  def __init__(self):
    self.trip = Trip()
  
  def reset(self):
    self.trip = Trip()

  def build_destiny_travel(self):
    self.trip.destiny_travel = "New York"
  
  def build_lodging(self):
    self.trip.lodging = "Five Stars"

  def build_airplane_ticket(self):
    self.trip.airplane_ticket = "VIP Zone"

  def build_places_visit(self):
    self.trip.places_visit = ["Times Square", "Central Park", "Statue of Liberty"]

  def build_middle_transport(self):
    self.trip.middle_transport = "Rent a Car"

  def my_trip(self):
    return self.trip
  

#! ==== Create New Builder (Instance) with Data Base ====
# Nueva implementación de Builder para construir viajes desde la base de datos
class DataTravel(Builder):
  def __init__(self, data):
    self.trip = Trip() 
    self.data = data 

  def reset(self): 
     self.trip = Trip()
  
  def build_destiny_travel(self):
    new_destiny = self.trip.destiny_travel = self.data["Destination"]
    return new_destiny
  
  def build_lodging(self):
    new_lodging = self.trip.lodging = self.data["Accommodation type"]
    return new_lodging
  
  def build_airplane_ticket(self):
     self.trip.airplane_ticket = self.data["Transportation type"]

  def build_middle_transport(self):
     self.trip.middle_transport = self.data["Transportation type"]

  def data_travel(self):
    return self.trip
  
  

#? === 4) Director: Builder - Coordinate all process of construction used Object(order) ===
class DirectorTravel():
  def builder_travel(self, travel):
    travel.reset()
    travel.build_destiny_travel()
    travel.build_lodging()
    travel.build_lodging()
    travel.build_airplane_ticket()
    travel.build_places_visit()
    travel.build_middle_transport()


#!==== Load Data Base from Data CSV ====
#Función para cargar datos desde el archivo CSV
def load_data_travel(data_frame, num_row = 1):
  data_travel_list = []

  for index, row in data_frame.iterrows():
    data_travel_list.append(row.to_dict())
    if index + 1 == num_row:
      break

  return data_travel_list


#* ==== === Call: Main === ====
if __name__ == "__main__": 
#=== Director ===
  director = DirectorTravel()
#==== Data CSV ====
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, "../../poo_data/Travel details dataset.csv")
  df = pd.read_csv(file_path)

  travel_data_base = load_data_travel(df)
#=== Execute ===
  builder_trip_new_yor = TripNewYorkBuilder()
  director.builder_travel(builder_trip_new_yor)
  trip_new_york = builder_trip_new_yor.my_trip()
  new_trip = builder_trip_new_yor.build_destiny_travel()
#> Data
  for trip_data in travel_data_base: 
    builder_trip_data = DataTravel(trip_data)
    director.builder_travel(builder_trip_data)
    new_travel_data = builder_trip_data.data_travel()

  print(" === Trip to New York === ")
  print(trip_new_york)
  print("Trip:", new_trip)
  print(" === New Travel === ")
  print("New:",new_travel_data)
  