# src/data_visualization.py
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_word_cloud(topic_idx, words):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Topic {topic_idx}')
    plt.savefig(f'./results/topic_{topic_idx}_wordcloud.png')
    plt.show()

if __name__ == "__main__":
    # Load topics from CSV
    topics_df = pd.read_csv('./results/topics.csv', index_col=0)

    # Plot word clouds for each topic
    for topic_idx, row in topics_df.iterrows():
        words = row['Top Words']
        plot_word_cloud(topic_idx, words)
