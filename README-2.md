# Spoiled

People who like spoilers are spoiled. This is where they get what they want.

The project is built on a simple premise: most readers do not simply want to avoid spoilers. They want control over them.

Instead of treating a spoiler as one blunt piece of information, Spoiled separates spoilers into layers. A reader can ask for a hint, a partial spoiler, a full spoiler, or only character fates. The goal is not to ruin the book all at once, but to let the reader decide how much they want to know and when.

---

## What the Project Does So Far

The current version of Spoiled is a command-line Python program. It allows the user to:

- View a shelf of books
- Search the shelf by title, author, genre, status, ending type, or tag
- Choose a book to spoil
- Choose why they want spoiler information
- Choose how much they want spoiled
- Reveal only the selected spoiler layer
- See an expiration date for each spoiler entry
- Optionally reveal character fates

The project currently uses a manually curated CSV file with 30 books. Each book contains structured spoiler information.

---

## Why the Project Uses a CSV

I chose to use a CSV file instead of hard-coding the books directly into Python. This makes the project easier to expand because I can add or revise books in `books.csv` without rewriting the program logic.

The CSV structure also supports the central idea of the project: spoilers are data. Each book has separate fields for:

- Hint
- Partial spoiler
- Full spoiler
- Character fates
- Ending type
- Tags
- Spoiler expiration date

---

## Files

- `spoiled.py`: The main Python program
- `books.csv`: The book and spoiler dataset
- `README.md`: Project documentation

---

## How to Run

Make sure `spoiled.py` and `books.csv` are in the same folder.

Then run:

```bash
python3 spoiled.py
