######
#TODO === ==== Array (Structure Of Data) ==== ===
######
from create_array import Array
from array_bidimensional import Grid
from array_cube import Cube


menu = Array(10)
twoDimension = Grid(3,3)
threeDimension = Cube(2,2,2)


# = 2D: Transform int(row & col) =
def print_dimension(values):
  for row in range(values.get_height()):
    for col in range(values.get_width()):
      values[row][col] = row * col
      
  return values

# = 3D : Transform int(row & col) =
def print_three_dimension(value):
  for row in range(value.get_height()):
    for col in range(value.get_width()):
      for z_axis in range(value.get_axis_z()):
        value[row][col][z_axis] = row * col * z_axis
      
  return value

def calculate_values_three_dimension(value):
    new_value = Array(value.get_height())
    for row in range(value.get_height()):
        new_value[row] = Array(value.get_width())
        for col in range(value.get_width()):
            new_value[row][col] = Array(value.get_axis_z())
            for z_axis in range(value.get_axis_z()):
                new_value[row][col][z_axis] = row * col * z_axis
    return new_value



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
  #? == Array two-dimensional ==
  print("2D Two Dimension")
  print(twoDimension);
  print(print_dimension(twoDimension)); # Transform int(row & col)
  print(twoDimension.get_height())
  print(twoDimension.get_width())
  print(twoDimension.__getitem__(1))
  print(twoDimension.__str__())
  print(twoDimension.length())
  #? === Array Three Dimensions ===
  print("3D Dimension")
  print(threeDimension)
  print(print_three_dimension(threeDimension))
  print(calculate_values_three_dimension(threeDimension))

