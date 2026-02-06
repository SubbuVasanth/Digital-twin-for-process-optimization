import pandas as pd
from src.config import INPUT_COLS, OUTPUT_COLS

def prepare_training_data():
    df = pd.read_csv("data/raw/digital-twin-data.csv")
    df = df.dropna().reset_index(drop=True)

    # Define "good operating states"
    good_df = df[
        (df["motorTemp"] < 90) &
        (df["efficiency"] > 0.80) &
        (df["wearLevel"] < 0.85)
    ]

    X = good_df[INPUT_COLS]
    y = good_df[OUTPUT_COLS]

    X.to_csv("data/processed/X.csv", index=False)
    y.to_csv("data/processed/y.csv", index=False)

    print("✅ Feature engineering completed")
