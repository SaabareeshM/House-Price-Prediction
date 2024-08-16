from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load the model and the columns
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

locations = data_columns[3:]  # First three are total_sqft, bath, bhk

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']

    # Create an input array for prediction
    x = np.zeros(len(data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    prediction = model.predict([x])[0]

    # Convert the prediction to lakhs and format the output
    prediction_in_lakhs = round(prediction, 2)
    formatted_price = f'{prediction_in_lakhs} lakhs'  # 89.5 lakhs format
    # Or for Indian numbering format like 89,50,000:
    formatted_price_in_inr = f'{prediction_in_lakhs * 100000:,.0f}'

    return render_template('index.html', prediction_text=f'Estimated House Price: {formatted_price} ({formatted_price_in_inr} INR)', locations=locations)


if __name__ == "__main__":
    app.run(debug=True)
