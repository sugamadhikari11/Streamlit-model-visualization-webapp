import streamlit as st
import pandas as pd
import numpy as np
from visualization import run_visualization  # Import the visualization function
from prediction import run_prediction

# Load the dataset
data = pd.read_csv('Train.csv')  # Adjust the path to your dataset

# Set the title of the app
st.set_page_config(page_title="Big Mart Sales Prediction", layout="wide")

# Add custom CSS for Big Mart theme styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #0E6E2B;  /* Green color for Big Mart */
        border-radius: 10px;  /* Rounded corners */
        padding: 10px;  /* Padding for the sidebar */
    }
    .sidebar .sidebar-content button {
        color: white;
        background-color: #0E6E2B;  /* Green background */
        border: none;  /* No border */
        border-radius: 5px;  /* Rounded corners */
        padding: 10px;  /* Padding for buttons */
        width: 100%;  /* Full width */
        text-align: left;  /* Align text to the left */
        cursor: pointer;  /* Pointer cursor on hover */
        transition: background-color 0.3s;  /* Smooth transition */
    }
    .sidebar .sidebar-content button:hover {
        background-color: #004d1f;  /* Dark green hover effect */
    }
    </style>
    """, unsafe_allow_html=True
)

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = "Welcome"  # Default page

# Create a sidebar for navigation
st.sidebar.title("Navigation")

# Sidebar buttons for navigation with emojis
def render_sidebar_buttons():
    if st.sidebar.button("🏠 Welcome"):
        st.session_state.page = "Welcome"
    if st.sidebar.button("📈 Prediction"):
        st.session_state.page = "Prediction"
    if st.sidebar.button("📊 Visualization"):
        st.session_state.page = "Visualization"

render_sidebar_buttons()

# Sidebar Enhancements with descriptions
if st.session_state.page == "Welcome":
    st.sidebar.subheader("Introduction")
    st.sidebar.write("This section introduces the app and its functionality.")
    st.sidebar.write("You can predict sales, visualize data, or explore other insights using this app.")

elif st.session_state.page == "Prediction":
    st.sidebar.subheader("Sales Prediction")
    st.sidebar.write("In this section, you can input various features to predict outlet sales.")

elif st.session_state.page == "Visualization":
    st.sidebar.subheader("Data Visualization")
    st.sidebar.write("Visualize various insights from the dataset using charts and graphs.")

# Welcome Page
if st.session_state.page == "Welcome":
    st.title("Welcome to Big Mart Sales Prediction")
    st.write("""
        This application allows you to predict sales based on various input features.
        Use the navigation bar to explore the application.
    """)
    st.image("https://media.licdn.com/dms/image/v2/C4E1BAQEYBUUDz5QoTQ/company-background_10000/company-background_10000/0/1636886041467/big_mart_nepal_cover?e=2147483647&v=beta&t=JgFMnOQk2v2oXgwo3qxqVaWeuhLZlOPyelzwrCHloyY", caption="Welcome to Big Mart Sales Prediction")  # Placeholder image
    st.write("""
    Kaggle Notebook Link: https://www.kaggle.com/code/tetsuyasugam/big-mart-sales-visualization-and-prediction
""")
# Prediction Page
elif st.session_state.page == "Prediction":
    run_prediction()

# Visualization Page
elif st.session_state.page == "Visualization":
    run_visualization(data)  # Call the visualization function