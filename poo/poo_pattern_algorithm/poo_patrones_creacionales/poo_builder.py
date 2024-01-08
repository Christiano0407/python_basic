######
#TODO: Builder (Constructor) - Pattern Design: Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
######
from abc import ABC, abstractmethod

#? === 1) Definition: Interfaces of builder (Order) / (Methods Abstract) ===
class Trip: 
  def __init__(self): 
    self.destiny_travel = ""
    self.lodging = ""
    self.airplane_ticket = ""
    self.places_visit = []
    self.middle_transport = ""

  def __str__(self): 
    pass


#? === 2) Implementation of Builder (Create Object) === 

  
  

#? === 3) Create Object (Constructor) / (Order) ===

  

#? === 4) Director: Builder - Coordinate all process of construction used Object(order) ===


#* ==== === Call: Main === ====
