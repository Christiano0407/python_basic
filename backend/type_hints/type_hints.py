# Type Hints - Python es un lenguaje de tipado dinámico. 
from typing import List, Optional

def sum (a:int, b:int) -> int:
  return a + b

message:[str] = "Hello, World"
new_message: str = "New Message"
new_message.index

lst:List[str] = ["Alma", "Natalia", "Pamela"]

lst_people:[int] = list([4, 7, 15, 25])

ages:Optional[int] = None
numbers:Optional[int] = 7
number_plus: int = 10

##POO
class Person: 
  def __init__(self, name:str, work:str, age:int) -> None:
    self.name = name
    self.work = work
    self.age = age

  def hello(self):
    return f"Hello {self.name} you work in {self.work} and age: {self.age}"


## === ##
if __name__ == "__main__":
  plus_sum = sum(4, 7)
  print(type(plus_sum))
  print(plus_sum)
  print(type(message))
  print(message)
  print(new_message)
  print(type(lst))
  print(lst)
  print(type(lst_people))
  print(lst_people)
  print(f"{ages} & {numbers}")

  people = Person("Luisa", "Journalist", 32)
  print(people.hello())