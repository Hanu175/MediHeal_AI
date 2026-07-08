from models.state import MediSphereState


MEDICINE_KEYWORDS = {
    "medicine",
    "medication",
    "tablet",
    "capsule",
    "pill",
    "dose",
    "schedule",
    "prescription",
    "drug",
    "mg",
    "ml",
    "after food",
    "before food",
    "once",
    "twice",
    "daily",
    "morning",
    "afternoon",
    "night",
    "bedtime",
    "hours",
    "hourly",
}


def supervisor(state: MediSphereState):

    # If a report image exists, always use the report parser
    if state.get("uploaded_report_path"):
        return {"next_agent": "report"}

    text = (state.get("user_input") or "").lower()

    if any(keyword in text for keyword in MEDICINE_KEYWORDS):
        return {"next_agent": "medication"}

    return {"next_agent": "report"}