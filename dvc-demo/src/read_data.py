import os

# Create directories if they don't exist
os.makedirs('data/processed', exist_ok=True)

# Read data, process it, and write to a new file
with open('data/data.txt', 'r') as f:
    content = f.read()

with open('data/processed/processed_data.txt', 'w') as f:
    f.write(content.upper())
