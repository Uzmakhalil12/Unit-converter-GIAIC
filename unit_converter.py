import streamlit as st
# Conversion dictionaries 
time_units = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,  
    "days": 86400,
    "weeks": 604800,        
    "months": 2628000,
    "years": 31536000
}

# Time Conversion Function 
def convert_time(value, unit_from, unit_to):
   """Convert time from one unit to another"""
   return value * ( time_units[unit_from] / time_units[unit_to])

# Streamlit UI
st.title("Unit Converter: Time")


st.header("Time Unit Converter")

unit_from = st.selectbox("From", list(time_units.keys()))
unit_to = st.selectbox("To", list(time_units.keys()))

    
time_value = st.number_input("Value" , min_value=0.0, format="%.2f")

if st.button("Convert Time Unit"):
    if from_unit == to unit:
         st.error("Please select a conversion type")
        
else:
     result = convert_time(time_value, unit_from, unit_to)
        st.success(f"{time_value} {unit_from} = {result:.2f} {unit_to}")



