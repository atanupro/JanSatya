import streamlit as st
from fake_news_detector import predict_fake_news
from sentiment_detector import predict_sentiment
from preprocess import preprocess_text

st.title("JanSatya - Fake News & Sentiment Detector (ML Version)")
user_input = st.text_area("Enter a news/message:")

if st.button("Analyze"):
    cleaned = preprocess_text(user_input)
    sentiment = predict_sentiment(cleaned)
    fake_status = predict_fake_news(cleaned)
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Fake News Prediction:** {fake_status}")
