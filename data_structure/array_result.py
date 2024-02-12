######
#! === Array ===
######
from create_array import Array
from array_bidimensional import Grid


menu = Array(10)
twoDimension = Grid(3,3)


# = Transform int(row & col) =
def print_dimension(values):
  for row in range(values.get_height()):
    for col in range(values.get_width()):
      values[row][col] = row * col
      
  return values


if __name__ == "__main__":
  #? = Array =
  print("1D First Dimension")
  iterator = menu.__iter__()
  print(menu)
  print(menu.items)
  print("Length:", menu.__len__())
  print("string:", menu.__str__())
  for item in iterator:
    print("Iter:", item)
  print("GetItem:", menu.__getitem__(1))
  print("SetItem:", menu.__setitem__(2,"Marvel"))
  #? = Array two-dimensional =
  print("2D Two Dimension")
  print(twoDimension);
  print(print_dimension(twoDimension)); # Transform int(row & col)
  print(twoDimension.get_height())
  print(twoDimension.get_width())
  print(twoDimension.__getitem__(1))
  print(twoDimension.__str__())
  print(twoDimension.length())

