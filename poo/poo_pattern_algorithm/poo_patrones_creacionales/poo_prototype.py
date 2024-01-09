######
#TODO: Prototype es un patrón de diseño creacional que nos permite copiar objetos existentes sin que el código dependa de sus clases. El patrón de diseño "Prototype" se utiliza para crear nuevos objetos duplicando un objeto existente, llamado prototipo
######
from abc import ABC, abstractmethod
import copy

#* ==== Instance - Prototype ====
class TripPrototype: 
  def __init__(self): 
    self.trip_id = int,
    self.user_name = ""
    self.trip = ""
    self.lodging = ""
    self.airplane_ticket = ""
    self.places_visit = []
    self.transport = ""
# - Crear la instancia para copiar -
  def clone(self):
    return copy.deepcopy(self)

  def __str__(self): 
    return f"Hi! Welcome {self.user_name} to travel with us. Your Trip {self.trip} and your airplane ticket {self.airplane_ticket} is ok. Also, your schedules for places visit {self.places_visit} with your lodging {self.lodging} confirm. And the end confirm your transport {self.transport}. Thank you."
  

#! ===== Call - Execute / Clients ===== 
if __name__ == "__main__":
# - Crear un prototipo de viaje (Trip) -
  prototype_travel = TripPrototype()

  prototype_travel.trip_id = 1
  prototype_travel.user_name = "Pamela Oviedo"
  prototype_travel.trip = "Chicago"
  prototype_travel.lodging = "Hotel Chicago"
  prototype_travel.airplane_ticket = "Chicago, U.S.A - VIP"
  prototype_travel.places_visit = ["Tour Chicago Night", "Rio Chicago & Museum Art Chicago", "Millennium Park & Cloud Gate"]

# - Clonar (Clone) el prototipo para crear nuevos viajes -
  trip_one = prototype_travel.clone()
  print("Trip:", trip_one)

  trip_two = prototype_travel.trip = "New York City"
  trip_two = prototype_travel.airplane_ticket = "New York, U.S.A. Ticket VIP"
  print("Next Travel:", trip_two)