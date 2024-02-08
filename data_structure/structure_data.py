##########
#TODO: === Structure Data (Estructura de Datos) ===
#* === ==== Algorithms & POO ==== ===
#! === Collección: Grafos, Jerárquicas, Lineales, Desordenadas.
########################
#? === Types Collections === Lineal 
list = ["Books", "Games", "Dogs", "Cats", "Marvel", "DC", "Technology", "Business"]
print(type(list)); 
list.append("Anime")
print(list)
list.sort()
print(list)
list.pop()
print(list)
list.insert(8, "Tech IA");
print(list)

#=== ===
def pyramid_sum(lower, upper, margin=0):
  blanks = " " * margin
  print(blanks, lower, upper)
  if lower > upper: 
    print(blanks, 0)
    return 0
  else: 
    result = lower + pyramid_sum(lower + 1, upper, margin + 4)
    print(blanks, result)
    return result
  

pyramid_sum(1, 4)
