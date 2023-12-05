###########
#* 1)
#?: "**": Son los operadores de expansión de diccionario. Estos operadores permiten pasar todos los valores de un diccionario a un objeto de Pydantic.
#?: Union es una herramienta en el módulo typing de Python que permite indicar que una variable, parámetro o atributo puede tener uno de varios tipos posibles. 
#?: Optional es otra construcción útil del módulo typing en Python y se utiliza para indicar que una variable o parámetro puede ser de un tipo específico o None.  es útil para expresar la posibilidad de que una variable pueda tener un valor o no, y ayuda a mejorar la claridad en la lectura del código y en el sistema de tipado estático.
#? Annotated se utiliza para agregar anotaciones adicionales a un tipo de variable.  Una o más anotaciones adicionales que se pueden utilizar para proporcionar información adicional sobre la variable.
###########
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
import os 
import pandas as pd
from pydantic import BaseModel
from typing import List, Union, Optional

# === Instance App API ===
app = FastAPI()
app.title = "My API with FastAPI"
app.version = "0.0.1"


# === Data Frame Data ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data_movies", "disney_movies.csv")
df = pd.read_csv(file_path)

# === POO ===
# Instancia de Objeto
class Movies(BaseModel): 
  id: Optional[int] = None
  title: Union[str, None] = None
  overview: str
  year: int
  rating: Union[float, int, None] = None
  category: str

# === Movies DataAPI & Pattern Singleton & Herencia => Polimorfirmo === 
class MovieSingleton: 
  _instance = None
  movies_api = [
  {
    "id": 1, 
    "title": "Avatar", 
    "overview": "vatar es una franquicia de medios estadounidense creada por James Cameron, que consiste en una serie planificada de películas épicas de ciencia ficción producidas por Lightstorm Entertainment y distribuidas por 20th Century Studios, así como productos relacionados, videojuegos y atracciones de parques temáticos", 
    "year": 2009,
    "rating": 7.8, 
    "category": "Acción" 
  }, 
  {
    "id": 2, 
    "title": "Avatar: The Way of Water", 
    "overview": "ake Sully y Ney'tiri han formado una familia y hacen todo lo posible por permanecer juntos. Sin embargo, deben abandonar su hogar y explorar las regiones de Pandora cuando una antigua amenaza reaparece.", 
    "year": 2022,
    "rating": 7.5, 
    "category": "Acción" 
  }
]
  
def __new__(cls): 
  '''
  __new__ es un método especial en Python que se utiliza para crear una nueva instancia de una clase.
  '''
  if not cls._instance:
    #cls._instance = super().__new__(cls) # Herencia Polimorfismo
    cls._instance.movies_objects = [Movies.parse_obj(movie) for movie in cls.movies_api] # Json => Parsear a Obj / dict
    return cls._instance  
  

def get_movies_object(self):
  return self.movies_objects
  
#===#
movie_singleton = MovieSingleton()

# Parsear la lista movies_api en una lista de objetos Movies
#movies_objects = [Movies.parse_obj(movie) for movie in movies_api] #List[Movies] = []
# Ahora, movies_objects es una lista de objetos de la clase Movies
""" for movie_obj in movies_objects:
  print(movie_obj.dict()) """
# === API CRUD ===
# ===GET
@app.get("/", status_code=status.HTTP_200_OK)
async def message(): 
  return {"message": str("Hello World, Movies")}


@app.get("/home", tags=["home"])
async def read_home(): 
  html_content = """
    <html>
        <head>
            <title>API Movies and FastAPI and Web Server Uvicorn</title>
        </head>
        <body>
            <h1>Hello World Movie API</h1>
        </body>
    </html>
    """
  return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)


@app.get("/movies", status_code=status.HTTP_200_OK, tags=["movies"])
async def get_movies():
  return {"movies": df.head(5).to_dict(orient="records")}

#===#
@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_all_movie(): 
  return movie_singleton.get_movies_object()

