## #1:Programming Oriented Objects (POO) ##  
# Instancia == Self (Instancia Actual) > Cuenta Bancaria (Class) == POO
class CuentaBancaria:

  def __init__(self, num_cuenta, nombre_titular, balance):
    self.num_cuenta = num_cuenta
    self.nombre_titular = nombre_titular
    self.balance = balance

  def generar_balance(self):
      return self.balance

  def depositar(self, monto):
    if monto > 0:
        self.balance += monto
        return self.balance


## Variables
mi_cuenta = CuentaBancaria("475-321-987", "Evans Smith", 25000)
user_pamela = CuentaBancaria("987-487-777", "Pamela Oviedo", 30000)


if __name__ == "__main__":
  print("Pamela: $", user_pamela.balance)

  balance = mi_cuenta.generar_balance()
  print("Balance: $", balance)
  depositos = mi_cuenta.depositar(8000)
  print("Depósito:: $", depositos)
  pamela = user_pamela.depositar(5000)
  print("Pamela: $", pamela)


## Results ##
#Pamela: $ 30000
#Balance: $ 25000
#Depósito:: $ 33000
#Pamela: $ 35000
