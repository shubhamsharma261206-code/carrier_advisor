from groq import Groq
from config import Config


class GroqAI:
    """
    Wrapper class for Groq API.
    Used for fast reasoning and routing.
    """

    def __init__(self):

        self.client = Groq(
            api_key=Config.GROQ_API_KEY
        )

        self.model = Config.GROQ_MODEL

    def generate(self, prompt: str) -> dict:
        """
        Generate response using Groq LLM.
        """

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.3,

                max_tokens=2048

            )

            return {
                "success": True,
                "data": response.choices[0].message.content,
                "error": None
            }

        except Exception as e:

            return {
                "success": False,
                "data": None,
                "error": str(e)
            }