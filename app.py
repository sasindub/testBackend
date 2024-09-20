from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
#from model.predict_model import predict_demand
import pandas as pd
from typing import List

app = FastAPI()

origins = [
    "https://whfgrx3r-8000.asse.devtunnels.ms",  # Frontend origin 
    "http://localhost:8000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


# model for the request
class PredictionRequest(BaseModel):
    region: int
    month: int
    population: int
    prev_demand: int = None

# model for the response
class DataPoint(BaseModel):
    label: str
    value: float

import pickle
import os
import pickle
import numpy as np
import pickle

# # Resolve the absolute path of the .pkl file
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # model_path = os.path.join(BASE_DIR, "vaccine_demand_model.pkl")
# # Load the trained model
# # model = pickle.load(open(model_path, "rb"))

def predict_demand():
 # Create a sample object
    data = {"key1": "value1", "key2": 42}

    # Save the object to a new .pkl file
    with open("new_model.pkl", "wb") as f:
        pickle.dump(data, f)

        # Resolve the absolute path of the .pkl file
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, "new_model.pkl")
    # Load the trained model
    model = pickle.load(open("/tmp/8dcd9c0505710e8/new_model.pkl", "rb"))
    return model_path

# Home route to render the HTML page
@app.get("/")
async def home(request: Request):   
    return {"message": predict_demand()}

# Prediction route to accept JSON request body
@app.post("/predict")
async def predict(request: PredictionRequest):
    #Extract the data from the request model
    prediction = predict_demand(request.region, request.month, request.population, request.prev_demand)
 
    return {"predicted_demand": prediction}
   

@app.get("/synthetic_vaccine_data", response_model=List[DataPoint])
async def get_synthetic_vaccine_data():

    df = pd.read_csv('synthetic_vaccine_data.csv')

    
    data = []
    for _, row in df.iterrows():
        data.append(DataPoint(
            label=f"Month {int(row['month'])}, Region {int(row['region'])}",
            value=float(row['demand'])
        ))

    return data