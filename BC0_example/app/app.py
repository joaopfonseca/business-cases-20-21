import os
from pathlib import Path
import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

PROJECT_ROOT = Path(os.path.abspath('')).resolve().parents[0]

app = Flask(__name__)  # Initialize the flask App
model = load(os.path.join(PROJECT_ROOT, 'analysis', 'best_decision_tree1.joblib'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = list(request.form.values())[0].split(',')
    final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)

    output = prediction[0][0] * 100

    return render_template('index.html', prediction_text='The customer has a {:.2f}% chance of subscribing.'.format(output))

if __name__ == "__main__":
    app.run(debug=True)