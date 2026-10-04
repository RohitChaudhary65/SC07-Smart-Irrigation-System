from pathlib import Path
import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_ROOT / "data" / "sample_input.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = PROCESSED_DIR / "cleaned_data.csv"


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


def load_data():
    """Load the Step-1 starter dataset."""
    return pd.read_csv(INPUT_FILE)


def clean_data(df):
    """Remove exact duplicate records."""
    before = len(df)

    cleaned = df.drop_duplicates().copy()

    after = len(cleaned)

    print(f"Records before cleaning: {before}")
    print(f"Duplicate records removed: {before - after}")
    print(f"Records after cleaning: {after}")

    return cleaned


def validate_data(df):
    """Validate the prepared dataset."""

    # Required columns
    assert list(df.columns) == REQUIRED_COLUMNS, (
        "Required columns do not match the expected data structure."
    )

    # Missing values
    assert df["sample_id"].notna().all(), (
        "sample_id contains missing values."
    )

    for col in NUMERIC_COLUMNS:
        assert df[col].notna().all(), (
            f"{col} contains missing values."
        )

    # Unique IDs
    assert df["sample_id"].is_unique, (
        "sample_id values must be unique."
    )

    # Data ranges
    assert df["soil_moisture_pct"].between(0, 100).all(), (
        "soil_moisture_pct must be 0-100."
    )

    assert df["temperature_c"].between(-10, 60).all(), (
        "temperature_c must be -10 to 60 degrees C."
    )

    assert df["humidity_pct"].between(0, 100).all(), (
        "humidity_pct must be 0-100."
    )

    assert df["rainfall_mm"].between(0, 500).all(), (
        "rainfall_mm must be 0-500 mm."
    )

    assert df["soil_ph"].between(0, 14).all(), (
        "soil_ph must be 0-14."
    )

    # Target validation
    assert df["irrigation_target"].isin([0, 1]).all(), (
        "irrigation_target must be 0 or 1."
    )

    print("VALIDATION PASSED")


def save_data(df):
    """Save cleaned and validated data."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Processed data saved to: {OUTPUT_FILE}")


def main():
    print("=== SC07 STEP-2 DATA PIPELINE ===")

    # 1. Load
    df = load_data()

    print(f"Input shape: {df.shape}")

    # 2. Clean
    cleaned_df = clean_data(df)

    # 3. Validate
    validate_data(cleaned_df)

    # 4. Save
    save_data(cleaned_df)

    print("=== PIPELINE COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()
