#===Class
class Pikachu: 
  type = "electric & Lightning"

  def __init__(self, name, level, health):
    '''
    Create Variables of Class. Parameters & Objects
    '''
    self.name = name
    self.level = level
    self.health = health
  #===Method===
  def __str__(self) -> str:
    return f"This Pokemon is {self.name} with level {self.level} and his {self.health}"
  
  def __repr__(self) -> str:
    return  f"Is {self.name} and Type of Pokemon is: {self.type} and increment level {self.level}."
  
  def increment_power(self, amount): 
    self.level += amount


#===Object & Variables of Instance & Object===
pokemon_1 = Pikachu("Pikachu", 9, 8) 
pokemon_2 = Pikachu("Charmander", 5, 5)
increment = pokemon_2.increment_power(5)

#=== Call ===
print(pokemon_1)
print(repr(pokemon_2))