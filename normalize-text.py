import sys
import re
import argparse
from collections import Counter

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

    parser.add_argument("-lowercase", action="store_true")

    parser.add_argument("-stem", action="store_true")

    parser.add_argument("-lemmatize", action="store_true")

    parser.add_argument("-stopwords", action="store_true")

    parser.add_argument("-myopt", action="store_true")

    args = parser.parse_args()

    print(args._get_args)

    #Read file
    with open(args.input_file) as f:
        text = f.read()

    # Normalize
    normalized_text = normalize_text(
        text,
        lowercase=args.lowercase,
        stem=args.stem,
        lemma=args.lemmatize,
        stopwords=args.stopwords,
        accent=args.myopt
    )
    
    # Tokenize
    tokens = tokenize(normalized_text)

    # Count
    token_counts = Counter(tokens)

    sorted_tokens = sorted(
        token_counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    # Output
    for token, count in sorted_tokens:
        print(f"{token} {count}")

    print(f"\nTotal tokens: {len(tokens)}", file=sys.stderr)


main()