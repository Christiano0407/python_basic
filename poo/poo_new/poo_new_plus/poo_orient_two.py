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
  # ==== Methods Of instance => Object ====
  def __init__(self, card, bank, user):
    self.__card = card
    self.__bank = bank
    self.__user = user

  def __str__(self) -> str:
    return f"My bank is founder in: {self.country}"
# > Getters (Get) <
  def get_card(self):
    return f"I'm {self.__user} and my card: {self.__card} and my Bank:{self.__bank}"
# > Setter (Change) <
  def set_card(self, new_creditCard, new_bank): 
    credit_card = self.__card = new_creditCard
    new_bank_site = self.__bank = new_bank
    return f"My new credit Card: {credit_card} and my new Bank: {new_bank_site}"

#====> Methods Of Class (@) / Decorators <=====


if __name__ == "__main__":
  user_card = BankCard("BBVA", "BBVABank", "Chris")
  print(str(user_card))
  print(user_card.get_card())
  print(user_card.set_card("CityCard", "Citybanamex"))
  print("New:",user_card.get_card())