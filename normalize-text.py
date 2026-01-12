import sys
import re

def normalize_text(
        text,
        lowercase=False,
 ):
    """
    Normalize human readable text to raw text
    """

    if lowercase:
        text = text.lower()

    return text

def tokenize(text):
    #remove punctuation
    text = re.sub(r"[^\w\s']", " ", text)
    tokens = text.split()
    return tokens

def main():
    print("hello")

main()