---
title: House Price Prediction App
emoji: 🏡
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.35.0"
app_file: app.py
pinned: false
---





# 🏡 House Price Prediction – Streamlit App

Predict house prices instantly using a trained Machine Learning model!  
This app takes user inputs and returns an estimated house price based on a regression model trained on real housing data.

---

## 🚀 Live Demo
Hugging Face Space link.

https://huggingface.co/spaces/Bicir/HousePrice



---

## 📌 Project Overview

This project uses **Machine Learning** to estimate housing prices based on user-provided features such as:

- Number of bedrooms
- Number of bathrooms
- Square footage (Area)

The goal is to provide a simple and interactive interface using **Streamlit**, allowing anyone to try the model online.

---

## 🧠 Model Used

The model (`model.pkl`) was trained using:

- **Scikit-Learn**
- Data preprocessing (handling missing values, encoding, scaling)
- Train/Test split
- Evaluation metrics:
  - **MSE** (Mean Squared Error)
  - **RMSE** (Root Mean Squared Error)
  - **R² Score**

The app loads the trained model and scaler to perform prediction in real-time.

---

## 📂 Project Structure

/
├── app.py # Streamlit user interface
├── model.pkl # Trained machine learning model
├── scaler.pkl # Scaler used during training (optional)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://huggingface.co/spaces/your-username/house-price-prediction
cd house-price-prediction

Install dependencies
pip install -r requirements.txt

Run the Streamlit app
streamlit run app.py


ow to Use the App

Enter the house features in the input fields

Click Predict Price

The model returns the predicted price instantly

Try adjusting the values to see price changes
