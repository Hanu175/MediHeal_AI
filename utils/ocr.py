import cv2
import pytesseract
from PIL import Image
from config.settings import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def preprocess_image(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(image_path)

    # Upscale 2x
    image = cv2.resize(
        image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC,
    )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.fastNlMeansDenoising(gray)

    gray = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )[1]

    return gray


def extract_text(image_path: str):
    processed = preprocess_image(image_path)

    custom_config = (
        "--oem 3 "
        "--psm 6 "
        "-c preserve_interword_spaces=1"
    )

    text = pytesseract.image_to_string(
        Image.fromarray(processed),
        config=custom_config,
    )

    return text.strip()