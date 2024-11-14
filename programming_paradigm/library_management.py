# Define the Book class
class Book:
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track whether the book is checked out
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"The book '{self.title}' has been checked out."
        else:
            return f"The book '{self.title}' is already checked out."

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return f"The book '{self.title}' has been returned."
        else:
            return f"The book '{self.title}' was not checked out."

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

# Define the Library class
class Library:
    def __init__(self):
        # Private list to store Book instances
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            return f"The book '{book.title}' by {book.author} has been added to the library."
        else:
            return "Only instances of the Book class can be added."

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f"Book with title '{title}' not found in the library."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"Book with title '{title}' not found in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return "Available books:\n" + "\n".join(available_books)
        else:
            return "No books are currently available."

