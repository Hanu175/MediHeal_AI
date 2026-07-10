from models.state import MediSphereState


def create_state(
    user_input: str = "",
    uploaded_report_path: str | None = None,
    medication_input: str | None = None,
    next_agent: str | None = None,
) -> MediSphereState:

    return {
        "user_input": user_input,

        "uploaded_report_path": uploaded_report_path,

        "report_summary": None,
        
        "report_json": None,

        "medication_input": medication_input,

        "medication_schedule": None,
        
        "chat_response": None,

        "next_agent": next_agent,

        "final_response": None,

        "messages": [],
    }