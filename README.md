# 📝 Word Count CLI

This repository contains two Python scripts to **count word frequencies** in UTF-8 text files.
Both variants use the same preprocessing:

* 🔡 Convert everything to **lowercase**
* 🔠 Allowed: letters, digits, **Umlauts (ä, ö, ü, ß)**, apostrophes `'`, and hyphens `-`
* 🧹 All other characters are replaced with spaces
* 🚫 Empty tokens are removed

---

## 📂 Scripts

* **`counter_method.py`**
  📖 Reads the entire file into memory and uses `collections.Counter`.
  ✅ Best for small to medium-sized files.

* **`streaming_method.py`**
  📄 Reads the file **line by line** and counts words with a dictionary.
  🧠 Recommended for very large files since it is memory-efficient.

---

## ✨ Features

* 🔎 Unified tokenization
* 🔀 Optional sorting:

  * `--sort-by-frequency` → by frequency (descending)
  * `--sort-by-length` → by word length (ascending)
  * Default: alphabetical
* 🕒 Logging with timestamps
* 🛡️ Robust error handling for file I/O

---

## ⚙️ Installation

1. Make sure Python **3.8+** is installed.
2. Clone the repository:

   ```bash
   git clone https://github.com/aaronkaipf/wordCount
   cd wordCount
   ```

---

## ▶️ Usage

### With `counter_method.py`

```bash
python counter_method.py input.txt -o counts.txt --sort-by-frequency
```

* 📥 Reads `input.txt`
* 🧮 Counts all words
* 📊 Sorts by frequency (most common first)
* 💾 Saves results in `counts.txt`

---

### With `streaming_method.py`

```bash
python streaming_method.py input.txt --sort-by-length
```

* 📥 Reads `input.txt` line by line
* 📏 Sorts words by length
* 💾 Writes results to `word_counts.txt` (default output file)

---

## 📤 Output Format

The result files consist of lines in the format:

```
word: count
```

Example:

```
python: 12
code: 5
ai: 3
```

---

## 🤔 Which method to choose?

* ⚡ **Counter Method** (`counter_method.py`): faster & simpler for small files
* 🐘 **Streaming Method** (`streaming_method.py`): better for large files (lower memory usage)

---

## 📚 Examples

### Example Input (`input.txt`):

```
Python is great. Python-code is fun!
AI and code belong together.
```

### Output with `counter_method.py --sort-by-frequency`

```
python: 2
code: 2
is: 1
great: 1
fun: 1
ai: 1
and: 1
belong: 1
together: 1
```

### Output with `streaming_method.py --sort-by-length`

```
ai: 1
is: 1
and: 1
fun: 1
code: 2
great: 1
python: 2
belong: 1
together: 1
```
