from pydantic import BaseModel, Field


class CareerRequest(BaseModel):
    """
    Request model for Career Advisor AI.
    """

    query: str = Field(
        ...,
        description="User's career-related query",
        example="I want to become an AI Engineer in India."
    )