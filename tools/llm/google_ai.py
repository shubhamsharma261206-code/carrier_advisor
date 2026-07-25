from google import genai
from google.genai import types

from config import Config


class GoogleAI:

    def __init__(self):

        self.client = genai.Client(
            api_key=Config.GOOGLE_API_KEY
        )

        self.model = Config.GOOGLE_MODEL

    def generate(self, prompt: str) -> str:
        """
        Generates a response from Gemini.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.3,
                    max_output_tokens=2048
                )
            )

            return response.text

        except Exception as e:

            return f"Gemini Error : {str(e)}"