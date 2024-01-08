######
#TODO: Builder (Constructor) - Pattern Design: Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
######
from abc import ABC, abstractmethod

#? === 1) Definition: Interfaces of builder (Order) / (Methods Abstract) ===
class Trip: 
  def __init__(self): 
    self.destiny_travel = ""
    self.lodging = ""
    self.airplane_ticket = ""
    self.places_visit = []
    self.middle_transport = ""

  def __str__(self): 
    return f"Your Trip {self.destiny_travel} is Tomorrow. Your airplane ticket {self.airplane_ticket} is for Five O'clock am. Your Lodging {self.lodging} is ok. Confirm this places for visit {self.places_visit}. Finally your transport is confirm {self.middle_transport}. Thank you. "


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
    trips = self.trip.destiny_travel = "New York"
    return trips
  
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
    


#* ==== === Call: Main === ====
if __name__ == "__main__": 
  director = DirectorTravel()

  builder_trip_new_yor = TripNewYorkBuilder()
  director.builder_travel(builder_trip_new_yor)
  trip_new_york = builder_trip_new_yor.my_trip()
  new_trip = builder_trip_new_yor.build_destiny_travel()

  print("Trip to New Yor")
  print(trip_new_york)
  print("New:", new_trip)