#=======#####
#TODO: ====== Encapsulamiento / Encapsulation ======= 
####========#
#* === Private: ("_")
class Bank: 
  def __init__(self):
    self._credit_card = "BBVA"


user = Bank()
print(user._credit_card)

#* ==== Very, Very Private: ("__")
class BankCard:
  # >= Attributes of Class <=
  country = "Mexico,City"
  nip_user = 745
  type_card = "Gold"
  # ==== Methods Of instance => Object ====
  def __init__(self, card:str, bank:str, user:str):
    self.__card = card
    self.__bank = bank
    self.__user = user

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
  def call_nip(self):
    print(f"Well, my type card is: {self.type_card}, my NIP: {self.nip_user} and my country {self.country}")

#!==== === Execute === ====
if __name__ == "__main__":
  user_card = BankCard("BBVA", "BBVABank", "Chris")
  print(str(user_card))
  user_card.call_nip()#===Call to method @decorator (decorador)
  print(user_card.get_card())
  print(user_card.set_card("CityCard", "Citybanamex"))
  print("New:",user_card.get_card())