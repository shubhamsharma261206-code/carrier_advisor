from pydantic import BaseModel


class CareerResponse(BaseModel):
    """
    Final response returned to the user.
    """

    career: str

    response: str

    sources: list[str] = []

    success: bool = True