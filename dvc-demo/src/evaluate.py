import os
import pickle
import json
import pandas as pd
from sklearn.metrics import accuracy_score


# Load the trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the test data
test_df = pd.read_csv('data/prepared/test.csv')

X_test = test_df['text']
y_test = test_df['sentiment']

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

# Save metrics to a JSON file
metrics = {'accuracy': accuracy}
with open('metrics.json', 'w') as f:
    json.dump(metrics, f, indent=4)

print(f'Model accuracy: {accuracy}')
print('Metrics saved to metrics.json')
