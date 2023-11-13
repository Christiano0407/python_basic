### POO - Singleton - Getters y Setters - Herencia ###
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

  def retirar(self, monto): 
    if monto > self.saldo: 
      raise ValueError("Lo siento. No tienes el crédito suficiente para retirar éste monto.")
    self.saldo -= monto

  def obtenerSaldo(self): 
    return self.saldo
  
# Herencia Polimorfismo POO
class CuentaAhorros(CuentaBancaria): 
  __instance = None
  
  def __init__(self, numero_cuenta, saldo, tipo_cuenta, tasa_intereses): 
    super().__init__(numero_cuenta, saldo, tipo_cuenta)
    self.tasa_intereses = tasa_intereses

  def tasasIntereses(self):
    return self.saldo + self.tasa_intereses
  
  @classmethod
  def getInstance(cls): 
    if cls.__instance is None: 
      cls.__instance = cls("040205789", 25000, "Gold", 0.05)
    return cls.__instance
    

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
  print(f"My saldo total: {saldos}")
  intereses = cuentaUser.tasasIntereses()
  print(f"Tasas de Intereses: {intereses}")