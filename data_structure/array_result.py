######
#! === Array ===
######
from create_array import Array

if __name__ == "__main__":
  menu = Array(10)
  iterator = menu.__iter__()
  print(menu)
  print(menu.items)
  print("Length:", menu.__len__())
  print("string:", menu.__str__())
  for item in iterator:
    print("Iter:", item)
  print("GetItem:", menu.__getitem__(1))
  print("SetItem:", menu.__setitem__(2, 4))
  
