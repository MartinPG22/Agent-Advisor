from langgraph.graph import StateGraph
from typing import TypedDict, List
from agents.middle_agents import budget_agent, legal_agent, marketing_agent
from agents.classify_query import classify_query
from agents.decision_agent import decision_agent
import json

class ClassifierState(TypedDict, total=False):
    query: str
    category: list[str]
    answer_legal: dict
    answer_budget: dict
    answer_marketing: dict
    

def join_agents(state: ClassifierState):
    required = state.get("category", [])
    if isinstance(required, str):
        required = [r.strip() for r in required.split(",")]

    completed = list(state.get("answer", {}).keys())

    if all(agent in completed for agent in required):
        return state
    return None

def route_to_agents(state: ClassifierState):
    cats = state["category"]
    if isinstance(cats, str):
        return [c.strip() for c in cats.split(",") if c.strip()]
    return cats

builder = StateGraph(ClassifierState)

builder.add_node("classify", classify_query)
builder.add_node("legal", legal_agent)
builder.add_node("budget", budget_agent)
builder.add_node("marketing", marketing_agent)
builder.add_node("join", join_agents)
builder.add_node("decision", decision_agent)

builder.set_entry_point("classify")

builder.add_conditional_edges(
    "classify",
    route_to_agents,
    {
        "legal": "legal",
        "budget": "budget",
        "marketing": "marketing"
    }
)

builder.add_edge("legal", "join")
builder.add_edge("budget", "join")
builder.add_edge("marketing", "join")
builder.add_edge("join", "decision")

builder.set_finish_point("decision")

graph = builder.compile()