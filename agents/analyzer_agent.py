import json

from tools.llm.groq_ai import GroqAI


class AnalyzerAgent:
    """
    Extracts structured information
    from the user's query.
    """

    def __init__(self, groq: GroqAI):
        self.groq = groq

    def analyze(self, user_query: str):

        prompt = f"""
You are an Information Extraction AI.

Extract the following fields from the user's query.

Return ONLY valid JSON.

Fields:
- career
- country
- education
- experience
- year

Rules:
- If a field is missing, use null.
- Do NOT explain anything.
- Do NOT use markdown.
- Return ONLY JSON.

Example:

{{
    "career": "AI Engineer",
    "country": "India",
    "education": "BCA",
    "experience": "Fresher",
    "year": "3rd Year"
}}

User Query:
{user_query}
"""

        result = self.groq.generate(prompt)

        print("\n========== GROQ RESULT ==========")
        print(result)
        print("=================================\n")

        if not result["success"]:

            print("Groq Error:", result["error"])

            return {
                "career": None,
                "country": None,
                "education": None,
                "experience": None,
                "year": None
            }

        response = result["data"]

        print("\n========== RAW RESPONSE ==========")
        print(response)
        print("==================================\n")

        # Remove markdown if Groq returns ```json ... ```
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        try:

            data = json.loads(response)

            print("\n========== PARSED JSON ==========")
            print(data)
            print("=================================\n")

            return {
                "career": data.get("career"),
                "country": data.get("country"),
                "education": data.get("education"),
                "experience": data.get("experience"),
                "year": data.get("year")
            }

        except Exception as e:

            print("\n========== JSON ERROR ==========")
            print(e)
            print(response)
            print("================================\n")

            return {
                "career": None,
                "country": None,
                "education": None,
                "experience": None,
                "year": None
            }