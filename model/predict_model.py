import os
import pickle
import numpy as np
import pickle

# Resolve the absolute path of the .pkl file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "vaccine_demand_model.pkl")
# Load the trained model
model = pickle.load(open(model_path, "rb"))

def predict_demand():
 # Create a sample object
    data = {"key1": "value1", "key2": 42}

    # Save the object to a new .pkl file
    with open("new_model.pkl", "wb") as f:
        pickle.dump(data, f)
    return model_path

# def test():
#     return model_path

#region, month, population, prev_demand