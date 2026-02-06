import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.twin_predict import recommend_best_state

# Simulated current machine condition (M4)
current_state = {
    "wearLevel": 0.85,              # very worn
    "bearingWear": 0.8,
    "operatingHours": 7800,
    "ambientTemp": 38,
    "humidity": 0.82,
    "insulationResistance": 2.8,  
}

result = recommend_best_state(current_state)

print("===== DIGITAL TWIN OUTPUT =====")
for k, v in result.items():
    print(f"{k}: {v}")
