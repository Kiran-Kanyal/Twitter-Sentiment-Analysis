from flask import Flask, request, jsonify, render_template
from predict import load_model_and_vectorizer, predict_user_input

app = Flask(__name__)

# Load model and vectorizer
model_path = 'trained_model.sav'
vectorizer_path = 'vectorizer.pkl'
model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']
    sentiment = predict_user_input(text, model, vectorizer)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
