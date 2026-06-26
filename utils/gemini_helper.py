from google import genai
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

client = genai.Client(
    api_key=API_KEY
)

def get_agri_advice(
    question
):

    prompt = f"""
You are an expert agricultural advisor.

Provide practical advice.

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text