import streamlit as st
import rasterio
import matplotlib.pyplot as plt

from preprocessing.ndvi import (
    calculate_ndvi
)

from models.stress_detection.stress_detector import (
    detect_stress
)

st.title(
    "Crop Stress Detection"
)

if st.button(
    "Analyze Stress"
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

    fig, ax = plt.subplots()

    labels = [
        "Healthy",
        "Moderate",
        "Stressed"
    ]

    values = [
        result["healthy_percent"],
        result["moderate_percent"],
        result["stressed_percent"]
    ]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Stress Distribution"
    )

    st.pyplot(
        fig
    )