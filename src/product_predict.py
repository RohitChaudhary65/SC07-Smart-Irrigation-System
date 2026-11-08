"""SC07 Product V1 inference for the saved ANN and Step 4 baseline."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "ann_model.pkl"
SCALER_PATH = ROOT / "models" / "scaler.pkl"
META_PATH = ROOT / "models" / "metadata.json"

FEATURES = [
    "soil_moisture_pct",
    "temperature_c",
    "humidity_pct",
    "rainfall_mm",
    "soil_ph",
]

# Starter-project validation limits from the repository data dictionary.
# They are input checks, not crop-specific agronomic recommendations.
LIMITS = {
    "soil_moisture_pct": (0.0, 100.0),
    "temperature_c": (-10.0, 60.0),
    "humidity_pct": (0.0, 100.0),
    "rainfall_mm": (0.0, 500.0),
    "soil_ph": (0.0, 14.0),
}

LABELS = {
    0: "Irrigation not required (model class 0)",
    1: "Irrigation required (model class 1)",
}


def validate_inputs(values: dict[str, Any]) -> dict[str, float]:
    """Validate and return clean numeric values in the ANN's exact feature order."""
    if not isinstance(values, dict):
        raise ValueError("Input must be provided as a dictionary.")

    clean: dict[str, float] = {}
    errors: list[str] = []

    for feature in FEATURES:
        raw = values.get(feature)
        if raw is None or str(raw).strip() == "":
            errors.append(f"{feature}: value is required.")
            continue

        try:
            number = float(raw)
        except (TypeError, ValueError):
            errors.append(f"{feature}: enter a valid number.")
            continue

        if not math.isfinite(number):
            errors.append(f"{feature}: value must be finite (not NaN or infinity).")
            continue

        low, high = LIMITS[feature]
        if not low <= number <= high:
            errors.append(f"{feature}: enter a value from {low:g} to {high:g}.")
            continue

        clean[feature] = number

    if errors:
        raise ValueError("\n".join(errors))

    return clean


def load_method():
    """Load the existing Step 3 ANN, scaler and metadata; never train here."""
    for path in (MODEL_PATH, SCALER_PATH, META_PATH):
        if not path.is_file():
            raise FileNotFoundError(
                f"Required Step 3 artifact is missing: {path.relative_to(ROOT)}. "
                "Restore it from the completed Step 3/4 branch."
            )

    metadata = json.loads(META_PATH.read_text(encoding="utf-8"))
    if metadata.get("features") != FEATURES:
        raise ValueError(
            "Feature order in models/metadata.json does not match Product V1."
        )
    if metadata.get("target") != "irrigation_target":
        raise ValueError("Unexpected target in models/metadata.json.")

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    if getattr(model, "n_features_in_", None) != len(FEATURES):
        raise ValueError("Saved ANN does not accept the expected five features.")
    if getattr(scaler, "n_features_in_", None) != len(FEATURES):
        raise ValueError("Saved scaler does not accept the expected five features.")

    scaler_features = list(getattr(scaler, "feature_names_in_", []))
    if scaler_features and scaler_features != FEATURES:
        raise ValueError("Saved scaler feature names/order do not match Product V1.")

    return model, scaler, metadata


def predict_one(model, scaler, values: dict[str, Any]) -> dict[str, Any]:
    """Run one prediction with the saved scaler and saved ANN."""
    clean = validate_inputs(values)
    frame = pd.DataFrame([[clean[name] for name in FEATURES]], columns=FEATURES)
    scaled = scaler.transform(frame)
    prediction = int(model.predict(scaled)[0])

    if prediction not in LABELS:
        raise ValueError(f"Saved ANN returned an unsupported class: {prediction}")

    # Step 4 baseline, retained exactly: irrigation ON below 30% soil moisture.
    baseline_prediction = int(clean["soil_moisture_pct"] < 30)

    if prediction == baseline_prediction:
        comparison = "ANN and baseline agree on this input."
    else:
        comparison = (
            "ANN and baseline differ on this input. Review the measurements "
            "and project limitations before acting."
        )

    return {
        **clean,
        "ann_prediction": prediction,
        "ann_label": LABELS[prediction],
        "baseline_prediction": baseline_prediction,
        "baseline_label": LABELS[baseline_prediction],
        "methods_agree": prediction == baseline_prediction,
        "comparison": comparison,
        "notice": (
            "Decision-support demonstration only. The current dataset and small "
            "Step 3 test split do not establish field accuracy. Check crop, soil, "
            "weather and local irrigation requirements before applying water."
        ),
    }
