####
#TODO: === Testing with Pytest ===
########
#? = Variable =
name = "Luisa"

#? == Functions ==

def sum(a, b): 
  return a + b


def call_name(user):
  if user == name:
    return name
  

def add(num_one, num_two): 
  return num_one + num_two


def divide(num_one, num_two): 
  if num_two == 0: 
    raise ValueError
  return num_one / num_two


def rest(num_one, num_two): 
  return num_one - num_two