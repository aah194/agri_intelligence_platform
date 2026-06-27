import streamlit as st

from utils.gemini_helper import (
    get_agri_advice
)

st.title(
    "AI Agricultural Advisor"
)

question = st.text_area(
    "Ask an agriculture question"
)

if st.button(
    "Get Advice"
):

    if question:

        with st.spinner(
            "Generating advice..."
        ):

            answer = get_agri_advice(
                question
            )

        st.write(
            answer
        )

st.divider()

if st.button(
    "Explain Latest Stress Analysis"
):

    healthy = 73.08
    moderate = 25.51
    stressed = 1.41

    prompt = f"""
    Healthy Vegetation: {healthy}%
    Moderate Vegetation: {moderate}%
    Stressed Vegetation: {stressed}%

    Explain this agricultural analysis in simple language
    and suggest actions for farmers.
    """

    response = get_agri_advice(
        prompt
    )

    st.subheader(
        "AI Interpretation"
    )

    st.write(
        response
    )