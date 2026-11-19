def route_query(query: str) -> str:
    """Deterministic demo only. Replace with structured, tested supervisor."""
    q = query.lower()
    internal = any(w in q for w in ("document", "uploaded", "knowledge base", "pdf", "image"))
    external = any(w in q for w in ("web", "internet", "latest", "current news"))
    return "both" if internal and external else "rag" if internal else "web" if external else "none"
