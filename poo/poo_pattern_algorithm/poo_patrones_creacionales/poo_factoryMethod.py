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
class IphoneFactory(ABC):
  @abstractmethod
  def create_iphone(self, name, price, quantity):
    pass


class IphoneFactory_csv(IphoneFactory):
    @classmethod
    def create_iphone(cls, name, price, quantity):
      return Iphone(name, price, quantity)

#==== Class Original ====
class Iphone: 
  #=== Attributes of Class === 
  brand = "Apple Iphone"
  
  #=== Method of Instance => Object ===
  def __init__(self, name:str, price:float, quantity:int):
    self.name = name
    self.price = price
    self.quantity = quantity

  def __str__(self) -> str: 
    return f"Hi!! New Iphone: {self.name} with unique price {self.price}. You needed this {self.brand}."

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
  def __init__(self, iphoneFactory):
    self.iphoneFactory = iphoneFactory
    self.iphone_all = []


  def add_iphone(self, name, price, quantity):
    iphone_plus = self.iphoneFactory.create_iphone(name, price, quantity)
    all_product = self.iphone_all.append(iphone_plus)
    return all_product


  def list_iphone(self):
    """ for iphone_plus in self.iphone_all:
      print(iphone_plus) """
    iphone_plus = self.iphone_all
    return iphone_plus


if __name__ == "__main__":
  #Call: Factory Method 
  csv_factory = IphoneFactory_csv() 
  store = StoreIphone(csv_factory)

  # Reading from CSV and creating Iphones
  plus_file = df
  items = []

  # Call: 
  for index,row in plus_file.iterrows():
    name = row["name"]
    price = row["price"]
    quantity = row["quantity"]

    iphone_instance = csv_factory.create_iphone(name, price, quantity)
    items.append(iphone_instance)
  
  for item in items:
    store.add_iphone(item.name, item.price, item.quantity)

  new_store = store.list_iphone()
  for iphone_plus in new_store:
    print(iphone_plus)
