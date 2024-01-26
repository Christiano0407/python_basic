####
#TODO: === Create: Test: Mocking 01 ===
#######
# agencia_viajes.py
class AgencyTravel:
  def __init__(self, country): 
    self.country = country

  def __str__(self):
    return f"My travel have as to country with visit is {self.country}" 

  def reserve_travel(self, destiny):
    # Implementación real para reservar vuelo 
    print(f"Reserve travel to {destiny}")
     # ... lógica de reservación ...
    return f"Reserve this travel to {destiny}"
  
  def reserve_hotel(self, hotel): 
    # Implementación real para reservar hotel
    print(f"Reserve {hotel} in {self.country}")
     # ... lógica de reservación ...
    return f"Reserve hotel {hotel} in this country {self.country}"


def travel_destiny(agency, destiny, hotel): 
  travel_to_destiny = agency.reserve_travel(destiny)
  travel_to_hotel = agency.reserve_hotel(hotel)

  return travel_to_destiny, travel_to_hotel