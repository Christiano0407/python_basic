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

 def prepend(self, data):
   new_node = Node(data)
   new_node.next = self.head
   self.head = new_node

 def search(self,movie, movie_director=None): 
   current_node = self.head
   
   while current_node:
    if current_node.data[0] == movie or (movie_director and  current_node.data[14] == movie_director):
      return current_node.data # Devuelve el nombre de la película y su índice
    current_node = current_node.next

   return False

 def delete(self, value):
   current_node = self.head
    # Caso especial si el nodo a eliminar es la cabeza (Head)
   if current_node is not None and current_node.data[0] == value:
     self.head = current_node.next
     current_node = None
     return
    # Buscar el nodo a eliminar y ajustar los enlaces
   while current_node is not None:
     if current_node.data[0] == value:
       break
     prev_node = current_node
     current_node = current_node.next

   if current_node == None:
     print("Hello, Your Value it's not present in this List.")
     return 
    
   prev_node.next = current_node.next
   current_node = None

 def insert(self, data, position): 
   new_node = Node(data)
   if position == 0:
     new_node.next = self.head
     self.head = new_node
     return
   
   current_node = self.head
   for _ in range(position - 1): 
     if current_node is None:
       raise IndexError("This element of Data, is out of Range")
     current_node = current_node.next

   if current_node is None: 
     raise IndexError("This element is out of range of Data")
   
   new_node.next = current_node.next
   current_node.next = new_node

 def get_position(self, data):
   current_node = self.head
   position = 0

   while current_node: 
     if current_node.data[0] == data:
       return position
     position += 1
     current_node = current_node.next

   raise ValueError("Data Not Found In This List")
   #return -1
 
 def insert_after(self, node, data):
   if node is None:
     print("Previous Node Not Be None")
     return
   new_node = Node(data)
   new_node.next = node.next
   node.next = new_node

 def print_list(self):
   current_node = self.head
   while current_node:
     print(current_node.data)
     current_node = current_node.next



#* ===== === Variables ===
elements_data = df.head(15)
linked_list = LinkedList()

for index, row in elements_data.iterrows(): 
  #linked_list.append(row["Movie"])
  linked_list.append(row.to_list())

""" for index, row in elements_data.iterrows(): 
    linked_list.append(row.to_list(),[row["Movie"], index, row["Director"]])  """ 


#!==== === === Execute === === ====
if __name__ == "__main__": 
  #print(linked_list)
  linked_list.print_list()
  #linked_list.delete(elements_data.iloc[1].tolist())
  print(linked_list.search("Thor", None))
  print(linked_list.search(None, "Jon Favreau"))
  print(linked_list.search(None, "Louis Leterrier"))
  print(linked_list.search("The Avengers", None))
  print(f"Position Of Movie: {linked_list.get_position('Avengers: Age of Ultron')}"); 
  print(f"Position Of Movie: {linked_list.get_position('The Incredible Hulk')}"); 
