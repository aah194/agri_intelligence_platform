import streamlit as st
import numpy as np
import os
import matplotlib.pyplot as plt

from preprocessing.ndvi import (
    calculate_ndvi
)

st.title(
    "NDVI Analysis"
)

st.write(
    "Demo NDVI Visualization"
)

if st.button(
    "Generate NDVI"
):

    nir = np.array([
        [200, 180, 220],
        [220, 210, 230],
        [250, 240, 255]
    ])

    red = np.array([
        [100, 120, 140],
        [140, 130, 150],
        [160, 170, 180]
    ])

    ndvi = calculate_ndvi(
        nir,
        red
    )

    fig, ax = plt.subplots()

    img = ax.imshow(
        ndvi,
        cmap="RdYlGn"
    )

    ax.set_title(
        "NDVI Map"
    )

    plt.colorbar(
        img,
        ax=ax,
        label="NDVI"
    )

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    fig.savefig(
        "outputs/ndvi_map.png",
        bbox_inches="tight"
    )

    st.success(
        "NDVI map saved to outputs/ndvi_map.png"
    )

    st.pyplot(
        fig
    )

    st.success(
        "NDVI Generated"
    )