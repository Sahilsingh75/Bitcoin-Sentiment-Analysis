# Bitcoin Sentiment Analysis

This project applies Natural Language Processing (NLP) techniques to analyze public sentiment related to Bitcoin. Using sentiment analysis, we aim to understand how people's opinions, extracted from text data, correlate with Bitcoin price trends.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [License](#license)

## Project Overview

The Bitcoin Sentiment Analysis project explores how public sentiment about Bitcoin is reflected in news articles, social media posts, or other textual data. The project leverages Python-based NLP libraries like `TextBlob` to classify sentiments as positive, neutral, or negative.

## Features

- **Sentiment Analysis**: Classifies the sentiment of Bitcoin-related text data as positive, negative, or neutral.
- **Data Visualization**: Visualizes sentiment trends over time using `matplotlib`.
- **Text Preprocessing**: Cleans raw text data, including removing unwanted characters using regular expressions (`re`).
- **Natural Language Processing**: Utilizes `TextBlob` to compute sentiment polarity and subjectivity.

## Installation

### Prerequisites
Ensure you have Python installed (preferably version 3.x).

### Step-by-step Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Sahilsingh75/Bitcoin-Sentiment-Analysis.git
   cd Bitcoin-Sentiment-Analysis

2. Create a virtual environment
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use: venv\Scripts\activate
  ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Jupyter notebook:
   ```bash
   jupyter notebook bitcoin-sentiment-analysis.ipynb
## Usage
Once you have set up the environment and installed the necessary dependencies, open the Jupyter notebook to explore the Bitcoin sentiment analysis workflow.

##Steps:
Load the text dataset (news articles, tweets, or any text related to Bitcoin).
Preprocess the text (cleaning and tokenization).
Use TextBlob to classify the sentiment of each text entry.
Visualize the results with matplotlib to observe sentiment trends over time.

## Results
This analysis helps in identifying trends in public sentiment surrounding Bitcoin. Visualizations generated from the notebook include:
Sentiment Analysis Scatter Plot: A scatter plot showing the relationship between polarity (how positive/negative a sentiment is) and subjectivity (how subjective/objective the sentiment is) for 2000 data points.
Sentiment Count Bar Chart: A bar chart displaying the count of Positive, Neutral, and Negative sentiments.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
