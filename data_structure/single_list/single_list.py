from read_data import df
from nodos import Node


class LinkedList:
 def __init__(self):
  self.head = None

 def append(self, data): 
  new_node = Node(data)
  if self.head is None:
    self.head = new_node
    return
    
  last_node = self.head

  while last_node.next:
    last_node = last_node.next
  last_node.next = new_node

 def print_list(self):
  current_node = self.head
  while current_node:
    print(current_node.data)
    current_node = current_node.next



#* === Variables ===
linked_list = LinkedList()
elements_data = df.head(5)
for index, row in elements_data.iterrows(): 
  linked_list.append(row.to_list())


#!==== === Execute === ====
if __name__ == "__main__": 
  #print(linked_list)
  linked_list.print_list()
