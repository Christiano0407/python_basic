### POO - Search Binary ## ==== algorithm "O(log n) Logarítmica" ===== ##

class Numbers: 
  def __init__(self, numbers):
    self.numbers = numbers

  #Algorithm Binary Search#
  def search_binary(self, number): 
    init_middle = 0
    final_middle = len(self.numbers) - 1

    while init_middle <= final_middle:
      middle = (init_middle + final_middle) // 2   #Point Middle
      if self.numbers[middle] == number:
        return middle
      elif number < self.numbers[middle]: 
         final_middle = middle - 1
      else: 
        init_middle = middle + 1
    return -1
  


## Call POO Numbers## 
if __name__ == "__main__": 
  list_numbers = [4, 5, 7, 10, 15, 25]
  lists = Numbers(list_numbers)
  number_user = int(input("User: Please, give me a number: "))
  position =  lists.search_binary(number_user)
  if position != -1: 
     print(f"Your number {number_user} this in position {position} ")
  else:
    print("Sorry! your number not add in the list. Please, give me your number.")

