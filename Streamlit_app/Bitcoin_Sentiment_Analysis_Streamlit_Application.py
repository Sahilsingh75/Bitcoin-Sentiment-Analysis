#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import re

# App title and description
st.title("Tweet Sentiment Analyzer")
st.write("Upload your tweet dataset (CSV) to analyze sentiment. Select the column containing tweet text, and optionally a date column for time-series analysis.")

# File uploader
uploaded_file = st.file_uploader("Upload your tweet dataset (CSV)", type="csv")

if uploaded_file is not None:
    # Load the dataset
    try:
        df = pd.read_csv(uploaded_file, low_memory=False)
        st.write("Dataset loaded successfully. Preview:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        st.stop()

    # Select column for tweet text
    st.subheader("Select Columns")
    text_column = st.selectbox("Select the column containing tweet text:", options=df.columns)
    
    # Validate text column
    if not df[text_column].dtype == "object":
        st.warning("Selected column does not appear to contain text data. Please select a different column.")
    
    # Optional date column selection
    date_column = st.selectbox("Select the column containing date/time (optional, for time-series plot):", 
                              options=["None"] + list(df.columns))

    # Clean tweet text
    def clean_tweet_text(text):
        if not isinstance(text, str):
            return ""
        text = re.sub(r"#\w+|@\w+|http\S+|[^\w\s]|\s+", " ", text)  # Remove hashtags, mentions, URLs, punctuation
        return text.strip().lower()

    # Sentiment analysis functions
    def calculate_polarity(text):
        try:
            return TextBlob(text).sentiment.polarity
        except:
            return 0.0

    def determine_sentiment(polarity):
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        return "Neutral"

    # Process the data
    st.subheader("Sentiment Analysis Results")
    df['cleaned_text'] = df[text_column].apply(clean_tweet_text)
    df['polarity_score'] = df['cleaned_text'].apply(calculate_polarity)
    df['sentiment_label'] = df['polarity_score'].apply(determine_sentiment)

    # Display processed data
    st.write("Processed dataset with sentiment:")
    st.dataframe(df[[text_column, 'sentiment_label', 'polarity_score']].head())

    # Sentiment distribution pie chart
    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots(figsize=(6, 6))
    sentiment_counts = df['sentiment_label'].value_counts()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['#4CAF50', '#B0BEC5', '#F44336'])
    plt.title("Sentiment Distribution of Tweets")
    st.pyplot(fig)

    # Time-series plot (if date column is provided)
    if date_column != "None":
        st.subheader("Sentiment Trend Over Time")
        try:
            df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
            if df[date_column].isna().all():
                st.warning("Date column contains invalid dates. Time-series plot cannot be generated.")
            else:
                daily_sentiment = df.groupby(df[date_column].dt.date)['polarity_score'].mean().rolling(window=3).mean()
                fig, ax = plt.subplots(figsize=(8, 4))
                sns.lineplot(x=daily_sentiment.index, y=daily_sentiment.values, color='#2196F3', ax=ax)
                plt.title("Smoothed Sentiment Trend (3-Day Moving Average)")
                plt.xlabel("Date")
                plt.ylabel("Average Polarity")
                plt.grid(True)
                st.pyplot(fig)
        except Exception as e:
            st.warning(f"Error generating time-series plot: {e}")

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(f"Average Polarity: {df['polarity_score'].mean():.3f}")
    st.write(f"Sentiment Breakdown:\n{df['sentiment_label'].value_counts().to_string()}")

