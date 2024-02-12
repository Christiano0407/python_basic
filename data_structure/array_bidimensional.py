######
#! === Array: Dos Dimensiones (Grid) = (Methods and Behavior or Conduct) (Init & Limit) ===
######
from create_array import Array

class Grid:
  def __init__(self, rows, columns, array_value="None"):
    self.data = Array(rows)
    for row in range(rows): 
      self.data[row] = Array(columns, array_value)

  def get_height(self):
    length = len(self.data)
    return length
  
  def get_width(self):
    width = len(self.data[0])
    return width
  
  def __getitem__(self, index): 
    return self.data[index]
  
  def __str__(self) -> str:
    result = ""

    for row in range(self.get_height()): 
      for col in range(self.get_width()):
        result += str(self.data[row][col]) + " "
        
      result += "\n"

    return result
  
  def length(self): 
    fill_length = self.data.__len__()
    return fill_length
