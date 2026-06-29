import streamlit as st
import rasterio
from utils.pdf_report import (
    generate_report
)
from preprocessing.ndvi import (
    calculate_ndvi
)

from models.stress_detection.stress_detector import (
    detect_stress
)

from models.forecasting.yield_predictor import (
    predict_yield
)

st.title(
    "Yield Forecasting"
)

if st.button(
    "Generate Forecast"
):

    WINDOW_SIZE = 512

    with rasterio.open(
        "datasets/sentinel/B04.tif"
    ) as red_src:

        red = red_src.read(
            1,
            window=rasterio.windows.Window(
                0,
                0,
                WINDOW_SIZE,
                WINDOW_SIZE
            )
        )

    with rasterio.open(
        "datasets/sentinel/B08.tif"
    ) as nir_src:

        nir = nir_src.read(
            1,
            window=rasterio.windows.Window(
                0,
                0,
                WINDOW_SIZE,
                WINDOW_SIZE
            )
        )

    ndvi = calculate_ndvi(
        nir,
        red
    )

    result = detect_stress(
        ndvi
    )

    prediction = predict_yield(
        result["healthy_percent"],
        result["moderate_percent"],
        result["stressed_percent"]
    )

    st.subheader(
        "Vegetation Health"
    )

    st.write(
        f"Healthy: {result['healthy_percent']}%"
    )

    st.write(
        f"Moderate: {result['moderate_percent']}%"
    )

    st.write(
        f"Stressed: {result['stressed_percent']}%"
    )

    st.success(
        prediction
    )
    pdf_file = generate_report(
    result["healthy_percent"],
    result["moderate_percent"],
    result["stressed_percent"],
    prediction
    )

    st.success(
    "PDF report generated successfully"
    )

    with open(
    pdf_file,
    "rb"
    ) as file:

     st.download_button(
        label="Download Report",
        data=file,
        file_name="agri_report.pdf",
        mime="application/pdf"
     )    