import pytest
from test.trip import AgencyTravel

#? > @decorator <
# Fixture para configuración inicial
@pytest.fixture
def travel_agency(): 
  agency = AgencyTravel()
  # Configuración inicial (puede incluirse aquí)
  yield agency
  # Limpiar después de la prueba (puede incluirse aquí)


def test_reservation_trip(travel_agency): 
  travel_agency.reserve_trip("London, United Kingdom")
  assert travel_agency.travel_reservation == "Hi! My reservation London, United Kingdom it's Amazing. Thank you."
  #assert travel_agency.travel_reservation == "Trip to London it's confirmed."

def test_reservation_hotel(travel_agency):
  travel_agency.reserve_hotel("London") 
  assert travel_agency.hotel_reserved == "Ok! my Hotel at in this city London is good."

def test_discounts(travel_agency): 
  travel_agency.reserve_discount(1000, 0.10)
  assert travel_agency.discount_travel == f"You pay with discount 900.0.Enjoy your trip."



  #!==== === Execute === ====
  if __name__ == "___main__": 
    test_reservation_trip()
    test_reservation_hotel()
  
