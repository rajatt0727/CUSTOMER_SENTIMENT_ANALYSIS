# src/sentiment_analysis.py
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

if __name__ == "__main__":
    feedback_df = pd.read_csv('./data/cleaned_feedback.csv')
    feedback_df['Sentiment'] = feedback_df['CleanedFeedbackText'].apply(get_sentiment)
    feedback_df.to_csv('./data/sentiment_feedback.csv', index=False)

    # Plot sentiment distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(feedback_df['Sentiment'], kde=True, bins=30, color='skyblue')
    plt.title('Sentiment Distribution of Customer Feedback')
    plt.savefig('./results/sentiment_distribution.png')
    plt.show()
