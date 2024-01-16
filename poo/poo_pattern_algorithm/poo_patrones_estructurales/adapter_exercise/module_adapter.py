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
class TripUser(NameTraveler): 
  def __init__(self, name_user: str): 
    self.name_user = name_user

  def name_traveler(self) -> str:
    return f"Hi! Confirm to user {self.name_user} with this travel."
  

class TripUserTransportation(TransportTrip): 
  def __init__(self, user_transport:str):
    self.user_transport = user_transport

  def transport_trip(self):
    return f"Hi!! Confirm Transport {self.user_transport}. Enjoy  will you Transport.Thank you."
  

class TripUserLodging(LodgingTrip): 
  def __init__(self, user_trip_lodging): 
    self.user_trip_lodging = user_trip_lodging

  def lodging_trip(self):
    return f"Hi!!! Confirm that you Lodging {self.user_trip_lodging} it's Ok. Please, enjoy you Lodging."
  

  #! ==== Concrete Implementation Instance ====
class UserNameTrip(ClientName):
  def get_name_traveler(self) -> ClientName:
    return NameTraveler("John Smith")


class UserTransportTrip(TripTransport): 
  def get_middle_transport(self) -> TripTransport:
    return TransportTrip("Flight")


class UserLodgingTrip(TripLodging): 
  def get_lodging(self) -> str:
    return LodgingTrip("Hotel") 
    

#// ========= Variables & Function & Main ===========
user_trip_first = UserNameTrip()
user_transport_first = UserTransportTrip()
user_lodging_trip = UserLodgingTrip()

def main_travel(): 
  unique_travel = set()

  for index, data_travel in df.head(5).iterrows():
    creator = None
    #-Variables of Data-
    plus_user_name = data_travel["Traveler name"]
    plus_transport_trip = data_travel["Transportation type"]
    plus_lodging_trip = data_travel["Accommodation type"]
    #-Unique Value-
    if plus_user_name not in unique_travel: 
      unique_travel.add(plus_user_name)
    elif plus_transport_trip not in unique_travel: 
      unique_travel.add(plus_transport_trip)
    elif plus_lodging_trip not in unique_travel: 
      unique_travel.add(plus_lodging_trip)
   #-Validation Data & creator-
    if data_travel["Traveler name"] == "John Smith":
      creator = user_trip_first
    elif data_travel["Transportation type"] == "Flight": 
      creator = user_transport_first
    elif data_travel["Accommodation type"] == "Hotel": 
      creator = user_lodging_trip

    #-Instance Creator-
    if creator: 
      if isinstance(creator, UserNameTrip): 
        trip_user = creator.get_name_traveler()
        print("User Name: ", trip_user.name_traveler())
      elif isinstance(creator, UserTransportTrip): 
        trip_user_transport = creator.get_middle_transport()
        print("User Transport", trip_user_transport.transport_trip())
      elif isinstance(creator, UserLodgingTrip): 
        trip_user_lodging = creator.get_lodging()
        print("User Lodging: ", trip_user_lodging.lodging_trip())



if __name__ == "__main__": 
  print("User: First Travel")
  main_travel()
