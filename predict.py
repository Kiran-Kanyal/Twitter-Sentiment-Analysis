import pickle

def load_model_and_vectorizer(model_path, vectorizer_path):
    """Load the model and vectorizer from specified paths."""
    with open(model_path, 'rb') as model_file, open(vectorizer_path, 'rb') as vectorizer_file:
        model = pickle.load(model_file)
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

def predict_user_input(user_input, model, vectorizer):
    """Predict sentiment of the user input."""
    # Transform the user input using the loaded vectorizer
    user_input_transformed = vectorizer.transform([user_input])

    # Predict using the loaded model
    prediction = model.predict(user_input_transformed)

    # Return prediction as a string ('Negative Tweet' or 'Positive Tweet')
    sentiment = 'Negative Tweet' if prediction[0] == 0 else 'Positive Tweet'
    return sentiment

# Example usage
if __name__ == "__main__":
    model_path = 'trained_model.sav'
    vectorizer_path = 'vectorizer.pkl'

    # Load model and vectorizer
    model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)

    # Example user input
    user_input = "This is a great product, I really loved it!"
    sentiment = predict_user_input(user_input, model, vectorizer)
    print(f'Prediction: {sentiment}')
