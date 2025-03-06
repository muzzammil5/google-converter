import streamlit as st

# Define unit categories and conversion factors
CATEGORIES = {
    'Length': ['meters', 'kilometers', 'miles', 'feet', 'inches'],
    'Weight': ['kilograms', 'grams', 'pounds', 'ounces'],
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
    'Volume': ['liters', 'milliliters', 'gallons', 'cubic meters']
}

CONVERSION_FACTORS = {
    'Length': {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    },
    'Weight': {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    },
    'Volume': {
        'liters': 1,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'cubic meters': 1000
    }
}

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == 'Celsius':
        celsius = value
    elif from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'Kelvin':
        celsius = value - 273.15
    
    # Convert Celsius to target unit
    if to_unit == 'Celsius':
        return celsius
    elif to_unit == 'Fahrenheit':
        return celsius * 9/5 + 32
    elif to_unit == 'Kelvin':
        return celsius + 273.15

# Streamlit UI Configuration
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("📐 Unit Converter by Muzzammil Hussain - GIAIC March 2025")

# Category Selection
category = st.selectbox("Select Category", list(CATEGORIES.keys()))

# Unit Selection Layout
col1, col2, col3 = st.columns(3)
with col1:
    value = st.number_input("Value", min_value=0.0, value=1.0, step=0.1)
with col2:
    from_unit = st.selectbox("From", CATEGORIES[category])
with col3:
    to_unit = st.selectbox("To", CATEGORIES[category])

# Conversion Logic
if category != 'Temperature':
    factors = CONVERSION_FACTORS[category]
    base_value = value * factors[from_unit]
    result = base_value / factors[to_unit]
else:
    result = convert_temperature(value, from_unit, to_unit)

# Display Result
st.success(f"**Result:** {value:.2f} {from_unit} = {result:.4f} {to_unit}")