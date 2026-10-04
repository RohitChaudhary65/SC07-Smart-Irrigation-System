# SC07 Smart Irrigation System - Data Quality Report

## 1. Dataset Overview

The Step-2 pipeline starts from the Step-1 starter dataset:

- File: `data/sample_input.csv`
- Records before cleaning: 20
- Number of columns: 7

The Step-2 pipeline also generates reproducible irrigation scenarios for the hybrid Fuzzy Logic + ANN approach.

- Generated scenario file: `data/processed/irrigation_scenarios.csv`
- Number of generated scenarios: 10,000
- Random seed: 42

## 2. Input Fields

The dataset contains the following fields:

- `sample_id`
- `soil_moisture_pct`
- `temperature_c`
- `humidity_pct`
- `rainfall_mm`
- `soil_ph`
- `irrigation_target`

Generated scenarios use:

- `scenario_id`
- `soil_moisture_pct`
- `temperature_c`
- `humidity_pct`
- `rainfall_mm`
- `soil_ph`
- `irrigation_target`

## 3. Cleaning

The Step-2 pipeline checks for and removes exact duplicate records.

For the starter dataset:

- Records before cleaning: 20
- Duplicate records removed: 0
- Records after cleaning: 20

No missing-value imputation was required for the current starter dataset because the required fields contain no missing values.

## 4. Validation

The prepared data was validated for:

- Required column names
- Missing values
- Unique identifiers
- Soil moisture range: 0-100
- Temperature range: -10 to 60 degrees C
- Humidity range: 0-100
- Rainfall range: 0-500 mm
- Soil pH range: 0-14
- `irrigation_target` values: 0 or 1

Validation result:

**PASS**

## 5. Scenario Generation

The scenario-generation process is implemented in:

`src/generate_scenarios.py`

The generation process uses a fixed random seed of 42 to make the generated scenarios reproducible.

The generated scenarios contain:

- 10,000 valid scenarios
- Soil moisture values within 0-100%
- Temperature values within -10 to 60 degrees C
- Humidity values within 0-100%
- Rainfall values within 0-500 mm
- Soil pH values within 0-14
- Irrigation target values of 0 or 1

The generated scenarios are saved as:

`data/processed/irrigation_scenarios.csv`

## 6. Hybrid Project Preparation

The SC07 project uses a hybrid Fuzzy Logic + ANN approach.

### ANN

The prepared data will support reproducible training, validation, and testing of the ANN component.

### Fuzzy Logic

The scenario plan includes:

- Normal scenarios
- Boundary scenarios
- Stress scenarios
- Invalid scenarios for validation testing

Invalid scenarios are intended for validation testing and are not included as valid ANN training data.

## 7. Reproducibility

The data preparation process is implemented through Python scripts.

- `src/prepare_data.py` performs cleaning and validation.
- `src/generate_scenarios.py` generates reproducible irrigation scenarios.
- Random seed: 42.

## 8. Limitations

The original starter dataset contains only 20 observations and represents development/test values.

The generated scenarios are project-development scenarios and should not be treated as agricultural or regulatory standards.

Further project steps will be required for the final Fuzzy Logic and ANN implementation.
