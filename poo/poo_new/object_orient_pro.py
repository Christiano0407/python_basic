class Item: 
  #=== Attributes ===
  brand = "Apple Iphone"
  #=== Methods of Instance ===
  def __init__(self, name:str, price:float, quantity:int): 
    self.name = name
    self.price = price
    self.quantity = quantity

  def __str__(self) -> str:
    return f"This Iphone is: {self.name} and his price {self.price} and now in Store have these quantity {self.quantity} and Brand is {self.brand}"
    
  def calculate_total_price(self) -> int:
    return self.price * self.quantity
  
  #==== Method Of Class ====
  @classmethod
  def attribute(cls) -> str:
   return cls.brand
  

#=== Variables ===
item1 = Item("Iphone15", 22500, 2) 
item2 = Item("Iphone7", 9000, 3)
item3 = Item.attribute()

#=== Call POO ===
if __name__ == "__main__":
  print(type(item1))
  print(item1)
  print(item2)
  """ print(str(item1)) """
  print(f"Total Price:{item1.calculate_total_price()}")
  print(f"Price Total: {item2.calculate_total_price()}")
  print(f"Instance:", item3)