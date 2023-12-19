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

> Create Virtual Environments for work in Python (Entorno Virtual)

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


```

> Correr el servidor (Pruebas)

```python
# Correr el Servidor Web (Uvicorn & FastAPI)
uvicorn main:app --reload

# Port (Puerto)
uvicorn main:app --reload --port 5000 

# Red (Solo poner el puerto)
uvicorn main:app --reload --port 5000 --host 0.0.0.0

#Swagger (FastAPI)

http://127.0.0.1:8000/docs

```

> Métodos HTTP

```
POST: crear un recurso nuevo.
PUT: modificar un recurso existente.
GET: consultar información de un recurso.
DELETE: eliminar un recurso.

```

> Status Code in FastAPI

[status](https://fastapi.tiangolo.com/es/reference/status/?h=status#fastapi.status.HTTP_404_NOT_FOUND)

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

> Términos Usados en FastAPI

```python
#: "**": Son los operadores de expansión de diccionario. Estos operadores permiten pasar todos los valores de un diccionario a un objeto de Pydantic.
#: Union es una herramienta en el módulo typing de Python que permite indicar que una variable, parámetro o atributo puede tener uno de varios tipos posibles. 
#: Optional es otra construcción útil del módulo typing en Python y se utiliza para indicar que una variable o parámetro puede ser de un tipo específico o None.  es útil para expresar la posibilidad de que una variable pueda tener un valor o no, y ayuda a mejorar la claridad en la lectura del código y en el sistema de tipado estático.
# Annotated se utiliza para agregar anotaciones adicionales a un tipo de variable.  Una o más anotaciones adicionales que se pueden utilizar para proporcionar información adicional sobre la variable.
# __new__ es un método especial en Python que se utiliza para crear una nueva instancia de una clase.

```

```PYTHON
# Fast API & Uvicorn 
# Siempre que llamamos a un Servidor tiene que ser Asíncrona 
# Use: /home/?query_param=Home
#Static: Para todo tipo de assets. (http://127.0.0.1:8000/static/images/astronauta_nave.jpg).Cuando tienes muchos archivos (imágenes) y vas a usar StaticFiles, es importante tener en cuenta el rendimiento. El StaticFiles de FastAPI está diseñado para ser eficiente con archivos pequeños, pero puede ser menos eficiente con archivos grandes. Puedes usar un CDN (Cloudinary).
#*OAuth 2.0 es un protocolo de autorización que permite a los usuarios autorizar a aplicaciones de terceros a acceder a sus datos sin tener que compartir sus credenciales de inicio de sesión.OAuth 2.0 funciona mediante la creación de un flujo de autorización en el que el usuario autoriza a la aplicación de terceros a acceder a sus datos.
```

```python
# @app.get("/") define una ruta en la raíz de tu aplicación. async def read_csv(): es la función que se ejecutará cuando se realice una solicitud GET a la ruta especificada. return {"data": df.head(5).to_dict(orient="records")} devuelve las primeras 5 filas del DataFrame df como un diccionario JSON.
# En el contexto de la función to_dict de pandas, el parámetro orient especifica el formato en el que se devolverá el diccionario. El valor "records" significa que los datos se representarán como una lista de registros, donde cada registro es un diccionario que contiene los datos de una fila del DataFrame.
# OS: Path => System Operator
# Prefixed => Ya no es necesario poner todo el "output".
# Tags => Dividir por parámetros la documentación (API) y ("path operations in this router").
#Query Parameters: Los parámetros de consulta son aquellos que se incluyen en la URL después del signo de interrogación ? y se separan por el símbolo &.

```

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

> POO And API (FastAPI) (endpoints) 

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

> Docs => Read in JSON (API) / (exampleAPI:8000/docs/) 

```python
#POST (To create data)
@app.post("/users/")
async def create_users(user: User):
    if type(search_user(user.id, user.name)) == User:
     return {"error": str("User Exist.")}
    else:
     users_list.append(user)
```
> Otra forma de hacer POST:

```python
# Previa Base de Movies.
@app.post('/movie/', status_code=200, tags=['movie'])
async def create_movie(request: Request):
    '''
    movies_api.append(movie_data) para agregar la nueva película al final de la lista movies_api. Ahora, la nueva película se agrega correctamente a la lista existente.
    '''
    movie_data = await request.json()

     # = Validación de datos (puedes agregar más validaciones según tus necesidades) =
    required_fields = ["id", "title", "overview", "year", "rating", "category"]
    if not all(item in movie_data for item in required_fields):
      raise HTTPException(status_code=400, detail="Missing required fields in movie data") 

     # = Agregar la nueva película a la lista movies_api =
    movies_api.append(movie_data)

    return movie_data

