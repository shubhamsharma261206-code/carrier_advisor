from pydantic import BaseModel, Field


class CareerRequest(BaseModel):
    """
    Request model for Career Advisor AI.
    """

    career: str = Field(
        ...,
        description="Desired career of the user",
        example="AI Engineer"
    )

    user_name: str | None = Field(
        default=None,
        description="Optional user name"
    )

    country: str = Field(
        default="India",
        description="Country for salary and market analysis"
    )

    experience: str = Field(
        default="Fresher",
        description="Experience level of the user"
    )