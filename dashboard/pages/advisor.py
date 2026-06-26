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