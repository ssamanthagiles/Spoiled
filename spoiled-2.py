"""
Spoiled

People who like spoilers are spoiled.
Let's spoil ourselves.

This program treats spoilers as layered information. A user can choose
a book, decide why they want to know more, and reveal only the amount
of information they want.
"""

import csv
from datetime import datetime

BOOKS_FILE = "books.csv"


def load_books(filename):
    """Load all books from the CSV file."""
    books = []

    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books.append(row)

    except FileNotFoundError:
        print(f"Error: Could not find {filename}.")
        print("Make sure books.csv is in the same folder as spoiled.py.")
        return []

    return books


def print_header():
    """Print the opening title."""
    print("=" * 60)
    print("SPOILED")
    print("People who like spoilers are spoiled.")
    print("Let's spoil ourselves.")
    print("=" * 60)
    print()

def check_expiration(book):
    if book["shelf_status"] in ["read", "spoiled", "read + spoiled", "read + partially spoiled"]:
        return "not applicable"

    if not book["spoiler_expiration_date"]:
        return "not set"

    try:
        today = datetime.today().date()
        expiration = datetime.strptime(book["spoiler_expiration_date"], "%Y-%m-%d").date()
    except ValueError:
        return "invalid date"

    if today > expiration:
        return "expired"

    days_left = (expiration - today).days
    return f"{days_left} day(s) left"


def show_shelf(books):
    """Display every book on the Spoiled shelf."""
    print("Your Spoiled Shelf:")
    print()

    for index, book in enumerate(books, start=1):
        expiration_status = check_expiration(book)

        print(f"{index}. {book['title']} by {book['author']}")
        print(f"   Status: {book['shelf_status']} | Expiration: {expiration_status}")

    print()


def search_shelf(books):
    """Let the user search by title, author, genre, status, ending type, or tag."""
    query = input("Search by title, author, genre, status, ending, or tag: ").lower().strip()
    matches = []

    for book in books:
        searchable_text = " ".join([
            book["title"],
            book["author"],
            book["genre"],
            book["shelf_status"],
            book["ending_type"],
            book["tags"]
        ]).lower()

        if query in searchable_text:
            matches.append(book)

    if not matches:
        print("No matches found. Showing the full shelf instead.")
        print()
        return books

    print()
    print("Search results:")
    print()

    for index, book in enumerate(matches, start=1):
        print(f"{index}. {book['title']} by {book['author']}")
        print(f"   Status: {book['shelf_status']} | Expiration: {check_expiration(book)}")

    print()
    return matches


def choose_book(books):
    """Ask the user to select a book by number."""
    while True:
        choice = input("Which book do you want to spoil? Enter a number: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(books):
                return books[choice - 1]

        print("Please enter a valid book number.")


def choose_intent():
    """Ask why the user wants spoiler information."""
    print()
    print("Why do you want to know?")
    print("1. I am deciding whether to read it")
    print("2. I need reassurance before continuing")
    print("3. I finished it and want explanation")
    print("4. I want the full ending")
    print("5. I only want to know who lives or dies")

    while True:
        choice = input("Choose a reason: ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            return choice

        print("Please choose a number from 1 to 5.")


def full_spoiler_available(book):
    """Return True if the user is allowed to view a full spoiler."""
    if book["shelf_status"] in ["read", "spoiled"]:
        return True

    if not book["spoiler_expiration_date"]:
        return True

    today = datetime.today().date()
    expiration = datetime.strptime(book["spoiler_expiration_date"], "%Y-%m-%d").date()

    return today >= expiration


def choose_spoiler_level(intent, book):
    """
    Ask how much the user wants spoiled.

    If the user asks for the full spoiler before the expiration date,
    the program warns them and lets them choose a lighter spoiler instead.
    """
    if intent == "5":
        return "character_fates"

    print()
    print("How much do you want spoiled?")
    print("1. Hint")
    print("2. Partial spoiler")
    print("3. Full spoiler")

    while True:
        choice = input("Choose a spoiler level: ").strip()

        if choice == "1":
            return "hint"

        if choice == "2":
            return "partial_spoiler"

        if choice == "3":
            if full_spoiler_available(book):
                return "full_spoiler"

            print()
            print("Not yet.")
            print("This book is still resisting you.")
            print(f"Full spoiler unlocks: {book['spoiler_expiration_date']}")
            print("Choose a hint or partial spoiler for now.")
            print()

        else:
            print("Please choose 1, 2, or 3.")


def update_shelf_status(book, spoiler_level):
    """
    Update the book's spoiler status after a reveal.
    """

    current_status = book["shelf_status"]

    if spoiler_level in ["hint", "partial_spoiler"]:
        if current_status == "read":
            book["shelf_status"] = "read + partially spoiled"
        elif current_status != "spoiled":
            book["shelf_status"] = "partially spoiled"

    elif spoiler_level in ["full_spoiler", "character_fates"]:
        if current_status == "read":
            book["shelf_status"] = "read + spoiled"
        else:
            book["shelf_status"] = "spoiled"


def reveal_spoiler(book, spoiler_level):
    """Reveal the selected spoiler layer for the chosen book."""
    print()
    print("=" * 60)
    print(f"{book['title']} by {book['author']}")
    print("=" * 60)
    print(f"Genre: {book['genre']}")
    print(f"Status: {book['shelf_status']}")
    print(f"Ending type: {book['ending_type']}")
    print(f"Expiration: {check_expiration(book)}")
    print()

    if spoiler_level == "hint":
        label = "HINT"
    elif spoiler_level == "partial_spoiler":
        label = "PARTIAL SPOILER"
    elif spoiler_level == "full_spoiler":
        label = "FULL SPOILER"
    else:
        label = "CHARACTER FATES"

    print(label)
    print("-" * 60)
    print(book[spoiler_level])
    print("-" * 60)

    if spoiler_level != "character_fates":
        print()
        see_fates = input("Do you also want character fates? yes/no: ").lower().strip()

        if see_fates == "yes":
            print()
            print("CHARACTER FATES")
            print("-" * 60)
            print(book["character_fates"])
            print("-" * 60)

    update_shelf_status(book, spoiler_level)

    print()
    print(f"New status: {book['shelf_status']}")


def main():
    """Run the Spoiled program."""
    books = load_books(BOOKS_FILE)

    if not books:
        return

    print_header()

    while True:
        print("What do you want to do?")
        print("1. View the whole Spoiled shelf")
        print("2. Search the shelf")
        print("3. Exit")

        action = input("Choose an option: ").strip()
        print()

        if action == "1":
            available_books = books
            show_shelf(available_books)

        elif action == "2":
            available_books = search_shelf(books)

        elif action == "3":
            print("Leaving the shelf unopened.")
            break

        else:
            print("Please choose 1, 2, or 3.")
            print()
            continue

        selected_book = choose_book(available_books)
        intent = choose_intent()
        spoiler_level = choose_spoiler_level(intent, selected_book)
        reveal_spoiler(selected_book, spoiler_level)

        print()
        again = input("Do you want to spoil another book? yes/no: ").lower().strip()

        if again != "yes":
            print("Leaving the shelf unopened.")
            break

        print()


if __name__ == "__main__":
    main()
