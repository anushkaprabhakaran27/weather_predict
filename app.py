import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Weather Prediction System",
    page_icon="🌦",
    layout="centered"
)

# Load model
model = joblib.load("weather_model.pkl")

# Title
st.title("🌦 Weather Prediction System")
st.markdown("### Predict the temperature using Machine Learning")
st.write("Enter the weather details below and click **Predict Temperature**.")


st.subheader("🌤 Weather Details")

day_of_year = st.number_input("Day of Year", 1, 366, 150)
month = st.number_input("Month", 1, 12, 6)
humidity = st.number_input("Humidity (%)", 0, 100, 70)
wind_speed = st.number_input("Wind Speed (km/h)", value=15.0)
pressure = st.number_input("Pressure (hPa)", value=1015.0)
cloud_cover = st.number_input("Cloud Cover (%)", 0, 100, 50)
previous_temp = st.number_input("Previous Temperature (°C)", value=28.0)


st.success("Prediction Completed Successfully!")

st.metric(
    label="🌡 Predicted Temperature",
    value=f"{prediction[0]:.2f} °C"
)