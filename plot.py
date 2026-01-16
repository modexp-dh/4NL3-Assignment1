import argparse
import matplotlib.pyplot as plt


def read_counts(filename):
    counts = []

    with open(filename, encoding="utf-8") as f:
        for line in f:
            _, count = line.strip().split("\t")
            counts.append(int(count))

    return counts


def main():
    parser = argparse.ArgumentParser(description="Plot Zipf distribution")

    parser.add_argument("input_file")
    parser.add_argument("--k", type=int, default=25)
    parser.add_argument("--output")

    args = parser.parse_args()

    frequencies = read_counts(args.input_file)
    k = args.k

    top_freqs = frequencies[:k]
    bottom_freqs = frequencies[-k:]

    top_ranks = list(range(1, k + 1))
    bottom_ranks = list(range(len(frequencies) - k + 1, len(frequencies) + 1))

    plt.figure(figsize=(14, 6))

    # Top 25
    plt.subplot(1, 2, 1)
    plt.bar(top_ranks, top_freqs)
    plt.yscale("log")
    plt.xlabel("Word Rank")
    plt.ylabel("Frequency (log scale)")
    plt.title(f"Top {k} Most Frequent Words")

    # Bottom 25
    plt.subplot(1, 2, 2)
    plt.bar(bottom_ranks, bottom_freqs)
    plt.yscale("log")
    plt.xlabel("Word Rank")
    plt.ylabel("Frequency (log scale)")
    plt.title(f"Bottom {k} Least Frequent Words")

    plt.tight_layout()

    if args.output:
        plt.savefig(args.output, dpi=300)
    else:
        plt.show()


main()