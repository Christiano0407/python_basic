#####
# Algorithm: O(log n) logarithm
# Pattern Design: Method Factory
# POO : Herencia / Polimorfismo
#lista_inicial: La lista que se va a ordenar.
#criterio: Una función lambda que define el criterio de ordenamiento.
#####
class OrderList: 
  def __init__(self, initial_list): 
    self._list = initial_list
    #self._order()

  def _order(self): 
    self._list.sort()

  def __len__(self): 
    return len(self._list)
  
  def __getitem__(self, element): 
    return self._list[element]
  
  def __str__(self):
    return str(self._list)
  

class ListOrderCriterion(OrderList): 
  def __init__(self, initial_list, criterion):
    super().__init__(initial_list)
    self._criterion = criterion
    self._order()
  
  def _order(self):
    self._list.sort(key=self._criterion) 


## Call POO ##
if __name__ == "__main__":
 order_list = [9, 7, 4, 25, 15, 2]
 order_criterion = lambda x: len(str(x))
 length_order_list = ListOrderCriterion(order_list, order_criterion)
 print(length_order_list)