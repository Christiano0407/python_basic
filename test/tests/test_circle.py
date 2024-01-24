import pytest
from test.shapes import Shape, Circle
import math


#*===
class TestCircle: 
  def test_one(self): 
    assert True


#*=== 
def test_circle_area(): 
  circle = Circle(2)
  assert circle.area() == 4 * math.pi


#!=== === Execute === ===
test_circle_area() 