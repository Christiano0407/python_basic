#=======#####
#TODO: ====== Encapsulamiento / Encapsulation ======= 
####========#
import re

#* === Private: ("_") ===
class Bank: 
  def __init__(self):
    self._credit_card = "BBVA"


user = Bank()
print(user._credit_card)

#* ==== Very, Very Private: ("__") ====
class BankCard:
  # >= Attributes of Class <=
  country = "Mexico,City"
  nip_user = 745
  type_card = "Credit"
  premium_card = "Platinum"
  gold_card = "Gold"
  my_credit = 40000
  months = 12
  time = 1
  new_pay_rate = 0.10
  # ==== Methods Of instance => Object ====
  def __init__(self, card:str, bank:str, user:str, num_card:int, annual_rate = float, pay_rate = float):
    self.__card = card
    self.__bank = bank
    self.__user = user
    self.__num_card = num_card
    self.annual_rate = annual_rate
    self.pay_rate = pay_rate

  def __str__(self) -> str:
    return f"My bank is founder in: {self.country}"
  # >= @decorador <=
  def decorador(func_nip) -> str:
      def wrapper(self):
            print(f"My bank is {self.__bank}. I'm {self.__user} and have my credit card {self.__card}")
            func_nip(self) # > decorador == call_nip() / Callback in Js <

      return wrapper
# > Getters (Get) <
  def get_card(self) -> str:
    return f"I'm {self.__user} and my card: {self.__card} and my Bank:{self.__bank}"
# > Setter (Change) <
  def set_card(self, new_creditCard, new_bank) -> str: 
    credit_card = self.__card = new_creditCard
    new_bank_site = self.__bank = new_bank
    return f"My new credit Card: {credit_card} and my new Bank: {new_bank_site}"
  
#====> Methods Of Class (@) / Decorators <=====
  @decorador
  def call_nip(self) -> str:
    print(f"Well, my type card is: {self.type_card}, my NIP: {self.nip_user} and my country {self.country}")
# Otra forma de llamar: decorador(call_nip)(user_card).

  @property # ==> Permite: Solo lectura (read) / @wrapper (Method Equal) <===
  def get_num_private(self):
     return self.__num_card
  # > Setter (Change) - Access to Getters and Setters - <
  @get_num_private.setter
  def get_num_private(self, new_numPrivate):
     if new_numPrivate == self.__num_card:
        self.__num_card = new_numPrivate
     else: 
       print("Sorry! You cannot change your number of card")

  @classmethod
  def get_type_card(cls, card, type_cards):
     if cls.type_card == card and cls.premium_card == type_cards:
        return f"Hello, you're are a user: {cls.premium_card}"
     elif cls.type_card == card and cls.gold_card == type_cards: 
        return f"You're a user VIP: {cls.gold_card}"
     elif cls.type_card == card:
        return f"Your Type of card is: {cls.type_card}"
     else: 
        return f"Sorry Your type card {cls.type_card} is only basic"

  @staticmethod
  def calculate_interest(principal, interest_rates, months_pay, times_pay): 
     '''
     Calcular el pago de interéses mensual
     '''
     r = interest_rates / months_pay
     n = months_pay / times_pay

     #interests = principal * ((1 + r)**n - 1) #Interés simple
     interests = principal * ((1 + r/n)**(n*times_pay) - 1) # Interés Compuesto

     return interests

  
  

#!==== === Execute === ====
if __name__ == "__main__":
  user_card = BankCard("BBVA", "BBVABank", "Chris", 102345678, 0.15, 0.6)
  print(str(user_card))
  user_card.call_nip()#===Call to method @decorator (decorador)
  print(user_card.get_card())
  print(user_card.set_card("CityCard", "Citybanamex"))
  print("New:",user_card.get_card())
  print("Property", user_card.get_num_private)
  user_card.get_num_private = 102345678
  """ print("Property change", user_card.num_private_card) """
  print(user_card.get_type_card(user_card.type_card, user_card.premium_card))
  months_calculate = round(BankCard.calculate_interest(user_card.my_credit, user_card.new_pay_rate, user_card.months, user_card.time))
  print(f"months_calculate: {months_calculate}")
  #months_calculate: 334.60943319369994