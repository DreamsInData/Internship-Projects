from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the model (update path if it's inside a folder)
MODEL_PATH = os.path.join('heart_disease_model.pkl')
model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form = request.form
    data = {
        'age': int(form['age']),
        'sex': int(form['sex']),
        'chest pain type': int(form['chest_pain']),
        'resting bp s': int(form['bp']),
        'cholesterol': int(form['cholesterol']),
        'fasting blood sugar': int(form['sugar']),
        'resting ecg': int(form['ecg']),
        'max heart rate': int(form['hr']),
        'exercise angina': int(form['angina']),
        'oldpeak': float(form['oldpeak']),
        'ST slope': int(form['slope'])
    }

    df = pd.DataFrame([data])
    probs = model.predict_proba(df)[0]
    pred = model.predict(df)[0]
    prob = probs[pred]  # probability of the predicted class (0 or 1)

    result = 'Heart Disease Detected' if pred == 1 else 'No Heart Disease'
    return render_template(
        'index.html',
        result=result,
        probability=f"{prob * 100:.2f}%"
    )

if __name__ == '__main__':
    app.run(debug=True)
