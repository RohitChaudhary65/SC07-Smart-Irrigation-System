# Step 5 - Product V1: SC07 Smart Irrigation System

> Complete the bracketed fields with the team's actual details and observations.
> Do not mark a test as passed until it has been run and evidence captured.

## Team and project
- Project code and title: SC07 - Smart Irrigation System
- Team name: [enter registered team name]
- Team members: [enter actual names]
- Step 5 branch: `step-5-product-v1`
- Commit: [enter commit hash after committing]

## User task
A farmer, gardener or irrigation operator enters soil moisture, temperature,
relative humidity, recent rainfall and soil pH. The application runs the saved
ANN and displays its irrigation class. It also shows the Step 4 soil-moisture
threshold baseline so the two methods can be compared.

## Interface and method
- Interface type: Streamlit web application
- Entry file: `app.py`
- Inference module: `src/product_predict.py`
- Saved ANN: `models/ann_model.pkl`
- Saved scaler: `models/scaler.pkl`
- Metadata: `models/metadata.json`
- Target: `irrigation_target` (0 = no irrigation, 1 = irrigation needed)
- Feature order:
  1. `soil_moisture_pct` (%)
  2. `temperature_c` (°C)
  3. `humidity_pct` (%)
  4. `rainfall_mm` (mm)
  5. `soil_ph` (unitless)

## Validation limits
These are the starter project's data-dictionary limits. They are not crop-specific
agronomic recommendations.

| Input | Accepted range |
|---|---:|
| Soil moisture | 0 to 100 % |
| Temperature | -10 to 60 °C |
| Relative humidity | 0 to 100 % |
| Recent rainfall | 0 to 500 mm |
| Soil pH | 0 to 14 |

## Data flow
User input -> validation -> saved StandardScaler -> saved ANN prediction ->
Step 4 baseline comparison -> readable recommendation and CSV download.

The supplied repository documents Fuzzy Logic + ANN as a planned method.
The saved artifacts present in this repository are an ANN and scaler, and
the Step 4 baseline is a soil-moisture threshold. This Product V1 does not
claim to execute a fuzzy controller.

## Run instructions
Run from the repository root:

```bash
python --version
python -m pip install -r requirements-product-v1.txt
python -m streamlit run app.py
```

Expected local address: `http://localhost:8501`

Stop the local server with `Ctrl+C`.

The saved ANN/scaler artifacts were serialized with scikit-learn 1.9.1.
Use that version to avoid model-persistence compatibility warnings/errors.

## Automated tests
Run from the repository root:

```bash
python -m unittest test_product_predict -v
```

Record the actual terminal output and result here:
- Date/time:
- Python version:
- scikit-learn version:
- Tests passed:
- Test output/evidence path:

## Manual test observations

| Case | Input / action | Expected behaviour | Actual observation | Pass/Fail |
|---|---|---|---|---|
| Normal | Use valid values in all five fields | ANN and baseline results display | [record] | [record] |
| Boundary | Test each documented minimum/maximum | Accepted by validation | [record] | [record] |
| Missing | Remove/omit a required value in a direct function test | Clear required-value error | [record] | [record] |
| Invalid | Try text, NaN/infinity and out-of-range values in direct tests | Clear validation error; no prediction | [record] | [record] |
| Missing model | In a temporary copy, rename one model artifact and launch | Clear model-loading error; no fake result | [record] | [record] |
| Consistency | Run `python -m src.check_product_prediction` and enter the same values in UI | Matching ANN class | [record] | [record] |

## Screenshots and evidence
Save actual screenshots in `docs/evidence/step5/`:
- `01-input-form.png`
- `02-normal-result.png`
- `03-validation-error.png`
- `04-test-output.png`

Do not include passwords, access codes or private information.

## Earlier feedback addressed
- [Paste each relevant Step 1-4 feedback item.]
- [Describe the correction and the file/commit proving it.]
- Unresolved issues: [state honestly, or write None only after review.]

## Limitations and responsible use
- The Step 3 report describes a test split of only four samples and 100%
  accuracy on that small split. This is not sufficient evidence of real-world
  generalisation.
- Starter data and validation ranges are not a substitute for crop-specific,
  soil-specific or local agricultural guidance.
- The application is decision support only; it does not operate a pump or
  guarantee crop outcomes.
- The current Product V1 uses the saved ANN and the Step 4 threshold baseline.
  It does not implement the planned fuzzy component.

## Team contributions
- [Member name]: [actual implementation/testing/documentation contribution]
- [Member name]: [actual contribution]
