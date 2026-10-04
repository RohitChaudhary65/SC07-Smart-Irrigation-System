from pathlib import Path
import random
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "irrigation_scenarios.csv"

RANDOM_SEED = 42
TOTAL_SCENARIOS = 10000


def classify_scenario(soil, temperature, humidity, rainfall, ph):
    """Classify a valid scenario for the Fuzzy Logic component."""

    # Stress: demanding irrigation conditions
    if (soil < 20 and rainfall < 10) or (
        temperature > 40 and humidity < 30
    ):
        return "stress"

    # Boundary: values close to defined input limits
    if (
        soil <= 5
        or soil >= 95
        or temperature <= -5
        or temperature >= 55
        or humidity <= 5
        or humidity >= 95
        or rainfall <= 5
        or rainfall >= 495
        or ph <= 1
        or ph >= 13
    ):
        return "boundary"

    return "normal"


def generate_scenarios():
    """Generate reproducible irrigation scenarios."""

    random.seed(RANDOM_SEED)

    scenarios = []

    for i in range(1, TOTAL_SCENARIOS + 1):

        soil_moisture = round(random.uniform(0, 100), 2)
        temperature = round(random.uniform(-10, 60), 2)
        humidity = round(random.uniform(0, 100), 2)
        rainfall = round(random.uniform(0, 500), 2)
        soil_ph = round(random.uniform(0, 14), 2)

        if soil_moisture < 35 and rainfall < 20:
            irrigation_target = 1
        else:
            irrigation_target = 0

        scenario_type = classify_scenario(
            soil_moisture,
            temperature,
            humidity,
            rainfall,
            soil_ph,
        )

        scenarios.append(
            {
                "scenario_id": f"SC07-{i:05d}",
                "soil_moisture_pct": soil_moisture,
                "temperature_c": temperature,
                "humidity_pct": humidity,
                "rainfall_mm": rainfall,
                "soil_ph": soil_ph,
                "irrigation_target": irrigation_target,
                "scenario_type": scenario_type,
            }
        )

    return pd.DataFrame(scenarios)


def validate_scenarios(df):
    """Validate generated scenarios."""

    assert len(df) == TOTAL_SCENARIOS
    assert df["scenario_id"].is_unique
    assert df["scenario_type"].isin(
        ["normal", "boundary", "stress"]
    ).all()

    assert df["soil_moisture_pct"].between(0, 100).all()
    assert df["temperature_c"].between(-10, 60).all()
    assert df["humidity_pct"].between(0, 100).all()
    assert df["rainfall_mm"].between(0, 500).all()
    assert df["soil_ph"].between(0, 14).all()
    assert df["irrigation_target"].isin([0, 1]).all()

    assert df.isnull().sum().sum() == 0

    print("SCENARIO VALIDATION PASSED")
    print("\nScenario type counts:")
    print(df["scenario_type"].value_counts())


def save_scenarios(df):
    """Save generated scenarios."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nScenarios saved to: {OUTPUT_FILE}")


def main():
    print("=== SC07 SCENARIO GENERATION ===")

    df = generate_scenarios()

    print(f"Generated scenarios: {len(df)}")

    validate_scenarios(df)
    save_scenarios(df)

    print("=== SCENARIO GENERATION COMPLETED ===")


if __name__ == "__main__":
    main()
