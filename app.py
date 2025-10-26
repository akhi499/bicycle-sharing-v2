from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('E:/Akhil/ML/mini project final/random_forest_model.joblib')

# The list of feature names from the trained model
feature_names = ['season_1', 'season_2', 'season_3', 'season_4', 'year_0', 'year_1', 'month_1',
 'month_2', 'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8',
 'month_9', 'month_10', 'month_11', 'month_12', 'holiday_0', 'holiday_1',
 'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4', 'weekday_5',
 'weekday_6', 'workingday_0', 'workingday_1', 'weather_condition_1',
 'weather_condition_2', 'weather_condition_3']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Create a dictionary to hold the input data for DataFrame creation
    input_data = {key: [int(value)] for key, value in data.items()}

    # Create a pandas DataFrame from the input data
    input_df = pd.DataFrame(input_data)

    # Create the full feature set with zeros
    features_df = pd.DataFrame(columns=feature_names)
    features_df.loc[0] = 0

    # One-hot encode the input and update the features DataFrame
    for col, val in input_data.items():
        # Special handling for yr and mnth as they are named differently in the form
        if col == 'yr':
            col_name = f'year_{val[0]}'
        elif col == 'mnth':
            col_name = f'month_{val[0]}'
        elif col == 'weathersit':
            col_name = f'weather_condition_{val[0]}'
        else:
            col_name = f'{col}_{val[0]}'
        if col_name in features_df.columns:
            features_df[col_name] = 1

    # Make prediction
    prediction = model.predict(features_df)

    output = round(prediction[0], 2)

    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(debug=True)
