import os
import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Create model directory if it doesn't exist
os.makedirs('model', exist_ok=True)

# Read processed data
df = pd.read_csv('data/prepared/train.csv')

X = df['text']
y = df['sentiment']

# Create a scikit-learn pipeline
text_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression()),
])

# Train the model
text_clf.fit(X, y)

# Save the trained model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(text_clf, f)

print('Model trained and saved to model/model.pkl')
