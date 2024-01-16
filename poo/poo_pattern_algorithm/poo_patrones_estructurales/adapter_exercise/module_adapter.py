#### ==== ####
#TODO 1) === Module (Import) Adapter === 
#TODO - Use other Pattern Design: Abstract Factory -
#### ==== ####
from abc import ABC, abstractmethod
import pandas as pd
import os
from datetime import datetime, timedelta

#? ==== Data Base Prove ====
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../../poo_data/Travel details dataset.csv")
df = pd.read_csv(file_path)
print(df.head(5))


#? ==== Interface Of Products ====
class NameTraveler(ABC): 
  @abstractmethod
  def name_traveler(self): 
    pass


class TransportTrip(ABC): 
  @abstractmethod
  def transport_trip(self): 
    pass


class LodgingTrip(ABC): 
  @abstractmethod
  def lodging_trip(self): 
    pass


#* ==== Abstract Factory - Create Instance of Object ====
class ClientName(ABC): 
  @abstractmethod
  def get_name_traveler(self) -> str: 
    pass


class TripTransport(ABC): 
  @abstractmethod
  def get_middle_transport(self) -> str: 
    pass


class TripLodging(ABC): 
  @abstractmethod
  def get_lodging(self) -> str: 
    pass


#! ===  Implementation Instance Of Object - Abstract Factory ===
  