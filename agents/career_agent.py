from services.prompt_manager import PromptManager


class CareerAgent:
    """
    Handles career overview and career-related information.
    """

    def __init__(self, llm):
        """
        llm can be GoogleAI or GroqAI.
        """
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

        result = self.llm.generate(prompt)

        return {
            "success": True,
            "agent": "career",
            "data": result,
            "error": None
        }