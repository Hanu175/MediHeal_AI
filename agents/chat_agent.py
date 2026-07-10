from models.state import MediSphereState
from services.chat_service import ChatService


def chat_agent(state: MediSphereState):

    try:

        answer = ChatService.ask(

            question=state.get("user_input", ""),

            report_summary=state.get("report_summary"),

            medication_schedule=state.get("medication_schedule"),

        )

        state["final_response"] = answer

    except Exception as e:

        state["final_response"] = f"❌ Error: {e}"

    return state