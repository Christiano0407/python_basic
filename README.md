# Python

> Basic Python

> Course of Python basic. Exercise and practice with Python. 

## Python con Platzi

> Root Complete Python in I.A

> platzi.com

[Platzi](https://platzi.com/)

> Roadmap
[roadmap](https://roadmap.sh/python)

## Herramienta Gitignore para Python

> Gitignore

[gitignore.io](https://www.toptal.com/developers/gitignore/)

> Python Docs

[Dev:python](https://devguide.python.org/getting-started/)

[Python.org](https://www.python.org/)

## Virtual Environments

> Create Virtual Environments for work in Python

```python
# Verificar donde esta python y pip
which python3
which pip3
# Si estas en linux o wsl debes instalar
sudo apt install -y python3-venv
# Poner cada proyecto en su propio ambiente, entrar en cada carpeta.
python3 -m venv env
# Activar el ambiente
source env/bin/activate
# Salir del ambiente virtual
deactivate
# Verificar las instalaciones
pip3 freeze

# Correr el Servidor Web (Uvicorn & FastAPI)
uvicorn main:app --reload

```

### Developer Project Python

> Terminal (Bash or ZSH)

> Para correr el juego debes seguir las siguientes instrucciones en las terminal: 

```sh
cd game
python3 game.py
python3 main.py
```

> Gestor de paquetes de Python (Pip)

> Python pip == npm 

[pypi](https://pypi.org/)
[pypi_requests](https://pypi.org/project/requests/)

### Comandos para instalar Python

> Verificar python en tu terminal de Windos e Linux

```python
# Verificar que existe Python (terminal):
python
python3
exit() 
# Para salir de la interfaz de Python
```

> Instalación 

```python
# Actualizar la terminal
apt update
sudo apt update
sudo apt -y upgrade
```

> Verificar instalación de Python

```python
python3 -V
```

> Instalación de gestor de paquetes de dependencias

[pypi](https://pypi.org/)

```python
sudo apt insstall -y python3-pip
# Verificar instalación
pip3 -V
```

> Dependencias en entorno profesional

```python
apt install -y build-essential libssl-dev libffi-dev python3-dev
```

### Herramientas para código en Python 

> Google Colab & Replit

[Google Colab](https://colab.research.google.com/?hl=es)
[Replit](https://replit.com/)

### Requests Python
```python
import requests

#Categories
def get_categories():
  r = requests.get('') #Request
  print(r.status_code)
  print(r.text)
  #print(type(r.text)) #str
  categories = r.json()
  for category in categories:
    print(category[""]) #Index
    #print(type(category)) #dic

# === Main === 
import request


def run():
  request.get_categories()


if __name__ == "__main__":
  run()

```
### Python Used Pandas

> Use Archive ".csv" as practice

```python

import pandas as pd


df = pd.read_csv("./data/amazon_laptop_prices_v01.csv")


if __name__ == "__main__":
  print(df.head(5))
  list_products = df.head(20)
  print(list_products)


```

### Web Server with Uvicorn and FastAPI

> Framework and Web Server

[FastAPI](https://fastapi.tiangolo.com/)
[Uvicorn](https://www.uvicorn.org/)

```python
# Install FastAPI
pip install fastapi

# Install Uvicorn
pip install "uvicorn[standard]"

```

> HTML Response With Python and FastAPI

```python

#from fastapi import FastAPI
#from fastapi.responses import HTMLResponse

#app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

```

> Add response_class

```python

## Request API FastAPI ##
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# App Server #
app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def get_home():
   html_content =  """
    <html>
        <head>
            <title>Some HTML in here</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Hello Dev! HTML & Python!</h1>
            <h2>Python Backend </h2>
        </body>
    </html>
    """
   return HTMLResponse(content=html_content, status_code=200)

```
### Programación Orientada a Objetos en Python (POO)

> La programación orientada a objetos (POO) es un paradigma de programación que organiza el código en torno a objetos. Los objetos son entidades que tienen un estado y un comportamiento. El estado de un objeto se representa mediante sus atributos, y su comportamiento se representa mediante sus métodos.

> La POO se basa en cuatro conceptos fundamentales:

> Clases: Las clases son plantillas que definen el estado y el comportamiento de los objetos.

> Objetos: Los objetos son instancias de clases.

> Atributos: Los atributos definen el estado de un objeto.

> Métodos: Los métodos definen el comportamiento de un objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)


persona = Persona("Juan", 30)
print(persona.nombre)
```

```python

# Ejemplo de clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

# Ejemplo de instanciación de una clase
persona = Persona("Juan", 30)

# Ejemplo de acceso a un atributo
print(persona.nombre)

# Ejemplo de llamada a un método
persona.saludar()

```

```python
# Instancia == Self (Instancia Actual) > Cuenta Bancaria (Class) == POO
class CuentaBancaria:

  def __init__(self, num_cuenta, nombre_titular, balance):
    self.num_cuenta = num_cuenta
    self.nombre_titular = nombre_titular
    self.balance = balance

  def generar_balance(self):
      return self.balance

  def depositar(self, monto):
    if monto > 0:
        self.balance += monto
        return self.balance


## Variables
mi_cuenta = CuentaBancaria("475-321-987", "Evans Smith", 25000)
user_pamela = CuentaBancaria("987-487-777", "Pamela Oviedo", 30000)


if __name__ == "__main__":
  print("Pamela: $", user_pamela.balance)

  balance = mi_cuenta.generar_balance()
  print("Balance: $", balance)
  depositos = mi_cuenta.depositar(8000)
  print("Depósito:: $", depositos)
  pamela = user_pamela.depositar(5000)
  print("Pamela: $", pamela)


## Results ##
#Pamela: $ 30000
#Balance: $ 25000
#Depósito:: $ 33000
#Pamela: $ 35000

```

```python
### Tip:
# POO con Funciones
javascript = {
    "nombre": "Javascript",
    "año": 1995
}

def description():
  print("%s fue creado en %s" % (javascript["nombre"], javascript["año"]))

description()

# POO Con Class: 
class Lenguaje:
  
  def __init__(self, nombre, año):
    self.nombre = nombre
    self.año = año

  def aprender(self):
    print("%s fue creado en %s" % (self.nombre, self.año))


#javascript = Lenguaje("javascript", 1995)
#javascript.aprender()

##
#Javascript fue creado en 1995
#javascript fue creado en 1995

```

> POO en Python con accesos y no accesos:

> Aplicar modificadores de acceso en Python: Principio de Encapsulamiento ("_")

```python

class Prestamo:
    def __init__(self, monto, tasa_de_interes, plazo):
        self.monto = monto
        self.tasa_de_interes = tasa_de_interes
        self.plazo = plazo

    # Acceso público
    def calcular_pago_mensual(self):
        return self.monto * self.tasa_de_interes / 12 / (1 - (1 + self.tasa_de_interes / 12) ** -self.plazo)

    # Acceso protegido
    def _calcular_pago_total(self):
        return self.calcular_pago_mensual() * self.plazo

    # Acceso privado
    def _calcular_intereses(self):
        return self.monto * self.tasa_de_interes * self.plazo


prestamo = Prestamo(100000, 0.08, 24)

print(prestamo.calcular_pago_mensual())
# 5000
print(prestamo._calcular_pago_total())
# 120000
print(prestamo._calcular_intereses())
# 96000


```

> Aplicar modificadores de acceso en Python: Getters y Setters

```python

class Prestamo:
    def __init__(self, monto, tasa_de_interes, plazo):
        self._monto = monto
        self.tasa_de_interes = tasa_de_interes
        self.plazo = plazo

    def calcular_pago_mensual(self):
        return self._monto * self.tasa_de_interes / 12 / (1 - (1 + self.tasa_de_interes / 12) ** -self.plazo)

    def calcular_pago_total(self):
        return self.calcular_pago_mensual() * self.plazo

    # Método getter para el atributo monto

    def get_monto(self):
        return self._monto

    # Método setter para el atributo monto

    def set_monto(self, monto):
        self._monto = monto


prestamo = Prestamo(100000, 0.08, 24)

print(prestamo._monto)
# 100000
print(prestamo.get_monto())
# 100000

prestamo.set_monto(200000)

print(prestamo.get_monto())
# 200000


```

> Aplicar modificadores de acceso en Python: Modificador de acceso público & Modificador de acceso privado

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Modificador de acceso público

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Modificador de acceso privado

    def _edad(self):
        return self._edad

    def _edad_setter(self, edad):
        self._edad = edad


persona = Persona("Juan Pérez", 30)

# Acceso público

print(persona.nombre)
# Juan Pérez

persona.nombre = "María García"

print(persona.nombre)
# María García

# Acceso privado

# print(persona.edad)
# AttributeError: 'Persona' object has no attribute 'edad'

persona._edad_setter(40)

print(persona._edad())
# 40


```

> Herencia en POO con Python:

```python
class Country(Player): 
  def __init__(self, name, team, selection, brand, stadium, salary): 
     super().__init__(name, team) #super is Father
     self.selection = selection
     self.brand = brand
     self.stadium = stadium
     self.__salary = salary
```

> Herencia & Polimorfismo(heredar y llamar de acurdo al contexto) 

```python
  # Player:
  def teams(self):
     return f"Player in: {self.team}"
  # Country:
  def teams(self):
     return super().teams() + " The Brand: " + self.brand + " Stadium: " + self.stadium + " and players wining in salary: " + str(self.__salary)
```

> En POO en Python, un @staticmethod es un decorador que se usa para definir un método estático. Los métodos estáticos son métodos que pertenecen a una clase, pero no dependen ni de la clase ni de una instancia de esta. Por lo tanto, no tienen acceso a los atributos de instancia de la clase y no pueden modificar el estado de la clase o de sus instancias.

> Para definir un @staticmethod, simplemente agregamos el decorador @staticmethod a la definición del método. Por ejemplo:

```python
class Country:
    @staticmethod
    def stadium():
        return "Estadio Azteca"


print(Country.stadium())  # Prints "Estadio Azteca"
```

> Multi Herencia 

```python

class Player:
  def __init__(self, name, team):
    self.__name = name
    self.team = team

  def score(self):
    return F"Goal!! {self.__name}"
  
  def teams(self):
     return f"Player in: {self.team}"
  

## < 2) Multi Herencia > ##
class Merchandise:
   def __init__(self, product):
      self.product = product

   def payProduct(self):
      return "I Use this boots: " + self.product 
  

## < 1) Herencia > ##
class Country(Player, Merchandise): 
  def __init__(self,name,team,product,selection,brand,stadium,salary): 
     super().__init__(name, team) #super is Father
     Merchandise.__init__(self,product) # Sí, cuando lo pasas por nombre (self).
     self.selection = selection
     self.brand = brand
     self.stadium = stadium
     self.__salary = salary

```

> Podemos llamarlo igual con super 

```python
# Multi Herencia
  def products(self):
     return super().payProduct
```

> Referencia: Héctor de León (Youtube)

[Hdeleon](https://www.youtube.com/watch?v=Z3XYBjQjZ9g&t=32s)

> Getters and Setters
```python
  #Getters
  def get_approved(self): 
    return self._approved_money
    #Setters
  def set_approved(self, approved_money): 
    self._approved_money = approved_money
```

> Usar Patrones de Diseño (Singleton) e y Herencia (Polimorfismo)
```python
class CuentaBancaria: 
  __instance = None #Pattern Singleton

  def __init__(self, numero_cuenta, saldo, tipo_cuenta): 
    self.numero_cuenta = numero_cuenta
    self.saldo = saldo
    self.tipo_cuenta = tipo_cuenta
  # Pattern Singleton
  @classmethod
  def getInstance(cls): 
    if cls.__instance is None: 
      cls.__instance = cls("041234567", 5000, "platinum")
    return cls.__instance

```

```python
class CuentaAhorros(CuentaBancaria): 
  __instance = None

  def __init__(self, numero_cuenta, saldo, tipo_cuenta, tasa_intereses): 
    super().__init__(numero_cuenta, saldo, tipo_cuenta)
    self.tasa_intereses = tasa_intereses

  def tasasIntereses(self):
    return self.saldo * self.tasa_intereses
  
  @classmethod #Patterns Singleton
  def getInstance(cls): 
    if cls.__instance is None: 
      cls.__instance = cls("040205789", 25000, "Gold", 0.05)
    return cls.__instance
```

```python
cuenta = CuentaBancaria.getInstance()
cuentaUser = CuentaAhorros.getInstance()
```
### Backend 

> Type Hints: Nos Ayudan al tipado en Python. / Python es un lenguaje de tipado dinámico.

> En general, los Type Hints en Python son similares a TypeScript para JavaScript. Ambos son sistemas de tipado estático que permiten especificar el tipo de datos de las variables y expresiones en el código.

> Sin embargo, hay algunas diferencias importantes entre los dos sistemas. En TypeScript, las anotaciones de tipos son obligatorias, mientras que en Python son opcionales. Además, TypeScript tiene un conjunto más amplio de tipos que Python.

```python
# Type Hints - Python es un lenguaje de tipado dinámico. #
def sum (a:int, b:int):
  return a + b

message:[str] = "Hello, World"

lst:[str] = list(["Alma", "Natalia", "Pamela"])


## === ##
if __name__ == "__main__":
  plus_sum = sum(4, 7)
  print(type(plus_sum)) # Tipo: "int"
  print(plus_sum)
  print(type(message)) #Tipo: "str"
```

### Backend Web Server With Fast API

> Fast API & Uvicorn

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def get_list():
  lst:[str] = list([2,4,7])
  return f"My list: {lst}"
```

> Call HTML with FastAPI

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# App Server #
app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def get_home():
   html_content =  """
    <html>
        <head>
            <title>Some HTML in here</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Hello Dev! HTML & Python!</h1>
            <h2>Python Backend </h2>
        </body>
    </html>
    """
   return HTMLResponse(content=html_content, status_code=200)

##HomePage
@app.get('/home', response_class=HTMLResponse)
async def get_page(): 
   html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Home Page</h1>
            <p>Hello World! Python In Backend!!! Amazing</p>
        </body>
    </html>
   """
   return HTMLResponse(content=html_content, status_code=200)


```

> API REST & API CRUD (APIFAST) Documentation With Swagger UI

[Swagger-ui](https://github.com/swagger-api/swagger-ui)
[Swagger](https://swagger.io/)

> Postman & Thunder Client & iNSOMNIA

[Postman](https://www.postman.com/)

[Thunder Client](https://www.thunderclient.com/)

[Insomnia](https://insomnia.rest/)

> POO And API (FastAPI)

> Pydantic es una biblioteca de Python para la validación de datos y la gestión de configuraciones. Se basa en la notación de tipos de Python para especificar los tipos y restricciones de los datos.

[FastAPI: Request Body](https://fastapi.tiangolo.com/tutorial/body/#create-your-data-model)

```python
from fastapi import FastAPI
from pydantic import BaseModel
# === POO (Instancia y Entidad del Objeto) ===
#A)
class User(BaseModel):
  name: str
  url: str 
  age: int

app = FastAPI()

#GET 
@app.get("/")
async def root():
  return {"message": str("Hello Users")}

@app.get("/usersClass/")
async def usersClass():
  user_instance = User(name="Mouredev", url="http://mouredev.dev", age=35)
  return user_instance

#POST
@app.post("/users/")
async def create_users(user: User):
  return user
```

> Path & Query (Parameters)

> TODO En general, los path parameters se utilizan para identificar un recurso específico en tu API, mientras que los query parameters se utilizan para filtrar o ordenar los resultados de una consulta.

> /userQuery/?query_param=Midudev (My Example)

```python
#GET: Path Parameter (int:id)
@app.get("/user/{id}")
async def user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]#[0]
  except: 
    return {"error": "Add a new User"}

#GET: Query Parameter (str:name)
""" @app.get("/userQuery/")
async def user_query(query_param: str = None):
  return {"query_param": query_param} """

@app.get("/userQuery/")
async def user_query(query_param: str = None):
  if query_param: 
    filter_user = [user for user in users_list if query_param.lower() in user.name.lower()]
    return {"users": [user.__dict__ for user in filter_user]}
  else: 
    return {"users": [user.__dict__ for user in users_list]}
```

```python
#GET: Query Parameter (str:name)
@app.get("/userDev/")
async def user_query(id: int, name: str):
  return searchUser(id, name)

def searchUser(id: int, name: str): 
    '''
     #users = filter(lambda user: user.id == id, users_list) 
     #user == "u"
     /userDev/?id=2&name=Midudev
     Se agregó un name: str al parámetro de la función user_query para permitir la búsqueda por name en los query parameters.
     Se utilizó la expresión generadora next para buscar el usuario de manera más eficiente.
     Se comparan los nombres de manera insensible a mayúsculas y minúsculas (name.lower()) para hacer la búsqueda del usuario no sensible a mayúsculas/minúsculas.
    '''
    user = next((u for u in users_list if u.id == id and u.name.lower() == name.lower()), None)
    try:
      if user:
        return user.__dict__
      else: 
        return {"error": "Error 404. Not Found User"}
    except: 
      return {"error": "Add a new User"}
```

> Algunos Ejemplos para Path & Query Parameters: 

```python
#### Path parameters:
#/users/{user_id}
#/files/{file_path}
#/products/{product_id}

#### Query parameters:
#/users?q=John
#/products?sort_by=price
#/orders?limit=10
```

> POST & PUT (API) 

> DOCS => Read in JSON (API)

```python
#POST (To create data)
@app.post("/users/")
async def create_users(user: User):
    if type(search_user(user.id, user.name)) == User:
     return {"error": str("User Exist.")}
    else:
     users_list.append(user)
```

```python
#PUT (To update data)
@app.put("/users/")
async def user(user: User): 
  user_found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      user_found = True

  if not user_found: 
     return {"error": "Sorry! This User Not Exist. Add a new User."}
```