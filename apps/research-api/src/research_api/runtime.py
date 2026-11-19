from pathlib import Path
import sys

# Starter packaging keeps reusable logical agents at repository root.
# Future Construction should make these installable workspace packages.
ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.graph import build_graph

_graph = None

def run_research(query: str) -> dict:
    global _graph
    if _graph is None:
        _graph = build_graph()
    result = _graph.invoke({"query": query, "route": "none", "evidence": [], "answer": "", "warnings": []})
    return {"query": query, "route": result["route"], "answer": result["answer"], "citations": [], "warnings": result["warnings"], "mode": "demo"}
