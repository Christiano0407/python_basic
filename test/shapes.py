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