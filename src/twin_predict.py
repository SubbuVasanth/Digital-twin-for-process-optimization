import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.twin_constraints import apply_physics_constraints
import joblib
import pandas as pd

model = joblib.load("models/digital_twin_xgb.pkl")

def recommend_best_state(current_state):
    df = pd.DataFrame([current_state])
    raw_pred = model.predict(df)[0]

    proposed = {
        "optimal_rpm": raw_pred[0],
        "optimal_motorTemp": raw_pred[1],
        "optimal_loadWeight": raw_pred[2],
        "optimal_powerConsumption": raw_pred[3],
        "optimal_efficiency": raw_pred[4],
    }

    final_state = apply_physics_constraints(
        current_state,
        proposed
    )

    return final_state
