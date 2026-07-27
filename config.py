import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Central configuration for Career Advisor AI.
    """

    # ======================================
    # API KEYS
    # ======================================

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    # ======================================
    # LLM SETTINGS
    # ======================================

    # Choose: "groq" or "gemini"
    LLM_PROVIDER = "groq"

    GOOGLE_MODEL = "gemini-2.0-flash"

    GROQ_MODEL = "llama-3.3-70b-versatile"

    # ======================================
    # APP SETTINGS
    # ======================================

    APP_NAME = "Career Advisor AI"

    VERSION = "1.0.0"

    DEBUG = True

    MAX_SEARCH_RESULTS = 5

    REQUEST_TIMEOUT = 20