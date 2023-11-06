# Python

> Basic Python

> Course of Python basic. Exercise and practice with Python. 

## Python con Platzi

> Root Complete Python in I.A

> platzi.com

[Platzi](https://platzi.com/)

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

> POO en Python con accesos y no accesos:

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

> Aplicar modificadores de acceso en Python:

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