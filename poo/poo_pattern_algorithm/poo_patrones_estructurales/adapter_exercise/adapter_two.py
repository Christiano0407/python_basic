######
#TODO:2) ==== Adapter (Two) ====
######
from module_adapter import main_travel, TripUser


#* ==>  (La clase que necesitamos adaptar) <==
class AdapterTrip:
  def user_travel(self): 
     users = TripUser("Luisa Pamela Rosas")
     #print("Go!!", users.name_user, users.name_traveler())
     return f"Hello, I'm: {users.name_user}. {users.name_traveler()}"

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
  main_travel()
  client_trip(adapter)

