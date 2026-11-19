def synthesize(query: str, evidence: list[dict], warnings: list[str]) -> str:
    if not evidence:
        return "No verified evidence is available for this query. Configure the required research adapters before relying on an answer."
    return "Evidence retrieved; verified citation-based synthesis is not yet implemented."
