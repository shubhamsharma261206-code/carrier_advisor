from services.prompt_manager import PromptManager
from tools.llm.google_ai import GoogleAI


class CareerAgent:
    """
    Handles career overview and career-related information.
    """

    def __init__(self, google: GoogleAI):
        self.google = google

    def execute(
        self,
        analysis: dict,
        search_result: dict
    ) -> dict:

        career = analysis.get("career")

        if not career:
            return {
                "success": False,
                "agent": "career",
                "data": "Career name could not be identified.",
                "error": "Missing career"
            }

        if search_result["success"]:
            search_data = str(search_result["data"])
        else:
            search_data = "No live search results available."

        prompt = PromptManager.career_prompt(
            career=career,
            search_data=search_data
        )

        result = self.google.generate(prompt)

        return {
            "success": True,
            "agent": "career",
            "data": result,
            "error": None
        }