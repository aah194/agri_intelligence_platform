import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from utils.gemini_helper import (
    get_agri_advice
)

st.title(
    "AI Agricultural Advisor"
)

question = st.text_area(
    "Ask your agriculture question"
)

if st.button(
    "Get Advice"
):

    if question.strip():

        response = get_agri_advice(
            question
        )

        st.success(
            response
        )

    else:

        st.warning(
            "Please enter a question."
        )