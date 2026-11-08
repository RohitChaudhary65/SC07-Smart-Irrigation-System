"""Create a reproducible ANN prediction from one saved validation row."""

from pathlib import Path

import pandas as pd

from src.product_predict import FEATURES, load_method, predict_one

ROOT = Path(__file__).resolve().parents[1]


def main():
    validation_path = ROOT / "data" / "processed" / "ann_validation.csv"
    if not validation_path.is_file():
        raise FileNotFoundError(f"Validation data not found: {validation_path}")

    sample = pd.read_csv(validation_path, nrows=1)
    missing = [name for name in FEATURES if name not in sample.columns]
    if missing:
        raise ValueError(f"Validation CSV is missing columns: {missing}")

    values = {name: sample.iloc[0][name] for name in FEATURES}
    model, scaler, _ = load_method()
    result = predict_one(model, scaler, values)

    output_path = ROOT / "data" / "reports" / "step5_reference_prediction.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([result]).to_csv(output_path, index=False)

    print(pd.DataFrame([result]).to_string(index=False))
    print(f"\nSaved reference result: {output_path}")


if __name__ == "__main__":
    main()
