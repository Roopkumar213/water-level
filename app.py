from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load trained model
with open("water_quality_model.pkl", "rb") as file:
    model = pickle.load(file)

# Mapping back to quality labels
quality_map = {0: "Bad", 1: "Average", 2: "Good"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        ph = float(data['ph'])
        prediction = model.predict([[ph]])[0]
        probs = model.predict_proba([[ph]])[0].tolist()

        response = {
            "ph": ph,
            "prediction": quality_map[prediction],
            "probabilities": {
                "Bad": round(probs[0]*100, 2),
                "Average": round(probs[1]*100, 2),
                "Good": round(probs[2]*100, 2)
            }
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
