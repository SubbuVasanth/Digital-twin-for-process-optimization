import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.physics_constraints import (
    safe_rpm,
    max_motor_temp,
    max_load,
    max_power
)

def apply_physics_constraints(current: dict, proposed: dict) -> dict:
    """
    Apply physics & safety constraints to ML-proposed state.
    """

    # 1️⃣ RPM constraint (wear-adaptive)
    rpm_limit = safe_rpm(
        base_rpm=2000,
        wear=current["wearLevel"],
        bearing_wear=current["bearingWear"]
    )
    proposed["optimal_rpm"] = min(proposed["optimal_rpm"], rpm_limit)

    # 2️⃣ Thermal constraint
    temp_limit = max_motor_temp(
        ambient=current["ambientTemp"],
        cooling_eff=current.get("coolingEfficiency", 0.8)
    )
    proposed["optimal_motorTemp"] = min(
        proposed["optimal_motorTemp"], temp_limit
    )

    # 3️⃣ Load constraint
    proposed["optimal_loadWeight"] = min(
        proposed["optimal_loadWeight"],
        max_load(current["wearLevel"])
    )

    # 4️⃣ Power constraint
    proposed["optimal_powerConsumption"] = min(
        proposed["optimal_powerConsumption"],
        max_power(current["insulationResistance"])
    )

    return proposed
