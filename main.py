from google import genai
import streamlit as st

api_key = st.secrets["api"]["key"]

client = genai.Client(api_key=api_key)

UNITS = {
    "Length": [
        "Meters",
        "Kilometers",
        "Centimeters",
        "Millimeters",
        "Miles",
        "Yards",
        "Feet",
        "Inches",
    ],
    "Time": [
        "Seconds",
        "Minutes",
        "Hours",
        "Days",
        "Weeks",
        "Months",
        "Years",
    ],
    "Weight": [
        "Kilograms",
        "Grams",
        "Milligrams",
        "Pounds",
        "Ounces",
        "Stone",
    ],
    "Temperature": [
        "Celsius",
        "Fahrenheit",
        "Kelvin",
    ],
    "Volume": [
        "Liters",
        "Milliliters",
        "Cubic Meters",
        "Gallons",
        "Quarts",
        "Cups",
    ],
    "Area": [
        "Square Meters",
        "Square Kilometers",
        "Square Feet",
        "Square Yards",
        "Acres",
        "Hectares",
    ],
}

st.set_page_config("🚀 Unit Converter", layout="wide")
st.title("🚀 Unit Converter")
st.write("Convert between different units of measurements.")

quantity = st.selectbox("Quantity", UNITS)
input_from = st.number_input("From:")

col1, col2 = st.columns(2)

with col1:
    unit_from = st.selectbox("From:", UNITS[quantity], key="unit_from")

with col2:
    unit_to = st.selectbox("To:", UNITS[quantity], key="unit_to")

if st.button("Convert"):
    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Convert {quantity} of {input_from} in {unit_from} to {unit_to}.",
    )
    st.write(result.text)
