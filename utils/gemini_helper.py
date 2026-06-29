import streamlit as st
from google import genai

API_KEY = st.secrets.get(
    "GEMINI_API_KEY",
    None
)

if API_KEY:
    client = genai.Client(
        api_key=API_KEY
    )
else:
    client = None


def get_agri_advice(
    question
):

    if client is None:
        return (
            "Gemini API key not configured. "
            "Add GEMINI_API_KEY in Streamlit secrets."
        )

    prompt = f"""
You are an expert agricultural advisor.

Provide practical farming advice.

Question:
{question}

Answer:
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return (
            f"Gemini Error: {str(e)}"
        )