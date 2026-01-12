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

def main():
    print("hello")

main()