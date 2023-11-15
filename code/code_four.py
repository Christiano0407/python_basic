####
# POO (Programming Oriented Objects) 
# Patter Design: Factory Method
# Algorithm: O(log n) => Search Binary 
## Estamos trabajando con una lista de precios de acciones ordenada y queremos buscar el precio de una acción específica.
####
#=== Add: Search - Target #
class FinancialSearchAlgorithm: 
  def search(self, stock_prices, target_stock): 
    pass

#=== Add: Algorithm #
class BinaryFinancialSearch(FinancialSearchAlgorithm):
  def search(self, stock_prices, target_stock):
    low_num = 0
    high_num = len(stock_prices) - 1

    while low_num <= high_num: 
      middle_num = (low_num  + high_num ) // 2
      middle_stock = stock_prices[middle_num]

      if middle_stock["symbol"] == target_stock:
        return middle_stock # Devolver el diccionario completo de acciones
      elif middle_stock["symbol"] < target_stock:
        low_num = middle_num + 1
      else: 
        high_num = middle_num - 1

    return None # Devolver None si no se encuentra el objetivo (Target)


#=== Search Algorithm (Pattern: Factory Method) #
class financialSearchFactory:
  @staticmethod
  def create_search_algorithm(type_algorithm): 
    if type_algorithm == "binary":
      return BinaryFinancialSearch()
    

## Call Stock & POO ##
if __name__ == "__main__": 
  #Market Stock Prices Data  
  stock_prices_list = [
    {"symbol": "APPL", "price": 187.44},
    {"symbol": "MSFT", "price": 370.27},
    {"symbol": "GOOG", "price": 135.41},
    {"symbol": "AMZN", "price": 145.80},
    {"symbol": "NVDA", "price": 496.56},
    {"symbol": "META", "price": 336.31},
    {"symbol": "BRK", "price": 537400.05},
    {"symbol": "TSLA", "price": 237.41},
    {"symbol": "LLY", "price": 610.82},
    {"symbol": "V", "price": 246.94},
  ]
  #Target
  target_stock_symbol = "TSLA"
  target_stock = "APPL"
  #Create Instance
  financial_factory = financialSearchFactory
  financial_algorithm = financial_factory.create_search_algorithm("binary")
  #Result Prices
  prices_market = financial_algorithm.search(stock_prices_list, target_stock)

  if prices_market is not None:
    print(f"The actions of Market:{target_stock} have a price ${prices_market['price']}")
  else: 
    print(f"Sorry! Your target is not exist!")
  

 
  