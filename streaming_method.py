import argparse
import logging
import re
from pathlib import Path

def preprocess_line(line: str) -> list[str]:
    """
    - Convert line to lowercase
    - Replace all characters except letters, digits, hyphens, and apostrophes with spaces
    - Remove empty tokens
    """
    line = line.lower()
    line = re.sub(r"[^a-z0-9äöüß'\-]+", " ", line)
    return [w for w in line.split() if w.strip()]

def count_streaming(file_path: Path) -> dict[str,int]:
    """
    Read the file line by line and count word occurrences.
    """
    counts: dict[str,int] = {}
    with file_path.open("r", encoding="utf-8") as f:
        for lineno, raw in enumerate(f, start=1):
            words = preprocess_line(raw)
            if not words:
                continue
            logging.debug(f"Line {lineno}: {len(words)} words")
            for w in words:
                counts[w] = counts.get(w, 0) + 1
    return counts

def main():
    parser = argparse.ArgumentParser(
        description="Count word frequencies (streaming) with various sorting options."
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
        "--sort-by-frequency",
        action="store_true",
        help="Sort results by frequency (descending)"
    )
    parser.add_argument(
        "--sort-by-length",
        action="store_true",
        help="Sort results by word length (ascending)"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    logging.info(f"Starting streaming count for {args.input_file}")

    try:
        counts = count_streaming(args.input_file)
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return

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