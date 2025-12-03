from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load cleaned car data for dropdowns
car_data = pd.read_csv('cleaned_car_data.csv')

# Load trained pipeline model
try:
    with open('linearRegressionModel.pk2', 'rb') as f:
        pipe = pickle.load(f)
except Exception as e:
    pipe = None
    print("Error loading model:", e)

@app.route('/')
def index():
    companies = sorted(car_data['company'].dropna().unique())
    car_models = sorted(car_data['name'].dropna().unique())
    years = sorted(car_data['year'].dropna().unique())
    fuel_types = sorted(car_data['fuel_type'].dropna().unique())

    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        years=years,
        fuel=fuel_types
    )

@app.route('/predict', methods=['POST'])
def predict():
    if pipe is None:
        return "<h3 style='color:red;text-align:center;'>Model failed to load. Please check your version or file.</h3>"

    try:
        company = request.form['companies']
        model_name = request.form['car_model']
        year = int(request.form['year'])
        fuel = request.form['fuel_type']
        km_driven = int(request.form['kilo_driven'])

        input_df = pd.DataFrame([[model_name, company, year, km_driven, fuel]],
                                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        predicted_price = pipe.predict(input_df)[0]
        predicted_price = f"₹{int(predicted_price):,}"

        return f"""
        <div style='text-align:center; margin-top:60px; font-family:serif;'>
            <h2>Predicted Price</h2>
            <p>{company} {model_name} ({year}, {fuel})</p>
            <p>Kilometers Driven: {km_driven}</p>
            <hr style='width:300px; margin:auto;'>
            <h3 style='color:gold; font-size:28px;'>Estimated Price: {predicted_price}</h3>
            <br>
            <a href='/' style='text-decoration:none; color:#007bff;'>Predict Another</a>
        </div>
        """
    except Exception as e:
        return f"<h3 style='color:red;text-align:center;'>Prediction failed: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)