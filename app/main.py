# app/main.py

from fastapi import FastAPI
from app.routes import endpoints

app = FastAPI(
    title="BiztelAI Chat Analyzer",
    description="Analyze agent chat transcripts to extract insights",
    version="1.0.0"
)

app.include_router(endpoints.router)
