import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_URL = "https://raw.githubusercontent.com/RohitChaudhary65/SC07-Smart-Irrigation-System/step-2-data-pipeline/data/sample_input.csv"

FEATURES = [
    "soil_moisture_pct",
    "temperature_c",
    "humidity_pct",
    "rainfall_mm",
    "soil_ph"
]

df = pd.read_csv(DATA_URL)
X = df[FEATURES]
y = df["irrigation_target"]

from sklearn.model_selection import train_test_split

_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = joblib.load(BASE_DIR / "models" / "ann_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")

ann_predictions = model.predict(scaler.transform(X_test))

baseline_predictions = (X_test["soil_moisture_pct"] < 30).astype(int)

results = pd.DataFrame({
    "actual": y_test.to_numpy(),
    "baseline_prediction": baseline_predictions.to_numpy(),
    "ann_prediction": ann_predictions
})

baseline_accuracy = accuracy_score(y_test, baseline_predictions)
ann_accuracy = accuracy_score(y_test, ann_predictions)

results_dir = BASE_DIR / "results"
results_dir.mkdir(exist_ok=True)

results.to_csv(results_dir / "baseline_comparison.csv", index=False)

comparison = {
    "test_samples": len(y_test),
    "metric": "accuracy",
    "baseline_accuracy": float(baseline_accuracy),
    "ann_accuracy": float(ann_accuracy),
    "difference_percentage_points": float((ann_accuracy - baseline_accuracy) * 100),
    "baseline_rule": "Irrigation ON if soil moisture < 30%; otherwise OFF"
}

with open(results_dir / "baseline_metrics.json", "w") as file:
    json.dump(comparison, file, indent=4)

print("SC07 Baseline vs ANN")
print("--------------------")
print(f"Test samples: {len(y_test)}")
print(f"Baseline accuracy: {baseline_accuracy:.2f}")
print(f"ANN accuracy: {ann_accuracy:.2f}")
print(f"Difference: {(ann_accuracy - baseline_accuracy) * 100:.1f} percentage points")
print("\nComparison saved to results/baseline_comparison.csv")
print("Metrics saved to results/baseline_metrics.json")
print("\nConfusion matrix (baseline):")
print(confusion_matrix(y_test, baseline_predictions))

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.bar(
    ["Baseline", "ANN"],
    [baseline_accuracy * 100, ann_accuracy * 100]
)
plt.ylabel("Accuracy (%)")
plt.title("Baseline vs ANN Accuracy")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(results_dir / "baseline_vs_ann.png")
plt.close()

print("Graph saved to results/baseline_vs_ann.png")