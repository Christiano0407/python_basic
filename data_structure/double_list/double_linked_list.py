####
#* ==== Lista: Doubly Linked List (Lista Doblemente Enlazada)  ( cada nodo tiene una referencia tanto al nodo siguiente como al nodo anterior) - Structure Of Data - ====
######
from double_node import Node
import pandas as pd
import os


#* === Data Base ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data", "mcu_box_office.csv")
df = pd.read_csv(file_path)


#* ==== Poo Class: Double Linked List ====
class DoubleLinkedList: 
  def __init__(self): 
    self.head = None

  def append(self, data):
    '''
    Agrega: Final de la lista.
    '''
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    last_node = self.head

    while last_node.next:
      last_node = last_node.next

    last_node.next = new_node
    new_node.prev = last_node

  def prepend(self, data):
    '''
    Agrega: Al Principio de la lista. 
    '''
    new_node = Node(data)
    new_node.next = self.head
    if self.head: 
      self.head.prev = new_node
    self.head = new_node

  def print_list(self):
    current_node = self.head
    while current_node: 
      print(current_node.data)
      current_node = current_node.next


##! ====== Variables and Data ======
data_new = df.head(12)
new_list = df.head(2)

double_linked_list = DoubleLinkedList()

for index, row  in data_new.iterrows():
  double_linked_list.append(row.to_list())

##? === ===== Main & Call ===== ===
double_linked_list.prepend(new_list)
double_linked_list.print_list()
