import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def run_prediction():

    # Load the saved model
    model = joblib.load('model.pkl')

    # Define and fit LabelEncoder for each categorical feature
    label_encoder_fat_content = LabelEncoder()
    label_encoder_fat_content.fit(['Low Fat', 'Regular'])  # fit for FatContent

    label_encoder_product_type = LabelEncoder()
    label_encoder_product_type.fit(['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 
                                    'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene', 
                                    'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood'])  # fit for ProductType

    label_encoder_outlet_size = LabelEncoder()
    label_encoder_outlet_size.fit(['Small', 'Medium', 'High'])  # fit for OutletSize

    label_encoder_location_type = LabelEncoder()
    label_encoder_location_type.fit(['Tier 1', 'Tier 2', 'Tier 3'])  # fit for LocationType

    label_encoder_outlet_type = LabelEncoder()
    label_encoder_outlet_type.fit(['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])  # fit for OutletType

    label_encoder_item_category = LabelEncoder()
    label_encoder_item_category.fit(['Food', 'Drink', 'Non-Consumable'])  # fit for ItemCategory

    # Create Streamlit widgets for user input
    st.title("Predict Outlet Sales")

    # Input fields for features
    weight = st.number_input("Weight", min_value=0.0, step=0.1)
    fat_content = st.selectbox("Fat Content", ['Low Fat', 'Regular'])
    product_type = st.selectbox("Product Type", ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 
                                                 'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 
                                                 'Health and Hygiene', 'Hard Drinks', 'Canned', 'Breads', 
                                                 'Starchy Foods', 'Others', 'Seafood'])
    mrp = st.number_input("MRP", min_value=0.0, step=0.1)
    outlet_size = st.selectbox("Outlet Size", ['Small', 'Medium', 'High'])
    location_type = st.selectbox("Location Type", ['Tier 1', 'Tier 2', 'Tier 3'])
    outlet_type = st.selectbox("Outlet Type", ['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])
    item_category = st.selectbox("Item Category", ['Food', 'Drink', 'Non-Consumable'])
    product_visibility_sqrt = st.number_input("Product Visibility (sqrt)", min_value=0.0, step=0.1)
    age_outlet = st.number_input("Age of Outlet", min_value=0, step=1)

    # Encode categorical inputs using label encoding
    encoded_fat_content = label_encoder_fat_content.transform([fat_content])[0]
    encoded_product_type = label_encoder_product_type.transform([product_type])[0]
    encoded_outlet_size = label_encoder_outlet_size.transform([outlet_size])[0]
    encoded_location_type = label_encoder_location_type.transform([location_type])[0]
    encoded_outlet_type = label_encoder_outlet_type.transform([outlet_type])[0]
    encoded_item_category = label_encoder_item_category.transform([item_category])[0]

    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'Weight': [weight],
        'FatContent': [encoded_fat_content],
        'ProductType': [encoded_product_type],
        'MRP': [mrp],
        'OutletSize': [encoded_outlet_size],
        'LocationType': [encoded_location_type],
        'OutletType': [encoded_outlet_type],
        'ProductVisibility_sqrt': [product_visibility_sqrt],
        'Item_Category': [encoded_item_category],
        'Age_Outlet': [age_outlet]
    })


    # Predict using the model
    if st.button("Predict"):
        prediction = model.predict(input_data)
        predicted_sales = prediction[0]
        
        # Convert the predicted outlet sales from sqrt scale back to the original scale
        outlet_sales = predicted_sales ** 2
        
        st.write(f"Predicted Outlet Sales: {outlet_sales}")

