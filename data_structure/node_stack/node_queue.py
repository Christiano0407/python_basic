######
#?: === Implementación de Queue basado en Nodos ===
######
import pandas as pd
import os

#* === Data Base ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data", "mcu_box_office.csv")
df = pd.read_csv(file_path)
data_head = df.head(5)
data_iloc = df.iloc[10:15]

#* === Node ===
class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None


#* ==== Stack - Queue - ====
class QueueNode:
  def __init__(self): 
     self.front = None
     self.prev = None

  def enqueue(self, item):
    new_node = Node(item)
    if self.prev is None: 
      self.front = new_node
      self.prev = new_node
    else:
      self.prev.next = new_node
      self.prev = new_node

  def dequeue(self): 
    if self.is_empty(): 
      raise IndexError("Queue is Empty. Sorry")
    front_node = self.front
    self.front = self.front.next
    if self.front is None:
      self.prev = None

    return front_node.data 
  
  def peek(self): 
    if self.is_empty():
      raise IndexError("Sorry! Your Queue Stack is Empty.")
    return self.front.data

  def is_empty(self): 
    return self.front is None
  
  def size(self): 
    count = 0
    current = self.front
    while current: 
      count += 1
      current = current.next
    return count


#* ====== === Main === ======
if __name__ == "__main__": 
  node_queue = QueueNode()
  
  node_queue.enqueue(data_iloc)

  print("Node Queue Peek:", node_queue.peek())
  print("Node Queue Data Size:",node_queue.size())

  """ while not node_queue.is_empty(): 
    print("Element:",node_queue.dequeue()) """
