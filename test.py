# from config.settings import llm

# response = llm.invoke("Reply with exactly: Gemini Connected")

# print(response.content)

import os
from config.settings import TESSERACT_PATH

print("Configured Path:")
print(TESSERACT_PATH)

print("\nExists:", os.path.exists(TESSERACT_PATH))