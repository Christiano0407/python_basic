####
#TODO: === Test Fruit: (02) === Use: Pytest - Fixture ===
#######
import pytest
from test.fruits import Fruit, FruitSalad


#? >= Arrange - Fixture (Before call Test) - <=
@pytest.fixture
def fruit_bowl():
  return [Fruit("Apple"), Fruit("Banana"), Fruit("Avocado")]

#*===
def test_fruit(fruit_bowl): 
  #Act
  fruit_salad = FruitSalad(*fruit_bowl)

  #assert
  assert all(fruit.cubed for fruit in fruit_salad.fruit) 


  if __name__ == "__main__":
    test_fruit() 
