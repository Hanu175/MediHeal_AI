import json
from pathlib import Path

import google.generativeai as genai

from config.settings import GOOGLE_API_KEY


genai.configure(api_key=GOOGLE_API_KEY)


class GeminiVisionService:

    def __init__(self):

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def parse_report(
        self,
        image_path: str,
    ):

        image = Path(image_path)

        prompt = """
You are the Medical Report Extraction Agent inside MediSphere AI.

STRICT SAFETY RULES

Never diagnose.

Never estimate severity.

Never recommend medication.

Never infer diseases.

Never provide urgency.

Never give treatment advice.

Your ONLY task is to extract the report into JSON.

Return ONLY valid JSON.

Format:

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

Status must ONLY be:

Within Reference Range

Above Reference Range

Below Reference Range

Cannot Determine

Explanation should explain ONLY what the laboratory parameter measures.

Never mention diseases.
"""

        response = self.model.generate_content(
            [
                prompt,
                image,
            ]
        )

        cleaned = response.text.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned.replace("```json", "")
            cleaned = cleaned.replace("```", "")

        return json.loads(cleaned)