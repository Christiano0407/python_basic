#===Class
class Pikachu: 
  type = "electric & Lightning" #Attribute
  attack_move = "Thunder"
  #=== Methods of Instance ===
  def __init__(self, name, level, health, power):
    '''
    Create Variables of Class. Parameters & Objects
    Los métodos de instancia operan en instancias específicas de la clase
    Permite crear objetos únicos con características individuales.
    '''
    self.name = name
    self.level = level
    self.health = health
    self.power = power

  def __str__(self) -> str:
    return f"This Pokemon is {self.name} with level {self.level} and his {self.health} have power: {self.power} and attack: {self.attack_move}"
  
  def __repr__(self) -> str:
    return  f"Is {self.name} and Type of Pokemon is: {self.type} and increment level {self.level}."
  
  def increment_power(self, amount) -> int: 
    self.level += amount

  def attack_power(self, powerAttack) -> int:
     self.power -= powerAttack
     self.level -= powerAttack
  #==== Method Of Class ====
  @classmethod
  def method_of_class(cls) -> str:
    '''
    los métodos de clase operan en la clase en sí.
    '''
    return cls.type



#===Object & Variables of Instance & Object===
pokemon_1 = Pikachu("Pikachu", 9, 8, 10) 
pokemon_2 = Pikachu("Charmander", 5, 5, 6)
increment = pokemon_2.increment_power(5)
attack = pokemon_1.attack_power(2)
pokemon_3 = Pikachu("Newto", 10, 10, 10)
new_method = pokemon_3.method_of_class()

#=== Call ===
print(pokemon_1)
print(repr(pokemon_2))
pokemon_2.attack_power(3)
print(pokemon_2)
print("New Method: ", new_method)