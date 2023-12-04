###########
#* 1)
###########
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
import os 
import pandas as pd
# === Instance App API ===
app = FastAPI()
app.title = "My API with FastAPI"
app.version = "0.0.1"

# === Data Frame Data ===
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data_movies", "disney_movies.csv")
df = pd.read_csv(file_path)
#Movies DataAPI
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

# === API CRUD ===
# ===GET
@app.get("/", status_code=200)
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
  return HTMLResponse(content=html_content, status_code=200)


@app.get("/movies", status_code=200, tags=["movies"])
async def get_movies():
  return {"movies": df.head(5).to_dict(orient="records")}

#Path Parameters:
@app.get("/movie/{id}", status_code=200, tags=["movie"])
async def get_movie(id: int):
  '''
  movie_id = filter(lambda movie: movie.id == id, movies_api)
  Web Server (Endpoints): http://127.0.0.1:8000/movie/1
  '''
  movie_id = next((m for m in movies_api if m["id"] == id), None)
  try: 
    if movie_id: 
      return movie_id
    else: 
      raise HTTPException(status_code=404, detail=f"Sorry! Your movie {id} not exist.")
  except Exception as e: 
     raise HTTPException(status_code=500, detail=f"Sorry, We have a Server Error {str(e)}")
  

@app.get("/movie/year/{year}", status_code=200, tags=["movie"])
async def get_year(year: int):
  year_movie = next((y for y in movies_api if y["year"] == year), None)
  try: 
    if year_movie:
      return year_movie
    else: 
      raise HTTPException(status_code=404, detail=f"Sorry, your movie it's not this year{year}.")
  except Exception as e: 
    raise HTTPException(status_code=500, detail=f"Server Error {str(e)}")
  

#Query Parameters:
@app.get("/movie/", status_code=200, tags=["movie"])
async def query_movie(id: int, title: str, category: str):
  '''
  WebServer (Endpoints): http://127.0.0.1:8000/movie/?id=1&title=Avatar or movie/?id=1&title=Avatar&category=Acci%C3%B3n (Acción)
  titles => O(n) Algorithm Lineal 
  ''' 
  titles = next((t for t in movies_api if t["id"] == id and t["title"] == title and t["category"] == category), None)
  try: 
    if titles: 
      return titles
    else: 
      raise HTTPException(status_code=404, detail=f"Sorry! your movie tittle {title} it's not searching")
  except Exception as e:
    raise HTMLResponse(status_code=500, detail=f"Server Error..., {str(e)}")
  

@app.get("/movie/", status_code=200, tags=["movie"])
async def get_movies_category(category: str): 
  return {item for item in movies_api if item["category"] == category}


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