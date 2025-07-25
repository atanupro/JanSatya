import joblib
import os

# Load trained model and vectorizer (placeholders for real model files)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_fake_news(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return "Fake" if prediction == 1 else "Real"
