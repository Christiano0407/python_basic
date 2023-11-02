# =====  HTTP Request ====== #
import requests

#Categories
def get_categories():
  r = requests.get('https://api.escuelajs.co/api/v1/categories')
  print(r.status_code)
  print(r.text)
  #print(type(r.text)) #str
  categories = r.json()
  for category in categories:
    print(category["name"])
    #print(type(category)) #dic



#Products
def get_products(): 
  response = requests.get('https://api.escuelajs.co/api/v1/products')
  print(response.status_code)
  print(response.text)

