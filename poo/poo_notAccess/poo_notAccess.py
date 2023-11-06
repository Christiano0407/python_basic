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
  

## < Herencia > ##
class Country(Player): 
  def __init__(self, name, team, selection, brand, stadium, salary): 
     super().__init__(name, team) #super is Father
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
     return super().teams() + " The Brand: " + self.brand + " Stadium: " + self.stadium + " and players wining in salary: " + str(self.__salary)
  # Method Static


# Variable #
#my_player = Player("David Beck", "Manchester United")
my_selection = Country("Beck", "Manchester", "England", "Adidas", "Wembley", 1000)
my_stadium = Country("CR7", "Manchester", "Portugal", "Nike", "DoDragon", 500)

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

    print("My Selection:",selections)
    print("Team:",selection_player)
    print("Info:", selection_info)
    print("Score:", selection_score)
    print("Salary:", selection_player)
    print(my_selection.teams())

