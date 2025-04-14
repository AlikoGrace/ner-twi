import re
import os


file_path = "../data/raw/anansi_story2.txt"


def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)  
    return sentences


with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()


sentences = split_into_sentences(text)


input_directory = os.path.dirname(file_path)
input_filename = os.path.basename(file_path)


output_filename = os.path.splitext(input_filename)[0] + "_sentences" + os.path.splitext(input_filename)[1]


output_path = os.path.join(input_directory, output_filename)


with open(output_path, "w", encoding="utf-8") as file:
    for sentence in sentences:
        file.write(sentence + "\n")

print(f"Sentences saved to: {output_path}")
