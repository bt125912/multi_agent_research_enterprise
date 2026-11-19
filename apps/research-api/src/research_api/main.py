from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Enterprise Research API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

class ResearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=4000)

@app.get("/health")
def health():
    return {"status": "ok", "mode": "demo", "live_research_ready": False}

@app.post("/api/v1/research")
def research(request: ResearchRequest):
    from research_api.runtime import run_research
    return run_research(request.query)
