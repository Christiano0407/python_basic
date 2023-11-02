# python_basic
Course of Python basic. Exercise and practice with Python. 

## Python con Platzi
> Root Complete Python in I.A
> platzi.com

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