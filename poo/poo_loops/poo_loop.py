################# POO: Loops (For) ##################
#Money - Borrow(Préstamo)
#factor_de_interes = (1 + self.interest_rate / 12) ** -self.time_pay
#pago_mensual = self.borrow * self.interest_rate / 12 / (1 - factor_de_interes)
#################################
class Borrow:
  def __init__(self, borrow, interest_rate, time_pay):
    self.borrow = borrow #Préstamo
    self.interest_rate = interest_rate #Tasa de Interés
    self.balance = borrow #Saldo
    self.time_pay = time_pay #Meses sin interéses

  def pay_for_months(self):
    return self.borrow * self.interest_rate / 12 / (1 - (1 + self.interest_rate / 12) ** -self.time_pay)
  
  def calculate_total_pay(self): 
    return self.pay_for_months() * self.time_pay
  
  def calculate_balance(self, month):
    if month == 0: 
      return self.balance
    else:
      return self.balance - self.pay_for_months()
    

#Variables
user_borrow = Borrow(10000, 0.05, 24)
client_borrow = Borrow(15000, 0.05, 36)

#Loop
for month in range(user_borrow.time_pay):
  month_pay = user_borrow.pay_for_months()
  balance_month = user_borrow.calculate_balance(month)
  print(f"Month: {month}: Pay for month = {month_pay:.2f}, my balance = {balance_month:.2f}")

#Call Borrow
if __name__ == "__main__":
  burrows = user_borrow.borrow
  #burrow_month = f"{user_borrow.pay_for_months():.2f}"
  #user_client = f"This is I Pay for Month: {month_pay:.2f} and my balance: {balance_month:.2f}"

  print(burrows)
  #print(burrow_month)
  #print(user_client)