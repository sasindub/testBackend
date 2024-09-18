import os
import joblib
import numpy as np

# Resolve the absolute path of the .pkl file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "vaccine_demand_model.pkl")
# Load the trained model
#model = joblib.load(model_path)

def predict_demand(region, month, population, prev_demand):
    #X = np.array([[month, region, population, prev_demand]])
    #prediction = model.predict(X)
    #return int(np.round(prediction[0]))
    return model_path
