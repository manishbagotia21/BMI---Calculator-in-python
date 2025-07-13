#!/usr/bin/env python3
"""
BMI Calculator – Lite
Author: Your Name
License: MIT
"""

from dataclasses import dataclass
from typing import Tuple

# ---------------------------------------
# Data classes and constants
# ---------------------------------------
@dataclass
class BMIResult:
    bmi: float
    category: str

_CATEGORIES: Tuple[Tuple[float, str], ...] = (
    (18.5, "Underweight"),
    (25.0, "Normal weight"),
    (30.0, "Overweight"),
    (float("inf"), "Obesity"),
)

# ---------------------------------------
# Core functions
# ---------------------------------------
def calc_bmi_metric(height_cm: float, weight_kg: float) -> BMIResult:
    """Return BMI (metric) and category."""
    bmi = weight_kg / ((height_cm / 100) ** 2)
    return BMIResult(round(bmi, 1), _classify(bmi))


def calc_bmi_imperial(height_ft: int, height_in: float, weight_lb: float) -> BMIResult:
    """Return BMI (imperial) and category."""
    total_inches = height_ft * 12 + height_in
    bmi = 703 * weight_lb / (total_inches ** 2)
    return BMIResult(round(bmi, 1), _classify(bmi))


def _classify(bmi: float) -> str:
    """Return the weight category for a given BMI."""
    for threshold, label in _CATEGORIES:
        if bmi < threshold:
            return label
    # Should never reach here
    return "Unknown"


# ---------------------------------------
# CLI helpers
# ---------------------------------------
def _prompt_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                raise ValueError
            return val
        except ValueError:
            print("  ✖ Please enter a positive number.")


def _main() -> None:
    print("=== BMI Calculator ===")
    mode = input("Choose units – [M]etric or [I]mperial? ").strip().lower()
    if mode == "i":
        ft = int(_prompt_float("Height - feet: "))
        inch = _prompt_float("         inches: ")
        lb = _prompt_float("Weight (pounds): ")
        result = calc_bmi_imperial(ft, inch, lb)
    else:
        cm = _prompt_float("Height (cm): ")
        kg = _prompt_float("Weight (kg): ")
        result = calc_bmi_metric(cm, kg)

    print(f"\nYour BMI is {result.bmi} → {result.category}\n")


# ---------------------------------------
# Entry point
# ---------------------------------------
if __name__ == "__main__":
    try:
        _main()
    except KeyboardInterrupt:
        print("\nBye!")
