# SC07 Smart Irrigation System - Data Quality Report

## 1. Dataset Overview

The Step-2 pipeline starts from the Step-1 starter dataset:

- File: `data/sample_input.csv`
- Records before cleaning: 20
- Number of columns: 7

## 2. Input Fields

The dataset contains the following fields:

- `sample_id`
- `soil_moisture_pct`
- `temperature_c`
- `humidity_pct`
- `rainfall_mm`
- `soil_ph`
- `irrigation_target`

## 3. Cleaning

The Step-2 pipeline checks for and removes exact duplicate records.

- Records before cleaning: 20
- Duplicate records removed: 0
- Records after cleaning: 20

No missing-value imputation was required for the current starter dataset because the required fields contain no missing values.

## 4. Validation

The prepared dataset was validated for:

- Required column names
- Missing values
- Unique `sample_id` values
- Soil moisture range: 0-100
- Temperature range: -10 to 60 degrees C
- Humidity range: 0-100
- Rainfall range: 0-500 mm
- Soil pH range: 0-14
- `irrigation_target` values: 0 or 1

Validation result:

**PASS**

## 5. Processing

The cleaned dataset is saved as:

`data/processed/cleaned_data.csv`

The preparation process is implemented in:

`src/prepare_data.py`

## 6. Reproducibility

The data preparation pipeline is implemented as a Python script so that the cleaning and validation process can be repeated.

## 7. Limitations

The current dataset contains only 20 starter observations and represents development/test values. It should not be treated as agricultural or regulatory standards.

Further Step-2 data/scenario preparation may be required according to the final project methodology.
