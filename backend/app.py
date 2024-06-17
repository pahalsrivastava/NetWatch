
from flask import Flask, request, jsonify
import joblib
from data_processing.preprocess import load_and_preprocess_data
import numpy as np

app = Flask(__name__)

model = joblib.load('ml_model/isolation_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    data = np.array(data).reshape(1, -1)  # Reshape for a single sample
    prediction = model.predict(data)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
