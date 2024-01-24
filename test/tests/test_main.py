import pytest
from test.main import sum, call_name, add, divide
import test.main as my_rest


#*===
def test_sum():
  assert sum(5, 5) == 10
  assert sum(7, 4) == 11
  assert sum(-5, -5) == -10
  assert sum(0, 0) == 0
  #assert sum(-1, 2) == 0 # = Assertion Error =
  

#*===
def test_name(): 
  assert call_name("Luisa") 


#*===
def test_add():
  assert add(10,10) == 20
  assert add(-1,1) == 0


#*===
def test_divide(): 
  assert divide(50, 2) == 25
  assert divide(100, 4) == 25 
  assert divide(10, 2) == 5


#*===
def test_rest(): 
  result = my_rest.rest(5, 1)
  assert result == 4



#! ====== Execute ======
if __name__ == "__main__":
  print("Previous Test...") 
  test_sum()
  test_name()
  test_add()
  test_divide()
  test_rest()
  print("All Tests Passed...:)") 