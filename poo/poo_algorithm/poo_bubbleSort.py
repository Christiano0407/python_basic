#### POO & Algorithm Bubble Sort ####

""" def bubble_sort(lst):
   #n = len(lst)
   for i in range(len(lst) - 1):
     for j in range(len(lst) -i -1):
       if lst[j] > lst[j + 1]:
         lst[j], lst[j + 1] = lst[j + 1] , lst[j]

   return lst """

def bubble_sort(list): 
  n = len(list)
  for i in range(n): 
    for j in range(0, n - i -1):
      if list[j] > list[j + 1]: 
        list[j], list[j + 1] = list[j + 1], list[j]

  return list


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
  
  def order_payments(self): 
    self.payments = bubble_sort(self.payments)
    return self.payments

  def pay_interest_rate(self): 
    interests = self.payment_total() - self.borrow
    return interests


  # Add Algorithm
def payments_for_months(borrow, months): 
  for month in range(months):
    pay_month = borrow.payment_month()
    pay_balance = borrow.balance_calculate(month)
    print(f"Pay for month: {pay_month:.2f}")
    print(f"My Balance for the Borrow: {pay_balance:.2f}")

def payment_list(borrow, months):
  for month in range(months):
    #my_balance = borrow.balance_calculate( month)
    payments_months = borrow.payment_month() #Pay Month
    pay_month = borrow.add_payments(payments_months) # Add List Payments
    formatted_payments = [f"{payment:.2f}" for payment in  pay_month] # Formatted
    print(f"Payment (Month): {', '.join(formatted_payments)}") #Join Payments in List
    #print(f"My Balance: {my_balance:.2f}")

  
#Variable - Class
user_plus = Borrow(10000, 0.08, 18, 25000)
user_borrow = Borrow(25000, 0.10, 36, 50000)
userOne_borrow = Borrow(5000, 0.4, 12, 10000)


#Call Class #
if __name__ == "__main__":
  #month = user_plus.payment_month()
  #total = user_plus.payment_total()
  bubble_pay = userOne_borrow.order_payments()
  formatted_bubble = [f"{pay:.2f}" for pay in bubble_pay]
  print(f"Pay in Order: {formatted_bubble}")
  payments_for_months(userOne_borrow, userOne_borrow.time_pay)
  payment_list(userOne_borrow, userOne_borrow.time_pay)
  #print(f"{userOne_borrow.payments:.2f}")
  #print(f"Pay for Month: {month:.2f} and Total Pay: {total:.2f}")
  #print(f"Interest_rate: {userOne_borrow.pay_interest_rate():.2f}")
