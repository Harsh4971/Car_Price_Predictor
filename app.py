# streamlit run app.py


import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('LinearRegressionModel.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Car Price Prediction 🚗')
st.write('This app predicts the price of used cars based on their specifications.')

# Input fields
name = st.text_input('Car Name (e.g., Hyundai Santro Xing)')
company = st.selectbox('Company', [
    'Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',
    'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',
    'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',
    'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo'
])
year = st.number_input('Year of Manufacture', min_value=1900, max_value=2023, step=1)
kms_driven = st.number_input('Kilometers Driven', min_value=0, step=1)
fuel_type = st.selectbox('Fuel Type', ['Diesel', 'Petrol', 'LPG'])

# Process car name to keep first 3 words
processed_name = ' '.join(name.split()[:3]).strip()

# Create input DataFrame
input_data = pd.DataFrame([[
    processed_name,
    company,
    year,
    kms_driven,
    fuel_type
]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

if st.button('Predict Price'):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f'Predicted Price: ₹{prediction:,.2f}')
    except Exception as e:
        st.error(f'Error in prediction: {str(e)}')