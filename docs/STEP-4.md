# Step 4 – Baseline Comparison

## 1. Comparison Question

Can a simple soil-moisture threshold baseline perform as well as the Step 3 Artificial Neural Network (ANN) when predicting irrigation requirements?

## 2. Baseline Rule

The baseline predicts irrigation ON when soil moisture is below 30%, and irrigation OFF otherwise.

This rule is simple, easy to understand, and reproducible. It provides a reference for comparing the ANN model.

## 3. Dataset and Evaluation

- Project: SC07 – Smart Irrigation System
- Dataset: Step 2 sample dataset
- Total samples: 20
- Training samples: 16
- Test samples: 4
- Train/test split: 80:20
- Random state: 42
- Evaluation metric: Accuracy

Both methods use the same test split and the same irrigation target.

## 4. Results

| Measure | Baseline | ANN |
|---|---:|---:|
| Test samples | 4 | 4 |
| Accuracy | 100% | 100% |

Accuracy difference (ANN − Baseline): 0 percentage points.

The baseline confusion matrix was:

```text
[[2 0]
 [0 2]]
```

All four test predictions were correct for the baseline. The ANN also achieved 100% accuracy on this test split.

## 5. Interpretation

The results show no measured accuracy improvement from the ANN over the simple baseline on this test set. Both methods classified all four test samples correctly.

## 6. Limitations

The test set contains only four samples, so the results are not sufficient to establish real-world performance or generalisation. The 30% threshold is a simple starting rule and may not be suitable for every soil type or crop. More representative data and field testing are needed.

## 7. Reproducibility

Run the baseline comparison from the project root using:

```bash
python src/baseline.py
```

The script saves:

- `results/baseline_comparison.csv`
- `results/baseline_metrics.json`

The comparison uses the Step 2 dataset, a fixed random state, and the saved Step 3 ANN model and scaler.

## 8. Contribution

Baseline implementation, execution, and comparison documentation: Kaif Khan.

## 9. Conclusion

On the current four-sample test split, the baseline and ANN both achieved 100% accuracy. The evidence does not demonstrate an accuracy improvement from the ANN. Further evaluation on a larger test set is required.