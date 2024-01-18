#######
#TODO: === Pattern Design Structural: Composite ===
#?: Composite es un patrón de diseño estructural que te permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.
##############
from abc import ABC, abstractmethod


#* === Interfaz Componente (Component) ===
class Trip(ABC):
  @abstractmethod
  def trip(self): 
    pass


#! ==> Class - Inheritance - <==
class UserTravel(Trip): 
  def __init__(self, name:str, country:str, lodging:str, transport:str):
    self.name = name
    self.country = country
    self.lodging = lodging
    self.transport = transport

  def trip(self) -> str: 
    return f"Hi! This Trip is for the user: {self.name} that visited {self.country}. Your lodging will have {self.lodging} and your transport is {self.transport}. Ok! Thank you and Enjoy your visited" 
  

#* ==== - Clase Compuesto (Composite) - ====
class CompositeTrip(Trip): 
  def __init__(self, country): 
    self.country = country
    self.travels = []

  def add(self, component): 
     self.travels.append(component)

  def country_travel(self, component) -> str: 
    return f"Trip at {component.country}. Enjoy your Visited."
  
  def country_lodging(self, component) -> str: 
    return f"Your Lodging {component.lodging} it's Ok. And Plus Country: {self.country}"
  
  def country_transport(self, component) -> str: 
    return f"Hello, your Transport {component.transport} it's Ok. Thank you and Enjoy your trip."
  
  def trip(self) -> str: 
    for travel in self.travels:
      users = travel.trip()
      return users


#* ======== - Execute - ========
if __name__ == "__main__": 
  # - Variables -
  triOne = UserTravel("Pamela", "United States", "Hotel", "Flying")
  tripTwo = UserTravel("Luisa", "City Mexico", "House", "Bicycle")
  tripThree = UserTravel("Alexa", "London", "Hotel", "Flying")

  print("Composite: Pattern Design")
  composite = CompositeTrip("France")
  composite.add(triOne)
  compositeTrip = CompositeTrip("Germany")
  compositeTrip.add(tripTwo)
  travelComposite = CompositeTrip("Canada")
  travelComposite.add(tripThree)

  print("Trip1", composite.trip())
  print("Trip2", compositeTrip.trip())
  print("Trip3", travelComposite.trip())
  print("Plus", composite.country_travel(triOne))
  print("Plus", composite.country_lodging(triOne))
  print("Plus", composite.country_transport(triOne))