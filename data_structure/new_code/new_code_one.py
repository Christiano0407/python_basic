## #TODO: === Algorithms (Big O Notation -time-) & Structure Data & Patterns Design (1) === #
from array import array

list_num = [2, 4, 7, 8, 10, 15, 18, 25]

#? === Est.Data: Array Dynamic (Changes) ===  
#Big O: O(1): Constant
list = [4, 7, 10]
print("list", list)
list.append(5); # O(n):Lineal
list.append(25);
print("New List:", list)

#? === Est.Data: Array Static (Not Changes) === 
# Big O: O(n): Lineal - log Num -
array_static = array("i", [1, 4, 5, 7, 18])
print("Static:", array_static)

#? ===== Est.Data: Array [String - characters] ======
string = "Never Stop Learn" # O(n)
new_string = ""
# Big O: O(n2) => O(n*n) 
for character in string: 
  new_string += character # O(n)

print(new_string) # Big O: O(n) - Lineal -

#? === Algorithm: two-pointer technique (Patrón de Dos Apuntadores) ===
# == Buscar un par que sume un valor específico en un arreglo ordenado ==
# = Big O: O(n) - Lineal (array) - =
def two_sum(array, target): 
  left,right = 0, len(array) - 1

  while left < right: 
    current_value = array[left] + array[right]
    if current_value == target: 
      return [array[left], array[right]]
    elif current_value < target: 
      left += 1
    else: 
      right -= 1

  return f"{None}: Your Sum it's not possible (Num not exist in this list)."

print(two_sum(list_num, 29 ))
print(two_sum(list_num, 27 ))
print(two_sum(list_num, 13 ))

#! === Exercise 1: Verifying Alien Dictionary - Two-pointer Technique - ===
def ordenar_lexicográficamente(palabras, orden_alfabetico):
  orden = {letra: i for i, letra in enumerate(orden_alfabetico)};
  
  for i in range(len(palabras) - 1):
    palabra_actual = palabras[i]
    palabra_siguiente = palabras[i + 1]

    for j in range(min(len(palabra_actual), len(palabra_siguiente))):
      if palabra_actual[j] != palabra_siguiente[j]:
        if orden[palabra_actual[j]] > orden[palabra_siguiente[j]]:
          return False
        break
    else:
      if len(palabra_actual > len[palabra_siguiente]):
        return False

  return True


if __name__ == "__main__":
  palabras_1 = ["alma", "luisa", "betty", "christina"]
  palabras_2 = ["natalia", "luisa", "alma", "betty", "christina"]

  orden_alfabetico_1 = "abcdefghijklmnopqrstuvwxyz"
  orden_alfabetico_2 = "nlabcdefgijkmnopqrstuvwxyz"

  print(ordenar_lexicográficamente(palabras_1, orden_alfabetico_1))
  print(ordenar_lexicográficamente(palabras_2, orden_alfabetico_2))
