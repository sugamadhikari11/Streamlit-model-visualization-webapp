import streamlit as st
import pandas as pd
from visualization import run_visualization  # Import the visualization function

# Load the dataset
data = pd.read_csv('Train.csv')  # Adjust the path to your dataset

# Set the title of the app
st.set_page_config(page_title="Big Mart Sales Prediction", layout="wide")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Prediction", "Visualization"])

# Welcome Page
if page == "Welcome":
    st.title("Welcome to Big Mart Sales Prediction")
    st.write("""
        This application allows you to predict sales based on various input features.
        Use the navigation bar to explore the application.
    """)
    st.image("https://via.placeholder.com/800x400", caption="Welcome to Big Mart Sales Prediction")  # Placeholder image

# Prediction Page
elif page == "Prediction":
    st.title("Sales Prediction")
    st.write("This section will contain the sales prediction functionality.")
    st.write("Currently, the prediction feature is not available as we don't have data.")

# Visualization Page
elif page == "Visualization":
    run_visualization(data)  # Call the visualization function