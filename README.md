# SC07 — Smart Irrigation System

## Project Overview

The **Smart Irrigation System** is a Soft Computing project planned to use **Fuzzy Logic + Artificial Neural Network (ANN)** to support irrigation decisions from environmental and soil conditions.

### Intended user
A farmer, gardener, or irrigation operator who needs a simple recommendation about whether irrigation is needed and an indicative irrigation level.

### Step-1 scope
Project Step 1 establishes the project contract, data dictionary, starter dataset, baseline logic, local data validation, and Product V1 sketch. The final Fuzzy + ANN implementation is planned for a later project step.

## Data Dictionary

| Field | Meaning | Type / Unit | Starter constraint |
|---|---|---|---|
| `sample_id` | Unique observation identifier | String | Must be unique |
| `soil_moisture_pct` | Soil moisture level | Numeric / % | 0–100 |
| `temperature_c` | Ambient temperature | Numeric / °C | -10–60 |
| `humidity_pct` | Relative humidity | Numeric / % | 0–100 |
| `rainfall_mm` | Recent rainfall amount | Numeric / mm | 0–500 |
| `soil_ph` | Soil acidity/alkalinity indicator | Numeric / pH | 0–14 |
| `irrigation_target` | Starter target for irrigation decision | Integer / 0 or 1 | 0 = No irrigation, 1 = Irrigation needed |

## Dataset notes

- `data/sample_input.csv` contains 20 inspectable starter observations.
- The Step-1 validation exercise uses a deliberate missing-value test before the final corrected dataset is committed.
- The values are project starter data for development/testing; they are not presented as agricultural or regulatory standards.

## Planned methods

### Baseline
A transparent threshold/rule-based decision is used as the comparison benchmark.

### M1 Soft Computing method
A combined **Fuzzy Logic + ANN** approach is planned:
1. Fuzzy logic will represent linguistic irrigation conditions such as dry/moist soil and low/high environmental demand.
2. ANN will learn a data-driven relationship between the sensor features and the irrigation target.
3. The final product will compare the baseline and Soft Computing result and expose validation/status information.

## Repository structure

```text
SC07-Smart-Irrigation-System/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── sample_input.csv
├── docs/
│   ├── STEP-1.md
│   ├── baseline-pseudocode.md
│   └── product-v1-sketch.png
└── src/
    └── validate_data.py
```
