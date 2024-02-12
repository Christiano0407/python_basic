##########
#TODO: === Structure Data (Estructura de Datos) ===
#* === ==== Algorithms & POO ==== ===
#* === Collección: Grafos, Jerárquicas, Lineales, Desordenadas.
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

#! === Función Recursiva (Atrás para adelante) ===
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

#! === Types Of Data Structure ===
list_types = ["Books", "Games", "Dogs", "Cats", "Marvel", "DC", "Technology", "Business"]
list = list_types
print(type(list))

tuples = "Books", "Games", "Dogs", "Cats", "Marvel", "DC", "Technology", "Business"

my_tuple = tuple(tuples)
my_tuples = (4, 7, "Luisa", "Pamela")
print(type(my_tuple))
print(type(my_tuples))


dicts = {"name": "Luisa", "age": 33, "Work": "Journalist"}
my_dict = dict(dicts)
print(type(my_dict))

sets = "Books", "Games", "Dogs", "Cats", "Marvel", "DC", "Technology", "Business", 4, 7
my_set = set(sets)
my_sets = {"Natalia", "Alma", 7, 4}
print(type(my_set))


