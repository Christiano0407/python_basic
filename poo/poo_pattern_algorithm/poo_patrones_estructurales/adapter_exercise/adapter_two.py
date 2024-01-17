######
#TODO:2) ==== Adapter (Two) ====
######
from module_adapter import main_travel, UserTransportTrip


#* ==>  (La clase que necesitamos adaptar) <==
class AdapterTrip:
  def user_travel(self): 
     main = main_travel()
     print("Main Data", main)
     return main
  

#! - Target (Interfaz que el cliente espera) - Herencia -
class TargetTrip: 
  def request(self):
    pass


#? === Pattern Design: Adapter (Adaptador que conecta la interfaz del Adaptee con la del Target) ===
class Adapter(TargetTrip): 
  def __init__(self, adaptee): 
    self.adaptee = adaptee

  def request(self):
    return f"Adapter Trip: {self.adaptee.user_travel()}"
  

#! > Client User <
def client_trip(target): 
  print(target.request())


#! >= Variables <=
trip = AdapterTrip()
adapter = Adapter(trip)


#* ==== Main ====
if __name__ == "__main__": 
  print("Adapter: Call Travel User")
  client_trip(adapter)

