from langgraph.graph import StateGraph
from langgraph.graph import END

from models.state import MediSphereState

from agents.report_parser import report_parser_agent
from agents.medication_manager import medication_manager_agent


# ----------------------------
# Supervisor
# ----------------------------

def supervisor(state: MediSphereState):

    next_agent = state.get("next_agent")

    if next_agent == "report":

        return "report"

    if next_agent == "medication":

        return "medication"

    return END


# ----------------------------
# Build Graph
# ----------------------------

builder = StateGraph(MediSphereState)

builder.add_node(
    "report",
    report_parser_agent
)

builder.add_node(
    "medication",
    medication_manager_agent
)

builder.set_conditional_entry_point(
    supervisor,
    {
        "report": "report",
        "medication": "medication",
        END: END
    }
)

builder.add_edge(
    "report",
    END
)

builder.add_edge(
    "medication",
    END
)

graph = builder.compile()