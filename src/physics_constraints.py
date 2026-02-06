def safe_rpm(base_rpm: float, wear: float, bearing_wear: float) -> float:
    """
    Compute wear-adaptive safe RPM.
    wear, bearing_wear ∈ [0, 1]
    """
    degradation = max(wear, bearing_wear)
    return base_rpm * (1 - 0.6 * degradation)


def max_motor_temp(ambient: float, cooling_eff: float = 0.8) -> float:
    """
    Maximum allowable motor temperature based on environment & cooling.
    """
    return ambient + 70 * cooling_eff


def max_load(wear: float) -> float:
    """
    Maximum load capacity reduces as wear increases.
    """
    return max(0.3, 1.0 - 0.5 * wear)


def max_power(insulation_resistance: float) -> float:
    """
    Electrical safety constraint.
    Lower insulation → lower safe power.
    """
    if insulation_resistance < 3.0:
        return 4.5
    elif insulation_resistance < 5.0:
        return 5.2
    return 6.0
