from PIL import Image
import google.generativeai as genai

from config.settings import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

image = Image.open("uploads/sample_report.png")

response = model.generate_content(
    [
        "Describe this image in one sentence.",
        image,
    ]
)

print(response.text)