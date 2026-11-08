import unittest

from src.product_predict import FEATURES, validate_inputs


class ProductValidationTests(unittest.TestCase):
    def setUp(self):
        self.values = {
            "soil_moisture_pct": "28",
            "temperature_c": "32",
            "humidity_pct": "45",
            "rainfall_mm": "2",
            "soil_ph": "6.5",
        }

    def test_normal_input(self):
        clean = validate_inputs(self.values)
        self.assertEqual(list(clean.keys()), FEATURES)
        self.assertEqual(clean["soil_moisture_pct"], 28.0)

    def test_boundary_values(self):
        self.values.update({
            "soil_moisture_pct": "0",
            "temperature_c": "-10",
            "humidity_pct": "100",
            "rainfall_mm": "500",
            "soil_ph": "14",
        })
        self.assertEqual(validate_inputs(self.values)["soil_ph"], 14.0)

    def test_out_of_range_values(self):
        for feature, bad_value in [
            ("soil_moisture_pct", "101"),
            ("temperature_c", "61"),
            ("humidity_pct", "-1"),
            ("rainfall_mm", "501"),
            ("soil_ph", "15"),
        ]:
            with self.subTest(feature=feature):
                changed = dict(self.values)
                changed[feature] = bad_value
                with self.assertRaises(ValueError):
                    validate_inputs(changed)

    def test_missing_and_nonnumeric_values(self):
        changed = dict(self.values)
        changed["soil_ph"] = ""
        with self.assertRaises(ValueError):
            validate_inputs(changed)

        changed = dict(self.values)
        changed["temperature_c"] = "abc"
        with self.assertRaises(ValueError):
            validate_inputs(changed)

    def test_nan_and_infinity(self):
        for value in ("nan", "inf", "-inf"):
            with self.subTest(value=value):
                changed = dict(self.values)
                changed["rainfall_mm"] = value
                with self.assertRaises(ValueError):
                    validate_inputs(changed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
