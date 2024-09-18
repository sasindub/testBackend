from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.predict_model import predict_demand
import pandas as pd
from typing import List

app = FastAPI()

# origins = [
#     "https://whfgrx3r-8000.asse.devtunnels.ms",  # Frontend origin 
#     "http://localhost:8000",  
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],  
#     allow_headers=["*"], 
# )


# # model for the request
# class PredictionRequest(BaseModel):
#     region: int
#     month: int
#     population: int
#     prev_demand: int = None

# # model for the response
# class DataPoint(BaseModel):
#     label: str
#     value: float


# Home route to render the HTML page
@app.get("/")
async def home():
    return {"message": "yes"}

# # Prediction route to accept JSON request body
# @app.post("/predict")
# async def predict(request: PredictionRequest):
#     #Extract the data from the request model
#     prediction = predict_demand(request.region, request.month, request.population, request.prev_demand)
 
#     return {"predicted_demand": prediction}
   

# @app.get("/synthetic_vaccine_data", response_model=List[DataPoint])
# async def get_synthetic_vaccine_data():

#     df = pd.read_csv('synthetic_vaccine_data.csv')

    
#     data = []
#     for _, row in df.iterrows():
#         data.append(DataPoint(
#             label=f"Month {int(row['month'])}, Region {int(row['region'])}",
#             value=float(row['demand'])
#         ))

#     return data

