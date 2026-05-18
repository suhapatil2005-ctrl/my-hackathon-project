from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)
CORS(app)
# ----------------------------
# LOAD DATASET
# ----------------------------

# Make sure CSV file is in same folder

df = pd.read_csv("StudentsPerformance.csv")

# ----------------------------
# PREPROCESSING
# ----------------------------
df['gender'] = df['gender'].map({
    'female': 0,
    'male': 1
})

X = df[['gender', 'math score', 'reading score']]

y = df['writing score']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------
# TRAIN MODEL
# ----------------------------

model = RandomForestRegressor()
model.fit(X_train, y_train)
# ----------------------------
# API ROUTE
# ----------------------------

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    gender = int(data['gender'])
    math = float(data['math'])
    reading = float(data['reading'])

    prediction = model.predict([[gender, math, reading]])

    return jsonify({
        'prediction': round(prediction[0], 2)
    })
# ----------------------------
# RUN SERVER
# ----------------------------

if __name__ == '__main__':
    app.run(debug=True)