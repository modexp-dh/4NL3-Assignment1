import sys
import re
import argparse

def normalize_text(
        text,
        lowercase=False,
        stem=False,
        lemma=False,
        stopwords=False,
        accent=False
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
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file")

    args = parser.parse_args()
    print(args.input_file)

main()