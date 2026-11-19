from langgraph.graph import StateGraph, START, END
from orchestration.state import ResearchState
from agents.supervisor.agent import route_query
from agents.multimodal_rag.agent import retrieve
from agents.web_search.agent import search
from agents.synthesis.agent import synthesize

def supervisor(state: ResearchState) -> dict:
    return {"route": route_query(state["query"])}

def rag(state: ResearchState) -> dict:
    evidence, warning = retrieve(state["query"])
    return {"evidence": state["evidence"] + evidence, "warnings": state["warnings"] + [warning]}

def web(state: ResearchState) -> dict:
    evidence, warning = search(state["query"])
    return {"evidence": state["evidence"] + evidence, "warnings": state["warnings"] + [warning]}

def synthesis(state: ResearchState) -> dict:
    return {"answer": synthesize(state["query"], state["evidence"], state["warnings"])}

def choose(state: ResearchState) -> str:
    return state["route"]

def build_graph():
    graph = StateGraph(ResearchState)
    graph.add_node("supervisor", supervisor)
    graph.add_node("rag", rag)
    graph.add_node("web", web)
    graph.add_node("synthesis", synthesis)
    graph.add_edge(START, "supervisor")
    graph.add_conditional_edges("supervisor", choose, {"none": "synthesis", "rag": "rag", "web": "web", "both": "rag"})
    graph.add_conditional_edges("rag", lambda state: "web" if state["route"] == "both" else "synthesis", {"web": "web", "synthesis": "synthesis"})
    graph.add_edge("web", "synthesis")
    # Both route runs RAG then web sequentially to avoid concurrent state updates.
    return graph.compile()
