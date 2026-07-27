from services.prompt_manager import PromptManager


class SalaryAgent:
    """
    Handles salary-related information for a career.
    """

    def __init__(self, llm):
        self.llm = llm

    def execute(
        self,
        analysis: dict,
        search_result: dict
    ) -> dict:

        career = analysis.get("career")
        country = analysis.get("country") or "India"
        experience = analysis.get("experience") or "Fresher"

        if not career:
            return {
                "success": False,
                "agent": "salary",
                "data": None,
                "error": "Career name not found."
            }

        if search_result["success"]:

            results = search_result["data"].get("results", [])

            search_data = "\n\n".join(
                item.get("content", "")
                for item in results
            )

        else:

            search_data = "No live search results available."

        prompt = PromptManager.salary_prompt(
            career=career,
            country=country,
            experience=experience,
            search_data=search_data
        )

        result = self.llm.generate(prompt)

        return {
            "success": True,
            "agent": "salary",
            "data": result,
            "error": None
        }