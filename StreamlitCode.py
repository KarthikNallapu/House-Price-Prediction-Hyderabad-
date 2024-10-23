import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
model_path = (r'C:\Users\karth\OneDrive\Desktop\NEW_HHPP\HHPP.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Mapping of location_encoded to Encoded Locations
location_map = {
    0: 'Banjara Hills',
    1: 'Gachibowli',
    2: 'Hitech City',
    3: 'Kokapet',
    4: 'Kondapur',
    5: 'Kukatpally',
    6: 'Manikonda',
    7: 'Miyapur',
    8: 'Nanakramguda',
    9: 'Nizampet'
}

# Streamlit app
st.title("Hyderabad House Price Prediction")

# Input form for user input
area = st.number_input("Area (sq. ft.)", min_value=500, step=1)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4])
location_encoded = st.selectbox("Location", list(location_map.keys()), format_func=lambda x: location_map[x])
year = st.number_input("Year", min_value=2024, step=1)

# Predict button
if st.button("Predict Price"):
    # Create a DataFrame with the input features
    input_features = pd.DataFrame({'Area': [area], 'No_of_Bedrooms': [bedrooms], 'location_encoded': [location_encoded], 'Year': [year]})


    # Use the model to predict the price
    predicted_price = model.predict(input_features)

    # Display the predicted price in INR
    st.success(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
