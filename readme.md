# Bike Sharing Demand Prediction

This project is a web application that predicts the demand for bike sharing based on various environmental and seasonal factors. It uses a pre-trained Random Forest Regressor model to make predictions through a user-friendly web interface.

## Features

- **Interactive Web Interface:** A clean and professional user interface allows users to input various parameters to get a prediction.
- **Machine Learning Model:** Utilizes a scikit-learn `RandomForestRegressor` model trained on the Bike Sharing Dataset.
- **Real-time Predictions:** The Flask backend processes user input and provides predictions in real-time.

## Technologies Used

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript

## Setup and Usage

To run this project locally, follow these steps:

1.  **Prerequisites:**
    - Python 3.x
    - pip (Python package installer)

2.  **Installation:**
    - Clone this repository or download the project files.
    - Install the required Python packages:
      ```bash
      pip install Flask scikit-learn pandas numpy
      ```

3.  **Running the Application:**
    - Navigate to the project directory in your terminal.
    - Run the Flask application:
      ```bash
      python app.py
      ```
    - Open your web browser and go to `http://127.0.0.1:5000` to use the application.

## File Structure

- `app.py`: The main Flask application file. It handles routing, data processing, and model prediction.
- `templates/index.html`: The frontend of the application, containing the user input form and prediction display.
- `random_forest_model (1).joblib`: The pre-trained machine learning model.
- `day_modified.csv`: The dataset used to train the model.
- `readme.md`: This file.

## How It Works

The user provides input for the following features through the web form:
- Season
- Year
- Month
- Holiday (Yes/No)
- Day of the Week
- Working Day (Yes/No)
- Weather Situation

When the "Predict" button is clicked, the frontend sends this data to the Flask backend. The backend then performs one-hot encoding on the categorical features to transform the input into the 32-feature format that the model expects. The model then predicts the bike rental count, which is sent back to the frontend and displayed to the user.
