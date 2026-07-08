from graph.workflow import graph

choice = input(
"""
Choose:

1 - Report Parser

2 - Medication Manager

Selection:
"""
)

if choice == "1":

    state = {
        "user_input": "Explain this report",
        "uploaded_report_path": "uploads/sample_report.png",
        "extracted_text": None,
        "report_summary": None,
        "medication_input": None,
        "medication_schedule": None,
        "next_agent": None,
        "final_response": None,
        "messages": []
    }

else:

    prescription = input(
        "\nPaste your prescription:\n\n"
    )

    state = {
        "user_input": prescription,
        "uploaded_report_path": None,
        "extracted_text": None,
        "report_summary": None,
        "medication_input": prescription,
        "medication_schedule": None,
        "next_agent": None,
        "final_response": None,
        "messages": []
    }

result = graph.invoke(state)

print("\n")
print(result["final_response"])