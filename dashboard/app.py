import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st
from PIL import Image

from models.landcover.inference import predict

st.set_page_config(
    page_title="Agri Intelligence Platform",
    layout="wide"
)

st.sidebar.title(
    "Modules"
)

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Land Cover",
        "NDVI",
        "Stress Detection",
        "Forecasting",
        "AI Advisor"
    ]
)

st.title(
    "Agri Intelligence Platform"
)

if module == "Land Cover":

    uploaded_file = st.file_uploader(
        "Upload Satellite Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(
            uploaded_file
        )

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        image.save(
            "temp_image.jpg"
        )

        result = predict(
            "temp_image.jpg"
        )

        st.success(
            f"Predicted Class: {result}"
        )

elif module == "NDVI":

    st.info(
        "NDVI Module Coming Soon"
    )

elif module == "Stress Detection":

    st.info(
        "Stress Detection Module Coming Soon"
    )

elif module == "Forecasting":

    st.info(
        "Forecasting Module Coming Soon"
    )

elif module == "AI Advisor":

    st.info(
        "AI Advisor Module Coming Soon"
    )