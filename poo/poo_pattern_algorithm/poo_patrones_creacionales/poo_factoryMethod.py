###
#TODO: Factory Method: Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.
###
from abc import ABC, abstractmethod
import pandas as pd
import csv
import os

#==== Root Data Base ====
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../poo_new/data_poo/poo_data.csv")
print("File Path:", file_path)
df = pd.read_csv(file_path)

# === Part: Factory Method ===
class LogisticDelivery(ABC):
  @abstractmethod
  def shipment(self, name, price, quantity, day, shipment, city):
    pass


class AirDelivery(LogisticDelivery):
  def shipment(self, name, price, quantity, shipment, city):
    if price > 25000 and quantity > 3:
      return f"Your product coming the same day for Air delivery."
    else:
      return "Sorry! The Air Delivery is only with subscription or more of two products and high price."
  

class GroundDelivery(LogisticDelivery):
  def shipment(self, name, price, quantity, shipment, city):
    if price > 1000 and quantity > 1:
      return f"Your Product it's coming today for ground delivery"
    else: 
      return f"Sorry. your product {name} not coming today."
    #return super().shipment(name, price, quantity, day, shipments, city)
class IphoneFactory(ABC):
  @abstractmethod
  def create_iphone(self, name, price, quantity, shipment, city):
    pass


class IphoneFactory_csv(IphoneFactory):
    @classmethod
    def create_iphone(cls, name, price, quantity, shipment, city=""):
      delivery = shipment.shipment(name, price, quantity, shipment, city)
      return Iphone(name, price, quantity, delivery)


#==== Class Original ====
class Iphone: 
  #=== Attributes of Class === 
  brand = "Apple Iphone"
  
  #=== Method of Instance => Object ===
  def __init__(self, name:str, price:float, quantity:int, shipment, city=""):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.shipment = shipment
    self.city = city

  def __str__(self) -> str: 
    return f"Hi!! New Iphone: {self.name} with unique price {self.price}. You needed this {self.brand}."
  
  def pay_total(self) -> int:
    total = self.price * self.quantity
    return total

  """ @classmethod
  def read_file_csv(cls, file_path):
    items = []

    with open(file_path, "r") as file:
      read = csv.read(file)
      header = next(read)

      for row in read:
        item_data = dict(zip(header, row))
        item_data["price"] = float(item_data["price"])
        instance_item = cls(**item_data)
        item_data.append(instance_item)

    return items """

class StoreIphone:
  def __init__(self, iphoneFactory, logisticDelivery):
    self.iphoneFactory = iphoneFactory
    self.iphone_all = []
    self.logisticDelivery = logisticDelivery

  def add_iphone(self, name, price, quantity, shipment, city=""):
    iphone_plus = self.iphoneFactory.create_iphone(name, price, quantity, shipment, city)
    all_product = self.iphone_all.append(iphone_plus)
    return all_product

  def list_iphone(self):
    """ for iphone_plus in self.iphone_all:
      print(iphone_plus) """
    iphone_plus = self.iphone_all
    return iphone_plus
  
  def deliveryShipment(self):
    if self.logisticDelivery == "Air":
      return AirDelivery()
    elif self.logisticDelivery == "Ground":
      return GroundDelivery()
    else: 
      raise ValueError("Invalid Delivery & Shipment.")

# ==== Execute ====
if __name__ == "__main__":
  #===Call: Factory Method 
  csv_factory = IphoneFactory_csv() 
  store = StoreIphone(csv_factory, "Air")
  print("store:", store)

  iphone_factory = IphoneFactory_csv()
  air_delivery = AirDelivery()
  ground_delivery = GroundDelivery()

  # Reading from CSV and creating Iphones
  plus_file = df
  items = []

  pay_total_price = Iphone("Iphone15", 40000, 1, air_delivery, "CDMX")
  iphone_air = iphone_factory.create_iphone("Iphone15", 45000, 2, air_delivery, "CDMX")
  iphone_ground = iphone_factory.create_iphone("IphoneX", 22000, 1, ground_delivery, "New York")

  #===: 
  for index,row in plus_file.iterrows():
    name = row["name"]
    price = row["price"]
    quantity = row["quantity"]

    # Decide si es entrega aérea o terrestre según tus criterios
    #delivery_method = air_delivery if price > 25000 and quantity > 2 else ground_delivery
    delivery_method = store.deliveryShipment()

    iphone_instance = csv_factory.create_iphone(name, price, quantity, delivery_method, "CDMX")
    items.append(iphone_instance)

    store.add_iphone(name, price, quantity, delivery_method, "CDMX")
  
  for item in items:
    store.add_iphone(item.name, item.price, item.quantity, delivery_method, "CDMX")

  new_store = store.list_iphone()

  for iphone_plus in new_store:
    print(iphone_plus)
#===
  print("Total:", pay_total_price.pay_total())
  print("Delivery:", iphone_air.delivery)
