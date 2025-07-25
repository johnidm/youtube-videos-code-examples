import os
import pickle
import pandas as pd

# Create predictions directory if it doesn't exist
os.makedirs('data/predictions', exist_ok=True)

# Load the trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Read unseen data
unseen_df = pd.read_csv('data/unseen_data.csv')

# Make predictions
predictions = model.predict(unseen_df['text'])

# Save predictions
predictions_df = pd.DataFrame({'text': unseen_df['text'], 'sentiment': predictions})
predictions_df.to_csv('data/predictions/predictions.csv', index=False)

print('Predictions saved to data/predictions/predictions.csv')
