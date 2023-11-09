#Algorithm: O(n) Lineal 
#POO - Programming Oriented Objects
class Borrow:
  def __init__(self, borrow, interest_rate, pay_time): 
    self.borrow = borrow
    self.interest_rate = interest_rate
    self.pay_time = pay_time
    #list > Pay
    self.balance = borrow
    self.payments = []

  def payment_months(self): 
    return self.borrow * self.interest_rate / 12 / (1 - (1 + self.interest_rate / 12) ** -self.pay_time)
  
  def calculate_total_pay(self): 
    total_pay = self.payment_months() * self.pay_time
    return total_pay

  def add_payments(self, payment): 
    self.payments.append(payment)
    return self.payments
  
  def calculate_balance(self, month):
    if month == 0:
      return self.balance
    else:
      self.balance -= self.payment_months() #Iterar
      return self.balance


def payments_for_months(borrow, months):

  for month in range(months):
    month_payment = borrow.payment_months()
    balance_month = borrow.calculate_balance(month)
    borrow_payment = balance_month - month_payment
    payment_add = borrow.add_payments(month_payment) #Month_payment
    formatted_payments =  [f"{payment:.2f}" for payment in payment_add]
    print(f"***** For Pay: {balance_month:.2f}")
    print(f"Months: {month}: Pay for month = {month_payment:.2f} and my balance = {balance_month:.2f}")
    print(f"Borrow Payment: {borrow_payment:.2f}")
    print(f"My payments (months): {', '.join(formatted_payments)}")


#Variables - Class
user_one = Borrow(8000, 0.05, 6)

## Call Borrow ###
if __name__ == "__main__": 
 payments_for_months(user_one, user_one.pay_time)