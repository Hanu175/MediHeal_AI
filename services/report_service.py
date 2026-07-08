import json
import time

from services.database_service import DatabaseService
from services.formatter_service import FormatterService
from services.gemini_service import GeminiService
from services.gemini_vision_service import GeminiVisionService
from services.ocr_service import OCRService


REPORT_SYSTEM_PROMPT = """
You are the Medical Report Parser Agent inside MediSphere AI.

STRICT SAFETY RULES

Never diagnose diseases.
Never estimate severity.
Never provide urgency.
Never recommend medications.
Never recommend treatment.
Never infer diseases.

ONLY

1. Extract every laboratory parameter.
2. Compare ONLY with the reference range present in the report.
3. Explain ONLY what each parameter measures.

Return ONLY valid JSON.

{
    "tests":[
        {
            "name":"",
            "value":"",
            "unit":"",
            "reference_range":"",
            "status":"",
            "explanation":""
        }
    ]
}
"""


class ReportService:

    @staticmethod
    def _clean_json(text: str):

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.startswith("```"):
            text = text.replace("```", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        return text.strip()

    @staticmethod
    def parse_medical_report(image_path: str):

        # ===================================================
        # Try Gemini Vision
        # ===================================================

        start = time.perf_counter()

        try:

            vision = GeminiVisionService()

            result = vision.parse_report(image_path)

            markdown = FormatterService.report_to_markdown(result)

            runtime = round(
                time.perf_counter() - start,
                2
            )

            DatabaseService.save(
                agent="Report Parser (Vision)",
                user_input=image_path,
                response=markdown,
                execution_time=runtime,
                status="SUCCESS",
            )

            return {
                "json": result,
                "markdown": markdown,
            }

        except Exception as e:

            print("Gemini Vision Failed")
            print(e)

        # ===================================================
        # OCR FALLBACK
        # ===================================================

        start = time.perf_counter()

        try:

            extracted_text = OCRService.extract(image_path)

            response = GeminiService.generate(
                REPORT_SYSTEM_PROMPT,
                extracted_text,
            )

            response = ReportService._clean_json(response)

            parsed = json.loads(response)

            markdown = FormatterService.report_to_markdown(
                parsed
            )

            runtime = round(
                time.perf_counter() - start,
                2
            )

            DatabaseService.save(
                agent="Report Parser (OCR)",
                user_input=image_path,
                response=markdown,
                execution_time=runtime,
                status="SUCCESS",
            )

            return {
                "json": parsed,
                "markdown": markdown,
            }

        except Exception as e:

            runtime = round(
                time.perf_counter() - start,
                2
            )

            DatabaseService.save(
                agent="Report Parser",
                user_input=image_path,
                response=str(e),
                execution_time=runtime,
                status="FAILED",
            )

            return {
                "json": {},
                "markdown": f"""
# Report Parsing Failed

The report could not be processed.

Error

{str(e)}
"""
            }