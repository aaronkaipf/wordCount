import argparse
import logging
import re
from collections import Counter
from pathlib import Path

def preprocess(text: str) -> list[str]:
    """
    - Convert all text to lowercase
    - Remove punctuation (except hyphens and apostrophes)
    - Remove empty tokens
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9äöüß'\-]+", " ", text)
    return [w for w in text.split() if w.strip()]

def count_with_counter(words: list[str]) -> Counter:
    """Count word frequencies using collections.Counter."""
    return Counter(words)

def main():
    parser = argparse.ArgumentParser(
        description="Count word frequencies in a text file."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input text file (UTF-8 encoded)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("word_counts.txt"),
        help="Path to the output file"
    )
    parser.add_argument(
        "--sort-by-length",
        action="store_true",
        help="Sort results by word length"
    )
    parser.add_argument(
        "--sort-by-frequency",
        action="store_true",
        help="Sort results by frequency (descending)"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    logging.info(f"Reading file: {args.input_file}")

    try:
        text = args.input_file.read_text(encoding="utf-8")
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return

    words = preprocess(text)
    logging.info(f"Total words found: {len(words)}")

    counts = count_with_counter(words)
    logging.info(f"Unique words: {len(counts)}")

    if args.sort_by_frequency:
        items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        logging.info("Sorting by frequency (descending)")
    elif args.sort_by_length:
        items = sorted(counts.items(), key=lambda x: len(x[0]))
        logging.info("Sorting by word length (ascending)")
    else:
        items = sorted(counts.items(), key=lambda x: x[0])
        logging.info("Sorting alphabetically")

    logging.info(f"Writing results to: {args.output}")

    try:
        with args.output.open("w", encoding="utf-8") as out:
            for word, freq in items:
                out.write(f"{word}: {freq}\n")
    except Exception as e:
        logging.error(f"Error writing output file: {e}")
        return

    logging.info("Process completed.")


if __name__ == "__main__":
    main()