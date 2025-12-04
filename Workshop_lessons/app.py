import streamlit as st
import pandas as pd
import joblib   # to load your saved model + scaler

st.title("🏠 House Price Prediction App")

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Input fields
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Bathrooms", min_value=0, step=1)
size = st.number_input("House Size (sqft)", min_value=0, step=50)

if st.button("Predict Price"):
    new_house = pd.DataFrame([{
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "HouseSize_sqft": size,
    }])

    # Scale numeric features
    new_scaled = scaler.transform(new_house)

    # Convert back to DataFrame with correct column names
    new_scaled_df = pd.DataFrame(new_scaled, columns=new_house.columns)

    # Predict
    prediction = model.predict(new_scaled_df)[0]

    st.success(f"Estimated House Price: ${prediction:,.2f}")
