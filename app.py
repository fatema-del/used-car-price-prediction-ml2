
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =====================================
# 1. PAGE SETTINGS
# =====================================

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# =====================================
# 2. LOAD TRAINED MODELS
# =====================================

@st.cache_resource
def load_models():
    folder = Path(__file__).parent

    linear_model = joblib.load(
        folder / "linear_regression_model.pkl"
    )

    decision_model = joblib.load(
        folder / "decision_tree_model.pkl"
    )

    return linear_model, decision_model


try:
    linear_model, decision_model = load_models()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()


# =====================================
# 3. WEBSITE TITLE
# =====================================

st.title("Used Car Price Prediction")

st.write(
    "Enter the vehicle information to predict "
    "its estimated price or price category."
)

st.divider()


# =====================================
# 4. SELECT MODEL
# =====================================

model_choice = st.radio(
    "Choose your prediction model:",
    ["Linear Regression", "Decision Tree Classifier"],
    horizontal=True
)

st.subheader("Vehicle Information")


# =====================================
# 5. INPUT FEATURES
# =====================================

col1, col2 = st.columns(2)

with col1:

    year = st.number_input(
        "Year",
        min_value=1900,
        max_value=2030,
        value=2018
    )

    manufacturer = st.text_input(
        "Manufacturer",
        value="ford"
    )

    model_name = st.text_input(
        "Model",
        value="f-150"
    )

    condition = st.text_input(
        "Condition",
        value="good"
    )

    cylinders = st.text_input(
        "Cylinders",
        value="6 cylinders"
    )

    fuel = st.text_input(
        "Fuel",
        value="gas"
    )

    odometer = st.number_input(
        "Odometer (miles)",
        min_value=0.0,
        value=80000.0
    )

    title_status = st.text_input(
        "Title Status",
        value="clean"
    )


with col2:

    transmission = st.text_input(
        "Transmission",
        value="automatic"
    )

    drive = st.text_input(
        "Drive",
        value="4wd"
    )

    vehicle_type = st.text_input(
        "Vehicle Type",
        value="truck"
    )

    paint_color = st.text_input(
        "Paint Color",
        value="white"
    )

    state = st.text_input(
        "State",
        value="ca"
    )

    seller_type = st.text_input(
        "Seller Type",
        value="dealer"
    )

    mileage_per_year = st.number_input(
        "Mileage Per Year",
        min_value=0.0,
        value=10000.0
    )

    is_luxury = st.selectbox(
        "Luxury Brand",
        ["No", "Yes"]
    )


# =====================================
# 6. PREPARE INPUT DATA
# =====================================

input_data = {
    "year": year,
    "manufacturer": manufacturer.strip(),
    "model": model_name.strip(),
    "condition": condition.strip(),
    "cylinders": cylinders.strip(),
    "fuel": fuel.strip(),
    "odometer": odometer,
    "title_status": title_status.strip(),
    "transmission": transmission.strip(),
    "drive": drive.strip(),
    "type": vehicle_type.strip(),
    "paint_color": paint_color.strip(),
    "state": state.strip(),
    "seller_type": seller_type.strip(),
    "mileage_per_year": mileage_per_year,
    "is_luxury": 1 if is_luxury == "Yes" else 0
}

input_df = pd.DataFrame([input_data])


# =====================================
# 7. MAKE PREDICTION
# =====================================

if st.button("Predict", type="primary"):

    try:

        if model_choice == "Linear Regression":

            prediction = linear_model.predict(input_df)[0]

            st.success("Price Prediction Complete")

            st.metric(
                "Estimated Car Price",
                f"${prediction:,.2f}"
            )

        else:

            prediction = decision_model.predict(input_df)[0]

            st.success("Category Prediction Complete")

            st.metric(
                "Predicted Price Category",
                prediction
            )

    except Exception as e:

        st.error(f"Prediction error: {e}")


# =====================================
# 8. FOOTER
# =====================================

st.divider()

st.caption(
    "CDS4003 | Used Car Price Prediction Project"
)

st.caption(
    "Predictions are estimates and should be "
    "used as decision-support information."
)
