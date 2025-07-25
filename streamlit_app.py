import streamlit as st
from fake_news_detector import predict_fake_news
from sentiment_detector import predict_sentiment
from preprocess import preprocess_text

st.title("JanSatya - Fake News & Sentiment Detection")
user_input = st.text_area("Enter a message")

if st.button("Analyze"):
    text = preprocess_text(user_input)
    sentiment = predict_sentiment(text)
    fake_status = predict_fake_news(text)
    st.write(f"Sentiment: {sentiment}")
    st.write(f"Fake News Detection: {fake_status}")
