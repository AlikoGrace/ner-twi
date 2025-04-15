import re
import os
import html

file_path = "../data/raw/news.txt"

def clean_text(text):
    # Unescape HTML entities (e.g., &nbsp;, &amp;)
    text = html.unescape(text)
    
    # Remove HTML tags (if any)
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove weird leftover entities like “\xa0” or multiple spaces
    text = text.replace('\xa0', ' ')  
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def split_into_sentences(text):
    # Clean the text before splitting
    text = clean_text(text)

    # Split by punctuation followed by space
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

# Load the raw text
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Process
sentences = split_into_sentences(text)

# Prepare output path
input_directory = os.path.dirname(file_path)
input_filename = os.path.basename(file_path)
output_filename = os.path.splitext(input_filename)[0] + "_sentences" + os.path.splitext(input_filename)[1]
output_path = os.path.join(input_directory, output_filename)

# Save sentences
with open(output_path, "w", encoding="utf-8") as file:
    for sentence in sentences:
        file.write(sentence.strip() + "\n")

print(f"Sentences saved to: {output_path}")
