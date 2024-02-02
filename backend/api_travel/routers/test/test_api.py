#####
#TODO:  === Pruebas unitarias  > Test Instance Of Class === 
#pytest routers/test/test_api.py
#######
import pytest
from fastapi.testclient import TestClient
from fastapi.exceptions import HTTPException
from main_trip import app


#* ==== === Tests === ==== 
client = TestClient(app)

def test_home():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello! Welcome at Home. Enjoy To Travel"}

def test_get_user_id():
  response = client.get("/travels/user/1")
  assert response.status_code == 200

def test_get_user_id():
  response = client.get("/travels/time/duration", params={"duration": 5})
  assert response.status_code == 200

def test_get_user_id():
  response = client.get("/travels/trip/transport", params={"transport": 5})
  assert response.status_code == 200

def test_get_user_id():
  response = client.get("/travels/users/lodging", params={"lodging": 5})
  assert response.status_code == 200

""" def test_post_user_id(): 
  response = client.post("/travels/user/6", json={"trip_users": [{"Trip ID": 6, "Traveler name": "Test User"}]})
  print(response.text)  # Imprimir el contenido del cuerpo de la respuesta
  assert response.status_code == 200 """

""" def test_post_user_id():
    try:
        response = client.post("/travels/user/6", json={"trip_users": [{"Trip ID": 6, "Traveler name": "Test User"}]})
        assert response.status_code == 200
    except HTTPException as e:
        print(e.detail)  # Imprimir el detalle del error
        raise e """
    

#! === Main ===
if __name__ == "__main__":
  pytest.main()