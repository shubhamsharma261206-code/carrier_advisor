from typing import List

from tools.llm.groq_ai import GroqAI


class RouterAgent:
    """
    Decides which agents should execute
    based on the user's request.
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

Your job is to decide which AI agents should execute.

Available Agents:

1. career
   - Career Overview
   - Skills
   - Responsibilities
   - Qualifications

2. salary
   - Salary
   - Pay Scale
   - Packages

3. trend
   - Future Scope
   - Job Demand
   - Hiring Trends
   - Market Growth

4. roadmap
   - Learning Path
   - Courses
   - Certifications
   - Projects

5. interview
   - Interview Questions
   - Resume
   - Preparation

User Query:

{user_query}

Rules:

Return ONLY comma separated values.

Example:

career,salary

or

career,trend,roadmap

Nothing else.
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