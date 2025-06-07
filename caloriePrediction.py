import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("calorie_prediction_voting_regressor_model.pkl")  # Replace with your actual filename

st.set_page_config(page_title="Calorie Burn Predictor", layout="centered")

st.title("🔥 Calorie Burn Predictor")

st.markdown("Enter your workout details to estimate how many calories you burned.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age (years)", min_value=10, max_value=100, step=1)
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, step=0.5)
duration = st.number_input("Workout Duration (minutes)", min_value=1.0, max_value=300.0, step=1.0)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=50, max_value=200, step=1)

# Convert gender to numeric if needed
gender_encoded = 1 if gender == "Male" else 0

if st.button("Predict Calories Burned"):
    input_data = np.array([[gender_encoded, age, weight, duration, heart_rate]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Calories Burned: **{prediction:.2f} kcal**")
