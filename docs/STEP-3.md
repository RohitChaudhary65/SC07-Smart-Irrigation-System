# Step 3 – ANN Model

## Project
SC07 – Smart Irrigation System

## Objective
The objective of Step 3 is to develop and evaluate an Artificial Neural Network (ANN) model for predicting the irrigation target using soil and environmental parameters.

## Dataset

The dataset used in this step is the output dataset prepared in Step 2.

Dataset:
- Rows: 20
- Columns: 7
- Features: 5
- Target: `irrigation_target`

### Input Features

1. `soil_moisture_pct`
2. `temperature_c`
3. `humidity_pct`
4. `rainfall_mm`
5. `soil_ph`

### Target

`irrigation_target`

## Data Preparation

The dataset was divided into training and testing sets using an 80:20 split.

- Training samples: 16
- Testing samples: 4
- Random state: 42
- Stratified split: Yes

The input features were standardized using `StandardScaler`.

## ANN Model

The ANN model was implemented using Scikit-learn `MLPClassifier`.

Model configuration:

- Hidden layers: `(16, 8)`
- Activation function: `ReLU`
- Solver: `Adam`
- Maximum iterations: 500
- Random state: 42

## Model Training

The model was trained using the scaled training data.

The repeatable training script is:

`src/train_ann.py`

The training script loads the Step 2 dataset, prepares the features, performs the train-test split, scales the data, trains the ANN model, evaluates the model, and saves the generated artifacts.

## Model Evaluation

The trained model was evaluated using the test dataset.

### Test Accuracy

Test Accuracy: **1.00 (100%)**

The test set contains only 4 samples, so this result represents the performance on this small test split and should not be treated as a general estimate of real-world performance.

### Classification Report

The model achieved:

- Class 0 Precision: 1.00
- Class 0 Recall: 1.00
- Class 0 F1-score: 1.00
- Class 1 Precision: 1.00
- Class 1 Recall: 1.00
- Class 1 F1-score: 1.00

## Confusion Matrix

The confusion matrix generated during notebook evaluation showed:

- Class 0: 2 correct predictions
- Class 1: 2 correct predictions
- Total correct predictions: 4
- Total test samples: 4

No incorrect predictions were observed in the test set.

## Prediction Output

The test predictions were saved as:

`results/ann_predictions.csv`

The file contains:

- Actual target values
- Predicted target values

## Saved Model Artifacts

The following model artifacts were generated:

- `models/ann_model.pkl`
- `models/scaler.pkl`
- `models/metadata.json`

The metadata file stores the project name, model configuration, features, target, dataset split information, and test accuracy.

## Notebook

The ANN implementation and evaluation are documented in:

`notebooks/02_ann_model.ipynb`

The notebook contains the data loading, preprocessing, model training, prediction, evaluation, and visualization steps.

## Reproducibility

The complete ANN training process can be reproduced by running:

```bash
python src/train_ann.py