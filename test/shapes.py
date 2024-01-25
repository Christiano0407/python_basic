import math

class Shape: 

  def area(self): 
    pass

  def perimeter(self): 
    pass


class Circle(Shape): 

  def __init__(self, radio):
    self.radio = radio

  def area(self): 
    return math.pi * self.radio **2 #Al Cuadrado
  
  def perimeter(self):
    return 2 * math.pi * self.radio
  

class Triangle(Shape): 
  def __init__(self, radio, base, height): 
    self.radio = radio
    self.base = base
    self.height = height

  def __str__(self): 
    return f"These all values: {self.base} and {self.height}"

  def area(self):
    return self.base * self.height / 2
  