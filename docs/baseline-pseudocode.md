# Baseline Pseudocode

## Goal
Create a simple, explainable benchmark for comparison with the planned Fuzzy + ANN method.

## Inputs
- soil_moisture_pct
- rainfall_mm

## Rule
1. Read the soil moisture and recent rainfall.
2. If soil moisture is low and recent rainfall is low, output `1` (irrigation needed).
3. Otherwise output `0` (no irrigation).
4. Record the baseline output.

## Example project threshold
For this starter benchmark, use:
- low soil moisture: `soil_moisture_pct < 35`
- low recent rainfall: `rainfall_mm < 5`

These are illustrative project thresholds only and are not agricultural or regulatory standards.

## Output
`baseline_irrigation_target`:
- `0` = No irrigation
- `1` = Irrigation needed

## Comparison plan
Later, compare this baseline decision with the Fuzzy + ANN result using the same validated input features.
