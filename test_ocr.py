from utils.ocr import extract_text

report_path = "uploads/sample_report.png"

text = extract_text(report_path)

print("\n===== OCR OUTPUT =====\n")
print(text)