import streamlit as st

st.title(
    "Yield Forecasting"
)

st.subheader(
    "NDVI-Based Yield Prediction"
)

ndvi = st.slider(
    "Average NDVI",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.01
)

if st.button(
    "Predict Yield"
):

    if ndvi > 0.7:

        prediction = "High Yield Expected"

    elif ndvi > 0.4:

        prediction = "Moderate Yield Expected"

    else:

        prediction = "Low Yield Expected"

    st.success(
        prediction
    )

    st.write(
        f"NDVI Used: {ndvi}"
    )