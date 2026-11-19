def search(query: str) -> tuple[list[dict], str]:
    # Do not claim live search without an approved provider integration.
    return [], "Web search unavailable: no search provider configured."
