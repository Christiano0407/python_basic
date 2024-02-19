####
#* ==== lista:  Enlazada Circular (Bucle: Retorna al primer Nodo) - Structure Of Data - ====
######
import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data", "mcu_box_office.csv")
df = pd.read_csv(file_path)

class Node(): 
  def __init__(self, data, next_node=None):
    self.data = data
    self.next = next_node


class LinkedListCircle:
  def __init__(self): 
    self.head = None

  def append(self, data): 
    new_node = Node(data)
    if not self.head: 
      self.head = new_node
      new_node.next = self.head # - Cada nuevo elemento/Index => Cabeza Principal - #
    else: 
      current = self.head
      while current.next != self.head: 
        current = current.next
      current.next = new_node
      new_node.next = self.head

  def print_list(self): 
    if not self.head: 
      return
    current = self.head
    while True: 
      print(current.data)
      current = current.next
      if current == self.head:
        break


#! ==== === Variables Of Data === ====
data_base = df.head(10)
circle_linked_list = LinkedListCircle()
for index,row in data_base.iterrows():
  circle_linked_list.append(row.to_list())

#? ======== Main & Call ==========
circle_linked_list.print_list()

