from google import genai
from config import Config
from ai.prompt import generate_prompt
from ai.fallback import fallback_report
import time

client = genai.Client(api_key=Config.GEMINI_API_KEY)


def generate_ai_response(question):

    response = client.models.generate_content(

        model="gemini-flash-latest",

        contents=question

    )

    return response.text



def generate_ai_report(disease, confidence):

    prompt = generate_prompt(disease, confidence)

    models = [
        "gemini-3.5-flash",
        "gemini-3.1-flash-lite",
        "gemini-3.1-flash-lite-preview",
        "gemini-flash-latest"
    ]

    for model_name in models:

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )
                return response.text

            except Exception as e:

                print("Gemini Error:", e)

                return fallback_report(
                    disease,
                    confidence
                )