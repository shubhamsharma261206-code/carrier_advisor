from config import Config

from tools.llm.google_ai import GoogleAI
from tools.llm.groq_ai import GroqAI


class LLMFactory:
    """
    Returns whichever LLM is selected in config.
    """

    @staticmethod
    def get_llm():

        if Config.LLM_PROVIDER.lower() == "groq":
            return GroqAI()

        return GoogleAI()