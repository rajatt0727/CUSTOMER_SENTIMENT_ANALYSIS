# src/exploratory_data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    feedback_df = pd.read_csv('./data/cleaned_feedback.csv')

    # Distribution of ratings
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Rating', data=feedback_df, palette='viridis', hue='Rating', legend=False)
    plt.title('Distribution of Customer Ratings')
    plt.savefig('./results/rating_distribution.png')
    plt.show()

    # Feedback over time
    feedback_df['FeedbackDate'] = pd.to_datetime(feedback_df['FeedbackDate'])
    feedback_df.set_index('FeedbackDate', inplace=True)
    feedback_df['Rating'].resample('ME').mean().plot(figsize=(14, 7), title='Average Monthly Ratings')
    plt.savefig('./results/average_monthly_ratings.png')
    plt.show()
