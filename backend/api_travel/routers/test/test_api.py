#####
#TODO:  === Pruebas unitarias  > Test Instance Of Class === 
#pytest routers/test/test_api.py
#######
import pytest
from unittest.mock import Mock
from routers.travel import Travels, TripFirst, DurationFirst, TransportFirst, LodgingFirst
from typing import List
import pandas as pd
import numpy as np
import os

#Trip ID,Destination,Start date,End date,Duration (days),Traveler name,Traveler age,Traveler gender,Traveler nationality,Accommodation type,Accommodation cost,Transportation type,Transportation cost

#1,"London, UK",5/1/2023,5/8/2023,7,John Smith,35,Male,American,Hotel,1200,Flight,600

#* === Tests
def test_api_travel():
 # Mock para el DataFrame
 #mock_df = Mock(spec=Travels) 
 mock_df = Mock(spec=Travels) 
 # Crear un objeto mock para la clase AgenciaViajes
 # Configura el comportamiento del DataFrame mock
 mock_df.__getitem__.return_value = {
        "Trip ID": [1],
        "Destination": ["London, UK"],
        "Start date": ["5/1/2023"],
        "End date": ["5/8/2023"],
        "Duration (days)": [7],
        "Traveler name": ["John Smith"],
        "Traveler age": [35],
        "Traveler gender": ["Male"],
        "Traveler nationality": ["American"],
        "Accommodation type": ["Hotel"],
        "Accommodation cost": [1200],
        "Transportation type": ["Flight"],
        "Transportation cost": [600]
    }
 # Crea una instancia de TripFirst con el DataFrame mock
 trip_instance = TripFirst(df=mock_df)
 # Llama al método trip_user con un ID de viaje
 result = trip_instance.trip_user(1)
 # Verificar el Resultado
 assert result == [
    {"Trip ID": 1, "Destination": "London, UK", "Start date": "5/1/2023", "End date": "5/8/2023",  "Duration (days)": 7, "Traveler name": "John Smith", "Traveler age": 35, "Traveler gender": "Male", "Traveler nationality": "American", "Accommodation type": "Hotel", "Accommodation cost": 1200, "Transportation type": "Flight", "Transportation cost": 600}
 ]
 

#! === Main ===
if __name__ == "__main__":
  pytest.main()