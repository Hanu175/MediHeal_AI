import time

from services.gemini_service import GeminiService
from services.database_service import DatabaseService


MEDICATION_SYSTEM_PROMPT = """
You are the Medication Management Agent inside MediSphere AI.

STRICT SAFETY RULES

Never diagnose diseases.
Never recommend changing medication.
Never tell users to stop medication.
Never change dosage.
Never prescribe medicines.
Never provide emergency advice.

ONLY

1. Organize medicines into an easy-to-follow schedule.
2. Explain what each medicine is commonly used for.
3. Explain timing instructions exactly as provided.
4. Explain food instructions if mentioned.

Return Markdown.

Format:

# Medication Schedule

For each medicine include:

- Medicine Name
- Schedule
- Common Purpose
- Instructions

Finish with:

This explanation is informational only and is not medical advice.
"""


class MedicationService:

    @staticmethod
    def generate_schedule(prescription: str):

        start = time.perf_counter()

        try:

            summary = GeminiService.generate(
                MEDICATION_SYSTEM_PROMPT,
                prescription
            )

            runtime = round(
                time.perf_counter() - start,
                2
            )

            DatabaseService.save(
                agent="Medication Manager",
                user_input=prescription,
                response=summary,
                execution_time=runtime,
                status="SUCCESS",
            )

            return summary

        except Exception as error:

            DatabaseService.save(
                agent="Medication Manager",
                user_input=prescription,
                response=str(error),
                execution_time=None,
                status="FAILED",
            )

            return f"""
# Medication Schedule

Unable to generate the medication schedule.

Error:

{error}
"""