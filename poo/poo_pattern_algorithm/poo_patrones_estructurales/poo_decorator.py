#########
#TODO: === Pattern Design Structural: Decorator ===
#?: También llamado: Decorador, Envoltorio, Wrapper - type: Russian Doll (Muñeca Rusa) -
#?: Decorator es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.
##############
#* 1) ==== Componente ====
class Component:
  def operation(self):
    pass

  def run(self): 
    pass



#* ==> Objeto Concreto <==
class Car(Component): 
  def operation(self) -> str:
    return "Car Porsche Model: Taycan GTS"
  
  def run(self): 
    return "900 Horses of force"


#* 2) === Decorador - (Add: Characteristics and Functions) - ===
class Decorator(Component): 
  def __init__(self, component):
     self._component = component

  def operation(self):
    return self._component.operation()
  
  def run(self): 
    return self._component.run()


#* > Decorador Concreto <
class FastDecorator(Decorator):
  def operation(self):
    return f"This is a {super().operation()} and is very Fast!!"

  def run(self): 
    return f"It's very Beautiful and fast {super().run()}. It's new Model." 



#* > Decorador Concreto <
class SportDecorator(Decorator): 
  def operation(self):
    return f"My sport {super().operation()} is Model 2024"
  


#! ==== === Main: Execute === ====
if __name__ == "__main__": 
  print("...Execute")
  car = Car()
  print(f"My {car.operation()}")

  car_fast = FastDecorator(car)
  print(f"Fast Car:{car_fast.operation()} and {car_fast.run()}")

  car_sport = SportDecorator(FastDecorator(car))
  print("Sport Car:", car_sport.operation())

