# src/generate_synthetic_data.py
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

def generate_synthetic_feedback(num_entries=1000):
    data = {
        'CustomerID': [fake.uuid4() for _ in range(num_entries)],
        'FeedbackDate': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_entries)],
        'FeedbackText': [fake.paragraph(nb_sentences=5) for _ in range(num_entries)],
        'Rating': np.random.randint(1, 6, num_entries)
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    feedback_df = generate_synthetic_feedback()
    feedback_df.to_csv('./data/raw_feedback.csv', index=False)
