from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI()

# Allow JS requests from any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain for production
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    features = np.array([data["Bedrooms"], data["Bathrooms"], data["HouseSize_sqft"]]).reshape(1, -1)
    scaled = scaler.transform(features)
    prediction = float(model.predict(scaled)[0])
    return {"prediction": prediction}
