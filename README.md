# Python

> Basic Python

> Course of Python basic. Exercise and practice with Python. 

## Python con Platzi

> Root Complete Python in I.A

> platzi.com

[Platzi](https://platzi.com/)

> Roadmap
[roadmap](https://roadmap.sh/python)

> Topics Python - GitHub

[Topics_Python](https://github.com/topics/python)

> Awesome Python - GitHub

[Awesome_Python](https://github.com/vinta/awesome-python?tab=readme-ov-file#awesome-python)

> The Algorithm Python - GitHub

[TheAlgorithm_Python](https://github.com/TheAlgorithms/Python)

[The_Algorithm](https://github.com/TheAlgorithms)

> Hugging Face Python  - GitHub

[HuggingFace](https://github.com/huggingface)

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

> Test with pytest in Python 

[unittest](https://docs.python.org/3/library/unittest.html)

[pytest](https://docs.pytest.org/en/7.4.x/how-to/usage.html)

```
# pytest (Global)

# pytest /root

# Siempre comenzar con: "test_module". Ejemplo:"test_main.py"

# Importar e usar módulos: "from - import"
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

> UUID (Identificador Único Universal) en Python

[UUID](https://docs.python.org/es/3/library/uuid.html)

[UUID_English](https://docs.python.org/3/library/uuid.html)

```
UUID (Identificador Único Universal) en Python es una clase que representa un identificador único de 128 bits. Estos identificadores son comúnmente utilizados para asignar identificadores únicos a objetos, evitando así posibles colisiones de identificadores en sistemas distribuidos. Los UUID son generados de manera que es muy improbable que dos UUID generados aleatoriamente sean iguales.

Python proporciona el módulo uuid que contiene la clase UUID. Puedes utilizar esta clase para generar UUID aleatorios o basados en nombres, como strings o bytes.
```

```python
import uuid

# Generar un UUID aleatorio
random_uuid = uuid.uuid4()
print("UUID Aleatorio:", random_uuid)

# Generar un UUID basado en el nombre (por ejemplo, un string)
nombre = "Ejemplo de UUID"
nombre_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, nombre)
print("UUID basado en el nombre:", nombre_uuid)

```

> Otra forma de trabajar con una Instancia de Clase e Métodos (@validator & @static). 

```python
  @staticmethod
  def parse_size(value):
      try:
          if value is None or pd.isna(value): 
            return {"value": None, "error": None}
          
          size__value = int(value)

          if size__value < 0: 
              raise ValueError("Size should be a positive integer")
          
          return {"value", size__value, "error": None} 
      except (ValueError, TypeError) as e:
        return {"value": None, "error": {str(e)}}

```

> Validar Int (Enteros)

```python
  if value.isdigit():
             size_value = int(value)
             if size_value < 0: 
               raise ValueError("Size should be positive integer")
             return {"value": size_value, "error": None }
          else:
            return {"value": None, "error": "Size should be a valid integer"}
```

```python
  @validator("size", pre=True, always=True)
  def parse_size(value):
    if value is None: 
      return None
    if isinstance(value, int):
      return value
    try: 
      return int(value)
    except (ValueError, TypeError):
      raise ValidationError("Size...should be a valid integer")

```

> Renombrar 

```python
df = df.rename(columns={"Size": "size"})
```

> Nota: POST / Endpoint para agregar nuevos productos & El método .empty

```python
df = df.append(product_dict, ignore_index=True)
df.to_csv(file_path, index=False)
```

```
Cuando agregas un nuevo producto al DataFrame con ignore_index=True, estás asegurándote de que los índices se recalculen, y cuando guardas el DataFrame en un archivo CSV con index=False, estás evitando que los índices se guarden en el archivo CSV. Esto es típico cuando trabajas con datos tabulares y no necesitas incluir los índices en tu archivo de datos guardado.
```

```
ignore_index=True y index=False son parámetros utilizados al agregar nuevos datos a un DataFrame en pandas.

ignore_index=True: Este parámetro se utiliza al concatenar o agregar nuevos datos a un DataFrame. Si está establecido en True, se ignorarán los índices existentes y se generará un nuevo índice continuo. Esto es útil cuando estás agregando filas adicionales y no te importa mantener los índices originales.

index=False: Este parámetro se utiliza al guardar un DataFrame a un archivo CSV. Cuando index se establece en False, los índices del DataFrame no se incluirán en el archivo CSV resultante. Esto es comúnmente útil si no necesitas conservar los índices en el archivo CSV.

```

```
El método .empty se utiliza en pandas para verificar si un DataFrame o una Serie están vacíos, es decir, si no contienen ninguna fila.
```

```python
import pandas as pd

# Crear un DataFrame vacío
df = pd.DataFrame()

# Verificar si el DataFrame está vacío
if df.empty:
    print("El DataFrame está vacío.")
else:
    print("El DataFrame no está vacío.")

```

> Nota: POO (Métodos de Clase y de Instancia)

```
Método de Instancia:
Definición: Un método de instancia opera en una instancia particular de la clase y tiene acceso a los atributos específicos de esa instancia.
Sintaxis: Se define con la palabra clave def y toma self como el primer parámetro.
Acceso: Puede acceder a atributos y métodos de la instancia a través de self.
```

```python
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo_de_instancia(self):
        return f"Valor del atributo: {self.atributo}"

# Uso del método de instancia
objeto = MiClase("Hola")
resultado = objeto.metodo_de_instancia()
print(resultado)

```

```
Método de Clase:
Definición: Un método de clase opera en la clase en sí y no en una instancia particular. Tiene acceso a los atributos de la clase, pero no a los de instancias individuales.
Sintaxis: Se define con la palabra clave @classmethod y toma cls como el primer parámetro.
Acceso: Puede acceder a atributos y métodos de la clase a través de cls.

@classmethod
@staticmethod
@property

```

```python
class MiClase:
    atributo_de_clase = "Valor de clase"

    @classmethod
    def metodo_de_clase(cls):
        return f"Valor del atributo de clase: {cls.atributo_de_clase}"

# Uso del método de clase
resultado = MiClase.metodo_de_clase()
print(resultado)

```

> Leer un Documento CSV

```python
import csv

# Leer un archivo CSV
with open('archivo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Escribir en un archivo CSV
with open('nuevo_archivo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Columna1', 'Columna2'])
    writer.writerow(['Dato1', 'Dato2'])


```

> Tips: Para leer un Archivo "CSV", utilizando un Método de Clase (@classmethod)

```python
import csv 

def __str__(self) -> str:
    return f"This Iphone is: {self.name} and his price {self.price} and now in Store have these quantity {self.quantity} and Brand is {self.brand}"

@classmethod
  def read_from_csv(cls, file_path):
    items = []

    with open(file_path, "r") as file:
      reader = csv.reader(file)
      header = next(reader)  # Leer la primera fila como encabezado

      for row in reader:
        # Crear un diccionario con las claves del encabezado y los valores de la fila
        item_data = dict(zip(header, row))

        # Crear una instancia de Item y agregarla a la lista
        item_instance = cls(**item_data)
        items.append(item_instance)

    return items
```

```python
#Desde el archivo "data_poo"
items_from_csv = Item.read_from_csv("./data_poo/poo_data.csv")

for item in items_from_csv:
  print(str(item))

#Terminal: 
#This Iphone is: IPhoneX and his price 15000 and now in Store have these quantity 5 and Brand is Apple Iphone
```

> @abstractmethod

```
@abstractmethod es un decorador en Python que se utiliza para definir un método abstracto en una clase abstracta. Un método abstracto es un método que no tiene implementación en la clase abstracta, y su implementación debe proporcionarse por las clases concretas que heredan de la clase abstracta. Este decorador se encuentra en el módulo abc (Abstract Base Classes) y se utiliza en conjunto con otras funcionalidades para definir clases y métodos abstractos.

Cuando un método se marca con @abstractmethod, se indica que las clases derivadas deben proporcionar una implementación concreta de ese método. Si una clase derivada no proporciona dicha implementación, se considera una clase abstracta y no se puede instanciar.

En este ejemplo, AbstractClass es una clase abstracta con un método abstracto abstract_method. La clase concreta ConcreteClass hereda de AbstractClass y proporciona una implementación concreta del método abstracto. Al intentar instanciar la clase abstracta directamente, se generará un TypeError. Solo se pueden instanciar clases concretas que implementen todos los métodos abstractos definidos en la clase abstracta.
```

```python
from abc import ABC, abstractmethod

# Clase abstracta con método abstracto
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Clase concreta que hereda de la clase abstracta
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract_method in ConcreteClass")

# Intento de instanciar la clase abstracta (esto generará un error)
# abstract_instance = AbstractClass()  # Generará un TypeError

# Instanciar la clase concreta
concrete_instance = ConcreteClass()
concrete_instance.abstract_method()  # Salida: Implementation of abstract_method in ConcreteClass

```


#### 

> Tips and Information of Python: 

> *args y **kwargs 

```
*args y **kwargs son convenciones en Python para pasar un número variable de argumentos a una función.

*args se utiliza para pasar una lista variable de argumentos posicionales. Puedes pensar en *args como una forma de representar una lista de argumentos no clave.

**kwargs se utiliza para pasar una lista variable de argumentos de palabras clave. Puedes pensar en **kwargs como una forma de representar un diccionario de argumentos de palabras clave.

En este ejemplo, args recoge los argumentos posicionales (1, 2, 3), y kwargs recoge los argumentos de palabras clave (nombre="John", edad=25). Esto hace que la función sea flexible y pueda manejar una variedad de argumentos sin tener que especificarlos todos de antemano.
```

```python
def ejemplo_funcion(*args, **kwargs):
    print("Argumentos posicionales (*args):", args)
    print("Argumentos de palabras clave (**kwargs):", kwargs)

# Uso de la función con diferentes tipos de argumentos
ejemplo_funcion(1, 2, 3, nombre="John", edad=25)

```

> from abc import ABC, abstractmethod

```
ABC y abstractmethod son clases y decoradores, respectivamente, proporcionados por el módulo abc en Python, que se utiliza para trabajar con clases y métodos abstractos.

ABC (Abstract Base Class): Es una clase base que se utiliza para declarar una clase abstracta. Una clase abstracta es una clase que no puede ser instanciada directamente y que puede contener métodos abstractos.

abstractmethod: Es un decorador que se utiliza para declarar un método abstracto dentro de una clase abstracta. Un método abstracto es un método que debe ser implementado por cualquier subclase concreta de la clase abstracta que lo contiene.
```

#### POO - Información Extra (Complementaria) -

> Poo: Herencia Múltiple: 

```
La herencia múltiple es un concepto en programación orientada a objetos (POO) que permite que una clase herede atributos y métodos de más de una clase base. En Python, la herencia múltiple se logra permitiendo que una clase tenga más de una clase padre. Esto significa que la clase hija hereda tanto de la primera clase como de la segunda clase, y así sucesivamente.

Es importante tener en cuenta que la herencia múltiple puede conducir a situaciones llamadas "diamante" o "problema del diamante", que ocurren cuando una clase tiene dos clases base que comparten una clase común. Esto puede causar ambigüedades en la resolución de métodos y atributos. Python resuelve este problema utilizando un orden de resolución de clases llamado el "MRO" (Method Resolution Order).
```

```python
# Definición de la primera clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Definición de la segunda clase base
class Volador:
    def volar(self):
        print(f"{self.nombre} está volando")

# Clase que hereda de ambas clases base (herencia múltiple)
class Pajaro(Animal, Volador):
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido de pájaro")

# Crear una instancia de la clase Pajaro
mi_pajaro = Pajaro("Piolín")

# Acceder a métodos de las clases base
mi_pajaro.hacer_sonido()  # Salida: Piolín hace un sonido de pájaro
mi_pajaro.volar()         # Salida: Piolín está volando

```

> Example Two:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Definición de la segunda clase base
class Volador:
    def __init__(self, type):
      self.type = type

    def volar(self):
        print(f"{self.nombre} está volando")

# Clase que hereda de ambas clases base (herencia múltiple)
class Pajaro(Animal, Volador):
    def __init__(self, name, type, color):
      Animal.__init__(self, name)
      Volador.__init__(self, type)
      self.color = color

    def __str__(self) -> str:
      print(f"My Animal {self.anima} is the type: {self.type} and color {self.color}")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido de pájaro")

    def animal_fly(self):
      return f"My Animal: {super().volar()}}"

```

> Tip: Los Patrones de Diseño (Pattern Design), pueden ayudar a evitar problemas con tu código (Herencia Múltiple). Checa los Patrones de Diseño: 

[Pattern Design - Patrones de Diseño](https://refactoring.guru/es)

> MRO" (Method Resolution Order).

```
El MRO determina el orden en el que se buscan los métodos y atributos en las clases base. Puedes obtener el MRO de una clase utilizando el atributo __mro__ o la función mro():
```

```python
print(Pajaro.__mro__)
# Salida: (<class '__main__.Pajaro'>, <class '__main__.Animal'>, <class '__main__.Volador'>, <class 'object'>)
```

> POO - Polimorfismo

```
Puedes usar Patrones de Diseño como: Creacionales (Factory Method o Abstract Factoy)
```

```
1- Polimorfismo de Sobrecarga (Compile-time):

También conocido como polimorfismo estático o de compilación.
Se refiere a la capacidad de una clase para proporcionar múltiples métodos con el mismo nombre pero con diferentes firmas (número o tipo de parámetros).
El compilador selecciona la función adecuada en función de la cantidad y tipo de argumentos.
```

```
2- Polimorfismo de Sobrescritura (Run-time):

También conocido como polimorfismo dinámico o de ejecución.
Ocurre cuando una clase derivada proporciona una implementación específica para un método que ya está definido en su clase base.
Se logra mediante el uso de punteros o referencias a la clase base.
```

> Duck Typing en Python:

```
"Duck Typing" es un concepto en programación que se refiere a la determinación del tipo de un objeto por sus métodos y propiedades en lugar de su tipo explícito o declaración de interfaz. La idea detrás de Duck Typing es que si un objeto se comporta como un pato (quack como un pato, camina como un pato), entonces trataremos ese objeto como un pato, sin importar su tipo real.

En Python, un lenguaje de programación de tipado dinámico, el Duck Typing es una característica natural. Veamos un ejemplo para entender cómo se usa en POO:

Respuesta: 
En este ejemplo, tenemos tres clases (Pato, Perro y Robot) que tienen un método llamado hacer_sonido. Luego, tenemos una función hacer_sonido_del_animal que toma un objeto como argumento y llama a su método hacer_sonido. Aunque las clases no comparten una interfaz común formal, el código funciona gracias al Duck Typing: si el objeto tiene un método hacer_sonido, podemos tratarlo como un "animal".

Beneficios en el Código:

Flexibilidad y Simplificación del Código:

Duck Typing permite que el código sea más flexible y menos dependiente de tipos específicos. Si un objeto tiene los métodos y atributos necesarios, se puede utilizar en un contexto específico sin preocuparse por su tipo real.
Menos Dependencia de Jerarquías de Clases:

No es necesario que las clases compartan una jerarquía común o implementen una interfaz explícita. Puedes trabajar con objetos basándote en su comportamiento más que en su tipo.
Facilita la Reutilización de Código:

Como no te limitas a trabajar con tipos específicos, puedes reutilizar código en situaciones diversas siempre que los objetos compartan el comportamiento necesario.
Promueve el Principio "EAFP" (Easier to Ask for Forgiveness than Permission):

Es una filosofía en Python que fomenta la escritura de código que simplemente intenta realizar una operación y maneja las excepciones si algo sale mal. Duck Typing se alinea bien con este principio ya que te permite asumir que los objetos tienen ciertas propiedades y métodos y manejar cualquier error que pueda surgir.
En resumen, Duck Typing en Python es una herramienta poderosa que te permite escribir código más flexible, genérico y fácil de mantener al centrarte en el comportamiento de los objetos en lugar de su tipo concreto. Esto facilita la adaptabilidad del código a medida que evoluciona y se expande.
```

```python
class Pato:
    def hacer_sonido(self):
        print("Quack, quack")

class Perro:
    def hacer_sonido(self):
        print("Woof, woof")

class Robot:
    def hacer_sonido(self):
        print("Beep, beep")

def hacer_sonido_del_animal(animal):
    animal.hacer_sonido()

pato = Pato()
perro = Perro()
robot = Robot()

hacer_sonido_del_animal(pato)  # Imprime: Quack, quack
hacer_sonido_del_animal(perro)  # Imprime: Woof, woof
hacer_sonido_del_animal(robot)  # Imprime: Beep, beep

```

> Encapsulamiento / Encapsulation - POO

```
Encapsulamiento en Programación Orientada a Objetos (POO) con Python:

El encapsulamiento es uno de los principios fundamentales de la programación orientada a objetos (POO). Consiste en ocultar los detalles internos de un objeto y limitar el acceso a ciertos componentes, mientras se expone una interfaz clara y definida para interactuar con dicho objeto. En Python, el encapsulamiento se logra principalmente mediante el uso de atributos y métodos privados.

Atributos y Métodos Privados:
En Python, la convención para indicar que un atributo o método es privado es agregar un guion bajo doble (__) como prefijo al nombre del atributo o método.

Respuesta: 
En este ejemplo, __nombre y __edad son atributos privados de la clase Persona. Se proporcionan métodos públicos get_nombre y set_nombre para obtener y modificar el nombre, respectivamente. Además, hay un método privado llamado __metodo_privado, que solo puede ser llamado desde dentro de la propia clase.

Beneficios del Encapsulamiento en Python:
Control de Acceso:

Los atributos y métodos privados permiten controlar el acceso a los detalles internos de una clase, evitando cambios no autorizados desde fuera de la clase.
Prevención de Acceso Directo:

Al utilizar métodos para acceder y modificar atributos, se evita el acceso directo a los atributos desde fuera de la clase, lo que facilita la gestión y evita problemas potenciales.
Facilita el Cambio de Implementación:

Al encapsular los detalles internos de una clase, se puede cambiar la implementación interna sin afectar el código que utiliza la clase. Los métodos públicos sirven como una interfaz estable para el resto del programa.
Mejora la Legibilidad y Mantenimiento:

Al proporcionar una interfaz clara y métodos bien definidos, el encapsulamiento mejora la legibilidad del código y facilita el mantenimiento a medida que el programa evoluciona.

Tips: 

Patrones de Diseño que se Benefician del Encapsulamiento:

Patrón de Diseño Singleton:

El encapsulamiento ayuda a implementar de manera efectiva el patrón Singleton, que garantiza que una clase tenga una única instancia y proporciona un punto global de acceso a ella. Al encapsular la creación y acceso a la instancia dentro de la propia clase, se controla el acceso y se evita la creación múltiple de instancias.
Patrón de Diseño Factory Method:

El encapsulamiento se utiliza en el patrón Factory Method para definir una interfaz para crear un objeto, pero deja que las subclases alteren el tipo de objetos que se crearán. La interfaz definida por el Factory Method actúa como una cápsula que encapsula la lógica de creación.
Patrón de Diseño Observer:

En el patrón Observer, el encapsulamiento se utiliza para permitir que un objeto (el sujeto) notifique a otros objetos (los observadores) sobre cambios en su estado sin revelar la implementación interna. Los observadores se suscriben al sujeto a través de una interfaz, lo que encapsula la comunicación.
Algoritmos y Big O Notation:

El encapsulamiento, en sí mismo, no está directamente relacionado con algoritmos específicos ni con la notación Big O. Sin embargo, puede influir en la eficiencia y organización del código, lo que puede afectar el rendimiento en términos de complejidad temporal y espacial.

Algoritmos de Búsqueda y Ordenación:

El encapsulamiento puede facilitar la implementación y mantenimiento de algoritmos de búsqueda y ordenación al proporcionar una interfaz clara para interactuar con estructuras de datos encapsuladas.
Big O Notation:

El encapsulamiento en sí mismo no determina la eficiencia de un algoritmo en términos de la notación Big O. Sin embargo, la forma en que se implementan y utilizan los métodos y atributos puede influir en la complejidad temporal y espacial del código.
En general, el encapsulamiento es una buena práctica en la programación orientada a objetos que contribuye a la modularidad y la organización del código. Al seleccionar algoritmos, la elección de estructuras de datos y la implementación de patrones de diseño, se pueden considerar factores como la complejidad temporal y espacial para garantizar un rendimiento óptimo en diferentes situaciones. El encapsulamiento contribuye a la claridad y mantenimiento del código, lo que puede facilitar la optimización y mejora del rendimiento en el desarrollo y la evolución del software.
```

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # Atributo privado
        self.__edad = edad       # Atributo privado

    def get_nombre(self):       # Método público
        return self.__nombre

    def set_nombre(self, nuevo_nombre):  # Método público
        self.__nombre = nuevo_nombre

    def __metodo_privado(self):  # Método privado
        print("Este es un método privado")

# Crear una instancia de la clase Persona
persona = Persona("Juan", 25)

# Acceder a un atributo privado usando un método público
print(persona.get_nombre())  # Imprime: Juan

# Modificar un atributo privado usando un método público
persona.set_nombre("Ana")

# Llamando a un método privado desde dentro de la clase
persona._Persona__metodo_privado()  # Imprime: Este es un método privado

```

> Getters y Setters - POO

```
Getters y Setters en Programación Orientada a Objetos (POO):

Los getters y setters son métodos utilizados en la programación orientada a objetos para acceder y modificar los valores de atributos privados de una clase. Estos métodos permiten controlar el acceso a los atributos y aplicar lógica adicional, como validaciones o transformaciones, al obtener o establecer el valor de un atributo.

Beneficios y Complemento con Encapsulamiento:
Control de Acceso:

Getters y setters permiten un control más granular sobre el acceso a los atributos. Puedes aplicar lógica específica, como validaciones, antes de permitir que el valor sea obtenido o modificado.
Encapsulamiento Reforzado:

Al utilizar getters y setters, refuerzas el encapsulamiento al proporcionar métodos específicos para acceder y modificar atributos. Esto evita el acceso directo a los atributos desde fuera de la clase.
Validación y Lógica Adicional:

Los setters permiten implementar lógica adicional al establecer un nuevo valor. Puedes realizar validaciones, conversiones u otras operaciones antes de asignar el valor al atributo.
Compatibilidad con Interfaces Comunes:

Al utilizar getters y setters, puedes seguir convenciones comunes de interfaces en tu código, facilitando la interoperabilidad y entendimiento del código por parte de otros programadores.
```

```python
Getters:
Un getter es un método que proporciona acceso a un atributo privado desde fuera de la clase. Su función principal es obtener el valor actual de un atributo. En Python, un getter típicamente tiene un nombre que comienza con "get" y seguido del nombre del atributo que representa.

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

# Uso del getter
persona = Persona("Juan")
print(persona.get_nombre())  # Imprime: Juan


Setters:
Un setter es un método que permite modificar el valor de un atributo privado desde fuera de la clase. Su función principal es establecer un nuevo valor para un atributo. En Python, un setter típicamente tiene un nombre que comienza con "set" y seguido del nombre del atributo que representa.

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

# Uso del setter
persona = Persona("Juan")
persona.set_nombre("Ana")
print(persona.get_nombre())  # Imprime: Ana


```

> (@) Decorators - Decoradores / Métodos de clase (Methods of class)

```
En programación orientada a objetos (POO) y en el contexto de Python, los decoradores son una característica que permite modificar o extender el comportamiento de funciones o métodos de manera declarativa. Los decoradores proporcionan una forma concisa de aplicar funciones adicionales a otras funciones o métodos.

Sintaxis Básica de un Decorador:
En Python, los decoradores se implementan utilizando funciones. Un decorador es una función que toma otra función como argumento y devuelve una nueva función. La sintaxis básica para aplicar un decorador a una función es utilizar el símbolo @ seguido del nombre del decorador justo encima de la definición de la función.

Los decoradores no están limitados a funciones simples; también se pueden aplicar a métodos de clases. Esto puede ser útil en POO para extender el comportamiento de métodos específicos de una clase.

Beneficios de Decoradores en POO:
Reutilización de Código:

Los decoradores permiten encapsular funcionalidades adicionales y aplicarlas a múltiples funciones o métodos sin repetir código.
Extensibilidad:

Puedes extender el comportamiento de funciones o métodos de manera fácil y modular mediante la aplicación de decoradores.
Separación de Responsabilidades:

Los decoradores permiten separar preocupaciones y mantener un código más limpio y organizado al dividir las funcionalidades adicionales en funciones decoradoras.
Legibilidad del Código:

Los decoradores pueden mejorar la legibilidad del código al eliminar la necesidad de incrustar lógica adicional directamente en la implementación de funciones o métodos.
```

> @cached_propert

```
@cached_property se encarga de almacenar en caché el resultado después de la primera vez que se calcula.

Cuando se menciona que una propiedad es "costosa", se refiere a que calcular su valor puede requerir recursos computacionales significativos, como tiempo de CPU, acceso a bases de datos, llamadas a servicios web, operaciones de red u otras operaciones que consumen tiempo. En otras palabras, calcular el valor de la propiedad puede ser una operación que lleva tiempo o recursos.

En el contexto de la programación, a veces es necesario calcular valores que no cambian frecuentemente, pero que son costosos de calcular. En estos casos, la memoización es una técnica que consiste en almacenar en caché el resultado de un cálculo para evitar tener que recalcularlo cada vez que se accede a la propiedad.
```

```python
from functools import cached_property

class MiClase:
    @cached_property
    def calcular_resultado_costoso(self):
        # Lógica costosa
        return resultado
```

> SOLID 

```
"SOLID" es un acrónimo que representa un conjunto de cinco principios de diseño de software en el contexto de la programación orientada a objetos (POO). Estos principios fueron introducidos por Robert C. Martin y son considerados guías fundamentales para lograr un diseño de código limpio, modular y fácil de mantener. Cada letra en "SOLID" representa uno de estos principios:

Principio de Responsabilidad Única (Single Responsibility Principle - SRP):

Este principio establece que una clase debe tener una única razón para cambiar. En otras palabras, una clase debe tener una única responsabilidad o función dentro del sistema.
Principio de Abierto/Cerrado (Open/Closed Principle - OCP):

Este principio postula que una clase debe estar abierta para la extensión pero cerrada para la modificación. Significa que debes poder agregar nuevas funcionalidades sin cambiar el código existente.
Principio de Sustitución de Liskov (Liskov Substitution Principle - LSP):

Este principio establece que los objetos de una clase base deben poder ser reemplazados por objetos de una clase derivada sin afectar la integridad del programa.
Principio de Segregación de Interfaces (Interface Segregation Principle - ISP):

Este principio indica que una clase no debe verse obligada a implementar interfaces que no utiliza. En lugar de tener interfaces monolíticas, es preferible tener interfaces específicas para cada cliente.
Principio de Inversión de Dependencias (Dependency Inversion Principle - DIP):

Este principio establece que las clases de alto nivel no deben depender de clases de bajo nivel, sino de abstracciones. Además, las abstracciones no deben depender de detalles, sino de otras abstracciones.
En conjunto, estos principios SOLID proporcionan pautas para diseñar software que es modular, fácil de entender, extensible y resistente a cambios. Siguiendo estos principios, los desarrolladores pueden crear sistemas más robustos y mantenibles a medida que evolucionan y crecen con el tiempo.
```

#### Python Tests

> Pytest

[pytest](https://docs.pytest.org/en/7.1.x/getting-started.html)

[pip_pytest](https://pypi.org/project/pytest/)

> Install

```
pip install -U pytest
```

> Create your first test


```python
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

> Puedes Ejecutar "pytest" desde la raíz o pytest -vv (ver una versión más detallada): 

> pytest - @pytest.fixture

[pytest_fixture](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)

```
@pytest.fixture es un decorador (decorator)

@pytest.fixture es un decorador en el framework de pruebas pytest que se utiliza para definir fixtures. Las fixtures son funciones o métodos que se ejecutan antes de las pruebas y pueden realizar configuraciones iniciales, proporcionar datos de prueba o realizar cualquier tarea necesaria para preparar el entorno de prueba. También pueden realizar limpieza después de que se ejecuten las pruebas.

```

> Prueba que se marca como lenta (@pytest.mark.slow) y Prueba pendiente de implementación (@pytest.mark.skip)

```
Los marcadores (@pytest.mark) son una herramienta útil para organizar y filtrar pruebas según ciertos criterios. En el ejemplo que proporcionaste, se están utilizando dos marcadores específicos:

@pytest.mark.slow:
Este marcador indica que la prueba asociada (test_proceso_lento) es considerada lenta. Esto puede ser útil para clasificar y ejecutar pruebas de manera diferente en función de su velocidad. Puedes ejecutar solo las pruebas lentas, ignorarlas, o ajustar la ejecución en función de la velocidad.

@pytest.mark.skip:
Este marcador indica que la prueba asociada (test_pendiente) está pendiente de implementación. La prueba se omite durante la ejecución, y el motivo de la omisión se proporciona en la razón. Esto es útil cuando tienes pruebas que aún no están completamente implementadas y deseas que se ignoren en ciertos contextos.
```

```python

@pytest.mark.slow
def test_proceso_lento():
    """Prueba que se marca como lenta."""
    assert True

@pytest.mark.skip(reason="Prueba pendiente de implementación")
def test_pendiente():
    """Esta prueba se marca como pendiente."""
    assert False


```

> Ejecutar solo las pruebas lentas:

```python
pytest -k slow
```

> Ejecutar todas las pruebas excepto las lentas:

```python
pytest -k "not slow"
```

> Ejecutar solo las pruebas pendientes:

```python
pytest -k skip
```

> Ejecutar todas las pruebas excepto las pendientes:

```python
pytest -k "not skip"
```

> Tips: 

```
Úsalo con Moderación:
No sobrecargues tus pruebas con demasiados marcadores. Utilízalos de manera efectiva y específica para su propósito. Un uso excesivo puede complicar la ejecución y comprensión de tus pruebas.

Integración con Herramientas de CI/CD:
Puedes aprovechar los marcadores al integrar pytest en tu flujo de trabajo de CI/CD para personalizar la ejecución de pruebas en función de los marcadores.
```

> En pytest, las funciones @pytest.mark y @pytest.mark.parametrize son herramientas poderosas para organizar y parametrizar pruebas.

> @pytest.mark.parametrize
Este decorador se utiliza para parametrizar las pruebas. Permite ejecutar la misma prueba con diferentes conjuntos de datos de entrada y verificar los resultados. Esto es útil para reducir la duplicación de código al escribir pruebas con escenarios similares.

```python
import pytest

def suma(a, b):
    return a + b

@pytest.mark.parametrize("entrada, esperado", [(1, 2, 3), (2, 3, 5), (5, 5, 10)])
def test_suma(entrada, esperado):
    assert suma(entrada[0], entrada[1]) == esperado

```

> El "mocking" es una técnica que se utiliza en pruebas unitarias para simular el comportamiento de objetos o módulos reales

```
El "mocking" es una técnica que se utiliza en pruebas unitarias para simular el comportamiento de objetos o módulos reales. En Python, puedes implementar el "mocking" utilizando la biblioteca unittest.mock que proporciona el módulo unittest.mock en Python 3.3 y versiones posteriores. En pytest, puedes utilizar el "mocking" de unittest.mock para crear objetos simulados (mocks) y controlar su comportamiento durante las pruebas.
```

> Ejemplo: "mocking"

```python
# calculadora.py
class Calculadora:
    def suma(self, a, b):
        return a + b

def funcion_a_testear(calculadora, x, y):
    resultado = calculadora.suma(x, y)
    return resultado

```

```python
import pytest
from unittest.mock import Mock
from proyecto.calculadora import Calculadora, funcion_a_testear

def test_funcion_a_testear():
    # Crear un objeto mock para la clase Calculadora
    mock_calculadora = Mock(spec=Calculadora)
    
    # Configurar el comportamiento simulado (en este caso, la suma devuelve 5)
    mock_calculadora.suma.return_value = 5
    
    # Llamar a la función que utiliza la calculadora
    resultado = funcion_a_testear(mock_calculadora, 2, 3)
    
    # Verificar que la función devuelva el resultado esperado
    assert resultado == 5
    
    # Verificar que la función suma de la calculadora fue llamada correctamente
    mock_calculadora.suma.assert_called_once_with(2, 3)

```

```
Cuándo Usar "Mocking":
Aislamiento de Dependencias:
Utiliza "mocking" para aislar la unidad que estás probando de las dependencias externas, como servicios web, bases de datos u otros módulos.

Simulación de Comportamientos Específicos:
Puedes utilizar mocks para simular comportamientos específicos de objetos o funciones, lo que facilita la creación de escenarios de prueba controlados.

Mejora de la Eficiencia en las Pruebas:
Al utilizar mocks, puedes evitar la ejecución de código real que no es relevante para la prueba en cuestión, mejorando así la eficiencia de tus pruebas unitarias.
```

> FastAPI : Test Client - TestClient

[TestClient](https://fastapi.tiangolo.com/reference/testclient/?h=test)

```
TestClient es una clase proporcionada por FastAPI para realizar pruebas de integración en tus aplicaciones web construidas con FastAPI. Te permite simular solicitudes HTTP y recibir respuestas de tu aplicación sin necesidad de ejecutar un servidor real. Esto es útil para automatizar pruebas y asegurarte de que tu aplicación se comporte como se espera.

¿Cuándo usar TestClient?
Pruebas de Integración: Se utiliza para realizar pruebas de extremo a extremo en tu aplicación, asegurándote de que todas las partes se integren correctamente.

Pruebas de Rutas y Lógica de Negocio: Es útil para probar rutas y la lógica de negocio de tu aplicación sin necesidad de un servidor real.

```

> Creación de una instancia:
Creas una instancia de TestClient pasándole tu aplicación FastAPI. Por ejemplo:

```python
from fastapi.testclient import TestClient
from main import app  # Reemplaza "main" con el nombre real de tu módulo principal

client = TestClient(app)

```

> Realización de solicitudes HTTP:
Utilizas los métodos de la instancia de TestClient (get, post, put, delete, etc.) para realizar solicitudes HTTP a rutas específicas de tu aplicación.

```python
response = client.get("/example")

```

> Verificación de respuestas:
Verificas la respuesta recibida utilizando aserciones en el objeto response. Puedes verificar el código de estado, el contenido del cuerpo, encabezados y más.

```python
assert response.status_code == 200
assert response.json() == {"key": "value"}
```

> Tip: 

```
Diferencias con pytest y unittest:
TestClient vs pytest y unittest:

TestClient se centra en realizar solicitudes HTTP a tu aplicación FastAPI y verificar las respuestas. Está diseñado específicamente para pruebas de integración en aplicaciones web construidas con FastAPI.
pytest y unittest son marcos de prueba más generales que admiten diferentes tipos de pruebas, no están específicamente diseñados para pruebas de aplicaciones web.
Interacción entre TestClient, pytest y unittest:

TestClient se utiliza comúnmente junto con pytest para realizar pruebas de integración en el ecosistema FastAPI. Puedes integrar pruebas de TestClient en tus archivos de prueba pytest.
unittest es otro marco de prueba que tiene su propia sintaxis y estructura. No es tan común usar TestClient directamente con unittest en el contexto de FastAPI.
Elección entre pytest y unittest:
pytest:

Es un marco de prueba popular y flexible con características avanzadas.
Permite parametrizar pruebas, proporciona un sistema de plugins extensible y ofrece una sintaxis clara y concisa.
Es ampliamente adoptado en la comunidad de Python.
unittest:

Forma parte de la biblioteca estándar de Python y sigue la convención de pruebas unitarias.
Ofrece una estructura más formal y orientada a objetos para organizar las pruebas.
A veces se elige si se trabaja en un entorno que prefiere herramientas de la biblioteca estándar.
La elección entre pytest y unittest generalmente se basa en preferencias personales y en la complejidad de las pruebas que estás realizando. Ambos son efectivos, pero pytest es más popular y ofrece más funcionalidades avanzadas. En el contexto de FastAPI, la combinación de TestClient y pytest es una opción común y efectiva para realizar pruebas de integración.
```

#### Backend & Frontend 

> Tip: Para conectar tu backend (API desarrollada con FastAPI) a tu frontend, puedes seguir estos pasos generales:

```
Despliega tu backend: Antes de poder conectar tu frontend, asegúrate de que tu backend esté desplegado y accesible en algún lugar. Puedes usar servicios en la nube como Heroku, AWS, Google Cloud, o cualquier otro proveedor que prefieras. Alternativamente, puedes ejecutar tu backend localmente mientras pruebas tu frontend.

Crea tu frontend: Desarrolla tu frontend utilizando la tecnología que prefieras, como React.js, Angular, Vue.js, o cualquier otro framework o biblioteca que elijas. Por ejemplo, si decides usar React.js, puedes configurar un nuevo proyecto usando Create React App.

Configura tu frontend para consumir la API: En tu frontend, configura las solicitudes HTTP para consumir los endpoints de tu API. Puedes usar la función fetch de JavaScript o bibliotecas como Axios para realizar solicitudes HTTP a tu backend. Por ejemplo, para obtener datos de un endpoint en tu API:
```

```javascript
fetch('https://tu-api.com/travels/duration?duration=5')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Haz algo con los datos recibidos
  })
  .catch(error => console.error('Error:', error));

```

```
Protege las credenciales del usuario (si es necesario): Si tu aplicación requiere autenticación de usuario, asegúrate de manejar correctamente las credenciales del usuario. Puedes usar tokens de acceso JWT y enviarlos en el encabezado de autorización de tus solicitudes HTTP.

Prueba la integración: Una vez que hayas configurado tu frontend para consumir la API, asegúrate de probar la integración para asegurarte de que todo funcione correctamente. Verifica que tu frontend pueda enviar solicitudes a tu backend y manejar las respuestas correctamente.

Maneja los errores y casos límite: Asegúrate de manejar correctamente los errores y casos límite en tu frontend. Esto puede incluir errores de red, respuestas de error del servidor, datos faltantes o incorrectos, entre otros.

Optimiza el rendimiento (si es necesario): Si experimentas problemas de rendimiento, considera optimizar tu frontend y backend para mejorar la velocidad de carga y la capacidad de respuesta de tu aplicación. Esto puede incluir técnicas como la optimización de imágenes, la reducción del tamaño de los archivos estáticos, el almacenamiento en caché de datos, entre otros.
```

> Interfaz Gráfica (GUI)

> PyQt5

[pyqt](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

[pip_pyqt5](https://pypi.org/project/PyQt5/)

[qt_python](https://doc.qt.io/)

```
# Para Windows:
pip install PyQt5

#Ubuntu:
sudo apt-get install python3-pyqt5
```

> Tip:

```
Convertir el archivo .ui a código Python: Utiliza la herramienta pyuic para convertir el archivo .ui en un archivo Python que contenga el código correspondiente a la interfaz gráfic
```

```bash
pyuic5 tu_interfaz.ui -o tu_interfaz.py
```

```
Si pyuic5 no se encuentra en tu sistema después de instalar python3-pyqt5, es posible que el paquete pyqt5-tools no esté instalado. Este paquete proporciona utilidades, incluido pyuic5, para trabajar con PyQt5.
```

```bash
sudo apt-get install pyqt5-dev-tools
```

```
Puedes intentar ubicar la ubicación del comando pyuic5 en tu sistema utilizando el comando whereis o which. 
```

```bash
whereis pyuic5

which pyuic5
```

```bash
#PyQT UI Design (XML)
sudo apt-get install qttools5-dev-tools
```

> Tkinter (Interface Python - GUI)

```bash
pip install requests tkinter
```

[tkinter_python](https://docs.python.org/es/3/library/tkinter.html#module-tkinter)

```
Para verificar si tkinter está disponible en tu sistema, puedes abrir un intérprete de Python e intentar importarlo:
```

```bash
python3 -c "import tkinter"
```

#### Types Collections (Tipos de Colecciones) / Structure Data (Estructura de Datos)

> Collección: Grafos, Jerárquicas, Lineales, Desordenadas. 

> Tip (Recomendado por un Estudiante en Platzi): 

```
Es muy importante saber cuando usar una cierta colección, ya que de ello depende tanto el tamaño que ocupará en memoría como la velocidad en ciertas tareas. De forma general es recomendable usar tuplas en lugar de listas siempre que no se requiera estar cambiando los valores, ya que ocupan menos espacio en memoría. Así como usar sets o diccionarios para busqueda de un elemento, ya que son más rapidos.
```

```python
import sys

colecciones = {"list": list(), "tuple": tuple(), "dict": dict(), "set": set()}

for name, value in colecciones.items():
    print(f'{name} = {sys.getsizeof(value)} bytes')
```

> Recordar: 

```
En Python, una tupla es una colección ordenada e inmutable de elementos. Se diferencia de una lista en que una vez creada, no se pueden modificar, agregar ni eliminar elementos individualmente. Sin embargo, al igual que las listas, las tuplas pueden contener elementos de diferentes tipos de datos, como enteros, cadenas, flotantes, otras tuplas, etc.
```

```python
mi_tupla = (1, 2, 3, "cuatro", 5.5)
```

```
En Python, un conjunto (set) es una colección desordenada y mutable de elementos únicos. Esto significa que un conjunto no permite elementos duplicados y se puede modificar agregando o eliminando elementos, pero no permite acceder a los elementos por índice, ya que no tienen un orden definido.

Los conjuntos se crean utilizando llaves {} o la función set(), y los elementos se separan por comas ,. Aquí tienes un ejemplo de cómo crear un conjunto:

```

```python
mi_set = {1, 2, 3, 4, 5}
```

```
En Python, dict es una estructura de datos que representa un diccionario, es decir, una colección de pares clave-valor, donde cada clave está asociada a un valor. Los diccionarios son mutables, lo que significa que puedes modificar, agregar o eliminar elementos una vez que han sido creados. Sin embargo, las claves en un diccionario deben ser únicas e inmutables, mientras que los valores pueden ser de cualquier tipo de datos y pueden ser mutables.

Los diccionarios se crean utilizando llaves {} y los pares clave-valor se separan por dos puntos :. Aquí tienes un ejemplo de cómo crear un diccionario:

```

```python
mi_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

```
En Python, una lista (list) es una estructura de datos que permite almacenar una colección ordenada de elementos. Las listas son mutables, lo que significa que puedes modificar, agregar o eliminar elementos después de que la lista haya sido creada. Además, las listas pueden contener elementos de diferentes tipos de datos, como números, cadenas, booleanos, otras listas, tuplas, diccionarios, etc.

Las listas se crean utilizando corchetes [] y los elementos se separan por comas ,. Aquí tienes un ejemplo de cómo crear una lista:

```

```python
mi_lista = [1, 2, 3, "cuatro", 5.5]
```

> Estructura de Datos: Nodos y Linked List

```
- Nodo: Punto de Intersección. 

- Linked list" (lista enlazada) es una estructura de datos lineal que consiste en una secuencia de elementos llamados nodos.O(n) Lineal

- Las listas enlazadas son una estructura de datos que almacena datos en forma de cadena. La estructura de una lista enlazada es tal que cada dato tiene una conexión con el siguiente (y a veces también con los datos anteriores). Cada elemento de una lista enlazada se denomina nodo.
```

```
En una lista enlazada, algunos de los métodos más comunes que se pueden agregar son:

append(data): Agrega un nuevo nodo con el dato data al final de la lista.
prepend(data): Agrega un nuevo nodo con el dato data al inicio de la lista.
insert_after(node, data): Inserta un nuevo nodo con el dato data después del nodo node.
delete(data): Elimina el primer nodo que contiene el dato data de la lista.
delete_at_position(position): Elimina el nodo en la posición position de la lista.
get_position(data): Devuelve la posición del primer nodo que contiene el dato data en la lista.
get_size(): Devuelve el número de nodos en la lista.
print_list(): Imprime los datos de todos los nodos en la lista.
reverse(): Invierte el orden de los nodos en la lista.
```

[Linked_list (Listas Enlazadas)](https://www.freecodecamp.org/news/introduction-to-linked-lists-in-python/)
