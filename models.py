class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = "available"

    def mark_borrowed(self):
        self.status = "borrowed"

    def mark_returned(self):
        self.status = "available"