
"""SC07 Smart Irrigation System - Product V1."""

import pandas as pd
import streamlit as st

from src.product_predict import (
    FEATURES,
    load_method,
    predict_one,
)


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="SC07 Smart Irrigation System",
    page_icon="🌱",
    layout="wide",
)


# --------------------------------------------------
# 2. APPLICATION HEADER
# --------------------------------------------------

st.title("🌱 Smart Irrigation System")

st.subheader(
    "Product V1 | Soil and Weather Based Irrigation Decision"
)

st.write(
    "Enter the current soil and weather measurements. "
    "The application uses the saved Step 3 ANN and compares "
    "its result with the Step 4 baseline."
)

st.info(
    "Decision-support prototype: this is not an automatic "
    "watering controller and does not replace local "
    "agricultural advice."
)


# --------------------------------------------------
# 3. INPUT LABELS
# --------------------------------------------------

LABELS = {
    "soil_moisture_pct": "Soil moisture (%)",
    "temperature_c": "Temperature (°C)",
    "humidity_pct": "Relative humidity (%)",
    "rainfall_mm": "Recent rainfall (mm)",
    "soil_ph": "Soil pH (unitless)",
}


# --------------------------------------------------
# 4. LOAD SAVED ANN MODEL AND SCALER
# --------------------------------------------------

@st.cache_resource
def get_saved_method():
    return load_method()


try:
    model, scaler, metadata = get_saved_method()

except Exception as error:

    st.error(
        f"Could not load the saved Step 3 method: {error}"
    )

    st.warning(
        "Check that models/ann_model.pkl, "
        "models/scaler.pkl and models/metadata.json exist, "
        "and install the project's recorded scikit-learn version."
    )

    st.stop()


st.success("Saved ANN and scaler loaded successfully.")


# --------------------------------------------------
# 5. METHOD INFORMATION
# --------------------------------------------------

with st.expander("Input limits and method information"):

    st.markdown(
        """
        - Soil moisture: 0–100%
        - Temperature: -10–60 °C
        - Relative humidity: 0–100%
        - Recent rainfall: 0–500 mm
        - Soil pH: 0–14
        """
    )

    st.caption(
        "These are the starter project's validation limits, "
        "not recommended crop-specific operating ranges."
    )

    st.write(
        "ANN features:",
        ", ".join(FEATURES)
    )

    st.write(
        "ANN architecture:",
        metadata.get("hidden_layers", "as saved")
    )

    st.write(
        "Step 4 baseline: irrigation ON when "
        "soil moisture is below 30%."
    )


# --------------------------------------------------
# 6. USER INPUT FORM
# --------------------------------------------------

st.header("Enter field measurements")

with st.form("irrigation_form"):

    col1, col2 = st.columns(2)

    with col1:

        soil_moisture = st.text_input(
            LABELS["soil_moisture_pct"],
            value="28",
            help="Accepted range: 0 to 100."
        )

        temperature = st.text_input(
            LABELS["temperature_c"],
            value="32",
            help="Accepted range: -10 to 60."
        )

        humidity = st.text_input(
            LABELS["humidity_pct"],
            value="45",
            help="Accepted range: 0 to 100."
        )

    with col2:

        rainfall = st.text_input(
            LABELS["rainfall_mm"],
            value="2",
            help="Accepted range: 0 to 500."
        )

        soil_ph = st.text_input(
            LABELS["soil_ph"],
            value="6.5",
            help="Accepted range: 0 to 14."
        )

    submitted = st.form_submit_button(
        "Get Irrigation Recommendation",
        type="primary",
        width="stretch"
    )


# --------------------------------------------------
# 7. PREDICTION AND VALIDATION
# --------------------------------------------------

if submitted:

    inputs = {
        "soil_moisture_pct": soil_moisture,
        "temperature_c": temperature,
        "humidity_pct": humidity,
        "rainfall_mm": rainfall,
        "soil_ph": soil_ph,
    }

    try:

        result = predict_one(
            model,
            scaler,
            inputs
        )

    except ValueError as error:

        st.error(
            f"Input validation failed:\n\n{error}"
        )

    except Exception as error:

        st.error(
            f"Recommendation could not be generated: {error}"
        )

    else:

        # ------------------------------------------
        # 8. IRRIGATION RECOMMENDATION
        # ------------------------------------------

        st.header("Recommendation")

        if result["ann_prediction"] == 1:

            st.warning(
                "ANN result: Irrigation required"
            )

        else:

            st.success(
                "ANN result: Irrigation not required"
            )

        # ------------------------------------------
        # 9. MODEL OUTPUT COMPARISON
        # ------------------------------------------

        a, b = st.columns(2)

        with a:

            st.metric(
                "Saved ANN output",
                result["ann_label"]
            )

        with b:

            st.metric(
                "Step 4 baseline output",
                result["baseline_label"]
            )

        if result["methods_agree"]:

            st.success(
                result["comparison"]
            )

        else:

            st.warning(
                result["comparison"]
            )

        # ------------------------------------------
        # 10. INPUT AND OUTPUT SUMMARY
        # ------------------------------------------

        st.subheader(
            "Input and output summary"
        )

        summary_rows = [
            {
                "Measurement / result": LABELS.get(key, key),
                "Value": str(value)
            }
            for key, value in inputs.items()
        ]

        summary_rows.extend(
            [
                {
                    "Measurement / result": "ANN class",
                    "Value": str(result["ann_prediction"])
                },
                {
                    "Measurement / result": "Baseline class",
                    "Value": str(result["baseline_prediction"])
                },
                {
                    "Measurement / result": "Methods agree",
                    "Value": str(result["methods_agree"])
                },
            ]
        )

        summary = pd.DataFrame(summary_rows)

        st.dataframe(
            summary,
            width="stretch",
            hide_index=True
        )

        # ------------------------------------------
        # 11. RESULT NOTICE
        # ------------------------------------------

        st.caption(
            result["notice"]
        )

        # ------------------------------------------
        # 12. DOWNLOAD RESULT AS CSV
        # ------------------------------------------

        csv_bytes = pd.DataFrame(
            [result]
        ).to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download result as CSV",
            data=csv_bytes,
            file_name="sc07_irrigation_recommendation.csv",
            mime="text/csv",
        )


# --------------------------------------------------
# 13. HOW THE APPLICATION WORKS
# --------------------------------------------------

st.divider()

st.subheader(
    "How this application works"
)

st.markdown(
    """
    1. The user enters five soil and weather measurements.

    2. Product V1 validates that every value is numeric,
       finite and inside the documented starter range.

    3. The existing saved scaler transforms the values
       in the original feature order.

    4. The saved ANN predicts irrigation class 0 or 1.

    5. The Step 4 threshold baseline is calculated separately
       and both results are displayed for comparison.

    **Important:** The repository describes Fuzzy Logic + ANN
    as a planned combined method. The supplied saved artifacts
    currently contain an ANN and scaler, plus the Step 4
    threshold baseline. This Product V1 therefore does not
    claim to execute a fuzzy controller.
    """
)
