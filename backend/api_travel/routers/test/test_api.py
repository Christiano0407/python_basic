#####
#TODO:  === Pruebas unitarias  > Test Instance Of Class === 
#pytest routers/test/test_api.py
#######
import pytest
from fastapi.testclient import TestClient
from main_trip import app


#* ==== === Tests === ==== 
client = TestClient(app)

def test_home():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello! Welcome at Home. Enjoy To Travel"}  
    

#! === Main ===
if __name__ == "__main__":
  pytest.main()