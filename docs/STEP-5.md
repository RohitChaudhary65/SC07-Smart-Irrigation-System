# Step 5 - Product V1: SC07 Smart Irrigation System

> Complete the bracketed fields with the team's actual details and observations.
> Do not mark a test as passed until it has been run and evidence captured.

## Team and project
- Project code and title: SC07 - Smart Irrigation System
- Team name: Fuzzy Pointers
- Team members:
  1. Rohit Chaudhary (Team Leader)
  2. Prince Kumar
  3. Md. Kaif Khan
  4. Avika
- Step 5 branch: `step-5-product-v1`
- Commit: `658a290`

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

Recorded test details:
- Date/time: 08-11-2026 16:12 IST
- Python version: 3.14.3
- scikit-learn version: 1.9.1
- Tests passed: 5 out of 5
- Test output/evidence path: `docs/evidence/step5/04-test-output.png`

Actual test output:

```text
test_boundary_values ... ok
test_missing_and_nonnumeric_values ... ok
test_nan_and_infinity ... ok
test_normal_input ... ok
test_out_of_range_values ... ok

Ran 5 tests in 0.001s

OK
```
## Manual test observations

| Case | Input / action | Expected behaviour | Actual observation | Pass/Fail |
|---|---|---|---|---|
| Normal | Soil moisture: 25%, Temperature: 30°C, Humidity: 65%, Rainfall: 0 mm, Soil pH: 7 | ANN and baseline results display | ANN predicted Class 0 (Irrigation not required), while baseline predicted Class 1 (Irrigation required). | Pass |
| Boundary | Test minimum and maximum values for all five inputs | Accepted by validation | Boundary value tests passed successfully in automated testing. | Pass |
| Missing | Omit a required input in a direct function test | Clear required-value error | Missing-value validation test passed successfully. | Pass |
| Invalid | Enter humidity as 250% in the application | Clear validation error; no prediction | Application displayed a clear humidity range error and did not crash. | Pass |
| Missing model | Temporarily rename a model artifact in a separate copy and launch | Clear model-loading error; no fake result | Not tested yet. | Not tested |
| Consistency | Compare direct prediction with the same values in the UI | Matching ANN class | Not tested yet. | Not tested |

## Screenshots and evidence
Save actual screenshots in `docs/evidence/step5/`:
- `01-input-form.png`
- `02-normal-result.png`
- `03-validation-error.png`
- `04-test-output.png`

Do not include passwords, access codes or private information.

## Earlier feedback addressed

- Added a Streamlit-based user interface to make the Smart Irrigation System usable.
- Connected the saved ANN model and StandardScaler for actual prediction without retraining when the user clicks the prediction button.
- Added input validation for missing, non-numeric, NaN, infinite and out-of-range values.
- Added comparison between the ANN prediction and the Step 4 soil-moisture threshold baseline.
- Added automated validation tests and captured screenshots as evidence.
- Corrections are available in `app.py`, `src/product_predict.py` and `test_product_predict.py`.
- Initial Product V1 implementation commit: `658a290`.

Unresolved issues:
- Specific Step 1–4 feedback items still need to be reviewed against the published project feedback.
- Missing-model and UI/direct-prediction consistency manual tests are not yet completed.
- The model has limited test evidence and requires further real-world validation.
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

All team members contributed equally to the development and completion of the SC07 Smart Irrigation System project. There were no fixed individual roles or separate responsibilities. All members worked together on project development, implementation, testing, documentation, improvements and uploading the project files to GitHub.

- **Rohit Chaudhary:** Equal contribution to project development, testing, documentation and GitHub uploading.
- **Prince Kumar:** Equal contribution to project development, testing, documentation and GitHub uploading.
- **Md. Kaif Khan:** Equal contribution to project development, testing, documentation and GitHub uploading.
- **Avika:** Equal contribution to project development, testing, documentation and GitHub uploading.

All team members participated collaboratively and shared responsibilities throughout the project.
