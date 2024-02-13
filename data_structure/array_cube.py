######
#! === Array: Tres Dimensiones (Cube: Axis Z - Eje Z - ) = (Methods and Behavior or Conduct) (Init & Limit) ===
######
from create_array import Array
from array_bidimensional import Grid


class Cube:
  def __init__(self, rows, columns, axis_z, array_value="None"): 
    self.data = Array(axis_z)
    for axis in range(axis_z):
      self.data[axis] = Grid(rows, columns, array_value)

  def get_height(self):
    length = len(self.data)
    return length
  
  def get_width(self):
    # Accede a la primera capa (en z)
    first_layer = self.data[0]
    # Obtiene la primera fila (en y) de la primera capa
    first_row = first_layer[0]
    # Devuelve la longitud de la primera fila
    width = first_row.__len__()
    return width

  
  def get_axis_z(self): 
    z_axis = len(self.data)
    return z_axis
  
  def __getitem__(self, index):
    return self.data[index]
  
  def __str__(self) -> str: 
    result = ""
    
    for row in range(self.get_height()): 
      for col in range(self.get_width()):
        for axis_z in range(self.get_axis_z()): 
          result += str(self.data[row][col][axis_z]) + " "

          result += "\n"

    return result


