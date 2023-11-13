#### POO - Singleton - Getters y Setters - Herencia ###
# El patrón de diseño Singleton garantiza que solo puede existir una instancia de una clase en un momento dado.
# Algoritmo O(n) lineal -  El algoritmo O(n) lineal funciona iterando sobre todos los días del año y calculando los intereses diarios. El número de días en un año es constante, por lo que el algoritmo tiene una complejidad de O(n).
# La expresión (1 + self.tasa_interes) ** (-dia / 365) es una función exponencial que representa el factor de descuento de los intereses diarios. El factor de descuento es un valor que se utiliza para calcular los intereses diarios, teniendo en cuenta el hecho de que los intereses se acumulan a lo largo del tiempo.
#####
class CuentaBancaria: 
  __instance = None #Pattern Singleton

  def __init__(self, numero_cuenta, saldo, tipo_cuenta): 
    self.numero_cuenta = numero_cuenta
    self.saldo = saldo
    self.tipo_cuenta = tipo_cuenta
  # Pattern Singleton
  @classmethod
  def getInstance(cls): 
    if cls.__instance is None: 
      cls.__instance = cls("041234567", 5000, "platinum")
    return cls.__instance
  
  def depositar(self, deposito): 
    self.saldo += deposito
  # Manejo de Excepciones 
  def retirar(self, monto): 
    try:
      self.saldo -= monto 
    except ValueError as e:
      print(e)

  def obtenerSaldo(self): 
    return self.saldo
  
# Herencia Polimorfismo POO
class CuentaAhorros(CuentaBancaria): 
  __instance = None

  def __init__(self, numero_cuenta, saldo, tipo_cuenta, tasa_intereses, meses): 
    super().__init__(numero_cuenta, saldo, tipo_cuenta)
    self.tasa_intereses = tasa_intereses
    self.meses = meses

  def tasasIntereses(self):
    return self.saldo * self.tasa_intereses
  
  def anualidadIntereses(self):
    return self.saldo * self.tasa_intereses * self.meses
  
  @classmethod #Patterns Singleton
  def getInstance(cls): 
    if cls.__instance is None: 
      cls.__instance = cls("040205789", 25000, "Gold", 0.05, 12)
    return cls.__instance
  #Algorithm: O(n)Lineal
  def calcularInteres(self): 
    intereses = 0
    for dia in range(365): 
      intereses += self.saldo * self.tasa_intereses * (1 + self.tasa_intereses) ** (-dia / 365)
      #intereses += self.saldo * self.tasa_intereses * (1 + self.tasa_intereses) ** (-dia / 30)
      #intereses += self.saldo * self.tasa_intereses * (1 + self.tasa_intereses) ** (-dia / 7)
    return intereses
  

#### ==== ####
if __name__ == "__main__": 
  cuenta = CuentaBancaria.getInstance()
  cuentaUser = CuentaAhorros.getInstance()

  print(f"Mi cuenta: {cuenta.numero_cuenta} y mi tarjeta es: {cuenta.tipo_cuenta}")
  cuenta.depositar(2000)
  print(cuenta.saldo)
  cuenta.retirar(5500)
  print(cuenta.saldo)
  saldos = cuenta.obtenerSaldo()
  print(f"My saldo total: ${saldos}")

  intereses = cuentaUser.tasasIntereses()
  print(f"Tasas de Intereses: ${intereses:.2f}")
  anual = cuentaUser.anualidadIntereses()
  print(f"Anualidad $:{anual}")
  calcular = cuentaUser.calcularInteres()
  print(f"Calcular Intereses por día: ${calcular:.2f}")