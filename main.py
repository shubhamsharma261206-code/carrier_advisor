from fastapi import FastAPI, HTTPException
import traceback

from models.request import CareerRequest
from services.orchestrator import Orchestrator


app = FastAPI(
    title="Career Advisor AI",
    version="1.0.0",
    description="Multi-Agent Career Advisor using FastAPI, Groq, Gemini and Tavily"
)

orchestrator = Orchestrator()


@app.get("/")
def home():

    return {
        "message": "Career Advisor AI is running."
    }


@app.post("/career")
def career_advisor(request: CareerRequest):

    try:

        response = orchestrator.execute(request.query)

        return response

    except Exception as e:

        traceback.print_exc()   # <-- Prints full error in terminal

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )