import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the best model and selected features 
model = joblib.load('best_model.pkl')
selected_features = joblib.load('selected_features.pkl')

# Streamlit app UI
st.title("Football Player Rating Prediction")
st.markdown("Enter the player's attributes to predict their rating. ")

# Input fields for the top selected features
user_input = {}
for feature in selected_features:
    user_input[feature] = st.number_input(f"{feature}", min_value=0.0, max_value=100.0, value=50.0)

# Convert user input to a DataFrame
input_df = pd.DataFrame([user_input])

# Predict the rating 
if st.button("Predict Overal Rating"):
    prediction = model.predict(input_df) [0]
    st.success(f"Predicted Overall Rating: {prediction:.2f}")


