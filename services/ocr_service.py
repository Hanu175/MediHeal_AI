from utils.ocr import extract_text


class OCRService:

    @staticmethod
    def extract(image_path: str):

        return extract_text(image_path)