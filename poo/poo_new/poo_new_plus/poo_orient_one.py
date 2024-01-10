#====######
#TODO: ==== Polimorfismo / Polymorphism ====
from abc import ABC, abstractmethod
####=====#
#1) Compile-time
class Cat:
  def sound(self):
    return "Miau!"
  

class Dog:
  def sound(self):
    return "Wow!"
  

my_cat = Cat()
my_dog = Dog()


print(my_cat.sound(), my_dog.sound())


#2) Run-time - Algorithm O(1)
class AnimalKing():
  @abstractmethod
  def animal_king(self):
    pass

class Animal(AnimalKing):
  def __init__(self, name:str):
    self.name = name

  def call_animal(self) -> str:
    return f"Hey! My animal is {self.name}"
  
  def animal_king(self) -> str:
    return f"Hey! The king is: {self.name}"
  

leon = Animal("Leon")


print(leon.animal_king())
print(leon.call_animal())
  




