def predict_sentiment(text):
    # Placeholder logic
    if any(w in text.lower() for w in ["fear", "hate", "panic"]):
        return "Negative"
    elif any(w in text.lower() for w in ["love", "happy", "hope"]):
        return "Positive"
    else:
        return "Neutral"
