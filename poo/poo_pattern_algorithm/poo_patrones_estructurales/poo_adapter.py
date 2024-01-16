#########
#TODO: - Pattern Structural - ==== Pattern Design: Adapter ====
#?:El patrón de diseño Adapter es un patrón estructural que permite que la interfaz de una clase existente se adapte para ser utilizada por otra interfaz.
#########
# -  (La clase que necesitamos adaptar) -
class DataAdaptee: 
  def specific_request(self):
    return "Adapter Specific Data Plus."
  

# - Target (Interfaz que el cliente espera) - Herencia -
class Target:
  def request(self):
    pass


# === Pattern Design: Adapter (Adaptador que conecta la interfaz del Adaptee con la del Target) ===
class Adapter(Target):
  def __init__(self, data):
    self.data = data

  def request(self): 
    return f"Adapter: {self.data.specific_request()}"
  

#-Client/ User-
def client_code(target): 
  print(target.request())


# - Variable - > Uso del Adapter para conectar el cliente con el Adaptee <
one_adaptee = DataAdaptee()
adapter = Adapter(one_adaptee)


if __name__ == "__main__":
  print(f"Cliente: Adaptee está funcionando con la interfaz Target normal.")
  client_code(adapter)
