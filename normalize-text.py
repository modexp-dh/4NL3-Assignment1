import sys
import re

def normalize_text(
        text,
        lowercase=False,
        remove_punctuation=False,
        remove_numbers=False
 ):
    """
    Normalize human readable text to raw text
    """

    if lowercase:
        text = text.lower()

    if remove_numbers:
        text = re.sub(r"\d+", "", text)

    if remove_punctuation:
        text = re.sub(r"[^\w\s']", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text

def main():
    print("hello")

main()