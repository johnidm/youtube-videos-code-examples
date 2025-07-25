import os
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

df_raw = pd.read_csv("data/data.csv", sep=",")

df_raw["text"] = df_raw["text"].str.upper()
df_raw.to_csv("data/processed/processed_data.csv", index=False)

print("Processed data saved to data/processed/processed_data.csv")
