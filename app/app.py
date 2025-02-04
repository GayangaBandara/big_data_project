from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([data['Feature1'], data['Feature2']]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"Predicted Price": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
