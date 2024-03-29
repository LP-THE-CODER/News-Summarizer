import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

# Download NLTK data
nltk.download('punkt')

def summarize():
    st.markdown("<h1 style='text-align: center; color: #0072B5;'>📰 News Summarizer</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #333;'>Summarize news articles with ease!</h3>", unsafe_allow_html=True)
    st.markdown("---")

    url = st.text_area("Paste the URL of the news article here:")
    if st.button("Summarize", key="summarize_button"):
        if url.strip() == "":
            st.warning("Please enter a valid URL.")
            return

        st.markdown("---")
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        st.subheader("Title:")
        st.write(article.title)

        st.subheader("Author(s):")
        st.write(article.authors)

        st.subheader("Publishing Date:")
        st.write(article.publish_date)

        st.subheader("Summary:")
        st.write(article.summary)

        analysis = TextBlob(article.text)
        polarity = analysis.polarity
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        st.subheader("Sentiment Analysis:")
        st.write(f"Polarity: {polarity:.2f}, Sentiment: {sentiment}")

        st.markdown("---")

summarize()

# Footer
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>🚀 Connect with me on LinkedIn and GitHub!</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><a href='https://www.linkedin.com/in/morla-lakshmi-prasanna-824072255' target='_blank'><img src='https://img.icons8.com/color/48/000000/linkedin.png'/></a>&nbsp;&nbsp;&nbsp;<a href='https://github.com/LP-THE-CODER' target='_blank'><img src='https://img.icons8.com/color/48/000000/github--v1.png'/></a></p>", unsafe_allow_html=True)
