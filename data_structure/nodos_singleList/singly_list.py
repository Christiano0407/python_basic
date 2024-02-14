########
#Todo: 2) POO ====== === Nodos (Messy List / Lista Desordenada) & Single List === ======
#########
#? ===== === Singly Linked List === =====
from nodos_singleList import Node


class SinglyLinkedList: 
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


#** ==== Create Linked List ==== *
linked_list = SinglyLinkedList()

#** ==== Add elements to the Linked List ==== *
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.append("Plus")
linked_list.append("Alma")
linked_list.append("Disney")
linked_list.append("Amazon")

#** ==== Add elements to the Linked List ==== *
linked_list.print_list()