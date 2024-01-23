###===###
#TODO: === Design Pattern Behavior - Work Algorithms - : Strategy (Estrategia) ===
#?: Strategy es un patrón de diseño de comportamiento que te permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.
#*: Imaginemos una agencia de viajes que quiere calcular el costo total de un paquete turístico utilizando diferentes estrategias de descuento
######===#####
from abc import ABC, abstractmethod


#* = Interfaz Estrategia (Strategy) =
class DiscountTripStrategy(ABC):
  @abstractmethod
  def apply_discount(self, amount: float) -> float:
    pass


#* == Estrategia Concreta (Concrete Strategy) - Descuento del 10% ==
class TripPercentDiscount(DiscountTripStrategy): 
  def apply_discount(self, amount: float) -> float:
    return amount * 0.10


#* == Estrategia Concreta (Concrete Strategy) - Descuento del 20% ==
class TripDiscount(DiscountTripStrategy): 
  def apply_discount(self, amount: float) -> float: 
    return amount * 0.20


#* === Contexto: Apply Strategy ===
class TravelPack:
  def __init__(self, name:str, cost: float, discount_cost: DiscountTripStrategy):
    self.name = name
    self.cost = cost
    self.discount_cost = discount_cost

  def calculate_discount(self) -> float: 
    total_cost_discount = self.discount_cost.apply_discount(self.cost)
    return total_cost_discount

    
  
#* ==== Cliente / Main ====
if __name__ == "__main__": 
  #  === > Variables <
  # >= Crear estrategias de descuento <=
  discount_one = TripPercentDiscount()
  discount_two = TripDiscount()

  # = Crear paquetes de viaje con diferentes estrategias =
  package_1 = TravelPack("Luisa Cantú", 10000, discount_one)
  package_2 = TravelPack("Pamela Oviedo", 20000, discount_two)


  # = Calcular y mostrar el costo total =
  print(f"Hi! {package_1.name} your Discount for the last Travel is: {package_1.calculate_discount()}")
  print(f"Good Afternoon, {package_2.name}. This message is for his confirm your discount: {package_2.calculate_discount()}")
