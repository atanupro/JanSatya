def predict_sentiment(text):
    if any(word in text.lower() for word in ["hate", "fear", "panic"]):
        return "Negative"
    elif any(word in text.lower() for word in ["love", "hope", "happy"]):
        return "Positive"
    return "Neutral"
