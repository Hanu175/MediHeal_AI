from services.gemini_service import GeminiService
from services.database_service import DatabaseService


CHAT_SYSTEM_PROMPT = """
You are MediSphere AI, an AI Healthcare Assistant.

You are allowed to:

• Explain laboratory tests.
• Explain report values.
• Explain medications and schedules.
• Summarize uploaded reports.
• Summarize medication schedules.

You may use general medical knowledge ONLY for explaining
medical terms and laboratory parameters.

STRICT RULES

Never diagnose.

Never infer diseases.

Never estimate severity.

Never recommend treatment.

Never prescribe medicines.

Never recommend dosage changes.

Never provide emergency advice.

If there is no report or medication schedule available,
politely tell the user to upload one first.

Always finish with:

"This explanation is informational only and is not medical advice."
"""


class ChatService:

    @staticmethod
    def ask(
        question: str,
        report_summary: str | None = None,
        medication_schedule: str | None = None,
    ):

        if not report_summary:
            report_summary = "No medical report has been uploaded."

        if not medication_schedule:
            medication_schedule = "No medication schedule has been generated."

        prompt = f"""
REPORT

{report_summary}

--------------------------------------------------

MEDICATION

{medication_schedule}

--------------------------------------------------

QUESTION

{question}
"""

        try:

            answer = GeminiService.generate(

                CHAT_SYSTEM_PROMPT,

                prompt,

            )

            DatabaseService.save(

                agent="AI Assistant",

                user_input=question,

                response=answer,

            )

            return answer

        except Exception as e:

            DatabaseService.save(

                agent="AI Assistant",

                user_input=question,

                response=str(e),

                status="FAILED",

            )

            return f"""
Unable to contact the AI service.

Error:

{e}

This explanation is informational only and is not medical advice.
"""