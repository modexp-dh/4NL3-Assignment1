import sys
import re
import argparse
from unidecode import unidecode
#please pip install unidecode if not installed
from collections import Counter

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "while", "with", "without",
    "to", "from", "of", "in", "on", "at", "by", "for", "about", "as",
    "is", "are", "was", "were", "be", "been", "being",
    "this", "that", "these", "those",
    "it", "its", "he", "she", "they", "them", "his", "her", "their",
    "you", "your", "we", "our", "i", "me", "my"
}

LEMMA_MAP = {
    "was": "be",
    "were": "be",
    "is": "be",
    "are": "be",
    "am": "be",
    "has": "have",
    "had": "have",
    "does": "do",
    "did": "do",
    "went": "go",
    "gone": "go",
    "better": "good",
    "best": "good",
    "worse": "bad"
}

def tokenize(text):
    #remove punctuation
    text = re.sub(r"[^\w\s']", " ", text)
    tokens = text.split()
    return tokens

def simple_stem(word):
    suffixes = [
        "ization", "ational", "fulness", "ousness",
        "iveness", "tional", "biliti",
        "ing", "edly", "edly", "edly",
        "ed", "ly", "es", "s"
    ]

    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]

    return word

def stem_tokens(tokens):
    return [simple_stem(t) for t in tokens]

def simple_lemma(word):
    if word in LEMMA_MAP:
        return LEMMA_MAP[word]

    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"

    if word.endswith("s") and len(word) > 3:
        return word[:-1]

    return word

def lemmatize_tokens(tokens):
    return [simple_lemma(t) for t in tokens]

def remove_stopwords(tokens):
    return [t for t in tokens if t not in STOPWORDS]

def normalize_text(
        text,
        lowercase=False,
        stem=False,
        lemma=False,
        stopwords=False,
        accent=False
 ):
    if lowercase:
        text = text.lower()

    if accent:
        text = unidecode(text)

    tokens = tokenize(text)

    if stem:
        tokens = stem_tokens(tokens)

    if lemma:
        tokens = lemmatize_tokens(tokens)

    if stopwords:
        tokens = remove_stopwords(tokens)

    return tokens

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file")

    parser.add_argument("-o", "--output", default="token_counts.txt")

    parser.add_argument("-lowercase", action="store_true")

    parser.add_argument("-stem", action="store_true")

    parser.add_argument("-lemmatize", action="store_true")

    parser.add_argument("-stopwords", action="store_true")

    parser.add_argument("-myopt", action="store_true")

    args = parser.parse_args()

    #Read file
    with open(args.input_file, encoding="utf-8") as f:
        text = f.read()

    # Normalize
    tokens = normalize_text(
        text,
        lowercase=args.lowercase,
        stem=args.stem,
        lemma=args.lemmatize,
        stopwords=args.stopwords,
        accent=args.myopt
    )

    # Count
    token_counts = Counter(tokens)

    sorted_tokens = sorted(
        token_counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    with open(args.output, "w", encoding="utf-8") as out:
        for token, count in sorted_tokens:
            out.write(f"{token}\t{count}\n")

    print(f"Total tokens: {len(tokens)}", file=sys.stderr)
    print(f"Saved token counts to {args.output}", file=sys.stderr)


main()