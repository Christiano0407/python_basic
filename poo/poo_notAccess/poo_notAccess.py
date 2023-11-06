## POO #2
#Not Access: POO - Class = Instance #
class Player:
  def __init__(self, name, team):
    self.__name = name
    self.team = team

  def score(self):
    return F"Goal!! {self.__name}"
  
  def teams(self):
     return f"Player in: {self.team}"
  

## < 2) Multi Herencia > ##
class Merchandise:
   def __init__(self, product):
      self.product = product

   def payProduct(self):
      return "I Use this boots: " + self.product 
  

## < 1) Herencia > ##
class Country(Player, Merchandise): 
  def __init__(self,name,team,product,selection,brand,stadium,salary): 
     super().__init__(name, team) #super is Father - not self
     Merchandise.__init__(self,product) #yes, self
     self.selection = selection
     self.brand = brand
     self.stadium = stadium
     self.__salary = salary

  def newBrand(self):
     return f"The {self.selection} have new Brand: {self.brand}"
  
  def playerSalary(self):
     return f"The {self.team} pay in salary: {self.__salary}"
  # Heredar y Polimorfismo (heredar y llamar de acurdo al contexto) #
  def teams(self):
     return super().teams() + " The Brand: " + self.brand + " Stadium: " + self.stadium 
  # Multi Herencia
  def products(self):
     return super().payProduct
  # Method Static


# Variable #
#my_player = Player("David Beck", "Manchester United")
my_selection = Country("David Beckam","Manchester United","M10 Adidas","England", "Adidas", "Wembley", 1000)
my_stadium = Country("CR7", "Manchester United","Nike R90","Portugal", "Nike", "DoDragon", 500)

## Call POO ##
if __name__ == "__main__":
    #myPlayers = my_player.score()
    #players = my_player.teams()
    #print(myPlayers)
    #print(players)
    selections = my_selection.selection
    selection_player = my_selection.teams()
    selection_info = my_selection.brand
    selection_score = my_selection.score()
    #name_selection = my_selection.__salary
    selection_player = my_selection.playerSalary()
    new_boots = my_selection.payProduct()
    print("My Selection:",selections)
    print("Team:",selection_player)
    print("Info:", selection_info)
    print("Score:", selection_score)
    print("Salary:", selection_player)
    print(my_selection.teams())
    print(new_boots)

