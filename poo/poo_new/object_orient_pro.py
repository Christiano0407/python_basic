class Item: 
  #=== Attributes of Class ===
  brand = "Apple Iphone"
  default_pay_rate = 0.6
  #=== Methods of Instance ===
  def __init__(self, name:str, price:float, quantity:int, pay_rate: float = None): 
    # Run Validation Of Arguments
    assert price > 0, f"Price {price} is not greater or equal to Zero"
    # ===Instances of Object
    self.name = name
    self.price = price
    self.quantity = quantity
    self.pay_rate = pay_rate if pay_rate is not None else self.default_pay_rate

    Item.all.append(self)

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
  

#=== Variables ===
item1 = Item("Iphone15", 22500, 2, 0.4) 
item2 = Item("Iphone7", 9000, 3)
item3 = Item.attribute()
item4 = Item("Mac Air", 35000, 1, 0.9)

#=== Call POO ===
if __name__ == "__main__":
  print(type(item1))
  print(item1)
  print(item2)
  """ print(str(item1)) """
  print(f"Total Price:{item1.calculate_total_price()}")
  print(f"Price Total: {item2.calculate_total_price()}")
  print(f"Instance:", item3)
  print(item4)
  print("Pay with Pay_rate:",item1.apply_pay_rate())
  print("Pay with Pay_rate:",item2.apply_pay_rate())

  #print(Item.__dict__)#=== All Attributes of Class Level
  #print(item1.__dict__)#=== All Attributes for instance Level