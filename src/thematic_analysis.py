# src/thematic_analysis.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def display_topics(model, feature_names, num_top_words):
    topics = {}
    for topic_idx, topic in enumerate(model.components_):
        topics[f"Topic {topic_idx}"] = " ".join([feature_names[i] for i in topic.argsort()[:-num_top_words - 1:-1]])
    return topics

if __name__ == "__main__":
    feedback_df = pd.read_csv('./data/cleaned_feedback.csv')

    # Vectorize the cleaned text
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(feedback_df['CleanedFeedbackText'])

    # Apply LDA for topic modeling
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(tfidf_matrix)

    num_top_words = 10
    tfidf_feature_names = vectorizer.get_feature_names_out()
    topics = display_topics(lda, tfidf_feature_names, num_top_words)

    # Save topics to a CSV file
    topics_df = pd.DataFrame.from_dict(topics, orient='index', columns=['Top Words'])
    topics_df.to_csv('./results/topics.csv')
