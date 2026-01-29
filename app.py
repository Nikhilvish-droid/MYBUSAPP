from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('bus_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract features from request
    features = [
        int(data['route']),
        int(data['hour']),
        int(data['day']),
        int(data['weather'])
    ]
    
    prediction = model.predict([features])
    delay = round(prediction[0], 2)
    
    return jsonify({'prediction': delay})

if __name__ == '__main__':
    app.run(debug=True)