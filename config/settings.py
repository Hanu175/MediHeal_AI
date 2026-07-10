# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "sqlite:///database/medisphere.db"
# )

# TESSERACT_PATH = os.getenv(
#     "TESSERACT_PATH",
#     r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# )

# if not os.path.exists(TESSERACT_PATH):
#     raise FileNotFoundError(
#         f"Tesseract executable not found at:\n{TESSERACT_PATH}"
#     )

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=GOOGLE_API_KEY,
#     temperature=0.2,
# )

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///database/medisphere.db"
)

TESSERACT_PATH = os.getenv(
    "TESSERACT_PATH",
    r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)
# import os
# import platform

# if platform.system() == "Windows":

#     DEFAULT_TESSERACT = (
#         r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
#     )

# else:

#     DEFAULT_TESSERACT = "/usr/bin/tesseract"


# TESSERACT_PATH = os.getenv(
#     "TESSERACT_PATH",
#     DEFAULT_TESSERACT,
# )


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2,
)