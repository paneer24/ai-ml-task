import cv2
import pytesseract
from PIL import Image
import re

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def extract_text(preprocessed_image):
    text = pytesseract.image_to_string(Image.fromarray(preprocessed_image))
    return text

def organize_text(raw_text):
    lines = raw_text.split('\n')
    organized = {}
    current_gland = None
    
    gland_pattern = re.compile(r'^([A-Z][a-z]+(\s+and\s+[A-Z][a-z]+)?|[A-Z]+)$')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if gland_pattern.match(line):
            current_gland = line
            organized[current_gland] = []
        elif current_gland:
            hormones = re.findall(r'\b[A-Z0-9]+(?:,\s*[A-Z0-9]+)*\b|\b[A-Z][a-z]+(?:-[a-z]+)?\b', line)
            organized[current_gland].extend(hormones)
    for gland, hormones in organized.items():
        organized[gland] = ', '.join(hormones)
    
    return organized

def process_image(image_path):
    preprocessed = preprocess_image(image_path)
    raw_text = extract_text(preprocessed)
    organized = organize_text(raw_text)
    return organized
result = process_image('sample.jpeg')
print(result)
with open('output_dictionary.txt', 'w') as f:
    f.write(str(result))