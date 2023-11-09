#### POO & Algorithm Bubble Sort ####

def bubble_sort(lst):
   #n = len(lst)
   for i in range(len(lst) - 1):
     for j in range(len(lst) -i -1):
       if lst[j] > lst[j + 1]:
         lst[j], lst[j + 1] = lst[j + 1] , lst[j]

   return lst


class Borrow: 
  def __init__(self, borrow, interest_rate, time_pay, balance):
    self.borrow = borrow
    self.interest_rate = interest_rate
    self.time_pay = time_pay
    self.balance_borrow = borrow
    self.balance = balance
    self.payments = []
  # Month Pay
  def payment_month(self): 
    return self.borrow * self.interest_rate / 12 / (1 - (1 + self.interest_rate / 12) ** -self.time_pay)
  #Total Pay
  def payment_total(self): 
    total_pay =  self.payment_month() * self.time_pay
    return total_pay
  # Balance - Borrow
  def balance_calculate(self, month): 
    if month == 0: 
      return self.balance_borrow
    else: 
      self.balance_borrow -= self.payment_month()
      return self.balance_borrow
    
  # Add Payments - list 
  def add_payments(self, payment): 
    self.payments.append(payment)
    return self.payments

  # Add Algorithm
def payments_for_months(borrow, months): 
  for month in range(months):
    pay_month = borrow.payment_month()
    pay_balance = borrow.balance_calculate(month)
    print(f"Pay for month: {pay_month:.2f}")
    print(f"My Balance for the Borrow: {pay_balance:.2f}")

  
#Variable - Class
user_plus = Borrow(10000, 0.08, 18, 25000)
user_borrow = Borrow(25000, 0.10, 36, 50000)


#Call Class #
if __name__ == "__main__":
  month = user_plus.payment_month()
  total = user_plus.payment_total()
  payments_for_months(user_borrow, user_borrow.time_pay)
  print(f"**** {month:.2f} and {total:.2f}")