from typing import TypedDict, Optional, List, Dict, Any


class MediSphereState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    # ----------------------------
    # User Request
    # ----------------------------
    user_input: str

    # ----------------------------
    # Uploaded Medical Report
    # ----------------------------
    uploaded_report_path: Optional[str]

    # ----------------------------
    # Report Parser Output
    # ----------------------------
    report_summary: Optional[str]
    
    report_json: Optional[dict]

    # ----------------------------
    # Medication Manager
    # ----------------------------
    medication_input: Optional[str]

    medication_schedule: Optional[str]
    
    chat_response: Optional[str]

    # ----------------------------
    # Supervisor Routing
    # ----------------------------
    next_agent: Optional[str]

    # ----------------------------
    # Final Output shown in UI
    # ----------------------------
    final_response: Optional[str]

    # ----------------------------
    # Conversation History
    # ----------------------------
    messages: List[Dict[str, Any]]