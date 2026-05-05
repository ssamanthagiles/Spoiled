import csv
import requests


def get_cover_url(title, author):
    """
    Searches Open Library for a book cover using the book title and author.
    Returns a cover image URL if Open Library finds one.
    Returns an empty string if no cover is found.
    """

    search_url = "https://openlibrary.org/search.json"

    params = {
        "title": title,
        "author": author,
        "limit": 1,
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
    except requests.RequestException:
        return ""

    data = response.json()

    if len(data["docs"]) == 0:
        return ""

    first_result = data["docs"][0]

    if "cover_i" not in first_result:
        return ""

    cover_id = first_result["cover_i"]
    cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

    return cover_url


def add_covers_to_csv(input_file, output_file):
    """
    Reads original books.csv file.
    Adds a cover_url column.
    Writes a new CSV file with the cover URLs included.
    """

    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        books = list(reader)

    for book in books:
        title = book["title"]
        author = book["author"]

        print(f"Finding cover for {title} by {author}...")

        cover_url = get_cover_url(title, author)
        book["cover_url"] = cover_url

    fieldnames = list(books[0].keys())

    if "cover_url" not in fieldnames:
        fieldnames.append("cover_url")

    with open(output_file, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


add_covers_to_csv("books.csv", "books_with_covers.csv")
