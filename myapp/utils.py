import os
import openai
from PIL import Image
import pytesseract

openai.organization = "org-RZDag05Cl7OVwTMGbmn7eYN4"
openai.api_key = "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"
pytesseract.pytesseract.tesseract_cmd = r'.//Tesseract-OCR//tesseract.exe'

def get_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = message,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )  
    answer = response.choices[0].text.strip()
    return answer