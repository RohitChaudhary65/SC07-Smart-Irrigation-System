import pandas as pd
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = PROJECT_ROOT / "data" / "sample_input.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def load_data():
    """Load the Step-1 starter dataset."""
    return pd.read_csv(RAW_DATA)


def inspect_data(df):
    """Display basic information about the dataset."""
    print("Dataset shape:", df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())


def clean_data(df):
    """Clean the dataset."""
    cleaned = df.copy()

    # Remove exact duplicate rows
    cleaned = cleaned.drop_duplicates()

    return cleaned


def main():
    df = load_data()

    print("Before cleaning:")
    inspect_data(df)

    cleaned_df = clean_data(df)

    print("\nAfter cleaning:")
    inspect_data(cleaned_df)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    output_file = PROCESSED_DIR / "cleaned_data.csv"
    cleaned_df.to_csv(output_file, index=False)

    print(f"\nCleaned data saved to: {output_file}")


if __name__ == "__main__":
    main()
