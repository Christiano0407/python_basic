import pytest
from test.trip import AgencyTravel

#? > @decorator <
# Fixture para configuración inicial
@pytest.fixture
def travel_agency(): 
  agency = AgencyTravel()
  yield agency


def test_reservation_trip(travel_agency): 
  travel_agency.reserve_trip("London, United Kingdom")
  assert travel_agency.travel_reservation == "Hi! My reservation London, United Kingdom it's Amazing. Thank you."
  #assert travel_agency.travel_reservation == "Trip to London it's confirmed."

def test_reservation_hotel(travel_agency):
  travel_agency.reserve_hotel("London") 
  assert travel_agency.hotel_reserved == "Ok! my Hotel at in this city London is good."



  #!==== Execute ====
  if __name__ == "___main__": 
    test_reservation_trip()
    test_reservation_hotel()
  
