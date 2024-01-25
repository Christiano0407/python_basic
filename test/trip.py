class AgencyTravel:
  def __init__(self): 
    self.travel_reservation = None
    self.hotel_reserved = None
    self.discount_travel = None

  def reserve_trip(self, destiny:str): 
     self.travel_reservation = f"Hi! My reservation {destiny} it's Amazing. Thank you."

  def reserve_hotel(self, city:str): 
    self.hotel_reserved = f"Ok! my Hotel at in this city {city} is good."

  def reserve_discount(self, price:int, discount:float):
    discounts = price * discount
    final_pay = price - discounts  
    self.discount_travel = f"You pay with discount {final_pay}.Enjoy your trip."