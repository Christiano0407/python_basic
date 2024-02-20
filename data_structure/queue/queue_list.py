######
#?: === Queue - (Primero en entrar...primero en salir): Una cola (queue) es una estructura de datos que sigue el principio de "primero en entrar, primero en salir" (FIFO, por sus siglas en inglés: First In, First Out). Funciona como una fila de personas en un supermercado: la primera persona que llega es la primera en ser atendida. ===
#* Stack: Stack: En una pila, el último elemento que se inserta es el primero en ser eliminado (LIFO, Last In, First Out).
######
import pandas as pd
import os

#* === Data Base ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data", "mcu_box_office.csv")
df = pd.read_csv(file_path)
data_head = df.head(5)
data_iloc = df.iloc[10:15]


#* ===== Queue =====
class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    if not self.is_empty():
      return self.items.pop(0)
    else: 
      raise IndexError("dequeue: Last Element empty")
    
  def peek(self):
    if not self.is_empty():
      return self.items[0]
    else: 
      raise IndexError("Peek (Method) is Empty")
    
  def is_empty(self):
    return len(self.items) == 0
  
  def size(self):
    return len(self.items)



#! ====== Main & Variables =====
if __name__ == "__main__":
  queue = Queue()
  print("Head Data: ", data_head)
  print("Iloc Data: ", data_iloc)

  new_data = df.iloc[15:20]
  new_data_one = df.iloc[21:-1]

  """ for index, row in new_data.iterrows(): 
    queue.enqueue(row) """

  """ for index, row in new_data_one.iterrows(): 
    queue.enqueue(row) """

  queue.enqueue(new_data)
  queue.enqueue(new_data_one)
  
  print(f"New Queue Data: {queue.peek()}")
  print(f"New Queue Data One: {queue.items}")

  while not queue.is_empty(): 
    print(f"Last element: {queue.dequeue()}")

  print(f"Size Queue Data: {queue.size()}")
