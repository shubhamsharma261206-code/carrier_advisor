import os
from dotenv import load_dotenv

# Load all variables from .env file
load_dotenv()


class Config:
    """
    Central configuration class for the entire application.
    All API keys and project settings are stored here.
    """

    # -------------------------
    # API KEYS
    # -------------------------
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    # -------------------------
    # LLM SETTINGS
    # -------------------------
    GOOGLE_MODEL = "gemini-2.5-flash"

    GROQ_MODEL = "llama-3.3-70b-versatile"

    # -------------------------
    # APPLICATION SETTINGS
    # -------------------------
    APP_NAME = "Career Advisor AI"

    VERSION = "1.0.0"

    DEBUG = True

    MAX_SEARCH_RESULTS = 5

    REQUEST_TIMEOUT = 20