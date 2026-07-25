from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config import Config
from models.request import CareerRequest
from models.response import CareerResponse


# --------------------------------------------------
# Create FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title=Config.APP_NAME,
    version=Config.VERSION,
    description="An AI-powered Career Advisor using Multi-Agent Architecture"
)


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.get("/")
async def home():

    return {
        "message": "Welcome to Career Advisor AI",
        "version": Config.VERSION,
        "status": "Running Successfully"
    }


# --------------------------------------------------
# Health Check Route
# --------------------------------------------------

@app.get("/health")
async def health_check():

    return {
        "status": "Healthy",
        "application": Config.APP_NAME
    }


# --------------------------------------------------
# Career Advisor Route
# --------------------------------------------------

@app.post("/career", response_model=CareerResponse)
async def career_advisor(request: CareerRequest):

    """
    This endpoint will later call the Orchestrator.
    Currently, it returns dummy data.
    """

    response = CareerResponse(
        career=request.career,
        response=f"You want to become a {request.career}. AI Agents will analyze this career shortly.",
        sources=[],
        success=True
    )

    return JSONResponse(
        status_code=200,
        content=response.model_dump()
    )