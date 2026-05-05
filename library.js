let books = [];

const bookGrid = document.getElementById("bookGrid");
const searchInput = document.getElementById("searchInput");

// Loads the CSV file and displays the books on the page.
fetch("books_with_covers.csv")
  .then(response => response.text())
  .then(csvText => {
    books = parseCSV(csvText);
    displayBooks(books);
  })
  .catch(error => {
    bookGrid.innerHTML = "<p>Could not load the Spoiled Library.</p>";
    console.error("CSV loading error:", error);
  });

// Turns the CSV text into an array of book objects.
function parseCSV(csvText) {
  const lines = csvText.trim().split("\n");
  const headers = splitCSVLine(lines[0]).map(header => header.trim());

  return lines.slice(1).map(line => {
    const values = splitCSVLine(line);

    const book = {};
    headers.forEach((header, index) => {
      book[header] = values[index] ? values[index].trim() : "";
    });

    return book;
  });
}

// Splits one CSV row while keeping commas inside quotation marks.
function splitCSVLine(line) {
  const values = [];
  let current = "";
  let insideQuotes = false;

  for (let char of line) {
    if (char === '"') {
      insideQuotes = !insideQuotes;
    } else if (char === "," && !insideQuotes) {
      values.push(current);
      current = "";
    } else {
      current += char;
    }
  }

  values.push(current);
  return values;
}

// Creates a card for each book and adds it to the library page.
function displayBooks(bookList) {
  bookGrid.innerHTML = "";

  if (bookList.length === 0) {
    bookGrid.innerHTML = "<p>No books match your search.</p>";
    return;
  }

  bookList.forEach(book => {
    const card = document.createElement("article");
    card.classList.add("book-card");

    card.innerHTML = `
      <div class="book-cover">
        ${
          book.cover_url
            ? `<img src="${escapeHTML(book.cover_url)}" alt="Cover of ${escapeHTML(book.title)}">`
            : `<span>${getInitials(book.title)}</span>`
        }
      </div>

      <div class="book-info">
        <p class="genre">${safeText(book.genre)}</p>

        <h2>${safeText(book.title)}</h2>

        <p class="author">${safeText(book.author)}</p>

        <p class="description">
          ${safeText(book.description) || "Choose how spoiled you want to be."}
        </p>

        <div class="spoiler-options">
          <button data-type="Hint" data-spoiler="${escapeHTML(book.hint)}">Hint</button>
          <button data-type="Character Fate" data-spoiler="${escapeHTML(book.character_fates)}">Character Fate</button>
          <button data-type="Partial Spoiler" data-spoiler="${escapeHTML(book.partial_spoiler)}">Partial Spoiler</button>
          <button data-type="Full Spoiler" data-spoiler="${escapeHTML(book.full_spoiler)}">Full Spoiler</button>
        </div>

        <div class="spoiler-box"></div>
      </div>
    `;

    const spoilerButtons = card.querySelectorAll(".spoiler-options button");
    const spoilerBox = card.querySelector(".spoiler-box");

    // Lets the user reveal one spoiler level at a time.
    spoilerButtons.forEach(button => {
      button.addEventListener("click", () => {
        const spoilerText = button.dataset.spoiler || "No spoiler available yet.";
        const spoilerType = button.dataset.type;

        // Clicking the same button again hides the spoiler.
        if (
          spoilerBox.classList.contains("show") &&
          spoilerBox.dataset.currentType === spoilerType
        ) {
          spoilerBox.textContent = "";
          spoilerBox.classList.remove("show");
          spoilerBox.dataset.currentType = "";
          button.classList.remove("selected");
          return;
        }

        spoilerButtons.forEach(btn => btn.classList.remove("selected"));

        spoilerBox.textContent = spoilerText;
        spoilerBox.classList.add("show");
        spoilerBox.dataset.currentType = spoilerType;
        button.classList.add("selected");
      });
    });

    bookGrid.appendChild(card);
  });
}

// Shows initials if a book does not have a cover image.
function getInitials(title) {
  if (!title) {
    return "SP";
  }

  const words = title
    .replaceAll(":", "")
    .replaceAll(",", "")
    .split(" ")
    .filter(word => word.length > 2);

  return words
    .slice(0, 2)
    .map(word => word[0])
    .join("");
}

// Filters the library as the user types in the search bar.
function filterBooks() {
  const searchTerm = searchInput.value.toLowerCase();

  const filteredBooks = books.filter(book => {
    return (
      safeText(book.title).toLowerCase().includes(searchTerm) ||
      safeText(book.author).toLowerCase().includes(searchTerm) ||
      safeText(book.genre).toLowerCase().includes(searchTerm) ||
      safeText(book.tags).toLowerCase().includes(searchTerm) ||
      safeText(book.ending_type).toLowerCase().includes(searchTerm)
    );
  });

  displayBooks(filteredBooks);
}

searchInput.addEventListener("input", filterBooks);

// Prevents blank values from breaking the page.
function safeText(text) {
  return text || "";
}

// Prevents text from being read as HTML.
function escapeHTML(text) {
  return String(text || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
