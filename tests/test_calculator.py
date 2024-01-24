###
#Todo: === Tests (02): Calculator ===
######
from calculator import add


def tests_add(): 
  assert add(5, 1) == 6
  assert add(7, 4) == 11
  assert add(-5, -5) == -10 
  assert add(0, 0) == 0
  assert add(1, 1) == 2  
  #assert add(-1, 2) == 0 # = Assertion Error = 


#* ==== Main ====
if __name__ == "__main__":
  print("Previous Test...") 
  tests_add()
  print("All Tests Passed...:)")