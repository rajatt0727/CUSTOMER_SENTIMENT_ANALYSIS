# completion_note.py
import pandas as pd

if __name__ == "__main__":
    feedback_df = pd.read_csv('data/sentiment_feedback.csv')
    
    num_feedback = len(feedback_df)
    avg_rating = feedback_df['Rating'].mean()
    sentiment_mean = feedback_df['Sentiment'].mean()
    sentiment_std = feedback_df['Sentiment'].std()
    
    with open('results/project_summary.txt', 'w') as file:
        file.write(f"Customer Feedback Analysis Project Summary\n")
        file.write(f"------------------------------------------\n")
        file.write(f"Total number of feedback entries: {num_feedback}\n")
        file.write(f"Average customer rating: {avg_rating:.2f}\n")
        file.write(f"Sentiment analysis - mean polarity: {sentiment_mean:.2f}\n")
        file.write(f"Sentiment analysis - standard deviation: {sentiment_std:.2f}\n")
        file.write(f"\nDetailed thematic analysis results are saved in the 'results/' directory as word cloud images.\n")
        file.write(f"\nRecommendations:\n")
        file.write(f"1. Focus on improving areas identified as negative in sentiment analysis.\n")
        file.write(f"2. Enhance services related to the most frequent terms in positive feedback.\n")
        file.write(f"3. Regularly monitor customer feedback to track changes in sentiment over time.\n")
