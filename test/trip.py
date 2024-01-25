class AgencyTravel:
  def __init__(self): 
    self.travel_reservation = None
    self.hotel_reserved = None

  def reserve_trip(self, destiny): 
     self.travel_reservation = f"Hi! My reservation {destiny} it's Amazing. Thank you."

  def reserve_hotel(self, city): 
    self.hotel_reserved = f"Ok! my Hotel at in this city {city} is good."
