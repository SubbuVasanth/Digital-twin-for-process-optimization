import pandas as pd

df = pd.read_csv("data/raw/digital-twin-data.csv")
df = df.dropna().reset_index(drop=True)

df.to_csv("data/processed/train.csv", index=False)
print("✅ Data ingestion complete")
