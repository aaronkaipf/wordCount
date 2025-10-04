# 📝 Word Count CLI

Dieses Repository enthält zwei Python-Skripte zum **Zählen von Worthäufigkeiten** in UTF-8-Textdateien.
Beide Varianten nutzen dieselbe Vorverarbeitung:

* 🔡 Alles wird **kleingeschrieben**
* 🔠 Erlaubt sind Buchstaben, Ziffern, **Umlaute (ä, ö, ü, ß)**, Apostrophe `'` und Bindestriche `-`
* 🧹 Alle anderen Zeichen werden durch Leerzeichen ersetzt
* 🚫 Leere Tokens werden entfernt

---

## 📂 Skripte

* **`counter_method.py`**
  📖 Liest die gesamte Datei in den Speicher und verwendet `collections.Counter`.
  ✅ Gut für kleine bis mittelgroße Dateien.

* **`streaming_method.py`**
  📄 Liest die Datei **zeilenweise** ein und zählt Wörter in einem Dictionary.
  🧠 Geeignet für sehr große Dateien, da speicherschonender.

---

## ✨ Features

* 🔎 Einheitliche Tokenisierung
* 🔀 Optionales Sortieren:

  * `--sort-by-frequency` → nach Häufigkeit (absteigend)
  * `--sort-by-length` → nach Wortlänge (aufsteigend)
  * Standard: alphabetisch
* 🕒 Logging mit Zeitstempeln
* 🛡️ Robustes Error-Handling bei Datei-I/O

---

## ⚙️ Installation

1. Stelle sicher, dass Python **3.8+** installiert ist.
2. Repository klonen:

   ```bash
   git clone https://github.com/aaronkaipf/wordCount
   cd wordCount
   ```

---

## ▶️ Nutzung

### Mit `counter_method.py`

```bash
python counter_method.py input.txt -o counts.txt --sort-by-frequency
```

* 📥 Liest `input.txt`
* 🧮 Zählt die Wörter
* 📊 Sortiert nach Häufigkeit (häufigste zuerst)
* 💾 Speichert Ergebnis in `counts.txt`

---

### Mit `streaming_method.py`

```bash
python streaming_method.py input.txt --sort-by-length
```

* 📥 Liest `input.txt` zeilenweise
* 📏 Sortiert Wörter nach Länge
* 💾 Schreibt Ergebnis in `word_counts.txt` (Standardausgabe-Datei)

---

## 📤 Ausgabeformat

Die Ergebnisdateien bestehen aus Zeilen im Format:

```
wort: anzahl
```

Beispiel:

```
python: 12
code: 5
ai: 3
```

---

## 🤔 Welche Methode wählen?

* ⚡ **Counter-Methode** (`counter_method.py`): schneller & einfacher bei kleinen Dateien
* 🐘 **Streaming-Methode** (`streaming_method.py`): besser für große Dateien (weniger Speicherverbrauch)

---

## 📚 Beispiele

### Beispiel-Input (`input.txt`):

```
Python ist toll. Python-Code macht Spaß!
AI und Code gehören zusammen.
```

### Ausgabe mit `counter_method.py --sort-by-frequency`

```
python: 2
code: 2
ist: 1
toll: 1
macht: 1
spaß: 1
ai: 1
und: 1
gehören: 1
zusammen: 1
```

### Ausgabe mit `streaming_method.py --sort-by-length`

```
ai: 1
ist: 1
und: 1
spaß: 1
code: 2
macht: 1
toll: 1
python: 2
gehören: 1
zusammen: 1
```
