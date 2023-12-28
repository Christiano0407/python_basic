#from data_poo import poo_data
#from data_poo.poo_data import *
import csv 

class Iphone: 
  #=== Attributes of Class ===
  brand = "Apple Iphone"
  default_pay_rate = 0.6
  #=== Methods of Instance ===
  def __init__(self, name:str, price:float, quantity:int, pay_rate: float = None): 
    # Run Validation Of Arguments
    assert price >= 0, f"Price {price} is not greater or equal to Zero"
    # ===Instances of Object
    self.name = name
    self.price = price
    self.quantity = quantity
    self.pay_rate = pay_rate if pay_rate is not None else self.default_pay_rate

    #Item.all.append(self)

  def __str__(self) -> str:
    return f"This Iphone is: {self.name} and his price {self.price} and now in Store have these quantity {self.quantity} and Brand is {self.brand}"
    
  def calculate_total_price(self) -> int:
    return self.price * self.quantity
  
  def apply_discount(self) -> float: 
    #return self.price =  self.price * self.pay_rate
    self.price = self.price * self.pay_rate

  #Attribute of Class & Instance
  def apply_pay_rate(self) -> float:
    return self.price * self.pay_rate
    
  #==== Method Of Class ====
  @classmethod
  def attribute(cls) -> str:
   return cls.brand
  
  @classmethod
  def read_from_csv(cls, file_path):
    items = []

    with open(file_path, "r") as file:
      reader = csv.reader(file)
      header = next(reader)  # Leer la primera fila como encabezado

      for row in reader:
        # Crear un diccionario con las claves del encabezado y los valores de la fila
        item_data = dict(zip(header, row))

        # Convertir 'price' a float antes de crear la instancia de Item
        item_data["price"] = float(item_data["price"])

        # Crear una instancia de Item y agregarla a la lista
        item_instance = cls(**item_data)
        items.append(item_instance)

    return items
  
  @staticmethod
  def is_integer(num):
    #We will count out the float that are point zero
    #for i.e: 5.0, 10.0
    if isinstance(num, float):
      #count out the float that are point zero
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else: 
      return False
    

#Hinheritance => Herencia / Polimorfismo (Polymorphism)
class Accessories(Iphone):
  def __init__(self, seth:str, airpod:str, airtag:str, wallet:str, adapter:str, wire:str, name:str, price:float, quantity:int):
    super().__init__(name, price, quantity)
    self.seth = seth
    self.airpod = airpod
    self.airtag = airtag
    self.wallet = wallet
    self.adapter = adapter
    self.wire = wire

  def __str__(self) -> str:
    return f"These are New Accessories for {self.name}: This is a new seth {self.seth} with the new {self.airpod} and {self.airtag}. This new {self.name} also bring {self.wallet}, one {self.adapter} and his wire {self.wire} for travels. All these products come {self.quantity} and unique price: {self.price} in Store."

#=== Variables ===
""" #item1 = Item("Iphone15", 22500, 2, 0.4) 
#item2 = Item("Iphone7", 9000, 3)
#item3 = Item.attribute()
#item4 = Item("Mac Air", 35000, 1, 0.9) """
items_from_csv = Iphone.read_from_csv("./data_poo/poo_data.csv")
new_accessories = Accessories("Seth MagSafe", "AirPodsPro12", "AirtagPro", "FineWoven", "USB-C", "Adapter MagSafe", "Iphone15", 35000, 2)

#=== Call POO ===
if __name__ == "__main__":
 """  #print(type(item1))
  #print(item1)
  #print(item2)
  print(str(item1))
  #print(f"Total Price:{item1.calculate_total_price()}")
  #print(f"Price Total: {item2.calculate_total_price()}")
  #print(f"Instance:", item3)
  #print(item4)
  #print("Pay with Pay_rate:",item1.apply_pay_rate())
  #print("Pay with Pay_rate:",item2.apply_pay_rate())

  #print(Item.__dict__)#=== All Attributes of Class Level
  #print(item1.__dict__)#=== All Attributes for instance Level """

for item in items_from_csv:
  print(str(item))

print(new_accessories)