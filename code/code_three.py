#####
# Algorithm: O(log n) logarithm
# Pattern Design: Method Factory
#####
class OrderPrice:

  def __init__(self, name, actual_price, historical_price):
    self.name = name
    self.actual_price = actual_price
    self.historical_price = historical_price
  #Return "Str"
  def __repr__(self) -> str:
    return f"OrderPrice({self.name}, {self.actual_price}, {self.historical_price})"
  #Compare Two Elements
  def __lt__(self, other_price):
    return self.actual_price < other_price.actual_price
  
  def __gt__(self, price_other):
    return self.actual_price > price_other.actual_price
  
##Polymorphism
class PortfolioPrice(OrderPrice):
  def __init__(self,name, actual_price, historical_price ,actions):
    super().__init__(name, actual_price, historical_price)
    self.actions = actions

  def __repr__(self) -> str:
    return f"Portfolio: {self.actions}"
  # Algorithm: Search Binary - O(log n)
  def search_actions_more_price(self):
    return max(self.actions)
  
#===#
price_action = [
   OrderPrice("Microsoft", 100, 90),
   OrderPrice("Google", 120, 110),
   OrderPrice("Disney", 150, 140),
   OrderPrice("Apple", 250, 240)
]

#===#
if __name__ == "__main__":
  portfolio_actions = PortfolioPrice("PortfolioActions", 0, 0, price_action)
  actions_with_more_price = portfolio_actions.search_actions_more_price()
  print(f"Actions Price: {actions_with_more_price}")
