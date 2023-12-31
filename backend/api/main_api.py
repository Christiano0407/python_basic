###########
#* 1)
###########
from fastapi import APIRouter, FastAPI, HTTPException, Request, status, Path, Query, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Union,Optional
from typing_extensions import Annotated
from jose import JWTError, jwt
from jwt_manager import AuthMiddleware, User, get_current_user
import pandas as pd
import os 
import json
import time
#from starlette.middleware import Middleware
#from starlette.applications import Starlette
""" import dotenv """
""" import jwt
import time """

# === Middleware === 
""" middleware = [
  Middleware(AuthMiddleware)
]
 """

# === Instance App API ===
app = FastAPI()
app.title = "My API with FastAPI"
app.version = "0.0.1"

#app = Starlette(Middleware=middleware)
# === Router ===
router = APIRouter()
# ==== OAuth2 ==== 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# === Data Frame Data (Disney) ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data_movies", "disney_movies.csv")
df = pd.read_csv(file_path)

# = My Data JSON =
movies_dir = os.path.dirname(__file__)
movies_api = os.path.join(movies_dir, "movieData", "movie.json")
with open(movies_api, "r") as f:
  movie_data = json.load(f)

# === Token Secrete Key ===
def get_secret_key(): 
  return os.environ.get("SECRET_KEY")

# === POO ===
# Instancia de Objeto
class Movies(BaseModel): 
  id: Union[int, None] = Field(..., gt=0) #Valor Requerido y Mayor a "0".
  title: Union[str, None] = Field(description="Titles of movies", max_length=150)
  overview: Union[str, None] = Field(default=None, title="Overview of Movies", description="The Overview of movies", max_length=600)
  year: int = Field(gt=0, description="The year of movie in Cinemas")
  rating: Union[float, int, None] = Field(ge=1, le=10)
  category: str = Field(min_length=1, max_length=15)

# === Movies DataAPI & Pattern Singleton & Herencia => Polimorfirmo === 
class MovieSingleton: 
  _instance = None

  def __new__(cls): 
    if not cls._instance:
      cls._instance = super().__new__(cls) # Herencia Polimorfismo
      cls._instance.movie_data = movie_data
      cls._instance.movies_objects = [Movies.parse_obj(movie) for movie in cls._instance.movie_data] # Json => Parsear a Obj / dict
      return cls._instance  
  

  def get_movies_object(self):
    return self.movies_objects

  
#=== Movie Singleton === #
movie_singleton = MovieSingleton()

# Parsear la lista movies_api en una lista de objetos Movies
#movies_objects = [Movies.parse_obj(movie) for movie in movies_api] #List[Movies] = []
# Ahora, movies_objects es una lista de objetos de la clase Movies
""" for movie_obj in movies_objects:
  print(movie_obj.dict()) """
#=== GET Token === 
""" @app.get("/user/me", tags=["auth"])
async def read_user_me(
  current_user: Annotated[User, Depends(get_current_user)],
):
  if not current_user: 
  # Manejar el error de autenticación
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Expired Authentication Token.",
      )
  # Accede a los datos del usuario después de la autorización
  return get_current_user """

@app.get("/user/me", tags=["auth"])
async def read_user_me(current_user: User = Depends(get_current_user)):
  # Accede a los datos del usuario autenticado
  return current_user

# === API CRUD ===
# ===GET
@app.get("/", status_code=status.HTTP_200_OK)
async def message(): 
  return {"message": str("Hello World, Movies")}


@app.get("/movies", status_code=status.HTTP_200_OK, tags=["movies"])
async def get_movies():
  return {"movies": df.head(5).to_dict(orient="records")}

#===#
@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_all_movie(): 
  '''
  he utilizado la función dict() de Pydantic para convertir cada objeto Movies a un diccionario antes de devolver la respuesta JSON.
  '''
  return movie_singleton.get_movies_object()
  """ #movies_objects = movie_singleton.get_movies_object()
  # Convertir los objetos Movies a diccionarios antes de serializar
  #json_response_movie = [movie.dict() for movie in movies_objects]
  #return JSONResponse(content=json_response_movie) """

