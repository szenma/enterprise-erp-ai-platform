from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    next: str

def finance_agent(state):
    return {"messages": ["Finance analysis complete"], "next": "END"}

def procurement_agent(state):
    return {"messages": ["Vendor scoring done"], "next": "END"}

# Multi-agent workflow
workflow = StateGraph(AgentState)
workflow.add_node("finance", finance_agent)
workflow.add_node("procurement", procurement_agent)

workflow.set_entry_point("finance")
workflow.add_edge("finance", "procurement")
workflow.add_edge("procurement", END)

graph = workflow.compile()