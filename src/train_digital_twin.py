import pandas as pd
import joblib
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor
import os
import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.feature_engineering import prepare_training_data

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# 1️⃣ Create X and y if not present
X_path = "data/processed/X.csv"
y_path = "data/processed/y.csv"

if not os.path.exists(X_path) or not os.path.exists(y_path):
    print("🔧 Preparing training data...")
    prepare_training_data()

# 2️⃣ Load training data
X = pd.read_csv(X_path)
y = pd.read_csv(y_path)

# 3️⃣ Train model
model = MultiOutputRegressor(
    XGBRegressor(
        n_estimators=400,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )
)

model.fit(X, y)

# 4️⃣ Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/digital_twin_xgb.pkl")

print("✅ Digital Twin model trained successfully")
