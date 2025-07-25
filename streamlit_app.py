import streamlit as st
from fake_news_detector import predict_fake_news
from sentiment_detector import predict_sentiment
from preprocess import preprocess_text

st.title("JanSatya - Real ML-Based Fake News & Sentiment Detector")
user_input = st.text_area("Enter a news or social media message")

if st.button("Analyze"):
    cleaned = preprocess_text(user_input)
    sentiment = predict_sentiment(cleaned)
    fake_status = predict_fake_news(cleaned)
    st.success(f"Sentiment: {sentiment}")
    st.warning(f"Fake News Detection: {fake_status}")
