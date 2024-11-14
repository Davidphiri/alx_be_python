class Book:
    def __init__(self, title, author):
        """Constructor to initialize the basic attributes of a book."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}"

# Derived class EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # Additional attribute for EBook

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"'{self.title}' by {self.author} (EBook, {self.file_size}MB)"

# Derived class PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Additional attribute for PrintBook

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"'{self.title}' by {self.author} (PrintBook, {self.page_count} pages)"

# Class to manage the library (composition)
class Library:
    def __init__(self):
        """Initialize an empty library with a list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        if isinstance(book, Book):  # Ensure it's an instance of Book or its subclass
            self.books.append(book)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
