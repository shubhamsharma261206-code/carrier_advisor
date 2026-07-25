import json

from tools.llm.groq_ai import GroqAI


class AnalyzerAgent:
    """
    Extracts structured information
    from the user's query.
    """

    def __init__(self, groq: GroqAI):
        self.groq = groq

    def analyze(self, user_query: str) -> dict:

        prompt = f"""
You are an information extraction AI.

Extract the following fields from the user query.

Return ONLY valid JSON.

Fields:

career
country
education
experience
year

Rules:

- If value is missing use null.
- Do not explain anything.
- Return JSON only.
- Do not use markdown.

Example:

{{
    "career":"AI Engineer",
    "country":"India",
    "education":"BCA",
    "experience":"Fresher",
    "year":"3rd Year"
}}

User Query:

{user_query}
"""

        result = self.groq.generate(prompt)

        if not result["success"]:

            return {
                "career": None,
                "country": None,
                "education": None,
                "experience": None,
                "year": None
            }

        try:

            data = json.loads(result["data"])

            return {
                "career": data.get("career"),
                "country": data.get("country"),
                "education": data.get("education"),
                "experience": data.get("experience"),
                "year": data.get("year")
            }

        except Exception:

            return {
                "career": None,
                "country": None,
                "education": None,
                "experience": None,
                "year": None
            }