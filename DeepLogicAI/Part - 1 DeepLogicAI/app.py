from PIL import Image
import numpy as np
import pytesseract
import PyPDF2
import csv
import re

# Function to extract key-value pairs from text
def extract_key_value_pairs(text):
    # Define patterns to extract key-value pairs
    patterns = {
        'Invoice Number': r'Invoice\s*Number:\s*(\w+)',
        'Date': r'Date:\s*(\d{2}/\d{2}/\d{4})',
        # Add more patterns as needed
    }

    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data[key] = match.group(1)

    return data

# Read image
img = Image.open('sample1.png')

# Convert image to NumPy array
arr = np.asarray(img)

# Convert 3D array to 2D list of lists
lst = []
for row in arr:
    tmp = []
    for col in row:
        tmp.append(str(col))
    lst.append(tmp)

# Save image data to CSV
with open('image_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lst)

# Read PDF and extract text
with open('sample1.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

# Extract key-value pairs from text
header_data = extract_key_value_pairs(text)

# Save key-value pairs to CSV
with open('pdf_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header_data.keys())
    writer.writerow(header_data.values())
