#####
#TODO:  === Pruebas unitarias  > Test Instance Of Class === 
#######
import pytest
from unittest.mock import Mock
from api_travel.routers.travel import TripFirst, DurationFirst, TransportFirst, LodgingFirst
from typing import List
import pandas as pd
import numpy as np
import os


#* === Tests
def test_api_travel():
 # Mock para el DataFrame
 mock_df = Mock() 
 # Crear un objeto mock para la clase AgenciaViajes
 # Configura el comportamiento del DataFrame mock
 mock_df.__getitem__.return_value=[
   {"Trip ID": 1, "Destination": "London", "Duration (days)": 7, "Accommodation type": "Hotel", "Transportation type": "Flight" }
 ]
 # Crea una instancia de TripFirst con el DataFrame mock
 trip_instance = TripFirst(df=mock_df)
 # Llama al método trip_user con un ID de viaje
 result = TripFirst.trip_user(1)
 # Verificar el Resultado
 assert result == [
    {"Trip ID": 1, "Destination": "London", "Duration (days)": 7, "Accommodation type": "Hotel", "Transportation type": "Flight" }
 ]

 def test_real_dataFrame():
  #! === Call Data Base ==
  script_dir = os.path.dirname(__file__)
  file_path = os.path.join(script_dir, "../../data_base", "Travel details dataset.csv")
  df = pd.read_csv(file_path)
  print(df.iloc[:, :5])
  #! ==> Clean of values: "NAN" and "Infinites" <== 
  df.replace([np.inf - np.inf], np.nan, inplace=True)
  df.dropna(inplace=True)
   
  real_df = df

  # Crea una instancia de TripFirst con el DataFrame real
  trip_instance = TripFirst(df=real_df) 
  # Llama al método trip_user con un ID de viaje
  result = trip_instance.trip_user(1)

  # Verifica si el resultado es el esperado
  assert isinstance(result, List)

#! === Main ===
if __name__ == "__main__":
  pytest.main()