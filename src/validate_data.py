import pandas as pd

REQUIRED_COLUMNS = [
    "sample_id",
    "soil_moisture_pct",
    "temperature_c",
    "humidity_pct",
    "rainfall_mm",
    "soil_ph",
    "irrigation_target",
]

NUMERIC_COLUMNS = [
    "soil_moisture_pct",
    "temperature_c",
    "humidity_pct",
    "rainfall_mm",
    "soil_ph",
    "irrigation_target",
]

def main():
    path = "data/sample_input.csv"
    df = pd.read_csv(path)

    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    assert list(df.columns) == REQUIRED_COLUMNS, "Required columns do not match the Data Dictionary."
    assert len(df) == 20, "Starter dataset must contain exactly 20 rows."
    assert df["sample_id"].notna().all(), "sample_id contains missing values."
    assert df["sample_id"].is_unique, "sample_id values must be unique."

    for col in NUMERIC_COLUMNS:
        assert df[col].notna().all(), f"{col} contains missing values."

    assert df["soil_moisture_pct"].between(0, 100).all(), "soil_moisture_pct must be 0–100."
    assert df["temperature_c"].between(-10, 60).all(), "temperature_c must be -10–60 °C."
    assert df["humidity_pct"].between(0, 100).all(), "humidity_pct must be 0–100."
    assert df["rainfall_mm"].between(0, 500).all(), "rainfall_mm must be 0–500 mm."
    assert df["soil_ph"].between(0, 14).all(), "soil_ph must be 0–14."
    assert df["irrigation_target"].isin([0, 1]).all(), "irrigation_target must be 0 or 1."

    print("STEP 1 DATA CHECK PASSED")

if __name__ == "__main__":
    main()
