########
#Todo: 1) POO ====== === Nodos (Messy List / Lista Desordenada) & Single List === ======
#########
#? ====== === Nodos === ======
class Node(): 
  def __init__(self,data,next_node=None):
   '''
   En esta versión corregida, next_node es un parámetro opcional que por defecto es None. Esto significa que si no se proporciona un nodo siguiente al crear un nuevo nodo, su atributo next se establecerá en None. 
   '''
   self.data = data
   self.next = next_node



#*==== Call ====
""" node_1 = None
node_2 = Node("A", None)
node_3 = Node("B", node_2)
node_4 = Node("C", node_2)
node_5 = Node("Plus", None)
node_6 = Node("p", node_3)
node_7 = Node("p", None)


print(node_2)
print(node_2.data)
print(node_3.next)
print(node_3.next.data)
print(node_4.next.data)

while node_4 != None:
  print(node_4.data)
  node_4 = node_4.next """


