## POO : Not Access Two & Herencia ##
### Préstamo en un sistema bancario ##

class approved_pay:
  def __init__(self, approved_money):
    self._approved_money = approved_money

    #Getters
  def get_approved(self): 
    return self._approved_money
    #Setters
  def set_approved(self, approved_money): 
    self._approved_money = approved_money



class Pay(approved_pay):
  def __init__(self, money, interest_rate, time_pay, balance, approved_money):
    super().__init__(approved_money)
    self.money = money # Monto del préstamo
    self.interest_rate = interest_rate #Interéses
    self.time_pay = time_pay #Tiempo a pagar
    self.__balance = balance #Private (__) / Saldo

  #Access Public #Protected (_)
  def calculate_pay_month(self): 
    return self.money * self.interest_rate / 12 / (1 - (1 + self.interest_rate / 12) ** -self.time_pay)
  #Protected Access
  def _calculate_total_pay(self): 
    return self.calculate_pay_month() * self.time_pay
  #Private & Protected
  def _calculate_interest_rate(self): 
    return self.money * self.interest_rate * self.time_pay
  #Credit User
  def user_credit(self): 
    return f"User pay for month: {self.__balance}"
  #Private
  def _calculate_iva(self):
    return  self.calculate_pay_month() * 0.16
  #Private
  def first_pay(self):
    return  self.calculate_pay_month() + self._calculate_iva()
  #Getters & Setters
  def set_approved(self, approved_money):
    return super().set_approved(approved_money)

# Variables = Users # 
user_credit = Pay(2000, 0.08, 12, 6000, 2500)
user_bank = Pay(8000, 0.10, 12, 10000, 2500)
user_one = Pay(15000, 0.15, 18, 5000, 2500)
user_two = Pay(35000, 0.20, 24, 30000, 2500)
user_three = Pay(50000, 0.25, 36, 10000, 2500)
# Call Pay #
if __name__ == "__main__": 
  user = f"Fred: Monto de su préstamo: {user_one.money:.2f} y pago total: {user_one._calculate_total_pay():.2f}, por mes pagaría: {user_one.calculate_pay_month():.2f} y los interéses del préstamo: {user_one._calculate_interest_rate():.2f}"
  user_house = f"Alma: préstamo para su casa: {user_three.money:.2f} y pago total: {user_three._calculate_total_pay():.2f} por mes pagaría: {user_three.calculate_pay_month():.2f} y su primer pago se le suma iva: {user_three.first_pay():.2f} y los interéses del préstamo: {user_three._calculate_interest_rate():.2f}"
  
  #print(f"Monto que se prestó: {user_credit.money:.2f}")
  #print(f"Pamela pay for month: {user_credit.calculate_pay_month():.2f}")
  #print(f"Pamela pay Total: {user_credit._calculate_total_pay():.2f}")
  #print(f"Interéses del préstamo: {user_credit._calculate_interest_rate():.2f}")
  print(user)
  print(user_house)
  print(user_credit.set_approved(25000))


    