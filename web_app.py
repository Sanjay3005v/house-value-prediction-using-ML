import streamlit as st
import numpy as np
import joblib

st.title("House Price Prediction")

# Load the trained model
model = joblib.load("house_model.pkl")

# Input fields for features (add/remove fields as per your model)
bedrooms = st.number_input('Bedrooms', min_value=0, max_value=20, value=3)
bathrooms = st.number_input('Bathrooms', min_value=0.0, max_value=10.0, value=2.0)
sqft_living = st.number_input('Sqft Living', min_value=100, max_value=20000, value=1800)
sqft_lot = st.number_input('Sqft Lot', min_value=100, max_value=100000, value=5000)
floors = st.number_input('Floors', min_value=1.0, max_value=4.0, value=1.0)
waterfront = st.selectbox('Waterfront', [0, 1])
view = st.number_input('View', min_value=0, max_value=4, value=0)
condition = st.number_input('Condition', min_value=1, max_value=5, value=3)
grade = st.number_input('Grade', min_value=1, max_value=13, value=7)
sqft_above = st.number_input('Sqft Above', min_value=100, max_value=10000, value=1500)
sqft_basement = st.number_input('Sqft Basement', min_value=0, max_value=5000, value=0)
yr_built = st.number_input('Year Built', min_value=1900, max_value=2022, value=1990)
yr_renovated = st.number_input('Year Renovated', min_value=0, max_value=2022, value=0)
zipcode = st.number_input('Zipcode', min_value=98000, max_value=98200, value=98103)
lat = st.number_input('Latitude', min_value=47.0, max_value=48.0, value=47.5)
long = st.number_input('Longitude', min_value=-123.0, max_value=-121.0, value=-122.0)
sqft_living15 = st.number_input('Sqft Living (15 nearest neighbors)', min_value=100, max_value=10000, value=1800)
sqft_lot15 = st.number_input('Sqft Lot (15 nearest neighbors)', min_value=100, max_value=100000, value=5000)
date = st.selectbox('Sold in 2014?', [0, 1])  # If you converted date to 0/1

# NOTE: Your model expects 19 features, but only 15 are provided.
# Make sure to include all features used during model training, in the correct order.
# Example: If you dropped only 'id' and 'price', all other columns (including 'date', 'yr_renovated', etc.) must be included.

# Collect features into array (order must match model training)
features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view,
                      condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated,
                      zipcode, lat, long, sqft_living15, sqft_lot15, date]])

if st.button("Predict"):
    price = model.predict(features)[0]
    st.success(f"Estimated House Price: ${price:,.2f}")
