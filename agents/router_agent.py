from typing import List
from tools.llm.groq_ai import GroqAI


class RouterAgent:
    """
    Decides which agents should execute.
    """

    def __init__(self, groq: GroqAI):
        self.groq = groq

        self.available_agents = [
            "career",
            "salary",
            "trend",
            "roadmap",
            "interview"
        ]

    def route(self, user_query: str) -> List[str]:

        prompt = f"""
You are an AI Router.

Available agents:

career
salary
trend
roadmap
interview

User Query:
{user_query}

Return ONLY comma separated agent names.

Example:
career,salary,trend
"""

        result = self.groq.generate(prompt)

        if not result["success"]:
            return ["career"]

        output = result["data"].lower()

        selected_agents = []

        for agent in self.available_agents:

            if agent in output:
                selected_agents.append(agent)

        if not selected_agents:
            selected_agents.append("career")

        return selected_agents