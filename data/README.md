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
