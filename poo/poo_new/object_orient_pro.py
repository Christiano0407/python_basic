#from data_poo import poo_data
#from data_poo.poo_data import *
import csv 

class Item: 
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
    

#Hinheritance => Herencia => Polimorfismo (Polymorphism)
  

#=== Variables ===
""" #item1 = Item("Iphone15", 22500, 2, 0.4) 
#item2 = Item("Iphone7", 9000, 3)
#item3 = Item.attribute()
#item4 = Item("Mac Air", 35000, 1, 0.9) """
items_from_csv = Item.read_from_csv("./data_poo/poo_data.csv")

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