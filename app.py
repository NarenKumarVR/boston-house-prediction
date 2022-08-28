from flask import Flask, request, url_for, redirect, render_template, jsonify

import pandas as pd
import joblib


import numpy as np


app = Flask(__name__)
reg1 =joblib.load('Xgbcopy.pkl')
cols = ['LSTAT','RM','PTRATIO','INDUS']


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final = np.array(int_features)
    final1 = pd.DataFrame([final], columns=cols)
    print(final1)
    prediction = reg1.predict(final1)

    return render_template('home.html', pred='Predicted House price will be {}'.format(prediction))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = reg1.predict(data_unseen)

    return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
