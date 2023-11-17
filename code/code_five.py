#########
#Use: POO (Programming Oriented Object)
#? Use: O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
#! Este código implementa el algoritmo Merge Sort, que es un algoritmo de ordenamiento divide y vencerás que funciona dividiendo la lista en dos mitades, ordenando cada mitad recursivamente y luego fusionando las dos mitades ordenadas en una lista ordenada.
#? Use: Patrón de diseño Strategy
#########
class MergeSort: 
  def __init__(self, lst):
    self.lst = lst
  #Merge: Algorithm 
  def merge(self, left_list, right_list): 
    order_list = []
    index_left = 0
    index_right = 0

    while index_left < len(left_list) and index_right < len(right_list): 
      if left_list[index_left] < right_list[index_right]: 
        order_list.append(left_list[index_left])
        index_left += 1
      else:
        order_list.append(right_list[index_right])
        index_right += 1 

    order_list += left_list[index_left:]
    order_list += right_list[index_right:]

    return order_list

 #Algorithm: Merge Sort
  def merge_sort(self, lst=None):
    if lst is None: 
      lst = self.lst

    if len(lst) <= 1: 
      return lst
    
    middle = len(lst) // 2
    left_list = self.merge_sort(lst[:middle])
    right_list = self.merge_sort(lst[middle:])

    return self.merge(left_list, right_list)


if __name__ == "__main__":
  my_list = [4, 2, 5, 7, 9, 10, 15, 20, 25, 50]
  #print(list)
  #print(type(list))
  algorithm_sort = MergeSort(my_list)
  sort_order_list = algorithm_sort.merge_sort()
  print(sort_order_list)
