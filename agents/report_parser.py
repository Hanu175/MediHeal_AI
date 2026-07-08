from models.state import MediSphereState
from services.report_service import ReportService


def report_parser_agent(state: MediSphereState):

    image_path = state.get("uploaded_report_path")

    if not image_path:

        state["final_response"] = "No report uploaded."

        return state

    try:

        result = ReportService.parse_medical_report(
            image_path
        )

        state["report_summary"] = result["markdown"]

        state["final_response"] = result["markdown"]

    except Exception as e:

        state["final_response"] = f"❌ Error: {str(e)}"

    return state