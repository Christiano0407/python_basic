####
#TODO: === Design Pattern Behavior - Work Algorithms - : Observer (Observar) ===
#?: Observer es un patrón de diseño de comportamiento que te permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento que le suceda al objeto que están observando.
########
from abc import ABC, abstractmethod
from typing import List


#? === Interfaz Observador (Observer - User) ===
class Observer(ABC): 
  @abstractmethod
  def updateTrip(self, message: str): 
    pass


#? ==== Interfaz Sujeto (Subject - Agency) (Observable) ====

class Subject(ABC): 
  @abstractmethod
  def add_observer_message(self, observer: Observer):
    pass

  @abstractmethod
  def remove_observer_message(self, observer: Observer):
    pass

  @abstractmethod
  def notify_observer_message(self, message:str):
    pass  

#? = ==>  Concreto Sujeto (Concrete Observable) <== =
class TravelAgency(Subject): 
  def __init__(self): 
    self._observers : List[Observer] = []
    self._special_offer = ""

  def add_observer_message(self, observer: Observer):
    if observer not in self._observers: 
      self._observers.append(observer)

  def remove_observer_message(self, observer: Observer):
    self._observers.remove(observer)

  def notify_observer_message(self, message: str):
    for observer in self._observers: 
      observer.updateTrip(message)

  def set_special_offer(self, offer: str): 
    self._special_offer = offer
    self.notify_observer_message(f"Hello, Have a good day. We have a new offer for you:{offer}")

#? == ===>  Concreto Observador (Concrete Observer) <=== ==
class Customer(Observer): 
  def __init__(self, name:str):
    self.name = name

  def updateTrip(self, message:str): 
    print(f"Hi! I'm {self.name}. I received your message: {message}. Thank you.")


#! ============= Execute ================
if __name__ == "__main__": 
   # Crear agencia de viajes
  travel_agency = TravelAgency()

  # Crear clientes
  girl_user = Customer("Luisa Pamela Evans")
  man_user = Customer("Robert Chris Johnson")
  family = Customer("Family Iron")
  
  # Suscribir clientes a la agencia
  travel_agency.add_observer_message(girl_user)
  travel_agency.add_observer_message(man_user)
  travel_agency.add_observer_message(family)
  
  # Establecer una oferta especial (esto notificará a los clientes
  travel_agency.set_special_offer(f"Hello! Enjoy your trip with a 25% of discount. Only Opportunity")

  # Cliente 1 cancela la suscripción
  travel_agency.remove_observer_message(family)
  
  # Establecer otra oferta especial (solo el Cliente 2 será notificado)
  travel_agency.set_special_offer("Congratulations!! You're the winner for the free trip: New York ")