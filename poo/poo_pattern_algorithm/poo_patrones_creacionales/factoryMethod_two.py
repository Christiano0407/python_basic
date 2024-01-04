#######
#TODO: Factory Method Two 
#######
from abc import ABC, abstractmethod
import pandas as pd
import csv
import os

#*==== === Data Base Root
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../poo_data/Travel details dataset.csv")
print("data file path",file_path)
#df = pd.read_csv(file_path)
# > Intenta cargar el archivo CSV e Errors
try:
    df = pd.read_csv(file_path)
    print("Data: Loaded Successfully")
    print(df.head(10))

except FileNotFoundError:
   print("Error: El Archivo CSV, no fue encontrado.")
except pd.errors.EmptyDataError:
   print("Error: El Archivo CSV o Base de Datos está Vacío.")
except pd.errors.ParserError:
   print("Error. Hubo un error al analizar el archivo.")
except Exception as e:
   print(f"Error Desconocido: {str(e)}")

#?=== Interface of Products - Factory Method
class DataTravel(ABC):
  @abstractmethod
  def travel_info(self):
    pass


#?==== Class of Product or Services
class Trip(DataTravel):
   def __init__(self, travel_id:int, destiny:str, travel_cost:float, transportation_type:str, transportation_cost:float):
      self.travel_id = travel_id
      self.destiny = destiny
      self.travel_cost = travel_cost
      self.transportation_type = transportation_type
      self.transportation_cost = transportation_cost

   """ def trip_destiny_new(self) -> str:
       return f"Your Travel {self.destiny} will cost ${self.travel_cost}. The type of transport {self.transportation_type} and cost: ${self.transportation_cost}" """
   
   def travel_info(self) -> str:
        return f"Your Travel to {self.destiny} and code travel:{self.travel_id}. This Travel will cost ${self.travel_cost}. The type of transport {self.transportation_type} and cost transportation is: ${self.transportation_cost}"
   

class CustomerTravel(DataTravel):
   def __init__(self, destiny:str, start_date:str, end_date:str ,name:str):
      self.destiny = destiny
      self.start_date = start_date
      self.end_date = end_date
      self.name = name

   def travel_info(self) -> str:
      return f"Thank you {self.name} for travel with us. Your Destiny {self.destiny} start date {self.start_date} and end {self.end_date}"
   

class TravelPack(DataTravel):
   def __init__(self, travel_id:int, destiny:str, duration:int, type_lodging:str, lodging_cost:float, type_transportation:str, transportation_cost:float):
      self.travel_id = travel_id
      self.destiny = destiny
      self.duration = duration
      self.type_lodging = type_lodging
      self.lodging_cost = lodging_cost
      self.type_transportation = type_transportation
      self.transportation_cost = transportation_cost

   def travel_info(self) -> str:
      return f"Thank you for your Travel with us. This pack {self.travel_id} is for {self.destiny} with duration days: {self.duration}. The principal lodging {self.type_lodging} with on cost ${self.lodging_cost} and unique promotion in transportation {self.type_transportation} with cost ${self.transportation_cost}"      
     

#?===== Factory Method - Create Interfaces =====
class TripCreator(ABC):
   @abstractmethod
   def create_trip(self, data):
      pass


class TripNew(TripCreator): 
   def create_trip(self, data):
      #return Trip(data["travel_id"], data["destiny"], data["travel_cost"], data["transportation_type"], data["transportation_cost"])
      return Trip(data["Trip ID"], data["Destination"], data["Accommodation cost"], data["Transportation type"], data["Transportation cost"])
   

class travelPackCreator(ABC):
   @abstractmethod
   def create_travel_pack(self, data):
      pass

class TravelPackNew(travelPackCreator):
   def create_travel_pack(self, data):
     return TravelPack(
        data["Trip ID"], data["Destination"], data["Duration (days)"], 
        data["Accommodation type"], data["Accommodation cost"], 
        data["Transportation type"], data["Transportation cost"]) 


#? === Customer ===
def main():
   # Data Iteration between files (rows)
   unique_travel = set()
   # Data Iteration between files (rows)
   for index, data_travel in df.head(5).iterrows():
      creator = None

      destination = data_travel["Destination"]

      """ if data_travel["Destination"] == "London, UK":
         creator = TripNew() """
      
      if destination not in unique_travel:
         unique_travel.add(destination)

      #Decide si crear una instancia de Trip o TravelPack
         if data_travel["Destination"] == "London, UK":   
            creator = TripNew()
         else:
            creator = TravelPackNew()
      
      if creator:
         if isinstance(creator, TripNew):
            trip_data_new = creator.create_trip(data_travel)
            print("Trip:", trip_data_new.travel_info()) 
         elif isinstance(creator, TravelPackNew):
            trip_create_data_new = creator.create_travel_pack(data_travel)
            print("Travel Pack:", trip_create_data_new.travel_info())

         """ trip_data_new = creator.create_trip(data_travel)
         trip_create_data_new = creator.create_travel_pack(data_travel)
         #print("Trip:", trip_data_new.trip_destiny_new()) 
         print("Trip Info:", trip_data_new.travel_info())
         if isinstance(trip_data_new, TravelPack):
            print("Travel Pack", trip_create_data_new.pack_info_travel()) """

         #print("Travel Pack:", trip_data_new.pack_info_travel())


#! ==== === Main === ====
if __name__ == "__main__":
   print("New Data Info Travel")
   main()