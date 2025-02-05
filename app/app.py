from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)  # Ensure Flask is initialized

# Load the trained model
model_path = "app/model.pkl"
model = pickle.load(open(model_path, "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([data['likes'], data['total_replies']]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"Predicted Comment Length": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Ensure correct port
