---

# House Price Prediction

This project aims to predict house prices in Bengaluru using a dataset from Kaggle and a Logistic Regression model.

## Project Overview

House prices are influenced by various factors such as location, size, number of bedrooms, and more. In this project, we develop a predictive model using Logistic Regression to estimate the price of houses based on several features.

## Dataset

The dataset used for this project is sourced from Kaggle:

- **Dataset:** [Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

The dataset contains information on house prices along with various attributes such as the area, number of bedrooms, number of bathrooms, and the location.

## Features

The key features used in this project include:

- `total_sqft`: The total area of the house in square feet.
- `bath`: The number of bathrooms.
- `bhk`: The number of bedrooms, halls, and kitchens.
- `location`: The location of the house.

## Model

The model used for prediction is **Logistic Regression**. The model was trained using the aforementioned features to predict the price range of houses in Bengaluru.

## Installation

To run this project, clone the repository and install the required dependencies using the `requirements.txt` file:

```bash
git clone https://github.com/SaabareeshM/House-Price-Prediction.git
pip install -r requirements.txt
```

## Usage

Once the dependencies are installed, you can run the Flask application to use the house price prediction model:

```bash
python app.py
```

You can then access the web application locally to input the house features and get the predicted price range.

## Results

The model was evaluated on the dataset, and the results indicate that the Logistic Regression model provides reasonable predictions based on the given features.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

---
