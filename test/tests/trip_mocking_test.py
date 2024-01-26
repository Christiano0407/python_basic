####
#TODO: === Execute: Test: Mocking 02 ===
#######
import pytest
from unittest.mock import Mock
from test.trip_moking import AgencyTravel, travel_destiny


def test_travel_destiny(): 
# Crear un objeto mock para la clase AgenciaViajes
  mock_agency = Mock(spec=AgencyTravel) # =Copy all Instance of class= / estás creando un mock

# Configurar el comportamiento simulado (en este caso, retornar mensajes ficticios)
  mock_agency.reserve_travel.return_value = "Simulated Travel Reserve"
  mock_agency.reserve_hotel.return_value = "Simulate Hotel Reserve"
  mock_agency.reserve_transport.return_value ="Simulated Transport Reserve"

# Llamar a la función que utiliza la agencia
  travel_to_destiny, travel_to_hotel, travel_to_transport = travel_destiny(mock_agency, "London", "Hotel London", "Airplane")

# Verificar que la función devuelva los resultados esperados
  assert travel_to_destiny == "Simulated Travel Reserve"
  assert travel_to_hotel == "Simulate Hotel Reserve"
  assert travel_to_transport =="Simulated Transport Reserve"

 # Verificar que los métodos de la agencia fueron llamados correctamente
  mock_agency.reserve_travel.assert_called_once_with("London")
  mock_agency.reserve_hotel.assert_called_once_with("Hotel London")
  mock_agency.reserve_transport.assert_called_once_with("Airplane")