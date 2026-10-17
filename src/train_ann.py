import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]

DATA_URL = (
    "https://raw.githubusercontent.com/RohitChaudhary65/"
    "SC07-Smart-Irrigation-System/step-2-data-pipeline/"
    "data/sample_input.csv"
)

FEATURES = [
    "soil_moisture_pct",
    "temperature_c",
    "humidity_pct",
    "rainfall_mm",
    "soil_ph",
]

TARGET = "irrigation_target"


df = pd.read_csv(DATA_URL)

X = df[FEATURES]
y = df[TARGET]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=500,
    random_state=42
)

model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("SC07 Smart Irrigation System - ANN")
print("-----------------------------------")
print("Dataset shape:", df.shape)
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Test Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


models_dir = ROOT / "models"
results_dir = ROOT / "results"

models_dir.mkdir(exist_ok=True)
results_dir.mkdir(exist_ok=True)


joblib.dump(model, models_dir / "ann_model.pkl")
joblib.dump(scaler, models_dir / "scaler.pkl")


metadata = {
    "project": "SC07 Smart Irrigation System",
    "model": "MLPClassifier",
    "hidden_layers": [16, 8],
    "activation": "relu",
    "solver": "adam",
    "max_iter": 500,
    "random_state": 42,
    "features": FEATURES,
    "target": TARGET,
    "test_accuracy": float(accuracy),
    "training_samples": len(X_train),
    "testing_samples": len(X_test)
}

with open(models_dir / "metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)


predictions = pd.DataFrame({
    "actual": y_test.to_numpy(),
    "predicted": y_pred
})

predictions.to_csv(
    results_dir / "ann_predictions.csv",
    index=False
)

print("\nModel, scaler, metadata and predictions saved successfully.")