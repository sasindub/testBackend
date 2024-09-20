import os
import pickle
import numpy as np
import pickle

# Resolve the absolute path of the .pkl file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "vaccine_demand_model.pkl")
# Load the trained model #
model = pickle.load(open("/tmp/8dcd9c3dc14c1d7/model/vaccine_demand_model.pkl", "rb"))

def predict_demand(region, month, population, prev_demand):
    X = np.array([[month, region, population, prev_demand]])
    prediction = model.predict(X)
    int(np.round(prediction[0]))
    return model_path

# def test():
#     return model_path

#region, month, population, prev_demand