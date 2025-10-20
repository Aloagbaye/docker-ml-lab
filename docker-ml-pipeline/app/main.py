import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Load model generated from train.py
model = joblib.load("model.pkl")

#fastapi app
app = FastAPI()

# pydantic for data formatting
class InputData(BaseModel):
    features: list

#predict api called during /predict with a POST request
@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)
    pred = model.predict(X)[0]
    return {"prediction": int(pred)}