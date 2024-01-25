####
#TODO: === Test Fruit: (01) === Use: Pytest
######
class Fruit:
  def __init__(self, name):
    self.name = name
    self.cubed = False

  def cube(self): 
    self.cubed = True


class FruitSalad: 
  def __init__(self, *fruit_bowl): 
    self.fruit = fruit_bowl
    self._cube_fruit()

  def _cube_fruit(self): 
    for fruit in self.fruit: 
      fruit.cube()