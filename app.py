import streamlit as st

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

elif page =="Visualization":
    st.title("Sales Visualization")
    st.write("This section will show sales visualization.")
    st.write("Currently, the visualization feature is not available as we don't have data.")