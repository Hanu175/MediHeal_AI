from models.state import MediSphereState
from services.medication_service import MedicationService


def medication_manager_agent(state: MediSphereState):

    prescription = state.get("medication_input")

    if not prescription:
        prescription = state.get("user_input")

    if not prescription:

        state["final_response"] = "No prescription provided."

        return state

    try:

        summary = MedicationService.generate_schedule(
            prescription
        )

        state["medication_schedule"] = summary

        state["final_response"] = summary

    except Exception as e:

        state["final_response"] = f"Error: {str(e)}"

    return state