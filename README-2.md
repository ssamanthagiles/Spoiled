# Spoiled

People who like spoilers are spoiled. This is where they get what they want.

Spoiled is a digital library for readers who want control over spoilers. Instead of treating a spoiler as one blunt reveal, the project separates spoiler information into layers. A reader can browse a shelf of books, choose a story, and decide how much they want to know.

The goal is not to ruin a book all at once. The goal is to let the reader choose how they spoil themselves.

---

## What the Project Does

Spoiled is a web-based library built with HTML, CSS, JavaScript, Python, and a CSV dataset.

The main website lets users browse and search a library of books. Each book has layered spoiler options, so the user can choose whether they want:

- A hint
- A partial spoiler
- Character fates
- The full spoiler

Python is used as a helper tool. The `covers.py` script searches Open Library for book cover images and writes those cover URLs into the CSV file. The website then uses the updated CSV to display book covers in the library.

---

## Project Files

- `index.html`
  The homepage for Spoiled.

- `style.css`
  The styling for the homepage.

- `library.html`
  The main library page where users browse and search books.

- `library.css`
  The styling for the library page.

- `library.js`
  The JavaScript file that loads the CSV, displays the books, handles search, and controls spoiler reveals.

- `books.csv`
  The original book dataset.

- `books_with_covers.csv`
  The updated dataset with book cover URLs.

- `covers.py`
  A Python helper script that finds cover images using Open Library.

- `spoiled-logo.png`
  The Spoiled logo.

- `README.md`
  Project documentation.

---

## Dataset

The project uses a CSV file as its main dataset. Each row represents one book in the Spoiled Library.

Each book includes:

- Title
- Author
- Genre
- Description
- Hint
- Partial spoiler
- Character fates
- Full spoiler
- Ending type
- Tags
- Cover image URL

Using a CSV makes the project easier to expand. I can add or revise books by editing the dataset instead of rewriting the website code.

---

## How to Run the Website

Make sure the project folder contains:

```text
spoiled/
├── images/
├── books.csv
├── books_with_covers.csv
├── covers.py
├── index.html
├── library.html
├── library.css
├── library.js
├── style.css
└── README.md

To run the website:
Open the project folder in the terminal (cd spoiled)
Run: python3 -m http.server
Open the local server link in your browser. It will usually be:
http://localhost:8000

The local server is needed because the JavaScript file loads book data from a CSV file.

## How to Use Spoiled

1. Click into the Spoiled Library.
2. Browse the book cards or use the search bar.
3. Search by title, author, genre, tag, or ending type.
4. Choose a spoiler level for a book.

Each book gives the user four options:

- Hint
- Character Fate
- Partial Spoiler
- Full Spoiler

The user can click one spoiler button at a time. Clicking the same button again hides the spoiler.

Example searches:

Little Women

classic

sisters

bittersweet

---

## Example Spoiler Output

For *Little Women*, the spoiler levels show different amounts of information.

### Hint

The ending is domestic, but it is not simple.

### Partial Spoiler

The sisters grow into separate lives, and one beloved sister does not survive.

### Character Fate

Beth dies; Jo marries Professor Bhaer; Amy marries Laurie; Meg marries John Brooke.

### Full Spoiler

Beth dies. Amy marries Laurie. Jo does not marry Laurie and instead marries Professor Bhaer, later building a school at Plumfield.

This shows the main idea of the project. The user does not have to see the full spoiler immediately. They can choose a smaller reveal first.

---

## Edge Cases

If no book matches the search, the site shows:

No books match your search.

If a book does not have a cover image, the site shows initials instead of leaving the cover area blank.

If a spoiler field is empty, the site shows:

No spoiler available yet.

Spoilers do not expire in the current version of the project. Earlier versions considered spoiler expiration dates, but the final website focuses on a collective digital library, instead of an individualized personal bookshelf/library.

---

## Use of Generative AI

I used generative AI as a coding and writing assistant while building this project.

I used it to help revise parts of my HTML, CSS, JavaScript, Python, and README documentation. It helped me debug layout issues, organize my code comments, and turn the project from a command-line idea into a visual website.  It also helped me organize and clean my CSV file so the book data would be easier to use in the website.

My own Goodreads library was the basis for the book choices and spoiler content. I chose the books, spoiler categories, visual direction, and final project design myself. I reviewed and edited the code and documentation before adding them to the final project.
