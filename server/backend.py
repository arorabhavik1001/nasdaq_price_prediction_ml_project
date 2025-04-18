from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model
with open('stock_price_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/ping', methods=['GET'])
def ping():
    return "Pong"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
