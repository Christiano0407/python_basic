################# POO: Loops (For) ##################
#Money - Borrow(Préstamo)
#factor_de_interes = (1 + self.interest_rate / 12) ** -self.time_pay
#pago_mensual = self.borrow * self.interest_rate / 12 / (1 - factor_de_interes)
#################################
class Borrow:
  def __init__(self, borrow, interest_rate, time_pay):
    self.borrow = borrow #Préstamo
    self.interest_rate = interest_rate #Tasa de Interés
    self.time_pay = time_pay #Meses sin interéses
    self.balance = borrow #Saldo

  def pay_for_months(self):
    return self.borrow * self.interest_rate / 12 / (1 - (1 + self.interest_rate / 12) ** -self.time_pay)
  
  def calculate_total_pay(self): 
    return self.pay_for_months() * self.time_pay
  
  def calculate_balance(self, month):
    if month == 0:
      return self.balance
    else:
      self.balance -= self.pay_for_months() #Iterar
      return self.balance
    
#For loop & Def (1)
def run_loop_emulation_pay(borrow, months):
  for month in range(months):
    pay_month = borrow.pay_for_months()
    month_balance = borrow.calculate_balance(month)
    print(f"***** For Pay: {month_balance:.2f}")
    print(f"Month: {month}: Pay for month = {pay_month:.2f}, my balance = {month_balance:.2f}")


#Variables
user_borrow = Borrow(10000, 0.05, 24)
client_borrow = Borrow(15000, 0.05, 36)
user_brenda = Borrow(8000, 0.05, 6)

#For Loop (2)
for month in range(user_borrow.time_pay):
  month_pay = user_borrow.pay_for_months()
  balance_month = user_borrow.calculate_balance(month)
  #print(f"Month: {month}: Pay for month = {month_pay:.2f}, my balance = {balance_month:.2f}")


#Call Borrow
if __name__ == "__main__":
  #burrows = user_borrow.borrow
  #print("Burrow:", burrows)
  #run_loop_emulation_pay(client_borrow, client_borrow.time_pay)
  run_loop_emulation_pay(user_brenda, user_brenda.time_pay)