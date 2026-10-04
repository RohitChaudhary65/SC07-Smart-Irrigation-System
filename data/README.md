# Data folder

This folder contains the Step-1 starter dataset for the Smart Irrigation System.

- `sample_input.csv` is the inspectable 20-row starter set.
- The final committed dataset is corrected after the deliberate validation test.
- The data are development/test values and are not agricultural or regulatory standards.

- ## Step-2 Data Pipeline

The Step-2 pipeline will inspect, clean, validate, and prepare the data for the Smart Irrigation System.

The pipeline will include:

- Data inspection and quality checks
- Missing-value checks
- Duplicate-record checks
- Data-type validation
- Input-range validation
- Target/output validation
- Reproducible data preparation
- Processed data/scenario generation as required by the project
- A data quality report documenting the preparation and validation results

The Step-1 starter dataset is retained as the starting point for the Step-2 pipeline.

## Step-2 Hybrid Data and Scenario Plan

The SC07 project uses a hybrid approach combining Fuzzy Logic and Artificial Neural Network (ANN).

### ANN data preparation

The ANN pipeline will use the prepared irrigation dataset with the following input features:

- `soil_moisture_pct`
- `temperature_c`
- `humidity_pct`
- `rainfall_mm`
- `soil_ph`

The target variable is:

- `irrigation_target`

The ANN dataset will be cleaned, validated, and divided into reproducible training, validation, and test datasets.

### Fuzzy Logic scenario preparation

The Fuzzy Logic component will use reproducible irrigation scenarios based on:

- Soil moisture
- Temperature
- Humidity
- Rainfall
- Soil pH

Scenarios will include:

- Normal operating conditions
- Boundary conditions
- Stress conditions
- Invalid-input conditions for validation testing

### Step-2 data quality

The preparation process will document:

- Input data source
- Data fields and units
- Cleaning steps
- Validation rules
- Generated records/scenarios
- Data quality results
- Reproducibility information

The final Step-2 preparation will provide sufficient valid documented records/scenarios for the allocated capstone requirements.

## Fuzzy Logic Scenario Categories

The Fuzzy Logic component will use the following scenario categories:

### 1. Normal scenarios

Normal scenarios represent valid operating conditions within the defined input ranges.

### 2. Boundary scenarios

Boundary scenarios test values close to or at the defined limits of the input ranges.

Examples include:

- Soil moisture near 0% or 100%
- Temperature near -10°C or 60°C
- Humidity near 0% or 100%
- Rainfall near 0 mm or 500 mm
- Soil pH near 0 or 14

### 3. Stress scenarios

Stress scenarios represent valid but demanding environmental conditions, such as:

- Very low soil moisture
- High temperature with low humidity
- Low rainfall
- Combinations of dry soil and high environmental demand

### 4. Invalid scenarios

Invalid scenarios are used only for validation testing and are not included as valid ANN training data.

Examples include:

- Soil moisture below 0% or above 100%
- Temperature outside -10°C to 60°C
- Humidity outside 0% to 100%
- Rainfall below 0 mm or above 500 mm
- Soil pH outside 0 to 14
- Invalid irrigation target values

The scenario category and validation rules will be documented so that the scenario-generation process remains reproducible.
