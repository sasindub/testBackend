import os
import joblib
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log to a file
    level=logging.ERROR,  # Log only errors and above
    format='%(asctime)s %(levelname)s:%(message)s'
)

# CORS settings
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

# Model request schema
class PredictionRequest(BaseModel):
    region: int
    month: int
    population: int
    prev_demand: int = None

# Model response schema
class DataPoint(BaseModel):
    label: str
    value: float

# Resolve the absolute path of the .pkl file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "vaccine_demand_model.pkl")

# Load the trained model with error handling
try:
    model = joblib.load(model_path)
    logging.info("Model loaded successfully.")  # Use logging instead of app.logger
except Exception as e:
    logging.error(f"Error loading the model: {str(e)}")
    model = None  # Set model to None to indicate loading failure

# Prediction function
def predict_demand(region, month, population, prev_demand):
    if model is None:
        raise RuntimeError("Model is not loaded.")
    
    # Prepare input features
    X = [[month, region, population, prev_demand]]
    prediction = model.predict(X)
    return int(prediction[0])

# Home route
@app.get("/")
async def home(request: Request):
    try:
        if model is None:
            raise HTTPException(status_code=503, detail="Service Unavailable: Model not loaded")
        msg = "Model is ready for predictions"
        return {"message": msg}
    except Exception as e:
        logging.error(f"Error in home route: {str(e)}")
        return JSONResponse(status_code=500, content={"error": "Internal Server Error"})

# Prediction route to accept JSON request body
@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        # Extract the data from the request model
        prediction = predict_demand(request.region, request.month, request.population, request.prev_demand)
        return {"predicted_demand": prediction}
    except RuntimeError as e:
        logging.error(f"Runtime error: {str(e)}")
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Route to fetch synthetic vaccine data from CSV
# @app.get("/synthetic_vaccine_data", response_model=List[DataPoint])
# async def get_synthetic_vaccine_data():
#     try:
#         df = pd.read_csv('synthetic_vaccine_data.csv')
#         data = []
#         for _, row in df.iterrows():
#             data.append(DataPoint(
#                 label=f"Month {int(row['month'])}, Region {int(row['region'])}",
#                 value=float(row['demand'])
#             ))
#         return data
#     except Exception as e:
#         logging.error(f"Error loading CSV data: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to load synthetic vaccine data")
