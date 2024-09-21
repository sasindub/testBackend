import os
import joblib
import numpy as np

# Resolve the absolute path of the .pkl file
model_path = os.path.join(os.path.dirname(__file__), "vaccine_demand_model.pkl")

# Load the trained model
model = joblib.load("/tmp/8dcda3923923393/model/vaccine_demand_model.pkl")

def predict_demand(region, month, population, prev_demand):
    X = np.array([[month, region, population, prev_demand]])
    prediction = model.predict(X)
    #return int(np.round(prediction[0]))
    return model_path

#region, month, population, prev_demand
