import pickle

import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('../ml-model/model.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(data['values']))
    return jsonify(prediction=prediction.tolist()), 201


if __name__ == "__main__":
    app.run(debug=True)
