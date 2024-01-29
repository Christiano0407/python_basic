from fastapi import APIRouter, status, HTTPException, Path, Query
import os
import pandas as pd
import numpy as np

#* === app & API Router ===
router = APIRouter()


#! === Call Data Base ==
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data_base", "Travel details dataset.csv")
df = pd.read_csv(file_path)
print(df.iloc[:, :5])

#! ==> Clean of values: "NAN" and "Infinites" <== 
df.replace([np.inf - np.inf], np.nan, inplace=True)
df.dropna(inplace=True)


#? ==== API ROOT / REST / CRUD ====
@router.get("/", status_code=status.HTTP_200_OK, tags=["travels"])
async def travel(): 
  return {"message": str("Hi! It's my first trip")} 