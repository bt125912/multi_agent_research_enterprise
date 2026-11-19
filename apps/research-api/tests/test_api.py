from fastapi.testclient import TestClient
from research_api.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json()["live_research_ready"] is False

def test_research_does_not_invent_evidence():
    response = client.post("/api/v1/research", json={"query": "latest web news"})
    assert response.status_code == 200
    body = response.json()
    assert body["route"] == "web"
    assert body["citations"] == []
    assert body["warnings"]
