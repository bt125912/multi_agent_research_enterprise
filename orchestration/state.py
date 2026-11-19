from typing import TypedDict

class ResearchState(TypedDict):
    query: str
    route: str
    evidence: list[dict]
    answer: str
    warnings: list[str]
