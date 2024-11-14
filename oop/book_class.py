class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's attributes."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """Returns a string that describes the book in a human-readable format."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a string that represents the book object for debugging purposes."""
        return f"Book('{self.title}', '{self.author}', {self.year})"



