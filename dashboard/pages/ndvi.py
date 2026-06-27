import streamlit as st
import numpy as np
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
        [200,180,220],
        [220,210,230],
        [250,240,255]
    ])

    red = np.array([
        [100,120,140],
        [140,130,150],
        [160,170,180]
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

    plt.colorbar(
        img,
        ax=ax,
        label="NDVI"
    )

    st.pyplot(
        fig
    )

    st.success(
        "NDVI Generated"
    )