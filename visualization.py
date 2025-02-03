import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_visualization(data):
    st.title("Sales Visualization")
    st.write("This section allows you to visualize different aspects of the sales data.")

    # Select the column for the x-axis
    x_column = st.selectbox("Select Column for X-axis", data.columns)

    # Select the column for the y-axis (default to Item_Outlet_Sales)
    y_column = st.selectbox("Select Column for Y-axis", data.columns, index=data.columns.get_loc('Item_Outlet_Sales'))

    # Select the type of visualization
    visualization_type = st.radio("Select Type of Visualization", ["Bar Chart", "Line Chart", "Box Plot", "Scatter Plot", "Histogram"])

    # Additional options for plots that require more variables
    if visualization_type in ["Scatter Plot", "Bar Chart"]:
        color_column = st.selectbox("Select Column for Color", data.columns, index=0)
    
    if visualization_type == "Scatter Plot":
        size_column = st.selectbox("Select Column for Size", data.columns, index=0)

    # Create the visualization based on user selection
    if st.button("Generate Visualization"):
        plt.figure(figsize=(10, 6))

        if visualization_type == "Bar Chart":
            sns.barplot(x=x_column, y=y_column, hue=color_column, data=data)
            plt.title(f'Bar Chart of {x_column} vs {y_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)

        elif visualization_type == "Line Chart":
            data.groupby(x_column)[y_column].mean().plot(kind='line')
            plt.title(f'Line Chart of {x_column} vs Average {y_column}')
            plt.xlabel(x_column)
            plt.ylabel(f'Average {y_column}')

        elif visualization_type == "Box Plot":
            sns.boxplot(x=x_column, y=y_column, data=data)
            plt.title(f'Box Plot of {x_column} vs {y_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)

        elif visualization_type == "Scatter Plot":
            sns.scatterplot(x=x_column, y=y_column, hue=color_column, size=size_column, sizes=(20, 200), data=data)
            plt.title(f'Scatter Plot of {x_column} vs {y_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)

        elif visualization_type == "Histogram":
            sns.histplot(data[y_column], bins=30, kde=True)
            plt.title(f'Histogram of {y_column}')
            plt.xlabel(y_column)
            plt.ylabel('Frequency')

        plt.xticks(rotation=45)
        st.pyplot(plt)