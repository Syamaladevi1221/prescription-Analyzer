from PIL import Image
import pytesseract
import io
import os

# ✅ Set the Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r"E:\Hackathon\tesseract.exe"

def extract_text_from_image(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    print("🔍 Extracted Text:", text)  # Optional debug log
    return text