#==== Path Parameters:
@app.get("/movie/{id}", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_movie(id: Annotated[int, Path(..., title="Movie ID", description="The ID of the Movie", ge=0)] ):
  '''
  movie_id = filter(lambda movie: movie.id == id, movies_api)
  Web Server (Endpoints): http://127.0.0.1:8000/movie/1
  Reemplacé m["id"] con m.id para acceder al atributo id de la instancia de la clase Movies.
  JSONResponse => este último enfoque es innecesario en este caso específico, ya que FastAPI maneja la serialización a JSON automáticamente.
  '''
  movie_id = next((m for m in movie_singleton.get_movies_object() if m.id == id), None)
  #print(type(movie_id)) # Agrega esta línea para imprimir el tipo. => <class 'main_api.Movies'>
  try: 
    if movie_id: 
      return movie_id #JSONResponse(content=movie_id)
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry! Your movie {id} not exist.")
  except Exception as e: 
     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Sorry, We have a Server Error {str(e)}")
  

@app.get("/movie/year/{year}", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_year(year: int = Path(ge=1985, le=2010)):
  year_movie = next((y for y in movie_singleton.get_movies_object() if y.year == year), None)
  try: 
    if year_movie:
      return year_movie
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry, your movie it's not this year{year}.")
  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Server Error {str(e)}")
  

#==== Query Parameters:
@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def query_movie(id: int = Query(title="Movie ID", ge=0), title: str = Query(title="Movie Title"), category: str = Query(title="Category Title")):
  '''
  WebServer (Endpoints): http://127.0.0.1:8000/movie/?id=1&title=Avatar or movie/?id=1&title=Avatar&category=Acci%C3%B3n (Acción)
  titles => O(n) Algorithm Lineal 
  ''' 
  titles = next((t for t in movie_singleton.get_movies_object() if t.id == id and t.title == title and t.category == category), None)
  try: 
    if titles: 
      return titles
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry! your movie tittle {title} it's not searching")
  except Exception as e:
    raise HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Server Error..., {str(e)}")


def movie_filtered(movies, category = None):
    if category is None or category not in movies:
       return [] 
    filtered_movies = [movie for movie in movies if movie.category == category]
    return filtered_movies


@app.get("/movie/", status_code=status.HTTP_200_OK, tags=["movie"])
async def get_movies_category(category: str = Query(None, title="Category Movie")): 
  try: 
    filtered_movies = movie_filtered(movie_singleton.get_movies_object(), category=category) 
    if filtered_movies:
      return JSONResponse(content=filtered_movies)
    else: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sorry, your movie category not found")
  except Exception as e: 
    raise HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Server Error..., {str(e)}")


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
  try: 
    # Obtener el máximo ID existente y asignar uno nuevo
    new_id = max((m.id for m in movie_singleton.get_movies_object()), default=0) + 1
    # Asignar el nuevo ID al objeto Movies
    movies.id = new_id
    # Convertir el objeto Movies a un diccionario
    #movie_dict = movies.dict()
    # Agregar el nuevo diccionario a la lista de movies_object
    movie_singleton.get_movies_object().append(movies)
    #movies_pattern = movie_singleton.get_movies_object()
    #movies_pattern.append(movie_dict)
    return movies.dict()

  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating movie: {str(e)}")
  
# ==== Token User & oAuth ====

@app.post("/login", tags=["auth"])
async def login(user: User): 
  '''
  # Aquí deberías realizar la autenticación del usuario, verificar las credenciales, etc.
  # Si las credenciales son válidas, puedes generar un token y devolverlo
  # Devuelve el token en la respuesta
  '''
  try: 
      token = generate_token(user.username, user.email)

      return {"access_token": token, "token_type": "bearer"}
  except Exception as e:
    raise HTTPException( status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


def generate_token(username: str, email:Optional[str]):
   # Define la clave secreta para firmar el token
   secret_key = get_secret_key()
   # Define las reclamaciones del token (puedes personalizar esto según tus necesidades)
   claims = {"sub": username, "email": email, "exp": time.time() + 3600}  # Expire en 1 hora
   #Generate Toke
   token = jwt.encode(claims, secret_key, algorithm="HS256")

   return token

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
    

#=== PUT => Usando POO (Instancia) / Esquema === & POO 
""" @app.put("/movie/{movie_id}", status_code=status.HTTP_200_OK, tags=["movie"])
async def update_movie(movie_id: int, update_movies: Movies): 
  for i, movie in enumerate(movie_singleton.get_movies_object()): 
    if movie["id"] == movie_id: 
        movie_singleton.get_movies_object()[i] = update_movies.dict()
        return movie_singleton.get_movies_object()[i]
    
  raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id} Not Exist.") """


@app.put("/movie/{movie_id}", status_code=status.HTTP_200_OK, tags=["movie"])
async def update_movie(movie_id: int, update_movies: Movies): 
  try: 
    index = next((i for i, movie in enumerate(movie_singleton.get_movies_object()) if movie.id == movie_id), None)
    if index is not None: 
      # Actualizar el elemento en la lista con los datos de update_movies
      movie_singleton.get_movies_object()[index] = update_movies
      # Devolver el elemento actualizado
      return movie_singleton.get_movies_object()[index]
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id} does not exist.")
  # Lanzar una excepción en caso de un error interno del servidor
  except Exception as e: 
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating movie: {str(e)}")


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
    if movie.id == movie_id:
        del movie_singleton.get_movies_object()[i]
        return None
  
  raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with this ID {movie_id} not found.")
