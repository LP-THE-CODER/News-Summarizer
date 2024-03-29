import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

# Download NLTK data
nltk.download('punkt')

# Function to summarize news articles
def summarize():
    # Title and description
    st.markdown("<h1 style='text-align: center; color: #0072B5;'>📰 News Summarizer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Summarize news articles with ease!</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Input URL
    url = st.text_input("Enter the URL of the news article:", "")

    # Summarization button
    if st.button("Summarize", key="summarize_button"):
        if url.strip() == "":
            st.warning("Please enter a valid URL.")
            return

        st.markdown("---")
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Display article information
        st.subheader("Title:")
        st.write(article.title)

        st.subheader("Author(s):")
        st.write(article.authors)

        st.subheader("Publishing Date:")
        st.write(article.publish_date)

        st.subheader("Summary:")
        st.write(article.summary)

        # Sentiment analysis
        analysis = TextBlob(article.text)
        polarity = analysis.polarity
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        st.subheader("Sentiment Analysis:")
        st.write(f"Polarity: {polarity:.2f}, Sentiment: {sentiment}")

        st.markdown("---")

# Run the summarization function
summarize()

# Footer with social media links
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>🚀 Connect with <span style='color: #FF5733; font-family: Arial, sans-serif;'>Lakshmi Prasanna Morla</span> on LinkedIn and GitHub!</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><a href='https://www.linkedin.com/in/morla-lakshmi-prasanna-824072255' target='_blank'><img src='https://img.icons8.com/color/96/000000/linkedin-circled--v3.png' style='margin-right: 20px;'/></a><a href='https://github.com/LP-THE-CODER' target='_blank'><img src='https://img.icons8.com/color/96/000000/github--v1.png' style='margin-left: 20px;'/></a></p>", unsafe_allow_html=True)
