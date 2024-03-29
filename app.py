import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

# Download NLTK data
nltk.download('punkt')

def summarize():
    url = st.text_area("URL")
    if st.button("Summarize"):
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        st.subheader("Title")
        st.text(article.title)

        st.subheader("Author")
        st.text(article.authors)

        st.subheader("Publishing Date")
        st.text(article.publish_date)

        st.subheader("Summary")
        st.text(article.summary)

        analysis = TextBlob(article.text)
        polarity = analysis.polarity
        sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
        st.subheader("Sentiment Analysis")
        st.text(f'Polarity: {polarity}, Sentiment: {sentiment}')

st.title("📰 News Summarizer 📝")

summarize()


# Footer
st.markdown("---")
st.markdown("🚀 Connect with me on [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/morla-lakshmi-prasanna-824072255) [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/LP-THE-CODER)")


