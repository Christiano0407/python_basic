### === ==== 2) POO - Search Binary ## ==== algorithm "O(log n) Logarítmica" ===== === ###
## Instance of Class POO##
class ListBinary: 
  def __init__(self, numbers): 
    self.numbers = numbers

#Algorithm
  def search_number(self, number): 
    try:
      init_middle = 0
      final_middle = len(self.numbers) - 1

      while init_middle <= final_middle: 
        middle = (init_middle + final_middle) // 2 ## Middle Point
        if self.numbers[middle] == number: 
          return middle
        elif number < self.numbers[middle]: 
          final_middle = middle - 1
        else: 
          init_middle = middle + 1
      raise ValueError(f"Sorry, but your {number} not exist in this list. Please, give me a number. ")
    
    except ValueError as e:
      print(e)
    finally:
      print("Sorry!! Your number, not exist.")


#=== Herencia Polimorfismo ===
class OrderList(ListBinary): 
  def __init__(self, numbers):
      super().__init__(numbers)
      self.numbers.sort() #Order Method


## ===Call POO === ##
if __name__ == "__main__":
  number_all = [2, 4, 6, 8, 10] 
  listOne = ListBinary(number_all)
  listTwo = OrderList([listOne])
  print(listOne)