#==== Path Parameters:
@app.get("/movie/{id}", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_movie(id: int):
  '''
  movie_id = filter(lambda movie: movie.id == id, movies_api)
  Web Server (Endpoints): http://127.0.0.1:8000/movie/1
  '''
  movie_id = next((m for m in movie_singleton.get_movies_object() if m["id"] == id), None)
  try: 
    if movie_id: 
      return movie_id
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry! Your movie {id} not exist.")
  except Exception as e: 
     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Sorry, We have a Server Error {str(e)}")
  

@app.get("/movie/year/{year}", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_year(year: int):
  year_movie = next((y for y in movie_singleton.get_movies_object() if y["year"] == year), None)
  try: 
    if year_movie:
      return year_movie
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry, your movie it's not this year{year}.")
  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Server Error {str(e)}")
  

#==== Query Parameters:
@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def query_movie(id: int, title: str, category: str):
  '''
  WebServer (Endpoints): http://127.0.0.1:8000/movie/?id=1&title=Avatar or movie/?id=1&title=Avatar&category=Acci%C3%B3n (Acción)
  titles => O(n) Algorithm Lineal 
  ''' 
  titles = next((t for t in movie_singleton.get_movies_object() if t["id"] == id and t["title"] == title and t["category"] == category), None)
  try: 
    if titles: 
      return titles
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry! your movie tittle {title} it's not searching")
  except Exception as e:
    raise HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Server Error..., {str(e)}")
  

@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_movies_category(category: str): 
  return {item for item in movie_singleton.get_movies_object() if item["category"] == category}


#===POST
# = BaseModel = 
""" @app.post("/movie/", tags=["movie"])
async def create_movies(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()): 
  movie.append({
  "id": id, 
  "title": title, 
  "overview": overview, 
  "year": year,
  "rating": rating, 
  "category": category
  })
  return movie """

""" @app.post('/movie/', status_code=status.HTTP_200_OK, tags=['movie'])
async def create_movie(request: Request):
    '''
    movies_api.append(movie_data) para agregar la nueva película al final de la lista movies_api. Ahora, la nueva película se agrega correctamente a la lista existente.
    '''
    movie_data = await request.json()

     # = Validación de datos (puedes agregar más validaciones según tus necesidades) =
    required_fields = ["id", "title", "overview", "year", "rating", "category"]
    if not all(item in movie_data for item in required_fields):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing required fields in movie data") 

     # = Agregar la nueva película a la lista movies_api =
    movies_api.append(movie_data)

    return movie_data
 """

# === Esquema e Usar Mi instancia (Class) ===
@app.post("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def created_movies(movies: Movies): 
  movie_dict = movies.dict()
  movie_dict["id"] = max((m["id"] for m in movie_singleton.get_movies_object()), default=0) + 1
  movies_api.append(movie_dict)
  return movie_dict

#===PUT
#Function getMovieIndex
""" def get_movie_index(movie_id):
   '''
   Se ha agregado la función get_movie_index para buscar el índice de una película en la lista según su ID.
   Sí, enumerate es una función incorporada en Python que se utiliza para agregar un contador a un iterable y devolverlo como un objeto enumerado. Este objeto enumerado contiene pares de índices y elementos del iterable.
   La función enumerate toma un iterable como argumento y devuelve un objeto enumerado
   '''
   for i, movie in enumerate(movies_api): 
     if movie["id"] == movie_id:
       return i
   return None """

# = El método PUT generalmente se utiliza para actualizar un recurso existente / Usando JSON =
""" @app.put("/movie/{movie_id}", status_code=status.HTTP_200_OK, tags=["movie"])
async def update_movie(movie_id: int, request: Request):
    '''
    Actualiza una película existente en la lista movies_api.
    La función replace_movie utiliza await request.json() para obtener los nuevos datos de la película del cuerpo de la solicitud.
    '''
    movie_data = await request.json()
    
    # = Buscar el índice de la película en la lista = 
    movie_index = get_movie_index(movie_id)

    if movie_index is not None:
      # = Actualizar los campos de la película con los nuevos datos =
      movies_api[movie_index].update(movie_data)
    else: 
      raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id} Not Exist.") """
    

#=== PUT => Usando POO (Instancia) / Esquema ===
@app.put("/movie/{movie_id}", status_code=status.HTTP_200_OK, tags=["movie"])
async def update_movie(movie_id: int, update_movies: Movies): 
  for i, movie in enumerate(movie_singleton.get_movies_object()): 
    if movie["id"] == movie_id: 
        movie_singleton.get_movies_object()[i] = update_movies.dict()
        return movie_singleton.get_movies_object()[i]
    
  raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id} Not Exist.")


#===DELETE
""" @app.delete("/movie/{movie_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["movie"])
async def delete_movie(movie_id: int): 
  '''
   a) Elimina (delete) una película de la lista movies_api.
   b) Si la película se encuentra, se utiliza movies_api.pop(movie_index) para eliminar la película de la lista. o usar: remove.
   c) Se devuelve una respuesta con un código de estado 204 (No Content), que indica que la operación de eliminación fue exitosa y no hay contenido para devolver.
  '''
  
  #data_movie = await request.json()

  index_movie = get_movie_index(movie_id)

  if index_movie is not None: 
    delete_movie = movies_api.pop(index_movie)
    return None
  else: 
    raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with this ID {movie_id} not found.") """


#=== DELETE => Usando POO (Instancia) / Esquema ===
@app.delete("/movie/{movie_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["movie"])
async def delete_movie(movie_id: int): 
  for i, movie in enumerate(movie_singleton.get_movies_object()):
    if movie["id"] == movie_id:
        del movie_singleton.get_movies_object()[i]
        return None
  
  raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with this ID {movie_id} not found.")
