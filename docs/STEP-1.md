# Project Step 1 — SC07 Smart Irrigation System

## Team responsibilities
- Project owner: Prince Kumar
- Data/documentation: Prince Kumar
- Validation and baseline: Prince Kumar
- Planned Soft Computing implementation: Team responsibility to be assigned/confirmed before the implementation phase.

> Add the remaining approved team members and responsibilities here before final team submission.

## Problem statement
Irrigation decisions can depend on changing soil and environmental conditions. The project will build a Smart Irrigation System that uses measurable conditions to provide a simple irrigation recommendation.

## Intended user
A farmer, gardener, or irrigation operator who needs a clear irrigation recommendation from available soil and environmental observations.

## Inputs and units
- Soil moisture: percentage (%)
- Temperature: degrees Celsius (°C)
- Relative humidity: percentage (%)
- Recent rainfall: millimetres (mm)
- Soil pH: pH scale

## Output
- `irrigation_target`: 0 = No irrigation, 1 = Irrigation needed

## Baseline method
A transparent threshold/rule-based benchmark will use soil moisture and recent rainfall to produce a simple irrigation decision. The baseline is only a project comparison benchmark, not an agricultural or regulatory standard.

## Planned M1 Soft Computing method
The planned M1 method is **Fuzzy Logic + Artificial Neural Network (ANN)**:
- Fuzzy Logic will transform continuous environmental conditions into interpretable linguistic conditions and a fuzzy irrigation recommendation.
- ANN will learn the relationship between the input features and the starter irrigation target.
- Later evaluation will compare the baseline and Soft Computing outputs and show validation/status information.

## Step-1 acceptance checkpoints
- Public shared GitHub repository is created and collaborators are accepted.
- Required repository structure is present.
- Data Dictionary is in the root README.
- 20-row starter data is committed after the validation exercise.
- Baseline pseudocode is committed.
- `src/validate_data.py` detects the deliberate missing-value failure and then passes after correction.
- Product V1 sketch is committed under `docs/`.

## Scope note
This document is for Project Step 1. The final Fuzzy + ANN model is not treated as completed in this step.
