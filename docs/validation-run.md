# Step-1 Local Run Notes

From the repository root:

```bash
python -m pip install -r requirements.txt
python src/validate_data.py
```

Expected final output:

`STEP 1 DATA CHECK PASSED`

To reproduce the required validation-failure evidence, temporarily remove the `soil_ph` value from row `IRR-005`, run the validator and capture the failure. Then restore the value, run again, and capture the final PASS. Do not commit the intentionally broken version.
