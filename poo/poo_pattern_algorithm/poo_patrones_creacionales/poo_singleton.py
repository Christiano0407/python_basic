### #TODO: Singleton: Singleton es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.
###
import csv


class Iphone: 
  # Variable para almacenar la única instancia (Pattern Singleton)
  _instance = None

  #=== Attributes of Class === 
  brand = "Apple Iphone"
  
  #=== Method of Instance => Object ===
  def __new__(cls, *args, **kwargs):
    '''
    __new__ method: Este método es llamado antes de __init__ al crear una nueva instancia de la clase. En el método __new__, se verifica si la variable _instance es None. Si es así, se crea una nueva instancia usando super(Iphone, cls).__new__(cls) y se asigna a la variable _instance. Si ya hay una instancia, se devuelve la misma instancia en lugar de crear una nueva.
    '''
    if not cls._instance:
      cls._instance = super(Iphone, cls).__new__(cls)
      return cls._instance
    else: 
      # Si la instancia ya existe, simplemente devolverla
      return cls._instance

  def __init__(self, name:str, price:float, quantity:int):
    '''
    __init__ method: Este método se ejecuta solo si se crea una nueva instancia. Aquí se inicializan los atributos de la instancia (name, price, quantity).
    '''
    self.name = name
    self.price = price
    self.quantity = quantity

  def __str__(self) -> str: 
    return f"Hi!! New Iphone: {self.name} with unique price {self.price}. You needed this {self.brand}."
  
  def pay_total(self) -> int:
    total_pay = self.price * self.quantity
    return total_pay
  
  #=== Method Of Class ===
  @classmethod
  def read_data_csv(cls, file_path):
    items = []

    with open(file_path, "r") as file:
      reader = csv.reader(file)
      header = next(reader) # Leer la primera fila como encabezado

      for row in reader:
        item_data = dict(zip(header, row)) 

        item_data["price"] = float(item_data["price"])

        instance_items = cls(**item_data)
        items.append(instance_items)

    return items
  

# ==== Variables ====
iphone1 = Iphone("Iphone11", 25000, 3)
iphone2 = Iphone("Iphone12", 30000, 2)
iphone3 = Iphone("Iphone15", 40000, 1)
user_iphone = Iphone("Iphone15", 40000, 2)

# ==== >= Call <= ====
if __name__ == "__main__":
  print(iphone1)
  print("Equal Instance:", iphone2 is iphone3) # Ambas instancias son iguales: True
  print("User Pay Total:", user_iphone.pay_total())
  
