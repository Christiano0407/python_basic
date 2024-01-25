import pytest
from test.shapes import Circle, Triangle
import math


#*===
class TestCircle: 
  def test_one(self): 
    assert True


#*=== 
def test_circle_area(): 
  circle = Circle(4)
  assert circle.area() == 16 * math.pi #3.1416

#*===
def test_circle_perimeter(): 
  circle = Circle(2)
  assert circle.perimeter() == 4 * math.pi #3.1416

#*===
def test_triangle_area(): 
  triangle = Triangle(2, 5, 4)
  assert triangle.area() == 20 / 2


#!=== === Execute === ===
if __name__ == "__main__":
  print("All Tests....")
  test_circle_area() 
  test_circle_perimeter()
  test_triangle_area()