```

> POST Usando POO (Instancia de Objeto)

```python
# === Esquema e Usar Mi instancia (Class) ===
@app.post("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def created_movies(movies: Movies): 
  try: 
    # Obtener el máximo ID existente y asignar uno nuevo
    new_id = max((m.id for m in movie_singleton.get_movies_object()), default=0) + 1
    # Asignar el nuevo ID al objeto Movies
    movies.id = new_id
    # Convertir el objeto Movies a un diccionario
    movie_dict = movies.dict()
    # Agregar el nuevo diccionario a la lista de movies_object
    movie_singleton.get_movies_object().append(movie_dict)
    #movies_pattern = movie_singleton.get_movies_object()
    #movies_pattern.append(movie_dict)
    return movie_dict

  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating movie: {str(e)}")

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

> HTTP Status Code

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[FastAPI_HTTP](https://fastapi.tiangolo.com/reference/exceptions/?h=http+ex)

```python

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

### Roouters & FastAPI

[APIRouter](https://fastapi.tiangolo.com/reference/apirouter/?h=apirou)

[APIRouter_Request ](https://fastapi.tiangolo.com/how-to/custom-request-and-route/?h=apirou)

> Beneficios de usar Routers en FastAPI: Organización modular: Los routers le permiten dividir su API en unidades más pequeñas y manejables, promoviendo la reutilización de código y mejorando la mantenibilidad.

> Mejor legibilidad: Los routers mejoran la legibilidad y comprensibilidad del código de su API, especialmente para aplicaciones más grandes con numerosos endpoints.

> Agrupación de endpoints relacionados: Los routers le permiten agrupar las operaciones de ruta en función de la funcionalidad o el dominio, lo que facilita la navegación y la comprensión de la estructura de la API.

> Encapsulación y espacios de nombres: Los routers proporcionan encapsulación al agrupar las operaciones de ruta relacionadas dentro de un espacio de nombres específico, lo que reduce la probabilidad de conflictos de nombres y mejora la organización del código.

> Implementación modular: Los routers se pueden implementar de forma independiente, lo que le permite implementar o actualizar selectivamente partes específicas de su API sin afectar a toda la aplicación.

> FastAPI proporciona una poderosa característica llamada routers que le permite organizar y estructurar su API de manera modular y mantenible. Los routers son esencialmente clases que agrupan operaciones de ruta (endpoints) relacionadas, lo que facilita la gestión y el escalado de su API a medida que crece en complejidad.

```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


app.include_router(router)

```

> Import in Fast API

> Recuerda: "__init__.py", para que te pueda leer e puedas tu paquete (todos tus módulos)
```python
 routers
│   ├── __init__.py
│   ├── __pycache__
│   ├── products.py
│   └── user.py
```

```python
#Una forma de importar e leer tu archivo que estás importando. 
from routers.products import router as product_router
```

```python
app.include_router(product_router)
```

> APIRouter

[APIRouter](https://fastapi.tiangolo.com/reference/apirouter/?h=apirout)

```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


app.include_router(router)
```

> Bigger Applications - Multiple Files

[multiple_files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin

```

> Para Obtener e trabajar con Data (CSV)

[Kaggle](https://www.kaggle.com/)

> StaticFiles 

[StaticFiles](https://fastapi.tiangolo.com/reference/staticfiles/?h=static#fastapi.staticfiles.StaticFiles)

[StaticFiles](https://fastapi.tiangolo.com/tutorial/static-files/?h=stati)

```
 Cuando tienes muchos archivos (imágenes) y vas a usar StaticFiles, es importante tener en cuenta el rendimiento. El StaticFiles de FastAPI está diseñado para ser eficiente con archivos pequeños, pero puede ser menos eficiente con archivos grandes.
```

> File y Staticfiles 

```
File y Staticfiles son dos tipos de datos diferentes en FastAPI que se utilizan para manejar archivos.

File es un tipo de datos especial de FileUpload de FastAPI que proporciona información adicional sobre el archivo, como el nombre del archivo, el tamaño del archivo y el tipo del archivo. Se utiliza para recibir archivos subidos por los usuarios.

Staticfiles es un tipo de datos que representa un archivo estático, como un archivo de imagen, CSS o JavaScript. Se utiliza para servir archivos estáticos a los usuarios.

Diferencias:

Propósito:
File se utiliza para recibir archivos subidos por los usuarios.
Staticfiles se utiliza para servir archivos estáticos a los usuarios.
Información adicional:
File proporciona información adicional sobre el archivo, como el nombre del archivo, el tamaño del archivo y el tipo del archivo.
Staticfiles no proporciona ninguna información adicional sobre el archivo.
Ubicación:
File se almacena en la memoria del servidor o en un sistema de archivos externo.
Staticfiles se almacena en un sistema de archivos externo, como un servidor web.
Necesidad de subir imágenes:

Si necesitas subir imágenes, debes usar el tipo de datos File. File te permite acceder al nombre del archivo, el tamaño del archivo y el tipo del archivo, que son necesarios para procesar y almacenar las imágenes.

```

> UploadFile

[Uploadfiles](https://fastapi.tiangolo.com/reference/uploadfile/?h=up#fastapi.UploadFile.filename)

```python
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

```

> CDN (Content Delivery Network)

[Cloudinary](https://cloudinary.com/)

> puedes usar Cloudinary para mejorar el rendimiento de los archivos estáticos en tu aplicación FastAPI. Cloudinary es un servicio CDN que proporciona una amplia gama de funciones para optimizar el rendimiento de los archivos multimedia.

> Cloudinary puede ayudarte a mejorar el rendimiento de los archivos estáticos de las siguientes maneras:

> Almacenamiento en caché en la nube. Cloudinary almacena los archivos multimedia en caché en la nube, lo que puede reducir significativamente el tiempo de carga de los archivos.
> Optimización de imágenes. Cloudinary puede optimizar las imágenes para reducir su tamaño y mejorar su rendimiento.
> CDN global. Cloudinary tiene una red de servidores CDN global, lo que puede mejorar el rendimiento de los archivos multimedia para los usuarios que se encuentran lejos del servidor web.

```python
#Import StaticFiles.
#from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

### Security oAuth2 & Mildware

> FastAPI

> OAuth 2.0 es un protocolo de autorización que permite a los usuarios autorizar a aplicaciones de terceros a acceder a sus datos sin tener que compartir sus credenciales de inicio de sesión.OAuth 2.0 funciona mediante la creación de un flujo de autorización en el que el usuario autoriza a la aplicación de terceros a acceder a sus datos.

```
OAuth 2.0 es un protocolo de autorización ampliamente utilizado en el mundo de la seguridad web para permitir que una aplicación acceda a recursos protegidos en nombre de un usuario. A continuación, te proporcionaré una visión general de cómo funciona OAuth 2.0 en el contexto de la autenticación y algunos consejos sobre seguridad.

Flujo Básico de OAuth 2.0:
Solicitud de Autorización (Authorization Request): La aplicación (cliente) solicita permiso al usuario para acceder a sus recursos protegidos.

Redireccionamiento a la Autoridad de Autorización (Authorization Server): El usuario es redirigido a la autoridad de autorización, donde autentica al usuario y otorga permisos a la aplicación.

Obtención del Código de Autorización (Authorization Code): Después de la autenticación exitosa, la aplicación recibe un código de autorización.

Intercambio del Código de Autorización por Tokens de Acceso: La aplicación intercambia el código de autorización por tokens de acceso y, en algunos casos, un token de actualización.

Uso del Token de Acceso: La aplicación utiliza el token de acceso para realizar solicitudes a los recursos protegidos en nombre del usuario.

Consideraciones de Seguridad en OAuth 2.0:
HTTPS: Todas las comunicaciones deben estar protegidas mediante el uso de HTTPS para evitar ataques de tipo "man-in-the-middle".

Almacenamiento Seguro de Tokens: Los tokens deben almacenarse de forma segura. En el lado del cliente, se suelen almacenar en cookies seguras o en el almacenamiento local.

Tiempo de Vida Limitado de Tokens: Los tokens deben tener tiempos de vida limitados para reducir el riesgo en caso de que sean interceptados.

Validación de Tokens: Los servidores deben validar los tokens antes de confiar en su contenido. Esto incluye verificar firmas y asegurarse de que el emisor del token sea legítimo.

Protección contra Ataques CSRF: Se deben implementar medidas para proteger contra ataques de Cross-Site Request Forgery (CSRF), como el uso de tokens anti-CSRF.

Consentimiento del Usuario: Los usuarios deben estar informados y dar su consentimiento antes de otorgar permisos a una aplicación.

Seguridad en la Aplicación: La aplicación debe implementar prácticas de seguridad sólidas, incluido el manejo seguro de secretos y la protección contra vulnerabilidades conocidas.

Actualizaciones de Token: Utiliza tokens de actualización para obtener nuevos tokens de acceso cuando sea necesario sin requerir que el usuario vuelva a autenticarse.

Revocación de Tokens: Implementa la capacidad de revocar tokens si es necesario (por ejemplo, si el usuario revoca los permisos de la aplicación).

Escenarios de Concesión Apropiados: Utiliza el flujo de concesión más apropiado para tu aplicación (por ejemplo, el flujo de autorización de código para aplicaciones web).

Es importante seguir las especificaciones y recomendaciones de seguridad de OAuth 2.0 y tener en cuenta las características específicas de tu aplicación al implementar la autenticación con OAuth 2.0.
```

[FastAPI_Security](https://fastapi.tiangolo.com/tutorial/security/)

[FastAPI_oAuth2](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

> Instalar Bibliotecas

> Configura el proveedor de identidad.

> Añade los middlewares de OAuth 2.0. Para proteger tus rutas con OAuth 2.0, necesitas añadir los middlewares de OAuth 2.0 a tu aplicación FastAPI. 

> OpenAPI define los siguientes esquemas de seguridad:

> apiKey: una clave específica de la aplicación que puede provenir de:

> Un parámetro de consulta.
> Un encabezado.
> Una galleta.

> http: sistemas de autenticación HTTP estándar, que incluyen:

> bearer: un encabezado Authorizationcon un valor de Bearermás un token. Esto se hereda de OAuth2.

> Autenticación básica HTTP.

> Resumen HTTP, etc.

> oauth2: todas las formas de OAuth2 para manejar la seguridad (llamadas "flujos").

> Varios de estos flujos son apropiados para crear un proveedor de autenticación OAuth 2.0 (como Google, Facebook, Twitter, GitHub, etc.):

> implicit
> clientCredentials
> authorizationCode

> Pero hay un "flujo" específico que se puede utilizar perfectamente para manejar la autenticación directamente en la misma aplicación:

> password: algunos de los próximos capítulos cubrirán ejemplos de esto.

> openIdConnect: tiene una forma de definir cómo descubrir datos de autenticación OAuth2 automáticamente.

> Este descubrimiento automático es lo que se define en la especificación OpenID Connect.

```
pip install fastapi-oauth2 pydantic
```

```python
from fastapi import FastAPI
from fastapi_oauth2 import OAuth2, OAuth2Settings
```

> Install Multipart

```
pip install python-multipart
```

```python
En Python, el módulo multipart proporciona una clase MultipartEncoder para crear solicitudes HTTP multipart. Las solicitudes multipart se utilizan para enviar datos que contienen tanto datos de formulario como archivos.

La clase MultipartEncoder toma un diccionario como argumento. El diccionario contiene los datos de formulario que se enviarán en la solicitud. Los datos de formulario se pueden especificar como cadenas, números, listas o diccionarios.

Para enviar archivos con una solicitud multipart, utilice el método add_file() de la clase MultipartEncoder. El método add_file() toma dos argumentos: el nombre del archivo y el contenido del archivo.
```

[Guide_multipart](https://andrew-d.github.io/python-multipart/)

> Mildware

[FastAPI_Mildware](https://fastapi.tiangolo.com/tutorial/middleware/)

> JWT (Jason Web Token)

[JWT](https://jwt.io/)

![](https://supertokens.com/static/b0172cabbcd583dd4ed222bdb83fc51a/9af93/jwt-structure.png)

> Autenticación basada en tokens

![](https://static.platzi.com/media/user_upload/autenticaci%C3%B3nBasadaEnTokens-9088a5af-4c44-43f8-8e4f-bc944c04e6dc.jpg)

> PyJWT

> PyJWT (Python JSON Web Token) es una biblioteca de Python que se utiliza para codificar y decodificar tokens JWT (JSON Web Token). Un token JWT es un objeto de seguridad que se utiliza para autenticar a los usuarios en aplicaciones web y móviles. Los tokens JWT se emiten por un servidor de autenticación y luego se envían al cliente, que los utiliza para demostrar su identidad al acceder a recursos protegidos en el servidor.

[PyJWT](https://pyjwt.readthedocs.io/en/stable/#)

[PyJWT_cryptography](https://cryptography.io/en/latest/)

```
pip install "python-jose[cryptography]"

```

```python
from jose import JWTError, jwt
```

> Como buenas practicas: 1- La información contenida en el payload es facilmente detectable, por lo que es importante que no vaya información sencible o podra ser hackeada. 2- La llave es gran parte de lo que da la seguridad en jwt, por lo que no debe quedar expuesta en el código y es sano usar un .env depronto con la libreria

> Install passlib

[oAuth2_JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

```
pip install "passlib[bcrypt]
```

> Tip: Autenticación, Autorización y Token. 

```

En general, la autenticación debe venir primero, seguida de la autorización.

La autenticación es el proceso de verificar la identidad de un usuario. Este proceso suele implicar la solicitud de un nombre de usuario y una contraseña. Una vez que el usuario proporciona esta información, el sistema de autenticación la compara con una base de datos de usuarios válidos. Si la información coincide, el usuario se considera autenticado.

La autorización es el proceso de determinar qué recursos o acciones puede realizar un usuario. Este proceso suele implicar la asignación de roles o permisos a los usuarios. Un rol es un conjunto de permisos que determina qué puede hacer un usuario. Un permiso es la capacidad de realizar una acción específica.

En el contexto de un sistema de API, la autenticación se utiliza para verificar que el usuario que está realizando una solicitud es quien dice ser. La autorización se utiliza para determinar si el usuario tiene permiso para realizar la solicitud.

Por lo tanto, la secuencia lógica para desarrollar un sistema de autenticación y autorización es la siguiente:

Definir los roles y permisos necesarios. ¿Qué roles se necesitan en el sistema? ¿Qué permisos se asignan a cada rol?
Implementar el proceso de autenticación. ¿Cómo se verificará la identidad de los usuarios? ¿Qué datos se solicitarán a los usuarios?
Implementar el proceso de autorización. ¿Cómo se determinarán los permisos de los usuarios?
En el caso específico de la creación de un token, la creación del token se puede realizar en cualquier momento durante el proceso de desarrollo. Sin embargo, es importante tener en cuenta que el token debe ser compatible con el proceso de autenticación y autorización.
```

```
pip install dotenv
```

> Validación de Datos con Pydantic

> Pydantic es la biblioteca de validación de datos más utilizada para Python.

[Pydantic](https://docs.pydantic.dev/latest/)

> Podemos usar typing, para pasar una lista (List); para mejorar el tipado del código (usas una versión más vieja de Python) con Union. 


```python
from typing import List, Union, Optional
```

> Podemos pasar "status", en fastapi 

```python
from fastapi import FastAPI, HTTPException, Request, status
```

[status](https://fastapi.tiangolo.com/es/reference/status/?h=status#fastapi.status.HTTP_404_NOT_FOUND)

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[HTTP_CAT](https://http.cat/)

> Para pasar de JSON (tienes datos) e utilizar una instancia (POO), puedes pasar toda esa información a un dict()

```python
# Parsear la lista movies_api en una lista de objetos Movies
movies_objects = [Movies.parse_obj(movie) for movie in movies_api] #List[Movies] = []
# Ahora, movies_objects es una lista de objetos de la clase Movies
for movie_obj in movies_objects:
  print(movie_obj.dict())
```

> Field Validation (Pydantic)

> En Pydantic, el atributo Field se utiliza para proporcionar configuraciones adicionales a un campo de un modelo. Puedes usar Field para especificar reglas de validación, valores predeterminados y otras opciones para personalizar el comportamiento de un campo específico. 

```python

from typing import List
from pydantic import BaseModel, Field, ValidationError

class Person(BaseModel):
    name: str
    age: int = Field(..., gt=0, description="Age of the person (must be greater than 0)")
    email: str = Field(..., regex=r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", description="Valid email address")

class Employee(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., max_length=50)
    skills: List[str] = Field(..., min_items=1, max_items=10)

# Ejemplo de uso
try:
    person_data = {"name": "John", "age": 30, "email": "john@example.com"}
    person = Person(**person_data)
    print(person)
except ValidationError as e:
    print(e.json())

try:
    employee_data = {"id": 1, "name": "Alice", "skills": ["Python", "FastAPI", "SQL"]}
    employee = Employee(**employee_data)
    print(employee)
except ValidationError as e:
    print(e.json())


```

> ValidationError

```python 
try:
    person_data = {"name": "John", "age": 30, "email": "john@example.com"}
    person = Person(**person_data)
    print(person)
except ValidationError as e:
    print(e.json())

```
>  Puedes agregar validación a este parámetro de ruta usando la clase Path de FastAPI 

> Annotated se utiliza para agregar anotaciones adicionales a un tipo de variable.  Una o más anotaciones adicionales que se pueden utilizar para proporcionar información adicional sobre la variable.

> Path y Query para validar parámetros en FastAPI. Ambos son usados para manejar diferentes tipos de parámetros, y puedes aplicar validaciones a ambos.

> Path se utiliza para parámetros de ruta, que son parte de la URL.

> Query se utiliza para parámetros de consulta, que se pasan como parte de la URL después del signo de interrogación (?).

```python
from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

```

> FastAPI & JSONResponse (Pydantic)

[FastAPI](https://fastapi.tiangolo.com/tutorial/response-model/?h=jsonresponse#return-a-response-directly)

> La conversión a JSON es un paso común cuando estás construyendo APIs RESTful. Cuando tu aplicación FastAPI devuelve datos, especialmente datos que pueden ser consumidos por otros sistemas o clientes web, generalmente se prefiere el formato JSON para la respuesta.

> serializar a JSON & APIs RESTful

```python
@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_all_movie(): 
  '''
  he utilizado la función dict() de Pydantic para convertir cada objeto Movies a un diccionario antes de devolver la respuesta JSON.
  '''
  #return movie_singleton.get_movies_object()
  movies_objects = movie_singleton.get_movies_object()
  # Convertir los objetos Movies a diccionarios antes de serializar
  json_response_movie = [movie.dict() for movie in movies_objects]
  return JSONResponse(content=json_response_movie)
```

> Podemos conectar nuestra API con frontend e usarla (APIs RESTful) 

> La conversión a JSON es un paso común cuando estás construyendo APIs RESTful. Cuando tu aplicación FastAPI devuelve datos, especialmente datos que pueden ser consumidos por otros sistemas o clientes web, generalmente se prefiere el formato JSON para la respuesta.

> En este contexto:

> Interoperabilidad: JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y ampliamente aceptado. La mayoría de los lenguajes de programación pueden trabajar fácilmente con datos en formato JSON, lo que facilita la interoperabilidad entre diferentes sistemas.

> Legibilidad: JSON es fácil de leer y entender tanto para humanos como para máquinas. Al devolver datos en formato JSON, facilitas a los desarrolladores y a las herramientas de consumo de APIs procesar y trabajar con los datos de manera eficiente.

> Compatibilidad con el estándar HTTP: La mayoría de las bibliotecas y herramientas que trabajan con HTTP/APIs esperan o pueden manejar respuestas en formato JSON. Esto incluye bibliotecas en el lado del cliente (como axios en JavaScript) y herramientas de prueba de APIs.

> En resumen, convertir los datos a JSON al devolverlos en una respuesta de API hace que la API sea más fácil de consumir y utilizar en un contexto web o de servicios. FastAPI proporciona funcionalidades integradas para la serialización automática de objetos Pydantic a JSON cuando se devuelven en respuestas de ruta.

> Nota: 

```
1.FastAPI manejará la serialización automáticamente.
2.FastAPI maneja automáticamente la serialización de objetos Pydantic a JSON, no necesitas envolver tu respuesta en JSONResponse 
```

> RedirectResponse

[RedirectResponse](https://fastapi.tiangolo.com/tutorial/response-model/?h=jsonresponse#return-a-response-directly)

> RedirectResponse en FastAPI se utiliza para redirigir a los clientes a otra URL. Puedes usarlo cuando quieras redirigir al usuario a una nueva ubicación después de que se ha realizado una acción, como un envío de formulario o cualquier otra operación.

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def read_root():
    # Al acceder a la ruta "/", el usuario será redirigido a "/docs"
    return RedirectResponse(url="/docs")

```

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

> En este ejemplo, cuando alguien accede a la ruta principal ("/"), se le redirigirá a la ruta "/docs". Puedes personalizar la URL de redirección según tus necesidades.

> Esto puede ser útil, por ejemplo, después de que un usuario ha enviado un formulario y deseas redirigirlo a una página de confirmación o a otra ubicación específica.

> Python Dotenv

```python
pip install python-dotenv
```

> Python-dotenv es una biblioteca de Python que permite leer y escribir variables de entorno desde un archivo .env. El archivo .env es un archivo de texto simple que contiene pares clave-valor, donde la clave es el nombre de la variable de entorno y el valor es el valor de la variable.

> Para usar python-dotenv, primero debe importar el módulo:

```python
import dotenv
```

> Puede llamar al método load() para leer el archivo .env:

```python
dotenv.load(".env")
```

> Importar un formato "JSON" y Agregarlo a la instancia de Clase. 

```python
movies_dir = os.path.dirname(__file__)
movies_api = os.path.join(movies_dir, "movieData", "movie.json")
with open(movies_api, "r") as f:
  movie_data = json.load(f)
```

```python
def __new__(cls): 
    if not cls._instance:
      cls._instance = super().__new__(cls) # Herencia Polimorfismo
      cls._instance.movie_data = movie_data
      cls._instance.movies_objects = [Movies.parse_obj(movie) for movie in cls._instance.movie_data] # Json => Parsear a Obj / dict
      return cls._instance  
```

> Note: 

> Nota: Depends. 

```
En el contexto de la autenticación OAuth2 en FastAPI, Depends se utiliza para declarar las dependencias necesarias para autenticar y autorizar a un usuario. Al utilizar Depends con funciones de seguridad proporcionadas por FastAPI, puedes asegurarte de que ciertas condiciones se cumplan antes de que la ruta protegida se ejecute.

Un ejemplo común es el uso de Depends con la función oauth2_scheme proporcionada por FastAPI para manejar la autenticación OAuth2. Aquí hay un ejemplo básico
```

```python
oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Aquí podrías realizar la validación del token y devolver el usuario actual
    # o lanzar una excepción HTTPException si la autenticación falla.
    return token

@app.get("/private-data/")
async def get_private_data(current_user: str = Depends(get_current_user)):
    return {"message": "Accedido a datos privados", "user": current_user}

```

> Note:

```python
claims = jwt.decode(token, secret, algorithm=["HS256"])
```

```
jwt: Se refiere al módulo o la biblioteca que estás utilizando para manejar tokens JWT. En este caso, parece que estás utilizando la biblioteca PyJWT. Asegúrate de haber importado el módulo antes de usarlo, por ejemplo: import jwt.

token: Es el token JWT que deseas decodificar. Este es el token que ha sido generado previamente y que contiene información cifrada.

secret: Es la clave secreta utilizada para firmar el token JWT. En el caso de algoritmos de firma como "HS256" (HMAC con SHA-256), se utiliza una clave secreta compartida entre el emisor (quien crea el token) y el receptor (quien lo valida).

algorithm=["HS256"]: Indica el algoritmo de firma que se utilizó para generar el token JWT. En este caso, se está especificando que el algoritmo es HMAC con SHA-256 (HS256). La lista proporcionada en algorithm permite especificar varios algoritmos en caso de que el token esté firmado con más de uno.

El resultado de jwt.decode() es un diccionario que representa las reclamaciones (claims) contenidas en el token JWT. Las reclamaciones son declaraciones sobre una entidad (por ejemplo, un usuario) y pueden incluir información como la identificación del usuario, el tiempo de expiración del token, roles, etc. El nombre claims se utiliza comúnmente para referirse a estas declaraciones en el contexto de los tokens JWT. Después de la decodificación, puedes acceder a la información contenida en el token a través del diccionario claims.
```

```python
if "exp" in claims and claims["exp"] < time.time():
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Expired Authentication Token." #Token de autenticación caducado
    )
```

```
"exp" : Expiración del Token. 
```

```python
username = claims["sub"] #Subject == Sujeto
```

> Starlette (Para hacer templates - Interfaz -Jinja2)

[starlette](https://www.starlette.io/)

> Middleware

[FastAPI_Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)

[Advanced_Middleware](https://fastapi.tiangolo.com/advanced/middleware/)

> Test Middleware 

[test_middleware](https://jaketrent.com/post/test-middleware-header-fastapi/)

> Middleware for Starlette/FastAPI 

[starlette_github](https://github.com/open-telemetry/opentelemetry-python/issues/710)

```
Un "middleware" es una función que funciona con cada solicitud antes de que sea procesada por cualquier operación de ruta específica . Y también con cada respuesta antes de devolverlo.
```

```python
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

```python
from fastapi import Depends, HTTPException, Request
from fastapi.middleware import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def setup(self, app: FastAPI) -> None:
        print("AuthMiddleware: Setup")

    async def handle(self, request: Request, call_next: Callable) -> HTTPResponse:
        username, password = request.headers.get("Authorization", "").split(" ")
        if not username or not password:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Implementar la lógica de autenticación con username y password

        # Si la autenticación es correcta:
        response = await call_next(request)
        return response

        # Si la autenticación falla:
        raise HTTPException(status_code=401, detail="Invalid credentials")

app.add_middleware(AuthMiddleware())


```

> HTTP Tips & FastAPI HTTP

[HowHTTP](https://howhttps.works/es/)

[fastAPI_HTTP](https://fastapi.tiangolo.com/deployment/https/?h=call+http)

> Importante: from starlette.middleware.base import BaseHTTPMiddleware ? 

[starlette_Middleware](https://www.starlette.io/middleware/#httpsredirectmiddleware)

```
El motivo por el que tu código no leía from fastapi.middleware import BaseHTTPMiddleware y tuviste que pasar a from starlette.middleware.base import BaseHTTPMiddleware se debe a la estructura interna de FastAPI.

FastAPI se basa en Starlette: FastAPI está construido sobre la base de Starlette, un framework web de alto rendimiento y flexible para Python. Esto significa que FastAPI hereda funcionalidades de Starlette, incluyendo la clase BaseHTTPMiddleware para crear middlewares.

Importación en FastAPI: En las versiones recientes de FastAPI (0.67.0+), la clase BaseHTTPMiddleware se ha trasladado a Starlette para evitar la redundancia y simplificar la arquitectura interna. Por eso, ya no está directamente disponible en fastapi.middleware.

Solución: Tu solución de utilizar from starlette.middleware.base import BaseHTTPMiddleware es correcta y ahora tu código debería funcionar sin problemas.

Recomendaciones:

Actualice su documentación: Si está trabajando con código o tutoriales escritos antes de la versión 0.67.0 de FastAPI, es importante tener en cuenta este cambio en la importación. Actualice su documentación y ejemplos de código para reflejar la nueva ubicación de la clase BaseHTTPMiddleware.
Manténgase actualizado: Consulte la documentación oficial de FastAPI para obtener la información más reciente sobre cambios y actualizaciones.
Comunidad de FastAPI: La comunidad de FastAPI es activa y servicial. Puede encontrar ayuda y recursos en el repositorio de GitHub, el canal de Discord y otros canales de la comunidad.
Espero que esta explicación haya aclarado el porqué de la necesidad de cambiar la importación de la clase BaseHTTPMiddleware. Si tiene más preguntas, no dude en preguntar.
```

> Nota: 

```python
#df.iterrows() y df.columns son funciones de pandas, una biblioteca de Python para el análisis de datos. Aquí te explico qué significan:

#df.iterrows(): Es un método de pandas que se utiliza para iterar sobre las filas de un DataFrame. Retorna un generador que proporciona índices de fila y Series correspondientes a las filas del DataFrame.

for index, row in df.iterrows():
    # index es el índice de la fila
    # row es una Serie que contiene los datos de la fila
    # Puedes acceder a los valores de la fila usando row['NombreColumna']

```

```
La expresión for _, row in df.iterrows(): es una forma común en Python de iterar sobre las filas de un DataFrame usando el método iterrows() de pandas. Aquí se explica cada parte de la expresión.

df.iterrows():: El método iterrows() de pandas se utiliza para iterar sobre las filas de un DataFrame. Retorna un generador que produce pares (índice, Serie) para cada fila del DataFrame. En este caso, el índice no se utiliza y la Serie (row) representa los datos de la fila actual.

En resumen, la expresión for _, row in df.iterrows(): se utiliza para iterar sobre todas las filas de un DataFrame (df). En cada iteración, row contendrá los datos de la fila actual en forma de una Serie de pandas, y el índice correspondiente se descarta utilizando el guion bajo (_). Este enfoque es común cuando solo estás interesado en los datos de las filas y no necesitas utilizar los índices.
```

> @Validator 

```
El decorador @validator en Pydantic te permite agregar validaciones personalizadas a los campos de tu modelo. Puedes utilizarlo para realizar acciones específicas antes de que los datos lleguen al modelo. En el ejemplo que te proporcioné, estoy utilizando @validator para realizar la conversión del campo size a un entero.
```