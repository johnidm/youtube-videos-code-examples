import os
import pandas as pd
from sklearn.model_selection import train_test_split
import yaml

# Load parameters
with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

prepare_params = params['prepare']
test_size = prepare_params['test_size']
random_state = prepare_params['random_state']

# Create directories if they don't exist
os.makedirs('data/prepared', exist_ok=True)

# Read processed data
df = pd.read_csv('data/processed/processed_data.csv')

# Split data into training and testing sets
X = df['text']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Save the split data
train_df = pd.DataFrame({'text': X_train, 'sentiment': y_train})
test_df = pd.DataFrame({'text': X_test, 'sentiment': y_test})

train_df.to_csv('data/prepared/train.csv', index=False)
test_df.to_csv('data/prepared/test.csv', index=False)

print('Data split into training and testing sets.')
