from flask import Flask, render_template, request
import numpy as np 
import pandas as pd 
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict_output():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # reading data from html page
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = request.form.get('reading_score'),
            writing_score = request.form.get('writing_score')
        )
        input_df = data.get_data_as_dataframe()
        # prediction 
        predict_pipeline = PredictPipeline()
        output = predict_pipeline.predict(input_df)
        result = f'Your predicted maths marks is {int(output[0])}'

        return render_template('home.html', result = result)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)