from agents.router_agent import RouterAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.career_agent import CareerAgent
from agents.salary_agent import SalaryAgent
from agents.trend_agent import TrendAgent
from agents.roadmap_agent import RoadmapAgent
from agents.interview_agent import InterviewAgent

from services.response_builder import ResponseBuilder

from tools.llm.groq_ai import GroqAI
from tools.search.search_tool import SearchTool


class Orchestrator:
    """
    Main controller of the Career Advisor AI.
    Responsible for coordinating all agents.
    """

    def __init__(self):

        # -------------------------
        # Initialize Tools
        # -------------------------

        self.llm = GroqAI()

        self.search = SearchTool()

        # -------------------------
        # Initialize Agents
        # -------------------------

        self.router = RouterAgent(self.llm)

        self.analyzer = AnalyzerAgent(self.llm)

        self.career_agent = CareerAgent(self.llm)

        self.salary_agent = SalaryAgent(self.llm)

        self.trend_agent = TrendAgent(self.llm)

        self.roadmap_agent = RoadmapAgent(self.llm)

        self.interview_agent = InterviewAgent(self.llm)

        # -------------------------
        # Response Builder
        # -------------------------

        self.response_builder = ResponseBuilder()

    def execute(self, user_query: str):

        """
        Main execution pipeline.
        """

        # -------------------------
        # Step 1
        # Decide which agents to execute
        # -------------------------

        selected_agents = self.router.route(user_query)

        # -------------------------
        # Step 2
        # Extract structured information
        # -------------------------

        analysis = self.analyzer.analyze(user_query)

        # -------------------------
        # Step 3
        # Search latest information
        # -------------------------

        search_result = self.search.search(user_query)

        # -------------------------
        # Step 4
        # Execute selected agents
        # -------------------------

        responses = {}

        if "career" in selected_agents:
            responses["career"] = self.career_agent.execute(
                analysis,
                search_result
            )

        if "salary" in selected_agents:
            responses["salary"] = self.salary_agent.execute(
                analysis,
                search_result
            )

        if "trend" in selected_agents:
            responses["trend"] = self.trend_agent.execute(
                analysis,
                search_result
            )

        if "roadmap" in selected_agents:
            responses["roadmap"] = self.roadmap_agent.execute(
                analysis,
                search_result
            )

        if "interview" in selected_agents:
            responses["interview"] = self.interview_agent.execute(
                analysis,
                search_result
            )

        # -------------------------
        # Step 5
        # Build final response
        # -------------------------

        return self.response_builder.build(responses)