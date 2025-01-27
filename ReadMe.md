# Big Mart Sales Prediction

This project is a web application built using Streamlit that allows users to predict sales for Big Mart based on various input features. The application utilizes a trained machine learning model to provide sales predictions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)


## Features

- User-friendly interface for inputting features.
- Predict sales based on user inputs.
- Responsive design for various screen sizes.

## Technologies Used

- [Streamlit](https://streamlit.io/) - For building the web application.
- [Pandas](https://pandas.pydata.org/) - For data manipulation and analysis.
- [Joblib](https://joblib.readthedocs.io/en/latest/) - For loading the trained machine learning model.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/big-mart-sales-prediction.git
   cd big-mart-sales-prediction
   ```

2. **Create a virtual environment (optional but recommended)**:  

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```
3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

    ```bash
    streamlit run app.py
    ```