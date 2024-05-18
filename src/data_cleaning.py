# src/data_cleaning.py
import pandas as pd
import string

def clean_text(text):
    text = text.lower()  # Lowercase text
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

if __name__ == "__main__":
    feedback_df = pd.read_csv('./data/raw_feedback.csv')
    
    # Check for missing values
    if feedback_df.isnull().sum().any():
        feedback_df.dropna(inplace=True)

    feedback_df['CleanedFeedbackText'] = feedback_df['FeedbackText'].apply(clean_text)
    feedback_df.to_csv('./data/cleaned_feedback.csv', index=False)
