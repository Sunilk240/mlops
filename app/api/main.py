from flask import Flask, request, jsonify
import joblib
import os
import json

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('app/model/saved/model.joblib')
vectorizer = joblib.load('app/model/saved/vectorizer.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Handle invalid JSON
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        try:
            data = request.get_json()
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid JSON format'}), 400

        text = data.get('text', '')

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)[0]
        probability = model.predict_proba(text_vectorized)[0]

        return jsonify({
            'prediction': int(prediction),
            'sentiment': 'positive' if prediction == 1 else 'negative',
            'confidence': float(max(probability))
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/version', methods=['GET'])
def version():
    return jsonify({'version': '1.0.0'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 