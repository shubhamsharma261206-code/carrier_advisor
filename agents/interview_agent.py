from services.prompt_manager import PromptManager
from tools.search.search_helper import SearchHelper


class InterviewAgent:
    """
    Generates interview preparation guidance
    for a selected career.
    """

    def __init__(self, llm):
        self.llm = llm

    def execute(
        self,
        analysis: dict,
        search_result: dict
    ) -> dict:

        career = analysis.get("career")

        if not career:
            return {
                "success": False,
                "agent": "interview",
                "data": None,
                "error": "Career name not found."
            }

        search_data = SearchHelper.extract_content(search_result)

        prompt = PromptManager.interview_prompt(
            career=career,
            search_data=search_data
        )

        result = self.llm.generate(prompt)

        return {
            "success": True,
            "agent": "interview",
            "data": result,
            "error": None
        }