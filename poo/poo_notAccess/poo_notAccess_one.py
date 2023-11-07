## POO : Not Access Two ##

class Pay:
  def __init__(self, money, interest_rate, time_pay, balance):
    self.money = money
    self.interest_rate = interest_rate
    self.time_pay = time_pay
    self.__balance = balance #Private (__)

  #Access Public #Protected (_)
  def calculate_pay_month(self): 
    return self.money * self.interest_rate / 12 / (1 - (1 + self.interest_rate / 12) ** -self.time_pay)
  #Protected Access
  def _calculate_total_pay(self): 
    return self.calculate_pay_month() * self.time_pay
  #Private & Protected
  def _private_interest_rate(self): 
    return self.money * self.interest_rate * self.time_pay
  def user_credit(self): 
    return f"User pay for month: {self.__balance}"


# Variables # 
user_credit = Pay(2000, 0.08, 12, 6000)
user_bank = Pay(4000, 0.15, 12, 10000)
user_one = Pay(1500, 0.15, 18, 5000)

# Call Pay #
if __name__ == "__main__": 
  print("Pamela credit:", user_credit.money)
  print("User Bank pay month:", user_credit.calculate_pay_month())
  print("Pay Total User Bank:", user_bank._calculate_total_pay())
  print("user Credit",user_credit._private_interest_rate())


    