from PyPDF2 import PdfReader
import re

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def calculate_ats_score(text):

    keywords = [
        "python","machine learning","sql","django",
        "api","data analysis","react","javascript"
    ]

    text = text.lower()

    score = 0

    for word in keywords:
        if word in text:
            score += 10

    return min(score,100)