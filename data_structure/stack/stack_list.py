#### 
#?: Stack: === Un "stack" es una estructura de datos que sigue el principio de LIFO (Last In, First Out), lo que significa que el último elemento que se inserta es el primero en ser eliminado. Funciona como una pila de platos en la que solo puedes agregar o quitar el plato más superior. ===
#####
#* === Data Base ===
import pandas as pd
import os


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data", "mcu_box_office.csv")
data_base = pd.read_csv(file_path)
new_head_data = data_base.head(4) # = Traer Data =
new_iloc_data = data_base.iloc[10:15] # = Traer Data por Individual =

#* ==== Stack ====
class Stack: 
  def __init__(self):
    self.items = []

  def push(self, item):
    '''
    Agregar Elementos
    '''
    self.items.append(item)

  def pop(self):
    '''
    Para quitar y devolver el elemento superior,
    '''
    if not self.is_empty():
      return self.items.pop()
    else: 
      raise IndexError("Sorry! Used Pop from Empty Stack")
    
  def peek(self):
    '''
    Para obtener el elemento superior sin quitarlo
    '''
    if not self.is_empty():
      return self.items[-1]
    else: 
      raise IndexError("Peek, from Empty Stack")  
    
  def is_empty(self): 
    '''
    Para verificar si el stack está vacío
    '''
    return len(self.items) == 0
  
  def size(self):
    '''
    Para obtener el tamaño del stack.
    '''
    return len(self.items)


  #* ==== Main & Variables ====
if __name__ == "__main__": 
  stack = Stack()

  first_data = data_base.head(1)
  second_data = data_base.head(2)
  three_data = data_base.head(3)
  four_data = data_base.head(6)

  stack.push(first_data)
  stack.push(second_data)
  stack.push(three_data)
  print(f"Stack {stack.peek()}")
  print(f"Stack Size: {stack.size()}")
  print(f"Stack Empty: {stack.is_empty()}")

  while not stack.is_empty():
    print(f"Pop Stack: {stack.pop()}")  

  print(f"Stack Size: {stack.size()}")
  stack.push(four_data)
  print(f"New Stack {stack.peek()}")

  print(f"New Data Head: {new_head_data}")
  print(f"New Data Iloc:{new_iloc_data}");
