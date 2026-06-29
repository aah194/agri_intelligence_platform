import streamlit as st
import rasterio
import tempfile
import matplotlib.pyplot as plt
import os

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
    "Upload & Analyze"
)

uploaded_red = st.file_uploader(
    "Upload B04 (Red Band)",
    type=["tif"]
)

uploaded_nir = st.file_uploader(
    "Upload B08 (NIR Band)",
    type=["tif"]
)

if uploaded_red and uploaded_nir:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".tif"
    ) as red_file:

        red_file.write(
            uploaded_red.read()
        )

        red_path = red_file.name

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".tif"
    ) as nir_file:

        nir_file.write(
            uploaded_nir.read()
        )

        nir_path = nir_file.name

    with rasterio.open(
        red_path
    ) as red_src:

        red = red_src.read(1)

    with rasterio.open(
        nir_path
    ) as nir_src:

        nir = nir_src.read(1)

    ndvi = calculate_ndvi(
        nir,
        red
    )

    fig, ax = plt.subplots()

    img = ax.imshow(
        ndvi,
        cmap="RdYlGn"
    )

    plt.colorbar(
        img,
        ax=ax,
        label="NDVI"
    )

    ax.set_title(
        "NDVI Heatmap"
    )

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    fig.savefig(
        "outputs/upload_ndvi_map.png",
        bbox_inches="tight"
    )

    st.pyplot(
        fig
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
        "Results"
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